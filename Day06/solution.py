from collections import deque


def find_marker(line: str, marker_len: int) -> int:
    last_chars = deque()
    index = 0
    for char in line:
        index += 1
        last_chars.append(char)
        if len(last_chars) > marker_len:
            last_chars.popleft()
        if len(set(last_chars)) == marker_len:
            return index
    return -1


def main() -> None:
    line: str = ""
    with open("input.txt", "r") as file:
        line = file.readline().strip()

    print(find_marker(line, 4))
    print(find_marker(line, 14))


if __name__ == "__main__":
    main()
