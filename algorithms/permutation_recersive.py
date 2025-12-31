def jaygasht(l, temp=[]):
    if not l:
        print(temp)
    else:
        for i in range(len(l)):
            jaygasht(l[:i] + l[i + 1 :], temp + [l[i]])


numbers = [1, 2, 3, 4]
jaygasht(numbers)
