with open("something.txt", "w") as out:
    for i in range(100):
        out.write("А я запишу все эти строки в влюбом случае\n")
    raise Exception