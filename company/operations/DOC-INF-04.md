# Pulse 복제·보존 상태

LumenArc AX · 서비스 운영 인계 · 내부 공유 (가상 기업의 합성 자료)

| 관리 항목 | 값 |
|---|---|
| 문서 번호 | DOC-INF-04 |
| 작성 부서/책임 | Database Operations |
| 작성 시각 | 2027-03-08T08:55:00+09:00 |
| 버전 / 상태 | 1.0 / 관측 |
| 효력 | 2027-03-08T08:55:00+09:00 |
| 업무 범위 | PRJ-03 |
| 보관 위치 | company/operations/DOC-INF-04.md |

BEGIN DOC-INF-04

## DB 운영 인수인계 — 복제 및 보존

복제 인벤토리는 프로젝트·환경·스냅샷 시각별로 내보낸 JSON이다. 이전 스냅샷은 시점 비교를 위해 남겨 둔다. Primary 확정 데이터, replica 적용 데이터, 미적용 로그의 복구 가능한 끝 시각, 백업 스냅샷은 서로 다른 필드다.

## Replay 절차의 데이터 전제

replay_available_through까지의 backlog는 checksum 확인 후 적용할 수 있다. 성공적으로 replay하면 replica 적용 시각은 해당 backlog 끝 시각에 도달한다. 계획은 실행 결과가 아니므로 검증 전 적용 완료로 기록하지 않는다.

## 고객 보고와 보존

실제 데이터 손실은 확인되지 않았으며 UNKNOWN을 0으로 치환할 수 없다. 계약 RPO는 재개 시 보존 데이터와 장애 직전 확정 데이터의 차이를 기준으로 계산한다. 현재 벽시각에서 마지막 관측을 뺀 값을 손실로 간주하지 않는다. Primary와 replica의 쓰기를 동시에 열지 않는다.

## 보관 부속

- [replication_inventory.json](exports/replication_inventory.json)

필드 정의·수집 범위는 [데이터 사전](../DATA_DICTIONARY.md)을 참조합니다. 부속은 문서와 함께 읽되 기간·상태·적용 대상을 확인합니다. 자료 미확보는 확인 불가로 기록합니다.

END DOC-INF-04
