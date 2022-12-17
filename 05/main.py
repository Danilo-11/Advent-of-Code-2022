import re
from copy import deepcopy


def read_instruction(instruction):
    # 'move 1 from 3 to 5\n'
    instruction = instruction.strip()
    move = re.findall("\d{1,2}", instruction)
    move = [int(x) for x in move]
    return move


def main():
    # part 1
    starting_stacks = []
    lines_to_skip = 0
    with open('input.txt') as f:
        line = "s"
        while line != "":
            line = f.readline()
            line = line.strip()
            starting_stacks.append(line)
            lines_to_skip += 1

    # remove empty line
    starting_stacks.pop()

    # check how many stacks are needed
    num_of_stacks = int(starting_stacks.pop().split("   ")[-1])

    stacks1 = []
    for i in range(num_of_stacks):
        new_list = []
        stacks1.append(new_list)

    for element in reversed(starting_stacks):
        element = element.replace("    ", " [_]")
        element = element.replace("[", "")
        element = element.replace("]", "")

        splitted = element.split(" ")

        # add empty place if missing
        for i in range(len(splitted), num_of_stacks):
            splitted.append("_")

        for i in range(num_of_stacks):
            if splitted[i] != "_":
                stacks1[i].append(splitted[i])

    stacks2 = deepcopy(stacks1)

    # get instructions
    with open('input.txt') as f:
        lines = f.readlines()

    # skip the first lines that are not instructions
    instructions = lines[lines_to_skip:]

    for instruction in instructions:
        num_of_crates, start, end = read_instruction(instruction)

        # move crates (part 1)
        for i in range(num_of_crates):
            stacks1[end - 1].append(stacks1[start - 1].pop())

        # move crates (part 2)
        stacks2[end - 1].extend(stacks2[start - 1][-num_of_crates:])
        del(stacks2[start - 1][-num_of_crates:])

    # print stacks
    for stack in stacks1:
        print(stack)

    print("\nTop crate names:")
    for stack in stacks1:
        print(stack[-1], end="")

    print("\n")

    # part 2
    # print stacks
    for stack in stacks2:
        print(stack)

    print("\nTop crate names:")
    for stack in stacks2:
        print(stack[-1], end="")



if __name__ == '__main__':
    main()
