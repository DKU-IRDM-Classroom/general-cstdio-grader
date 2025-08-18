import sys
import json


def generate_result(total_score: int, pass_score: int):
    return {
        'version': 1,
        'status': "pass",
        'max_score': total_score,
        'tests': [
            {
                'name': 'Test',
                'status': 'pass' if pass_score > 0 else 'fail',
                'score': pass_score,
                'message': 'some_message_here',
                'test_code': 'some_command_heere',
                'filename': 'some_filename_here',
                'line_no': 0,
                'duration': 0,
            },
        ],
    }


if __name__ == '__main__':
    total_score = int(sys.argv[1])
    pass_score = int(sys.argv[2])
    result = generate_result(total_score, pass_score)
    with open('results.json', 'w') as file_pointer:
        json.dump(result, file_pointer, indent=2)
