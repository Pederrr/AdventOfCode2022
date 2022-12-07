from typing import List, Tuple


def file_size(file: str) -> int:
    parts = file.split(" ")
    if parts[0] != "dir":
        return int(parts[0])
    return 0


def is_command(line: str) -> bool:
    return line[0] == "$"


def read_dir(lines: List[str], index: int, dir_sizes: List[int]) -> Tuple[int, int]:
    assert(lines[index][0:5] == "$ cd ")
    assert(lines[index + 1] == "$ ls")
    index += 2
    size = 0
    while index < len(lines) and not is_command(lines[index]):
        size += file_size(lines[index])
        index += 1
    while index < len(lines) and lines[index] != "$ cd ..":
        idx, subdir_size = read_dir(lines, index, dir_sizes)
        index = idx
        size += subdir_size
    dir_sizes.append(size)
    return index + 1, size


def find_dir_to_remove(dir_sizes: List[int]) -> int:
    unused_space = 70000000 - dir_sizes[-1]
    needed_space = 30000000 - unused_space

    result = 0
    result_freed_space = needed_space
    
    for size in dir_sizes:
        freed_space = size - needed_space
        if freed_space > 0 and freed_space < result_freed_space:
            result_freed_space = freed_space
            result = size
    return result

    
def main() -> None:
    lines: List[str] = []
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]
    dir_sizes: List[int] = []
    read_dir(lines, 0, dir_sizes)

    print(sum(filter(lambda elem: elem <= 100000, dir_sizes)))

    print(find_dir_to_remove(dir_sizes))

        
if __name__ == "__main__":
    main()
