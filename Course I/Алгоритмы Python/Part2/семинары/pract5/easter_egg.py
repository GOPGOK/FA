"""
выполните расчет временных затрат для 5 функций работы со списками и работы с массивами,
и выскажите обоснованное предположение полученной разницы во времени исполнения
"""
# Очевидно, что из-за специфики реализации массивы намного быстрее выполняются т.к. хранят не ссылки на объекты, а непосредственно объекты + у них фиксированный тип

import array as ar
import timeit

import numpy as np

ar1 = ar.array("i", [1, 2, 2, 3, 4])
ar2 = ar.array(
    "i",
    [
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
    ]
    * 10000,
)
sp1 = [1, 2, 2, 3, 4]
sp2 = [
    1,
    2,
    2,
    3,
    4,
    1,
    2,
    2,
    3,
    4,
    1,
    2,
    2,
    3,
    4,
    1,
    2,
    2,
    3,
    4,
    1,
    2,
    2,
    3,
    4,
    1,
    2,
    2,
    3,
    4,
    1,
    2,
    2,
    3,
    4,
] * 10000
np1 = np.array([1, 2, 2, 3, 4])
np2 = np.array(
    [
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
        1,
        2,
        2,
        3,
        4,
    ]
    * 10000
)
a = timeit.default_timer()
len(ar1)
print(
    "\nвремя на измерение длины массива array из 5 элементов",
    timeit.default_timer() - a,
)
a = timeit.default_timer()
len(ar2)
print(
    "время на измерение длины массива array из 350000 элементов",
    timeit.default_timer() - a,
)

a = timeit.default_timer()
np1.shape[0]
print(
    "\nвремя на измерение длины массива numpy из 5 элементов",
    timeit.default_timer() - a,
)

a = timeit.default_timer()
np2.shape[0]
print(
    "время на измерение длины массива numpy из 350000 элементов",
    timeit.default_timer() - a,
)

a = timeit.default_timer()
len(sp1)
print("\nвремя на измерение длины списка из 5 элементов", timeit.default_timer() - a)
a = timeit.default_timer()
len(sp2)
print("время на измерение длины списка из 350000 элементов", timeit.default_timer() - a)
