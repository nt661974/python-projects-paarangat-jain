def listMax(list=[]):
    if not list:
        return None
    else:
        return max(list)


def doTest(list):
    print("listMax(", end="")
    if list == None:
        print("None) is ", end="")
        pass
    else:
        n = len(list)
        print("[", end="")
        for i in range(0, n):
            print("{}".format(list[i]), end="")
            if i < n - 1:
                print(", ", end="")
                pass
            pass
        print("]) is ", end="")
        pass
    max = listMax(list)
    if max == None:
        print("None")
        pass
    else:
        print("{}".format(max))
        pass
    pass


def main():
    list1 = [77, 33, 19, 99, 42, 6, 27, 4]
    list2 = [-3, -42, -99, -1000, -999, -88, -77]
    list3 = [425, 59, -3, 77, 0, 36]
    doTest(list1)
    doTest(list2)
    doTest(list3)
    doTest(None)
    doTest([])
    return 0


if __name__ == "__main__":
    main()
    pass
