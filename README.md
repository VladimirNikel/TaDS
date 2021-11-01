# Тестирование и отладка интернет-сервисов

## 1 лабораторная работа
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

Чтобы запустить выполнение приложения, необходимо выполнить команду `python3 ./laba1/salary_calculation.py`
