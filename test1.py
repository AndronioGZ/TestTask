#==========
#Вопрос 1:
#==========

def IsEven(value):
    if((value & 1) == 0):
        print("Even")
    else:
        print("Not Even")

"""В предлагаемом варианте используется оператор получения остатка от деления, и проверяется равенство результата нулю, соответственно если проверять остаток от деления на 2, получится либо 0(четное) либо 1(нечетное). При работе с отрицательными числами в Python можно получить не тот результат, что интуитивно ожидается.

Я решил использовать побитовую логическую операцию, чтобы "обнулить" все биты кроме 1го, и "проверить" его. Например, 00100101 & 00000001 выдаст 00000001.  В двоичной системе счисления все числа, заканчивающиеся на 0 четные, на 1 - нечетные. Проблема с отрицательными значениями не должна всплыть, т.к. за знак числа будет отвечать другой бит."""