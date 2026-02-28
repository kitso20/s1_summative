import copy
import json
import random
import pytest

random.seed(42)

from summative import (
    reverse_list,
    sum_even_numbers,
    find_common_skills,
    stage_summary,
    sliding_window_sum,
)

_SKILLS_POOL = ["Python", "SQL", "Git", "Docker", "Java", "React", "Rust", "Go", "Kotlin", "C++"]

_REVERSE_CASES = [
    (items, list(reversed(items)))
    for _ in range(20)
    for items in [[random.randint(-100, 100) for _ in range(random.randint(1, 15))]]
]

_SUM_EVEN_CASES = [
    (numbers, sum(n for n in numbers if n % 2 == 0))
    for _ in range(20)
    for numbers in [[random.randint(-50, 50) for _ in range(random.randint(1, 15))]]
]

_COMMON_SKILLS_CASES = [
    (applicants, skill_sets[0].intersection(*skill_sets[1:]))
    for _ in range(20)
    for common in [set(random.sample(_SKILLS_POOL, random.randint(1, 3)))]
    for applicants in [{
        name: list(common | (set(random.sample(_SKILLS_POOL, random.randint(1, 4))) - common))
        for name in random.sample(["A", "B", "C", "D", "E"], random.randint(2, 4))
    }]
    for skill_sets in [[set(v) for v in applicants.values()]]
]

_SLIDING_CASES = [
    (nums, w, [sum(nums[i:i + w]) for i in range(len(nums) - w + 1)])
    for _ in range(20)
    for n in [random.randint(3, 15)]
    for nums in [[random.randint(1, 100) for _ in range(n)]]
    for w in [random.randint(1, n)]
]


