from typing import List


def insert(values: List[int], value: int) -> None:
    if value > values[0]:
        values[0] = value
    else:
        return

    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            values[i], values[i + 1] = values[i + 1], values[i]


def main() -> None:
    current_sum = 0
    result = [0, 0, 0]

    with open("calories.txt", "r") as file:
        for line in file:
            line = line.strip()

            if (line == ""):
                insert(result, current_sum) 
                current_sum = 0
            else:
                current_sum += int(line);

    print(result)
    print(sum(result))


if __name__ == "__main__":
    main()
