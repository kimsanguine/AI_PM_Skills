# troubleshooting — exclusions

## "한국어로 'X 도구' vs 'X 생성기' 가 매칭 안 됨"

- 0.40 threshold + char-bigram이 표준. 그래도 missed면 `--threshold 0.30`.
- 단어 형태 변화가 큰 도메인은 직접 add 시 키워드 일치 더 신경.

## "중복 추가 어떻게 막나?"

- 의도적으로 막지 않음. JSONL은 history. 잘못된 entry는 새 entry로 supersede + `why`에 "supersedes ex-..." 기록.

## "마음 바뀌면?"

- 영구 삭제 없음. 대신 새 entry로 reopen 사실 기록.
- 또는 별도 audit log를 add — exclusions 자체는 immutable.

## "이름이 변경된 competitor"

- exclusion 추가할 때 `--competitor "Old name" --competitor "New name"` 양쪽 다 적음.
- 또는 별도 entry로 "Old → New transition" 기록.
