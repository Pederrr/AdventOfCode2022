from typing import List, Tuple


def parse_stacks(lines: List[str]) -> List[List[str]]:
    stacks: List[List[str]] = [[] for _ in range(9)]
    for i in range(len(lines) - 1 - 1, -1, -1):
        stack_index = 0
        for j in range(1, len(lines[i]), 4): 
            if lines[i][j] != " ":
                stacks[stack_index].append(lines[i][j])
            stack_index += 1
        
    return stacks


def parse_instruction(line: str) -> Tuple[int, int, int]:
    values = line.split(" ") 

    # -1 to src and dest indices, because we are indexing from 0
    return int(values[1]), int(values[3]) - 1, int(values[5]) - 1


def move_crates_9000(source: List[str], destination: List[str], count: int) -> None:
    for _ in range(count):
        destination.append(source.pop())


def move_crates_9001(source: List[str], destination: List[str], count: int) -> None:
    to_move: List[str] = []
    for _ in range(count):
        to_move.append(source.pop())

    destination += reversed(to_move)


def print_solution(stacks: List[List[str]]) -> None:
    for stack in stacks:
        print(stack[-1], end="")
    print("")


def main() -> None:
    stack_lines: List[str] = []
    instructions: List[str] = []
    with open("input.txt", "r") as file:
        stcks = True
        for line in file:
            line = line[:-1] # strip \n from end of lines
            if line == "":
                stcks = False
                continue

            if stcks:
                stack_lines.append(line)
            else:
                instructions.append(line)

    # part 1
    stacks = parse_stacks(stack_lines)

    for instruction in instructions:
        count, src, dest = parse_instruction(instruction)
        move_crates_9000(stacks[src], stacks[dest], count)

    print_solution(stacks)

    # part 2

    stacks = parse_stacks(stack_lines)

    for instruction in instructions:
        count, src, dest = parse_instruction(instruction)
        move_crates_9001(stacks[src], stacks[dest], count)

    print_solution(stacks)


if __name__ == "__main__":
    main()
