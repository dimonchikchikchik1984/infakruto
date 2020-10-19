def cool_wrap(func):
    def wrapper(inlist):
        otvet = func(inlist)
        if otvet==0:
            return('Нет(')
        elif otvet > 10:
            return('Очень много')
        else:
            return otvet
    return wrapper


@cool_wrap
def f(list):
    k = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            k += 1
    return k
