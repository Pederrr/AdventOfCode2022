from typing import Tuple


def parse_section_range(range_str: str) -> Tuple[int, int]:
    sec_range = range_str.split("-")
    return (int(sec_range[0]), int(sec_range[1]))


def containts(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    return range2[0] >= range1[0] and range2[1] <= range1[1]


def overlaps(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    return range2[0] >= range1[0] and range2[0] <= range1[1]


def main() -> None:
    fully_contained = 0 
    overlaping = 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip();
            ranges = line.split(",")
            elf1 = parse_section_range(ranges[0])
            elf2 = parse_section_range(ranges[1])
            if containts(elf1, elf2) or containts(elf2, elf1):
                fully_contained += 1

            # part 2
            if overlaps(elf1, elf2) or overlaps(elf2, elf1):
                overlaping += 1

    print(fully_contained)
    print(overlaping)


if __name__ == "__main__":
    main()
