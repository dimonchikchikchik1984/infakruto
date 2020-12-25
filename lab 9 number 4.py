import numpy as np
from random import randint


class PrintVariance(Exception):
    pass


class PrintMean(Exception):
    pass


class PrintCount(Exception):
    pass


def server_coroutine():
    aggregator = []
    try:
        while True:
            try:
                to_add = yield
                aggregator.append(to_add)
            except PrintVariance:
                yield np.var(aggregator)
            except PrintMean:
                yield np.mean(aggregator)
            except PrintCount:
                yield len(aggregator)
    finally:
        pass



if __name__ == "__main__":

    coroutine = server_coroutine()
    next(coroutine)

    for i in range(randint):

        coroutine.send(i)
        if i % 2 == 0:
            print( coroutine.throw(PrintVariance))
            next(coroutine)
        if i % 3 == 0:
            print(coroutine.throw(PrintMean))
            next(coroutine)
        if i % 5 == 0:
            print(coroutine.throw(PrintCount))
            next(coroutine)

    coroutine.close()