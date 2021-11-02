# 1 лабораторная работа. Т
> Необходимо реализовать механизм расчета премии по результатам Performance Review программиста.
> Для предоставляемых данных:
> - ЗП инженера - [70 000..750 000] (только целочисленные значения или преобразование ЗП в таковое)
> - Результат квартального Performance Review [1..5]
> - Уровень инженера - [7..17]
> - Размер премии от квартальной ЗП:
>   - 5% если lvl < 10;
>   - 10% если 10 <= lvl < 13
>   - 15% если 13 <= lvl < 15
>   - 20% если lvl >= 15
> - Модификатор премии:
>   - 0% - если результат pref-review < 2 
>   - 25% - если 2 <= результат pref-review < 2.5
>   - 50% - если 2.5 <= результат pref-review < 3
>   - 100% - если 3 <= результат pref-review < 3.5 
>   - 150% - если 3.5 <= результат pref-review < 4 
>   - 200% - если результат pref-review >= 4
>
> (!) С применением практик тест-дизайна.
> 
> (!) Написать ПО, которое не будет иметь багов.


## Ход работы:

Чтобы запустить выполнение приложения, необходимо выполнить команду ```python3 salary_calculation.py```

Чтобы запустить тестирование сервиса, необходимо выполнить команду ```python3 -m pytest -rA test_calculation.py```


## Результаты выполнения тестирования

При таком виде класса тестирования
```python
class TestParametrized(object):

    @pytest.mark.parametrize(["salary", "mark_review", "lvl"], [value_list for value_list in AllPairs([
        list(range(70000, 750000, 5000)),
        [decimal.Decimal(num/10) for num in range(10, 50)],
        list(range(7, 17, 1))
    ])])
    def test(self, salary, mark_review, lvl):
        result = salary_calculation.calculation(input_salary=salary, 
                                                mark_performance_review=mark_review, 
                                                lvl_engineer=lvl)
        print(f"{salary} {mark_review} {lvl} {result}")
        assert result
```

Получены результаты тестирования, приведенные в файле `result_test_with_print.md`



А при таком виде класса тестирования
```python
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
```

Получены результаты тестирования, приведенные в файле `result_test.md`



## Инструменты:
- **GIT** (устанавливается командой `sudo apt install git -y`)
- **Python** (устанавливается командой `sudo apt install python3 -y`)
- Установщик пакетов **Python PIP3** (устанавливается командой `sudo apt install python3-pip -y`)
- Установленные **модули**:
    + **pytest** `sudo pip3 install pytest`
    + **allpairspy** `sudo pip3 install allpairspy`