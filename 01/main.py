def main():
    list_of_calories = []
    calories = 0
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if line != "":
                calories += int(line)
            else:
                list_of_calories.append(calories)
                calories = 0

    # get the biggest calorie amount
    max_value = max(list_of_calories)
    max_index = list_of_calories.index(max_value)
    print(max_value)
    print(max_index)

    # get the sum of the 3 biggest amounts of calorie
    list_of_calories.sort(reverse=True)
    top_3 = list_of_calories[0] + list_of_calories[1] + list_of_calories[2]
    print(top_3)


if __name__ == '__main__':
    main()
