import multiprocessing


def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [multiprocessing.Process(target=worker()) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)

#function must accept in the input some arguments. In another case we should write empty brackets