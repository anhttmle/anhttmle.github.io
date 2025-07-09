document.addEventListener('DOMContentLoaded', function() {
    // Flag to prevent multiple simultaneous loads (but allow refresh)
    let isLoading = false;

    // Google Spreadsheet URL
    const spreadsheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQIV-wb9Qbl4fW_o1JZrUDxgc3xKUHh5_v3DlhKBSJQF-jW6xbpeg6u_9II8Kk8HADuUX9SOqyrImJV/pub?gid=0&single=true&output=csv';

    // Function to convert CSV to array of rows
    function csvToRows(csv) {
        // Handle quoted values with commas
        const rows = [];
        let inQuotes = false, value = '', row = [];
        for (let i = 0; i < csv.length; i++) {
            const char = csv[i];
            if (char === '"') {
                inQuotes = !inQuotes;
            } else if (char === ',' && !inQuotes) {
                row.push(value);
                value = '';
            } else if ((char === '\n' || char === '\r') && !inQuotes) {
                if (value !== '' || row.length > 0) row.push(value);
                if (row.length > 0) rows.push(row);
                value = '';
                row = [];
            } else {
                value += char;
            }
        }
        if (value !== '' || row.length > 0) {
            row.push(value);
            rows.push(row);
        }
        return rows.filter(r => r.length > 1);
    }

    // Function to render pie charts for each person
    function renderPieCharts(assetNames, people, assetRatios) {
        const container = document.getElementById('pie-charts-container');
        container.innerHTML = '';
        people.forEach((person, idx) => {
            // Tạo canvas cho từng người
            const card = document.createElement('div');
            card.className = 'mb-4';
            card.innerHTML = `<h6>${person}</h6><canvas class="pie-chart-canvas" id="pie-chart-${idx}" height="250" style="max-width:350px"></canvas>`;
            container.appendChild(card);
            // Dữ liệu tỉ trọng
            const data = assetRatios.map(row => parseFloat(row[idx].replace(/%/g, '').replace(/,/g, '')) || 0);
            console.log(`Pie chart data for ${person}:`, data);
            console.log(`Asset names:`, assetNames);
            new Chart(document.getElementById(`pie-chart-${idx}`), {
                type: 'pie',
                data: {
                    labels: assetNames,
                    datasets: [{
                        data: data,
                        backgroundColor: [
                            '#4e79a7','#f28e2b','#e15759','#76b7b2','#59a14f','#edc949','#af7aa1','#ff9da7','#9c755f','#bab0ab','#b07aa1','#7aafb0','#a1b07a','#b0a17a','#7ab0a1'
                        ]
                    }]
                },
                options: {
                    plugins: {
                        legend: { position: 'bottom' },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const label = context.label || '';
                                    const value = context.parsed;
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = ((value / total) * 100).toFixed(1);
                                    return `${label}: ${percentage}%`;
                                }
                            }
                        }
                    },
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        });
    }

    // Function to render asset value table
    function renderAssetTable(assetNames, people, assetValues) {
        const table = document.getElementById('financial-table');
        table.innerHTML = '';
        // Header
        const thead = document.createElement('thead');
        thead.className = 'thead-dark';
        const trHead = document.createElement('tr');
        trHead.innerHTML = `<th>Asset</th>` + people.map(p => `<th class="asset-value-header">${p}</th>`).join('');
        thead.appendChild(trHead);
        table.appendChild(thead);
        // Body
        const tbody = document.createElement('tbody');
        assetNames.forEach((asset, i) => {
            const tr = document.createElement('tr');
            // if (i === 0) tr.style.fontWeight = 'bold'; // Bỏ bôi đậm dòng đầu tiên
            tr.innerHTML = `<td>${asset}</td>` + assetValues[i].map(v => `<td class="asset-value-cell">${formatNumber(v)}</td>`).join('');
            tbody.appendChild(tr);
        });
        // Tính tổng cho từng người
        const totalByPerson = assetValues.reduce((acc, row) => acc.map((sum, i) => sum + (parseFloat(row[i]) || 0)), new Array(assetValues[0].length).fill(0));
        const trTotal = document.createElement('tr');
        trTotal.style.fontWeight = 'bold';
        trTotal.innerHTML = `<td>Total (VNĐ)</td>` + totalByPerson.map(v => `<td class="asset-value-cell">${formatNumber(v)}</td>`).join('');
        tbody.appendChild(trTotal);
        table.appendChild(tbody);
        document.getElementById('data-container').style.display = 'block';
        document.getElementById('loading').style.display = 'none';
    }

    // Format currency
    function formatCurrency(value) {
        if (!value || isNaN(value)) return value;
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            maximumFractionDigits: 2
        }).format(parseFloat(value.toString().replace(/,/g, '')));
    }

    function formatNumber(value) {
        if (!value || isNaN(value)) return value;
        return new Intl.NumberFormat('en-US', {
            maximumFractionDigits: 0
        }).format(parseFloat(value.toString().replace(/,/g, '')));
    }

    // Main load function
    async function loadFinancialData() {
        if (isLoading) return;
        isLoading = true;
        try {
            const response = await fetch(spreadsheetUrl);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const csvData = await response.text();
            // Parse CSV
            const rows = csvToRows(csvData);
            if (rows.length < 2) throw new Error('No data');
            // Header
            const header = rows[0];
            // Xác định vị trí các cột người
            let people = [];
            let personColIdx = [];
            for (let i = 3; i < header.length; i += 2) {
                if (header[i]) {
                    people.push(header[i]);
                    personColIdx.push(i);
                }
            }
            // Lấy tên tài sản
            const assetNames = rows.slice(2).map(r => r[0]);
            // Lấy NAV từ cột B
            const navValues = rows.slice(2).map(r => parseFloat(r[1].replace(/,/g, '')) || 0);
            // Lấy số lượng tài sản cho từng người (cột của mỗi người)
            const assetQuantities = rows.slice(2).map(r => personColIdx.map(idx => parseFloat(r[idx].replace(/,/g, '')) || 0));
            // Tính giá trị = số lượng × NAV
            const assetValues = assetQuantities.map((quantities, i) => 
                quantities.map(qty => qty * navValues[i])
            );
            // Lấy tỉ trọng tài sản cho từng người
            const assetRatios = rows.slice(2).map(r => personColIdx.map(idx => r[idx+1]));
            // Render
            renderPieCharts(assetNames, people, assetRatios);
            renderAssetTable(assetNames, people, assetValues);
        } catch (error) {
            console.error('Error loading financial data:', error);
            document.getElementById('error').style.display = 'block';
            document.getElementById('error-message').textContent = 'Failed to load financial data. Please check the spreadsheet URL and ensure it is publicly accessible.';
            document.getElementById('loading').style.display = 'none';
        } finally {
            isLoading = false;
        }
    }

    loadFinancialData();
}); 