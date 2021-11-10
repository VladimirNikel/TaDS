import decimal
import random


def calculation(input_salary: int, mark_performance_review: decimal.Decimal, lvl_engineer: int) -> int:
    """
    Необходимо реализовать механизм расчета премии по результатам Performance Review программиста.
    Для предоставляемых данных:
    - ЗП инженера - [70 000..750 000] (только целочисленные значения или преобразование ЗП в таковое)
    - Результат квартального Performance Review [1..5]
    - Уровень инженера - [7..17]
    - Размер премии от квартальной ЗП:
        - 5% если lvl < 10;
        - 10% если 10 <= lvl < 13
        - 15% если 13 <= lvl < 15
        - 20% если lvl >= 15
    > - Модификатор премии:
    >   - 0% - если результат pref-review < 2
    >   - 25% - если 2 <= результат pref-review < 2.5
    >   - 50% - если 2.5 <= результат pref-review < 3
    >   - 100% - если 3 <= результат pref-review < 3.5
    >   - 150% - если 3.5 <= результат pref-review < 4
    >   - 200% - если результат pref-review >= 4
    """

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

    # преобразование премии согласно уровню инженера
    if lvl_engineer < 10:
        result = result * 0.05
    elif 10 <= lvl_engineer < 13:
        result = result * 0.1
    elif 13 <= lvl_engineer < 15:
        result = result * 0.15
    elif lvl_engineer >= 15:
        result = result * 0.2

    # преобразование премии согласно оценке performance review
    if mark_performance_review < 2:
        result = result * 0
    elif 2 <= mark_performance_review < 2.5:
        result = result * 0.25
    elif 2.5 <= mark_performance_review < 3:
        result = result * 0.5
    elif 3 <= mark_performance_review < 3.5:
        result = result * 1
    elif 3.5 <= mark_performance_review < 4:
        result = result * 1.5
    elif mark_performance_review >= 4:
        result = result * 2

    return int(result)


if __name__ == "__main__":
    # salary_input [70 000..750 000]
    salary_input = random.randint(70000, 750000)

    # performance_review [1..5]
    performance_review = random.randint(10, 50)/10

    # level_engineer [7..17]
    level_engineer = random.randint(7, 17)

    bonus_output = calculation(input_salary=salary_input, mark_performance_review=decimal.Decimal(performance_review),
                               lvl_engineer=level_engineer)
    print(f"При месячном окладе в {salary_input} рублей, при результатах performance review в {performance_review} "
          f"и уровне инженера {level_engineer} премия равна: {bonus_output} рублей")
