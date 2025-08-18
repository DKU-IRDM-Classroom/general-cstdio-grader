import sys

from typing import List

from pathlib import Path


def read_lines(file_path: Path) -> List[List[str]]:

    try:
        content = file_path.open('r').read()
    except Exception:
        sys.exit(2)

    content = (
        content
        .strip()
        .replace('\r\n', '\n')
        .replace('\r', '\n')
        .strip()
    )

    lines = []
    for line in content.split('\n'):
        line = [token.strip() for token in line.split()]
        if line:
            lines.append(line)

    return lines


def main():

    if len(sys.argv) != 3:
        sys.exit(3)

    ans_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    lines_ans = read_lines(ans_path)
    lines_out = read_lines(out_path)

    if len(lines_ans) != len(lines_out):
        sys.exit(2)

    for line_ans, line_out in zip(lines_ans, lines_out):

        if len(line_ans) != len(line_out):
            sys.exit(2)

        for token_ans, token_out in zip(line_ans, line_out):
            if token_ans != token_out:
                sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
