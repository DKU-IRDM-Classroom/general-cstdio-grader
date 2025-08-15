# stdio-grader-action

입력 파라미터(3개)

* grader-repo (필수): 비공개 grader 저장소 URL
* grader-token (필수): grader 읽기용 PAT
* full-score (필수): 만점(정수). round(통과/총케이스 × 만점)

학생 저장소 전제: 현재 워크스페이스(=학생 repo)에 main.c 존재, 실행파일명은 main.

grader 규약: generate.py가 반드시

* num_cases.txt (정수 1줄)

* cases/n.in, cases/n.ans (또는 루트 n.in, n.ans) 생성

출력(한국어)

* 케이스별: 정답, 오답, 형식 오류, 시간 초과, 메모리 초과, 실행 오류, 출력 초과

* 컴파일 실패 시: “컴파일 실패: 점수 0점으로 처리됩니다.”

* 집계:

    ** 채점 요약: PASS/TOTAL

    ** 최종 점수: SCORE/FULL

보안/격리: --network none, --read-only, --cap-drop ALL, no-new-privileges, PID/CPU/MEM 제한, /tmp tmpfs(noexec), 출력 크기 제한(1MiB)

학생 템플릿 워크플로 예시

```yml
name: Autograde

on:
  push:
    branches: [ main ]

jobs:
  grade:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: 채점 실행
        uses: MyOrg-Teaching/stdio-grader-action@v1
        with:
          grader-repo: https://github.com/MyOrg-Teaching/MyAssignment-grader
          grader-token: ${{ secrets.GRADER_ACCESS_TOKEN }}
          full-score: "10"
```
