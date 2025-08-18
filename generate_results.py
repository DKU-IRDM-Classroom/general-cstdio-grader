import sys
import json

from pathlib import Path


def main():

    base_dir = Path(sys.argv[1]).absolute()
    total_score = int(sys.argv[2])

    statuss = []
    for n in range(1, total_score + 1):
        result_path = base_dir / f'{n}.result'
        if not result_path.exists():
            sys.exit(1)
        with open(result_path, 'r') as file_pointer:
            result = file_pointer.read().strip()
            if result == 'pass':
                statuss.append('pass')
            elif result == 'fail':
                statuss.append('fail')
            else:
                sys.exit(1)

    results = {
        'version': 1,
        'status': 'fail' if 'fail' in statuss else 'pass',
        'max_score': total_score,
        'tests': [
            {
                'name': f'Test {n}',
                'status': status,
                'score': 1 if status == 'pass' else 0,
                'message': '',
                'test_code': '',
                'filename': '',
                'line_no': 0,
                'execution_time': 0,
            } for n, status in enumerate(statuss, start=1)
        ],
    }

    with open(base_dir / 'results.json', 'w') as file_pointer:
        json.dump(results, file_pointer)


if __name__ == '__main__':
    main()
