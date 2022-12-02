elf_values = { "A": 0, "B": 1, "C": 2}
part1_values = { "X": 0, "Y": 1, "Z": 2} 
part2_values = { "X": -1, "Y": 0, "Z": 1 }

def calculate_score(me: int, elf: int) -> int:
    if (me - elf) % 3 == 1:
        return 6
    if me == elf:
        return 3
    return 0

def main() -> None:
    score1 = 0
    score2 = 0

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip();
            elf = elf_values[line[0]]
            me = part1_values[line[2]]
            score1 += me + 1 + calculate_score(me, elf)

            # part 2 
            me2 = (elf + part2_values[line[2]]) % 3
            score2 += me2 + 1 + calculate_score(me2, elf)

    print(score1)
    print(score2)

if __name__ == "__main__":
    main()
