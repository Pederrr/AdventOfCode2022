from typing import List


def calculate_priority(char: str) -> int:
    if char.islower():
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27


def find_common_item(strings: List[str]) -> str:
    common_chars = set(strings[0])
    for string in strings:
        common_chars = common_chars.intersection(set(string))
    assert(len(common_chars) == 1)
    return common_chars.pop()


def main() -> None:
    priorities = 0
    group_priorities = 0
    with open("input.txt", "r") as file:
        line_count = 0
        lines: List[str] = []
        for line in file:
            line_count += 1
            line = line.strip();
            lines.append(line)

            first_compartment = line[0:len(line) // 2]
            second_compartment = line[len(line) // 2:]
            char = find_common_item([first_compartment, second_compartment])
            priorities += calculate_priority(char)

            if line_count == 3:
                char = find_common_item(lines)
                group_priorities += calculate_priority(char)
                line_count = 0
                lines = []
                
    print(priorities)
    print(group_priorities)
                


if __name__ == "__main__":
    main()
