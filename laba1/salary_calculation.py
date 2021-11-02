import decimal
import random


def calculation(input_salary: int, mark_performance_review: decimal.Decimal, lvl_engineer: int) -> int:
    # проверка условий
    if not input_salary or not mark_performance_review or not lvl_engineer:
        raise TypeError("Параметр пуст")
    if input_salary < 70000 or input_salary > 750000:
        raise ValueError("Зарплата находится за допустимыми пределами")
    if mark_performance_review < 1 or mark_performance_review > 5:
        raise ValueError("Оценка performance_review за допустимыми пределами")
    if lvl_engineer < 7 or lvl_engineer > 17:
        raise ValueError("Уровень инженера за допустимыми пределами")

    result = input_salary

    # преобразование зарплаты согласно уровню инженера
    if lvl_engineer < 10:
        result = result * 1.05
    elif 10 <= lvl_engineer < 13:
        result = result * 1.1
    elif 13 <= lvl_engineer < 15:
        result = result * 1.15
    elif lvl_engineer >= 15:
        result = result * 1.2

    # преобразование зарплаты согласно оценке performance review
    if mark_performance_review < 2:
        result = result
    elif 2 <= mark_performance_review < 2.5:
        result = result * 1.25
    elif 2.5 <= mark_performance_review < 3:
        result = result * 1.5
    elif 3 <= mark_performance_review < 3.5:
        result = result * 2
    elif 3.5 <= mark_performance_review < 4:
        result = result * 2.5
    elif mark_performance_review >= 4:
        result = result * 3

    return int(result)


if __name__ == "__main__":
    # salary_input [70 000..750 000]
    salary_input = random.randint(70000, 750000)

    # performance_review [1..5]
    performance_review = random.randint(10, 50)/10

    # level_engineer [7..17]
    level_engineer = random.randint(7, 17)

    salary_output = calculation(input_salary=salary_input, mark_performance_review=decimal.Decimal(performance_review),
                                lvl_engineer=level_engineer)
    print(f"При месячном окладе в {salary_input} рублей, при результатах performance review в {performance_review} "
          f"и уровне инженера {level_engineer} премия равна: {salary_output} рублей")
