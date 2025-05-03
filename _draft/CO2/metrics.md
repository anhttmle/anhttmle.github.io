## NATURA Metrics Reference

A quick overview of NATURA’s core measurement categories and how they relate:

- **User‑level activity**: raw counts, timestamps and rates around tutorials, waste submissions, campaigns, and rewards.  
- **Windowed activity**: the same metrics recalculated over a rolling period (e.g. last 7 days, last 30 days).  
- **Peer‑comparison**: how each user stacks up against others — leaderboards and percentiles.  

---

## 1. User Activity Metrics

### 1.1 Green Point  
- **Definition**  
  Total points earned by the user through carbon rewards.  
- **Data type**  
  Integer  
- **Calculation**  
  Sum of all Carbon Report → Carbon Reward → Green Point conversions.

### 1.2 Favourite Entry Point  
Tracks where users start their journey. Values are mutually exclusive per session.  
- **Values**  
  - `Integrated Platform` (e.g. Logistic, Resident, Banking, Fintech)  
  - `App/Web` (direct NATURA)  
  - `Anonymous` (no login)  
- **Metric**  
  Percentage of sessions by entry point.

### 1.3 Tutorial‑Skip Rates  
#### 1.3.1 Recycling Process Tutorial  
- **Definition**  
  % of steps NOT completed before dropping out.  
- **Formula**  
skip_rate = 1 - (steps_completed / total_steps)

- **Example**  
Finished 5/10 steps → skip_rate = 0.50 (50%).

#### 1.3.2 Waste Category Separation Instruction  
- **Definition**  
Same skip‐rate formula, measured per category.  
- **Storage**  
One record per (user, category): `total_steps`, `steps_completed`.

#### 1.3.3 Campaign/Mission Tutorial  
- **Definition**  
Skip rate per campaign or mission tutorial, same calculation.

### 1.4 Achievements & Rewards  
#### 1.4.1 Waste Diverted  
- **Definition**  
Total mass (kg) or count (units) of each waste category the user has sorted.  
- **Granularity**  
Per category and cumulative.

#### 1.4.2 Exchanged Rewards  
Breakdown of redeemed points into various reward types:  
- **Voucher**: count and total monetary value redeemed  
- **Donation**: count and total donated amount  
- **Carbon Certificate (CC)**: count and total CC units  

#### 1.4.3 Green Market Transactions  
- **Definition**  
Trades in the marketplace of CC or vouchers.  
- **Metrics**  
Number of transactions and total value exchanged.

### 1.5 Time Metrics  
#### 1.5.1 Total Active Time  
- **Definition**  
Sum of durations of all active sessions, aggregated per day.  
- **Unit**  
Minutes or hours.

#### 1.5.2 Streak (Active‐Day Sequence)  
- **Definition**  
Longest current run of consecutive days with ≥ 1 active session.

#### 1.5.3 Sorting Velocity  
- **Definition**  
Average waste sorted per unit time (e.g. kg/week).

#### 1.5.4 Time on Screen  
- **Breakdown**  
- NATURA App/Web overall  
- Tutorials by type (Recycling, Category Instruction, Campaign)

---

## 2. User Activity Window Metrics

Identical to Section 1 but scoped to a **sliding period** (e.g. last 7 days, 30 days).  
- **Naming convention**  
Suffix with window: e.g. `green_point_7d`, `streak_30d`.  
- **Use cases**  
Weekly digests, “Your last 7 days” dashboards.

---

## 3. Peer Comparison Metrics

### 3.1 Leaderboards  
- **Top N**  
e.g. Top 10, Top 100 by any key metric (Green Point, Velocity, etc.).  
- **Windows**  
Over different periods (daily, weekly, all‐time).

### 3.2 Percentile Rankings  
- **Definition**  
Percentage of users you outperform.  
- **Formula**  
percentile = (users_you_beat / total_active_users) × 100

- **Example**  
“You’re in the top 30% for sorting velocity.”  

---

### Appendix: Naming & Storage Tips

- **Metric prefixes**  
- Real‑time: `m_` (e.g. `m_green_point`)  
- Windowed: `w7_`, `w30_` (e.g. `w7_green_point`)  
- **Progress table**  
`(user_id, tutorial_id, total_steps, completed_steps, last_updated)`  
- **Daily aggregation**  
Pre‑aggregate time and mass metrics per user/day for efficient reporting.

## Data to Collect

1. **Users & Sessions**  
   - `user_id`  
   - `session_id`  
   - `entry_point` (enum: `IntegratedPlatform`, `AppWeb`, `Anonymous`)  
   - `session_start`, `session_end` (timestamps)

2. **Tutorial Progress**  
   - `user_id`, `tutorial_id`  
   - `tutorial_type` (`RecyclingProcess`, `CategoryInstruction`, `CampaignTutorial`)  
   - `total_steps`, `steps_completed`  
   - `last_updated` (timestamp)

3. **Waste Submissions**  
   - `user_id`, `submission_id`  
   - `category_id`, `weight_kg` or `count_units`  
   - `timestamp`

4. **Campaign & Mission Joins**  
   - `user_id`, `campaign_id` or `mission_id`  
   - `join_timestamp`  
   - Optional: `campaign_tutorial_progress` (same schema as Tutorial Progress)

5. **Rewards & Exchanges**  
   - `user_id`, `reward_id`  
   - `reward_type` (`Voucher`, `Donation`, `CC`)  
   - `points_redeemed`, `value` (monetary or CC units)  
   - `exchange_timestamp`

6. **Green Market Transactions**  
   - `transaction_id`  
   - `from_user_id`, `to_user_id`  
   - `item_type` (`CC`, `Voucher`)  
   - `quantity`, `total_value`  
   - `transaction_timestamp`

7. **Carbon Reports & Conversions**  
   - `bag_id`, `operator_id`, `logistic_id`, `recycler_id`  
   - `report_id`, `carbon_amount`  
   - `report_timestamp`

8. **Time on Screen**  
   - `user_id`, `screen_type` (`AppWeb`, `RecyclingTutorial`, `CategoryInstruction`, `CampaignTutorial`)  
   - `enter_timestamp`, `exit_timestamp`

9. **Daily Aggregates (for performance)**  
   - `(user_id, date)`  
     - `active_time_total`  
     - `waste_sorted_kg`  
     - `sessions_count`  
     - `green_points_earned`

10. **Peer Comparison / Leaderboards**  
    - `(metric_name, period, user_id, metric_value, rank, percentile)`

