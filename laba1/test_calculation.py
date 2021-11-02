import pytest
from allpairspy import AllPairs

import decimal
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


def test_correct_param():
    engineer1 = {
        "salary": 70000,
        "mark_review": decimal.Decimal(1),
        "lvl": 7,
        "prize": int(70000 * 1.05 * 1)
    }
    engineer2 = {
        "salary": 70001,
        "mark_review": decimal.Decimal(1.1),
        "lvl": 8,
        "prize": int(70001 * 1.05 * 1)
    }
    engineer3 = {
        "salary": 312700,
        "mark_review": decimal.Decimal(3.7),
        "lvl": 13,
        "prize": int(312700 * 1.15 * 2.5)
    }
    engineer4 = {
        "salary": 749999,
        "mark_review": decimal.Decimal(4.9),
        "lvl": 16,
        "prize": int(749999 * 1.2 * 3)
    }
    engineer5 = {
        "salary": 750000,
        "mark_review": decimal.Decimal(5),
        "lvl": 17,
        "prize": int(750000 * 1.2 * 3)
    }
    result1 = salary_calculation.calculation(input_salary=engineer1.get("salary"),
                                             mark_performance_review=engineer1.get("mark_review"),
                                             lvl_engineer=engineer1.get("lvl"))
    assert result1 == engineer1.get("prize")
    result2 = salary_calculation.calculation(input_salary=engineer2.get("salary"),
                                             mark_performance_review=engineer2.get("mark_review"),
                                             lvl_engineer=engineer2.get("lvl"))
    assert result2 == engineer2.get("prize")
    result3 = salary_calculation.calculation(input_salary=engineer3.get("salary"),
                                             mark_performance_review=engineer3.get("mark_review"),
                                             lvl_engineer=engineer3.get("lvl"))
    assert result3 == engineer3.get("prize")
    result4 = salary_calculation.calculation(input_salary=engineer4.get("salary"),
                                             mark_performance_review=engineer4.get("mark_review"),
                                             lvl_engineer=engineer4.get("lvl"))
    assert result4 == engineer4.get("prize")
    result5 = salary_calculation.calculation(input_salary=engineer5.get("salary"),
                                             mark_performance_review=engineer5.get("mark_review"),
                                             lvl_engineer=engineer5.get("lvl"))
    assert result5 == engineer5.get("prize")


class TestParametrized(object):

    @pytest.mark.parametrize(["salary", "mark_review", "lvl"], [value_list for value_list in AllPairs([
        list(range(70000, 750000, 5000)),
        [decimal.Decimal(num/10) for num in range(10, 50)],
        list(range(7, 17, 1))
    ])])
    def test(self, salary, mark_review, lvl):
        assert salary_calculation.calculation(input_salary=salary,
                                              mark_performance_review=mark_review,
                                              lvl_engineer=lvl)
