#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marine
#


def main():
    x, y = 100, 100

    # # conditional flow uses if, elif, else
    # if x < y:
    #     results = "X is less than Y"
    # elif x == y:
    #     results = "X is the same as Y"
    # else:
    #     results = "X is greater than Y"
    # print(results)
    # # conditional statements let you use "a if C else b"
    # results = "X is less than Y" if x < y else "X is greater or equal to Y"
    # print(results)
    # match-case makes it easy to compare multiple values
    value = 'tw'
    match value:
        case 'one':
            result = 1
        case 'two':
            result = 2
        case 'three' | 'four':
            result = (3, 4)
        case _:
            result = -1

    print(result)


if __name__ == "__main__":
    main()
