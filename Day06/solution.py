from collections import deque


def find_marker(line: str, marker_len: int) -> int:
    last_chars = deque()
    for i in range(0, len(line)):
        last_chars.append(line[i])
        if len(last_chars) > marker_len:
            last_chars.popleft()
        if len(set(last_chars)) == marker_len:
            return i + 1
    return -1


def main() -> None:
    line: str = ""
    with open("input.txt", "r") as file:
        line = file.readline().strip()

    print(find_marker(line, 4))
    print(find_marker(line, 14))


if __name__ == "__main__":
    main()
