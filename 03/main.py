import string


def main():
    # part 1
    priorities = list(string.ascii_letters)
    similarities = []

    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            split_at = int(len(line) / 2)
            left, right = line[:split_at], line[split_at:]
            similar = set(left) & set(right)
            similarities.extend(list(similar))

    sum_of_priorities = 0
    for x in similarities:
        sum_of_priorities += priorities.index(x) + 1

    print("Part 1\nSum of priorities:", sum_of_priorities)

    # part 2
    similarities = []
    with open('input.txt') as f:
        lines = f.readlines()

        for index in range(0, len(lines), 3):
            triple = lines[index:index + 3]
            similar = set(triple[0].strip()) & set(triple[1].strip()) & set(triple[2].strip())
            similarities.extend(list(similar))

    sum_of_priorities = 0
    for x in similarities:
        sum_of_priorities += priorities.index(x) + 1

    print("\nPart 2\nSum of priorities:", sum_of_priorities)


if __name__ == '__main__':
    main()
