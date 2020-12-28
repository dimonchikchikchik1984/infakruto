import pickle


def test_pickle(inp):
    with open('file.pickle', 'wb') as f:
        pickle.dump(inp, f)

    with open('file.pickle', 'rb') as f:
        out = pickle.load(f)

    return "Worked"


if __name__ == "__main__":
    info = iter([range(5)])
    print(test_pickle(info))
    func = print
    print(test_pickle(func))
