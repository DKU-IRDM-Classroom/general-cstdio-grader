#!/usr/bin/env python3

import sys

from typing import List

from pathlib import Path


def get_lines_from_file(file_path: Path) -> List[List[str]]:

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

    ans_lines = get_lines_from_file(ans_path)
    out_lines = get_lines_from_file(out_path)

    if len(ans_lines) != len(out_lines):
        print("[DEBUG] num lines mismatch", len(ans_lines), len(out_lines))
        sys.exit(2)

    for ans_line, out_line in zip(ans_lines, out_lines):

        if len(ans_line) != len(out_line):
            print("[DEBUG] num tokens mismatch", ans_line, out_line)
            sys.exit(2)

        for ans_token, out_token in zip(ans_line, out_line):
            if ans_token != out_token:
                print("[DEBUG] token mismatch", ans_token, out_token)
                sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
