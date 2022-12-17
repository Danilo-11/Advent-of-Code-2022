def get_start_of_packet_marker(signal):
    """Part 1"""
    for i in range(0, len(signal)):
        num_of_chars = i + 4
        marker = signal[i:num_of_chars]

        if len(set(marker)) == len(marker):
            return num_of_chars

    return -1


def get_start_of_message_marker(signal):
    """Part 2"""
    for i in range(0, len(signal)):
        num_of_chars = i + 14
        marker = signal[i:num_of_chars]

        if len(set(marker)) == len(marker):
            return num_of_chars

    return -1


def main():
    with open('input.txt') as f:
        signal = f.readline()
        signal = signal.strip()

    print("characters before first start-of-packet marker:", get_start_of_packet_marker(signal))
    print("characters before first start-of-message marker:", get_start_of_message_marker(signal))


if __name__ == '__main__':
    main()