class TestMyDataStructuresAssessment:

    # ─────────────────────────────────────────────
    # Question 1 - reverse_list
    # ─────────────────────────────────────────────

    @pytest.mark.parametrize("items, expected", [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([10], [10]),
        ([], []),
        (["a", "b", "c"], ["c", "b", "a"]),
        ([True, False, True], [True, False, True]),
        *_REVERSE_CASES,
    ])
    def test_reverse_list(self, items, expected):
        original = list(items)
        result = reverse_list(items)
        assert isinstance(result, list)
        assert result == expected
        assert items == original

    # ─────────────────────────────────────────────
    # Question 2 - sum_even_numbers
    # ─────────────────────────────────────────────

    @pytest.mark.parametrize("numbers, expected", [
        ([1, 2, 3, 4, 5, 6], 12),
        ([1, 3, 5, 7], 0),
        ([2, 4, 6, 8], 20),
        ([], 0),
        ([0, 1, 2], 2),
        ([-2, -3, -4], -6),
        *_SUM_EVEN_CASES,
    ])
    def test_sum_even_numbers(self, numbers, expected):
        result = sum_even_numbers(numbers)
        assert isinstance(result, int)
        assert result == expected

    # ─────────────────────────────────────────────
    # Question 3 - find_common_skills
    # ─────────────────────────────────────────────

    @pytest.mark.parametrize("applicants, expected", [
        (
            {"Lerato": ["Python", "SQL", "Git", "Docker"], "Thabo": ["Python", "SQL", "Java", "Git"], "Nandi": ["Python", "SQL", "Git", "React"]},
            {"Python", "SQL", "Git"},
        ),
        (
            {"Alice": ["Python", "Go"], "Bob": ["Java", "Rust"]},
            set(),
        ),
        (
            {"Solo": ["Python", "SQL", "Docker"]},
            {"Python", "SQL", "Docker"},
        ),
        (
            {"A": ["Python", "SQL", "Go"], "B": ["Python", "Java", "Rust"], "C": ["Python", "C++", "Kotlin"]},
            {"Python"},
        ),
        ({}, set()),
        *_COMMON_SKILLS_CASES,
    ])
    def test_find_common_skills(self, applicants, expected):
        result = find_common_skills(applicants)
        assert isinstance(result, set)
        assert result == expected
        all_skill_lists = [set(v) for v in applicants.values()]
        for skill in result:
            assert all(skill in skill_set for skill_set in all_skill_lists)

    # ─────────────────────────────────────────────
    # Question 4 - stage_summary
    # ─────────────────────────────────────────────

    @pytest.mark.parametrize("records, expected", [
        ([], {}),

        (
            [{"incident_id": "ESK-001", "area": "Soweto", "municipality": "CoJ", "province": "Gauteng",
              "stage": 2, "duration_hours": 2.5, "date": "2024-06-01", "start_time": "06:00",
              "end_time": "08:30", "status": "resolved", "scheduled": True, "affected_customers": 14200}],
            {"Stage 2": 2.5}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Soweto",  "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 2.5, "date": "2024-06-01", "start_time": "06:00",
                 "end_time": "08:30", "status": "resolved", "scheduled": True, "affected_customers": 14200},
                {"incident_id": "ESK-002", "area": "Sandton", "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 1.5, "date": "2024-06-02", "start_time": "09:00",
                 "end_time": "10:30", "status": "resolved", "scheduled": True, "affected_customers": 8750},
            ],
            {"Stage 2": 4.0}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Soweto",  "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 2.5, "date": "2024-06-01", "start_time": "06:00",
                 "end_time": "08:30", "status": "resolved", "scheduled": True, "affected_customers": 14200},
                {"incident_id": "ESK-002", "area": "Sandton", "municipality": "CoJ", "province": "Gauteng",
                 "stage": 4, "duration_hours": 4.0, "date": "2024-06-01", "start_time": "08:00",
                 "end_time": "12:00", "status": "resolved", "scheduled": True, "affected_customers": 8750},
            ],
            {"Stage 2": 2.5, "Stage 4": 4.0}
        ),

        (
            [
                {"incident_id": f"ESK-00{i}", "area": f"Area {i}", "municipality": "CoJ", "province": "Gauteng",
                 "stage": 1, "duration_hours": 2.0, "date": f"2024-06-0{i}", "start_time": "06:00",
                 "end_time": "08:00", "status": "resolved", "scheduled": True, "affected_customers": 5000}
                for i in range(1, 4)
            ],
            {"Stage 1": 6.0}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Bellville",      "municipality": "CoCT", "province": "Western Cape",
                 "stage": 1, "duration_hours": 1.0, "date": "2024-06-01", "start_time": "09:00",
                 "end_time": "10:00", "status": "resolved", "scheduled": True, "affected_customers": 3200},
                {"incident_id": "ESK-002", "area": "Khayelitsha",     "municipality": "CoCT", "province": "Western Cape",
                 "stage": 2, "duration_hours": 2.0, "date": "2024-06-01", "start_time": "10:00",
                 "end_time": "12:00", "status": "resolved", "scheduled": True, "affected_customers": 29500},
                {"incident_id": "ESK-003", "area": "Mitchells Plain", "municipality": "CoCT", "province": "Western Cape",
                 "stage": 3, "duration_hours": 3.0, "date": "2024-06-01", "start_time": "13:00",
                 "end_time": "16:00", "status": "resolved", "scheduled": False, "affected_customers": 21000},
            ],
            {"Stage 1": 1.0, "Stage 2": 2.0, "Stage 3": 3.0}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Centurion", "municipality": "CoT", "province": "Gauteng",
                 "stage": 6, "duration_hours": 5.0, "date": "2024-06-03", "start_time": "10:00",
                 "end_time": "15:00", "status": "resolved", "scheduled": True, "affected_customers": 33000},
                {"incident_id": "ESK-002", "area": "Germiston",  "municipality": "Ekurhuleni", "province": "Gauteng",
                 "stage": 6, "duration_hours": 3.0, "date": "2024-06-03", "start_time": "13:00",
                 "end_time": "16:00", "status": "resolved", "scheduled": True, "affected_customers": 11200},
            ],
            {"Stage 6": 8.0}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Soweto",  "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 1.1, "date": "2024-06-01", "start_time": "06:00",
                 "end_time": "07:06", "status": "resolved", "scheduled": True, "affected_customers": 5000},
                {"incident_id": "ESK-002", "area": "Sandton", "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 2.2, "date": "2024-06-02", "start_time": "08:00",
                 "end_time": "10:12", "status": "resolved", "scheduled": True, "affected_customers": 5000},
            ],
            {"Stage 2": 3.3}
        ),
    ])
    def test_stage_summary_logic(self, records, expected):
        assert stage_summary(records) == expected



    def _make_record(self, i, stage, duration_hours):
        """Helper to build a realistic full record."""
        return {
            "incident_id": f"ESK-{i:05d}",
            "area": f"Area {i}",
            "municipality": "City of Johannesburg",
            "province": "Gauteng",
            "stage": stage,
            "duration_hours": duration_hours,
            "date": f"2024-06-{(i % 28) + 1:02d}",
            "start_time": "06:00",
            "end_time": "08:00",
            "status": "resolved",
            "scheduled": True,
            "affected_customers": 5000 + i
        }

    @pytest.mark.parametrize("stage, num_records, hours_each", [
        (1,  5,  2.0),
        (2, 10,  1.5),
        (3,  3,  4.0),
        (4,  7,  0.5),
        (6, 20,  3.0),
    ])
    def test_stage_summary_single_stage_computed_total(self, stage, num_records, hours_each):
        records = [self._make_record(i, stage, hours_each) for i in range(num_records)]
        expected_total = round(num_records * hours_each, 2)
        result = stage_summary(records)

        assert f"Stage {stage}" in result
        assert result[f"Stage {stage}"] == expected_total
        assert len(result) == 1  


    @pytest.mark.parametrize("stage_config", [
        {1: (5,  2.0), 2: (3,  1.5)},
        {2: (4,  3.0), 4: (6,  2.5), 6: (2,  5.0)},
        {1: (1,  1.0), 2: (2,  2.0), 3: (3,  3.0), 4: (4, 4.0)},
        {3: (10, 0.5), 6: (10, 0.5)},
        {1: (8,  1.25), 2: (5, 2.75), 3: (3, 0.5), 4: (7, 1.0), 6: (4, 3.5)},
    ])
    def test_stage_summary_multi_stage_computed_totals(self, stage_config):
        records = []
        idx = 0
        for stage, (count, hours) in stage_config.items():
            for _ in range(count):
                records.append(self._make_record(idx, stage, hours))
                idx += 1

        result = stage_summary(records)

        assert len(result) == len(stage_config)
        for stage, (count, hours) in stage_config.items():
            key = f"Stage {stage}"
            expected = round(count * hours, 2)
            assert key in result, f"{key} missing from result"
            assert result[key] == expected, f"{key}: expected {expected}, got {result[key]}"




    def test_stage_summary_no_phantom_stages(self):
        records = [
            self._make_record(0, 2, 2.0),
            self._make_record(1, 4, 3.0),
        ]
        result = stage_summary(records)
        assert set(result.keys()) == {"Stage 2", "Stage 4"}


    def test_stage_summary_large_scale(self):
        stages = [1, 2, 3, 4]
        hours_each = 2.0
        records = [self._make_record(i, stages[i % 4], hours_each) for i in range(1000)]
        result = stage_summary(records)

        assert len(result) == 4
        for stage in stages:
            expected = round(250 * hours_each, 2)
            assert result[f"Stage {stage}"] == expected


    def test_stage_summary_loaded_from_json(self):
        with open("loadshedding.json", "r") as f:
            records = json.load(f)

        result = stage_summary(records)

        expected = {}
        for record in records:
            key = f"Stage {record['stage']}"
            expected[key] = round(expected.get(key, 0) + record['duration_hours'], 2)

        assert isinstance(result, dict)
        assert all(k.startswith("Stage ") for k in result.keys())
        assert result == expected



    def test_stage_summary_returns_dict(self):
        result = stage_summary([self._make_record(0, 2, 2.0)])
        assert isinstance(result, dict)

    def test_stage_summary_empty_returns_dict(self):
        result = stage_summary([])
        assert result == {}
        assert isinstance(result, dict)

    def test_stage_summary_values_are_numeric(self):
        result = stage_summary([self._make_record(0, 2, 2.0)])
        for val in result.values():
            assert isinstance(val, (int, float)), f"Expected numeric, got {type(val)}"

    def test_stage_summary_immutability(self):
        records = [
            self._make_record(0, 2, 2.5),
            self._make_record(1, 4, 4.0),
        ]
        original = copy.deepcopy(records)
        stage_summary(records)
        assert records == original, "Input was mutated!"


    # ─────────────────────────────────────────────
    # Question 5 - sliding_window_sum
    # ─────────────────────────────────────────────

    @pytest.mark.parametrize("numbers, window_size, expected", [
        ([2, 4, 6, 8, 10], 3, [12, 18, 24]),
        ([3, 7, 2, 5], 1, [3, 7, 2, 5]),
        ([1, 2, 3, 4], 4, [10]),
        ([10, 20, 30, 40, 50], 2, [30, 50, 70, 90]),
        ([5, 5, 5, 5, 5], 3, [15, 15, 15]),
        *_SLIDING_CASES,
    ])
    def test_sliding_window_sum(self, numbers, window_size, expected):
        result = sliding_window_sum(numbers, window_size)
        assert isinstance(result, list)
        assert len(result) == len(numbers) - window_size + 1
        for i, total in enumerate(result):
            assert total == sum(numbers[i:i + window_size])
        assert result == expected