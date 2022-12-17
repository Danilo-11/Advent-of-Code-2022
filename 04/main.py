def check(first, second):
    if (first[0] >= second[0] and first[1] <= second[1]) or (
            second[0] >= first[0] and second[1] <= first[1]
    ):
        return True
    else:
        return False


def check2(first, second):
    min1, max1 = first
    min2, max2 = second

    if (min1 >= min2 and min1 <= max2) or (min2 >= min1 and min2 <= max1):
        return True

    return False


def main():
    # part 1
    count = 0
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            left, right = line.split(",")
            # print(left, right)

            first = left.split("-")
            second = right.split("-")

            first = [int(x) for x in first]
            second = [int(x) for x in second]

            if check(first, second):
                count += 1
                print(line)

    print(count)

    # part 2
    count = 0
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            left, right = line.split(",")
            # print(left, right)

            first = left.split("-")
            second = right.split("-")

            first = [int(x) for x in first]
            second = [int(x) for x in second]
            if check2(first, second):
                count += 1
                print(line)

    print(count)


if __name__ == '__main__':
    main()
