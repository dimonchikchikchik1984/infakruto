class Mother:
    def __str__(self):
        return'Mother'
    pass


class Daughter(Mother):
    def __str__(self):
        return'Daughter'
    pass


if __name__ == "__main__":
    m=Mother()
    d=Daughter()
    print(m, d)


