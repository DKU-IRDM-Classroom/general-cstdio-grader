import sys

from typing import (
    List,
    Union,
)

from pathlib import Path

from generate import generate
from solve import solve


def write_lines(file_path: Path, lines: List[List[Union[int, float, str]]]):
    linestrs = []
    for line in lines:
        linestr = ' '.join([str(token) for token in line])
        linestrs.append(linestr)
    with file_path.open('w') as file_pointer:
        file_pointer.write('\n'.join(linestrs) + '\n')


def main():

    base_dir = Path(sys.argv[1]).absolute()

    num_cases_file_path = base_dir / 'num_cases.txt'
    with num_cases_file_path.open('r') as file_pointer:
        num_cases = int(file_pointer.read().strip())

    for i in range(1, num_cases + 1):
        lines_in = generate(i)
        lines_ans = solve(lines_in)
        write_lines(base_dir / f'{i}.in', lines_in)
        write_lines(base_dir / f'{i}.ans', lines_ans)


if __name__ == '__main__':
    main()
