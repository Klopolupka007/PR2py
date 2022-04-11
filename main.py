import random


def first():
    s = ["1", "2", "32", "43e2", "1", "3", "32", "2", "4"]
    for i in s:
        i = float(i)

    str = []
    for i in s:
        if (len(str) == 0):
            str.append(i)
        else:
            for y in range(0, len(str)):
                if (str[y] == i):
                    break
                elif (y == len(str) - 1):
                    str.append(i)
                    print(i)

    for i in range(0, int(len(s) / 2)):
        y = s[i]
        s[i] = s[len(s) - i - 1]
        s[len(s) - i - 1] = y


def searchX(x):
    str = []
    s = ["1", "2", "32", "43e2", "1", "3", "32", "2", "4"]
    print()
    y = 0
    for i in s:
        if i == x:
            str.append(y)
        y += 1
    print(str)


def EvenSum(s):
    print(sum(x for i, x in enumerate(s) if i % 2 == 0))


def MaxStr():
    s = ["1", "2", "32", "43e2", "1", "3", "32", "2", "4"]
    print(s, max(s))


if __name__ == '__main__':
    first()
    searchX("1")
    s = []
    for i in range(0, 10):
        s.append(random.randint(0, 10000))
    EvenSum(s)
    MaxStr()

    # 2 задание
    i = 0
    ['much','c','w'][i]

    # 3 задание
    x = [0xf or _ in 'abc']
    # Питон не обрабатывает часть после 0xf, поэтому и результат [15]

