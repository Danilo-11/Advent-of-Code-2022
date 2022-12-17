def get_win(opponent):
    if opponent == "R":
        return "P"
    elif opponent == "P":
        return "S"
    else:
        return "R"


def get_loose(opponent):
    if opponent == "R":
        return "S"
    elif opponent == "P":
        return "R"
    else:
        return "P"


def get_draw(opponent):
    return opponent


def get_play(opponent, player):
    if player == "X":
        return get_loose(opponent)
    elif player == "Y":
        return get_draw(opponent)
    else:
        return get_win(opponent)


def main():
    # part 1
    translate_opponent = {"A": "R", "B": "P", "C": "S"}
    translate_player = {"X": "R", "Y": "P", "Z": "S"}
    points = {"R": 1, "P": 2, "S": 3}
    score = 0
    draw = 3
    win = 6
    lose = 0

    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            split_line = line.split(" ")
            opponent = split_line[0]
            player = split_line[1]

            opponent = translate_opponent.get(opponent)
            player = translate_player.get(player)

            # draw
            if opponent == player:
                score += draw + points.get(player)
            elif opponent == "R" and player == "P":
                score += win + points.get(player)
            elif opponent == "R" and player == "S":
                score += lose + points.get(player)
            elif opponent == "P" and player == "R":
                score += lose + points.get(player)
            elif opponent == "P" and player == "S":
                score += win + points.get(player)
            elif opponent == "S" and player == "R":
                score += win + points.get(player)
            elif opponent == "S" and player == "P":
                score += lose + points.get(player)

    print("Score: {}".format(score))

    # part 2
    score = 0
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            split_line = line.split(" ")
            opponent = split_line[0]
            player = split_line[1]

            opponent = translate_opponent.get(opponent)

            # loose
            if player == "X":
                score += lose + points.get(get_loose(opponent))
            # draw
            elif player == "Y":
                score += draw + points.get(get_draw(opponent))
            # win
            else:
                score += win + points.get(get_win(opponent))

        print("Score: {}".format(score))


if __name__ == '__main__':
    main()
