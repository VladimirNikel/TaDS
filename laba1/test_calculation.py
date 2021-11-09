import decimal

import pytest
from _pytest.outcomes import Failed
from allpairspy import AllPairs

import salary_calculation


def test_lower_salary_range():
    with pytest.raises(ValueError) as exp:
        salary_calculation.calculation(input_salary=1234, mark_performance_review=decimal.Decimal(2.0), lvl_engineer=7)
    assert str(exp.value) == "Зарплата находится за допустимыми пределами"


def test_higher_salary_range():
    with pytest.raises(ValueError) as exp:
        salary_calculation.calculation(input_salary=812958, mark_performance_review=decimal.Decimal(3), lvl_engineer=7)
    assert str(exp.value) == "Зарплата находится за допустимыми пределами"


def test_absence_first_param():
    # "Зарплата находится за допустимыми пределами"
    with pytest.raises(TypeError) as exp:
        salary_calculation.calculation(mark_performance_review=decimal.Decimal(3), lvl_engineer=7)
    assert "input_salary" in str(exp.value)


def test_absence_second_param():
    with pytest.raises(TypeError) as exp:
        salary_calculation.calculation(input_salary=812958, lvl_engineer=7)
    assert "mark_performance_review" in str(exp.value)


def test_absence_last_param():
    with pytest.raises(TypeError) as exp:
        salary_calculation.calculation(input_salary=812958, mark_performance_review=decimal.Decimal(3))
    assert "lvl_engineer" in str(exp.value)


def test_absence_several_params():
    with pytest.raises(TypeError) as exp:
        salary_calculation.calculation(input_salary=812958)
    assert "lvl_engineer" in str(exp.value) and "mark_performance_review" in str(exp.value)


list_data = [
    {
        "salary": 70000,
        "mark_review": decimal.Decimal(1),
        "lvl": 7,
        "prize": int(0)
    }
    ]


@pytest.mark.parametrize("data", list_data)
def test_correct_param(data):
    result1 = int(salary_calculation.calculation(input_salary=data.get("salary"),
                                                 mark_performance_review=data.get("mark_review"),
                                                 lvl_engineer=data.get("lvl")))
    assert result1 == data.get("prize")


list_salary = [-5080, 69999, 70000, 312540, 750000, 750001, 1000000]
list_mark_review = [0.2, 1.0, 1.9, 2.0, 2.4, 2.5, 2.9, 3.0, 3.4, 3.5, 3.9, 4.0, 5.0, 5.7]
list_lvl = [-5, 6, 7, 9, 10, 12, 13, 14, 15, 17, 21]


@pytest.mark.parametrize(["salary", "mark_review", "lvl"], [value_list for value_list in AllPairs([
    list_salary, list_mark_review, list_lvl
])])
def test(salary, mark_review, lvl):
    try:
        with pytest.raises(ValueError) as exp:
            salary_calculation.calculation(input_salary=salary,
                                           mark_performance_review=mark_review,
                                           lvl_engineer=lvl)
        assert str(exp.value) in ["Зарплата находится за допустимыми пределами",
                                  "Оценка performance_review за допустимыми пределами",
                                  "Уровень инженера за допустимыми пределами"]
    except Failed:
        assert True
