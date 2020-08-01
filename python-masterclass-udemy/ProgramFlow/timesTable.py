
for i in range(1, 21):
    for j in range(1, 11):
        if j == 10:
            print("{0} x {1} {3:>2} {2:>3}".format(i, j, i * j, "="))
        else:
            print("{0} x {1:>2} {3:>2} {2:>3}".format(i, j, i * j, "="))
    print("------------------")

