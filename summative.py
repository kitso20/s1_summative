
# ============================
# TODO: Question 1
# ============================

def reverse_list(items: list) -> list:

    return items[::-1]


# ============================
# TODO: Question 2
# ============================

def sum_even_numbers(numbers: list[int]) -> int:


    return sum([i for i in numbers if i % 2 == 0])

# ============================
# TODO:Question 3
# ============================

def find_common_skills(applicants: dict[str, list[str]]) -> set[str]:
    result = []
    for k,v in applicants.items():
        for i in v:
            result.append(i)
    return set([i for i in result if result.count(i) == len(applicants)])



# ============================
# TODO:Question 4
# ============================
def stage_summary(records):
    res = {}
    if len(records) == 0:
        return {}
    for item in records:
        
            num = item['stage']
            if f'Stage {num}' not in res:
                res[f'Stage {num}'] = 0
                res[f'Stage {num}'] += item["duration_hours"]
            else:
                res[f'Stage {num}'] += item["duration_hours"]
    return {k:round(v,2) for k,v in res.items()}
    
stage_summary([
                {"incident_id": f"ESK-00{i}", "area": f"Area {i}", "municipality": "CoJ", "province": "Gauteng",
                 "stage": 1, "duration_hours": 2.0, "date": f"2024-06-0{i}", "start_time": "06:00",
                 "end_time": "08:00", "status": "resolved", "scheduled": True, "affected_customers": 5000}
                for i in range(1, 4)
            ])



# ============================
# TODO:Question 5
# ============================

def sliding_window_sum(numbers: list[int], window_size: int) -> list[int]:
    res = []
    for i in range(len(numbers) - window_size + 1):
        res.append(sum(numbers[i:i + window_size]))

    return res