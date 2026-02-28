# Assessment 004 - Summative

## Learning Outcomes assessed

- Data Structures
- Data Manipulation
- String Formatting
- Loops
- CLI Commands
- APIs

---

## Assessment Structure

The following Assessment has two sections:

- [Coding Assessment (Questions are below)](#fundamentals-coding-assessment)
- [Long Questions (Questions are below)](#long-format-questions) - `answers.txt`

You can answer them in any order.

---

## Your Goal

Read the instructions below for each [coding question](#fundamentals-coding-assessment), then complete each function in `summative.py` while ensuring that:

- The code is valid Python
- Each function behaves according to the instructions
- All unit tests pass successfully

Read the instructions below for each [long format question](#long-format-questions), then add your answer under each relevant comment in `answers.txt` while ensuring that:

- You DO NOT remove the comments
- Read each question carefully before answering the question

---

### How to run your tests

To run all your tests

```bash
python3 -m pytest tests/test_summative.py -v
```

To run your tests individually

```bash
python3 -m pytest tests/test_summative.py::test_reverse_list -v
```

or for more information within the stacktrace use

```bash
python3 -m pytest tests/test_summative.py::test_reverse_list -vv
```

---

## Scoring & Weighting

| Component                                     | Weight  |
| --------------------------------------------- | ------- |
| Coding Section (unit tests)                   | **50%** |
| Long-format Question (answers.txt)            | **50%** |

## Fundamentals Coding Assessment

This assessment consists of seven Python functions. Each function has a partially written
implementation. Your task is to **fix the bugs**, **complete the missing logic**, and **ensure all tests pass**.

### Project Structure

```text
fun-004-summative/
├── summative.py              # <-- This is where you write your solutions
├── answers.txt                     # <-- This is where you write your answers to the long questions
├── tests/
│   └── test_summative.py     # <-- These are the tests you must make pass
└── README.md                       # <-- Assessment instructions (this file) 
```

---

### Question 1 - `reverse_list(items)`

The data engineering team at a Johannesburg logistics company receives daily delivery records as an ordered list — but their reporting dashboard displays data in reverse chronological order, meaning the most recent entry must come first. Rather than reloading the data from scratch, the team needs a simple utility that flips any list they give it.

Apply your logic to the `reverse_list()` function. You will receive a list of items and must return a **new list** with the elements in reverse order. Do not modify the original list.

- **Input:**

```python
[1, 2, 3, 4, 5]
```

- **Output:**

```python
[5, 4, 3, 2, 1]
```



---

### Question 2 - `sum_even_numbers(numbers)`


A small accounting firm in Pretoria is auditing a list of transaction amounts. Their compliance rules only apply to even-numbered amounts (a quirk of their legacy system), so the auditors need a quick way to calculate the total of only the even values in any list of numbers they feed through.

Apply your logic to the `sum_even_numbers()` function. You will receive a list of integers and must return the **sum of only the even numbers** in the list. If there are no even numbers, return `0`.

- **Input:**

```python
[1, 2, 3, 4, 5, 6]
```

- **Output:**

```python
12
```

---

### Question 3 - `find_common_skills(applicants)`

A tech recruitment agency in the Sandton CBD is hosting a career fair for top South African engineering graduates. Each applicant has submitted a list of their skills. The hiring managers from various companies want to know which skills **every single applicant has in common**, so they can design a shared baseline technical test for all candidates.

Apply your logic to the `find_common_skills()` function. You will receive a dictionary where each key is an applicant's name and each value is a list of their skills. Return a set of skills that appear in **every applicant's** list.

- **Input:**

```python
{
    "Lerato": ["Python", "SQL", "Git", "Docker"],
    "Thabo":  ["Python", "SQL", "Java", "Git"],
    "Nandi":  ["Python", "SQL", "Git", "React"]
}
```

- **Output:**

```python
{"Python", "SQL", "Git"}
```

---

### Question 4 - `stage_summary(records)`

Eskom's public API has been down for weeks, but a junior developer on your team managed to pull a snapshot of load shedding incident data before it went offline. The data has been saved locally as `loadshedding.json` — a list of incidents recorded across South African suburbs, each showing which load shedding stage was active and for how long.

Your team lead needs a quick report: **how many total hours was each stage active, across all areas and all dates?**

Apply your logic to the `stage_summary()` function. It receives the list of incident records (already loaded from the JSON) and must return a dictionary where each key is a stage label (`"Stage 1"`, `"Stage 2"`, etc.) and each value is the **total hours** recorded for that stage — rounded to 2 decimal places.

Only include stages that actually appear in the data. If the input is empty, return an empty dictionary.

- **Input:** A list of incident dictionaries, e.g.:
```python
[
    {"incident_id": "ESK-20240601-001", "area": "Soweto", "municipality": "City of Johannesburg", "province": "Gauteng", "stage": 2, "duration_hours": 2.5, "date": "2024-06-01", "start_time": "06:00", "end_time": "08:30", "status": "resolved", "scheduled": true, "affected_customers": 14200},
    {"incident_id": "ESK-20240601-002", "area": "Sandton", "municipality": "City of Johannesburg", "province": "Gauteng", "stage": 4, "duration_hours": 4.0, "date": "2024-06-01", "start_time": "08:00", "end_time": "12:00", "status": "resolved", "scheduled": true, "affected_customers": 8750}
]
```

- **Output:**
```python
{"Stage 2": 2.5, "Stage 4": 4.0}
```

> **Note:** The order of keys in the returned dictionary does not matter. Your function only needs the `stage` and `duration_hours` fields — the rest of the data is there for context.



---

### Question 5 - `sliding_window_sum(numbers, window_size)`

Eskom's load management engineers in Megawatt Park, Sunninghill, are monitoring electricity consumption data collected every hour from a township substation. To smooth out spikes in the data, they use a **sliding window** technique — at each position, they calculate the total consumption across a fixed number of consecutive hours. This helps them identify sustained high-usage periods rather than single outlier readings.

Apply your logic to the `sliding_window_sum()` function. Given a list of numbers and a window size `k`, return a new list where each element is the **sum of `k` consecutive elements** starting at that position. The last window starts at index `len(numbers) - k`.

- **Input:**

```python
numbers = [2, 4, 6, 8, 10]
window_size = 3
```

- **Output:**

```python
[12, 18, 24]
```

Constraint: The output list will always have `len(numbers) - window_size + 1` elements.

---

### Question 6 - `sliding_window_sum(numbers, window_size)`


---
## Long-Format Questions

Please answer these in the `answers.txt` file (**DO NOT REMOVE THE COMMENTS AND DO NOT CHANGE THE FORMAT**)

### Comprehension Question 1 — Loops (10 Points)

A junior developer on your team at a Cape Town startup keeps writing code that works but uses the wrong loop for the job. Your tech lead has asked you to sit down with them and explain how loops work and how to decide which one to reach for.

In your own words, explain loops to this junior developer. Your explanation should cover what the different types of loops are, how they work, and most importantly how a developer decides which one to use in a given situation. Make sure your explanation is grounded in realistic situations a developer might actually find themselves in, not just theory.

---


### Comprehension Question 2 — Functions (10 Points)

You are a junior developer at a Johannesburg fintech startup. Your team is building a payment processing system and you notice that the same block of code for calculating transaction fees appears in five different places across the codebase. Every time the fee calculation needs to change, your teammate has to hunt down all five copies and update each one manually — and they keep missing some, causing bugs.
Explain what a function is in Python and how it works, why it would solve this specific problem, and what the benefit is of having the calculation logic defined in one place. Also explain what parameters and return values are, and how they would apply in this scenario.

---
### Comprehension Question 3 — APIs and HTTP (10 Points)

During your first week at a software company in Johannesburg, a non-technical product manager pulls you into a meeting and asks you to explain how the company's mobile app actually talks to the server. They've heard the word "API" thrown around constantly but have no idea what it means or how it works.

Explain APIs to this product manager in a way they can genuinely follow. Your explanation should cover what an API actually is and the role it plays, how the web communicates using HTTP, the different types of requests a client can make to a server and what each one is used for, and what an endpoint is and how it fits into the picture. You are welcome to use analogies to make your explanation clearer.

