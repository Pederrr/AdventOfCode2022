elf_values = { "A": 1, "B": 2, "C": 3}
me_values = { "X": 1, "Y": 2, "Z": 3} 
part2_values = { "X": -1, "Y": 0, "Z": 1 }

def calculate_score(me: int, elf: int) -> int:
    if (me - elf) % 3 == 1:
        return 6
    if me == elf:
        return 3
    return 0

def main() -> None:
    score = 0
    score2 = 0

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip();
            elf = elf_values[line[0]]
            me = me_values[line[2]]

            score += me + calculate_score(me, elf)

            # part 2 
            me2 = elf + part2_values[line[2]]
            if me2 > 3:
                me2 = 1
            elif me2 < 1:
                me2 = 3

            score2 += me2 + calculate_score(me2, elf)

    print(score)
    print(score2)

if __name__ == "__main__":
    main()
