# Software Development Life Cycle

1. Specify
2. Plan
3. Task
4. Implement

```mermaid
  flowchart LR
  prompt_spec(("Build Specs"))
  req["Requirements"]

  prompt_spec --> req
  req --> spec_state(["Refine & Review"])

  spec_state --> spec_prompt_edit(("EDIT"))
  spec_state --OK--> design(("Planning & Design"))

  design --> task["Tasks"]
  task --> task_state(["Review"])

  task_state --> task_edit(("EDIT"))
  task_state --OK--> implement(("Implement"))

  implement --> PR["PR"]
  PR --> implement_state(["Review"])
  implement_state --> implement_edit(("EDIT"))
  implement_state --OK--> commit(("Commit"))
  
  

  spec_prompt_edit --> prompt_spec
  task_edit --> design
  implement_edit --> implement

```

# Frameworks:
- OpenSpec - LIGHTWEIGHT
- Speckit (Github) - HEAVY
- Kiro - HEAVY

# Sample Structure
## 1. Why

## 2. What

## 3. Constraint
### i. Must
### ii. Must not
### iii. Out of scope

## 4. Current state

## 5. Tasks
### i. Task 01

- What
- Files
- Tests
- Verify


### ii. Task 02
### iii. Task 01
