# troubleshooting — decision-log

## "hit_rate가 null"

- 한 decision도 outcome backfill 안 됨. `update` 호출 필요.

## "3개월 됐는데 outcome이 애매하다"

- `alive_no_revenue` — 살아있긴 한데 매출 없음. 모호한 케이스에 명시적 vocabulary.
- 또는 outcome 유보 + reason에 "결정 보류" 노트 추가.

## "ID 찾기 귀찮다"

- `decision_log.py audit` 출력의 false_holds/missed_builds 에 id가 있음.
- 또는 `cat harness/decisions.jsonl | jq 'select(.project=="alpha-app")'`.

## "잘못 기록했다"

- append-only이라 직접 delete 불가. 새 entry add + `--reason "supersedes dec-XXX"` 명시.

## "Audit이 false_hold라고 하는데 우리는 일부러 hold 했다"

- outcome `external_success`가 *우리 판단이 틀렸다*는 사실. 일부러 hold한 이유가 valid해도 통계는 "기회 놓침"으로 잡힘. rubric 검토 신호.
