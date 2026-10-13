# Pulse 관측 타임라인

LumenArc AX · 서비스 운영 인계 · 내부 공유 (가상 기업의 합성 자료)

| 관리 항목 | 값 |
|---|---|
| 문서 번호 | DOC-INF-02 |
| 작성 부서/책임 | Monitoring |
| 작성 시각 | 2027-03-08T09:00:00+09:00 |
| 버전 / 상태 | 1.0 / 관측 |
| 효력 | 2027-03-08T09:00:00+09:00 |
| 업무 범위 | PRJ-03 |
| 보관 위치 | company/operations/DOC-INF-02.md |

BEGIN DOC-INF-02

## 통합 관측 수집 인계서

반출 범위는 2027-03-08 07:00~09:00 KST, Pulse·Harbor·Relay 관련 수집기다. 원본 로그는 수신 순서로 파트 파일에 저장했다. 애플리케이션·인프라·관측 파이프라인 신호와 prod/staging/dev가 섞여 있다. 파트 번호는 시각 순서가 아니다.

## 파싱 및 정규화

JSONL 한 행은 한 관측 이벤트다. event_at의 UTC 오프셋을 기준으로 시간축을 구성한다. ingested_at은 수집시각이며 늦게 도착한 사건을 새 사건으로 취급하지 않는다. 동일 event_id는 수집 재전송이다. event_id가 다른 사건은 신호가 같아도 별도 관측이다. trace_id 공란은 미기록이다.

## 당직 인계

Pulse 장애는 08:40 KST 인지되었고 09:00 현재 서비스 복구 확인을 받지 못했다. 기술 원인은 아직 확정되지 않았다. heartbeat·control-plane 상태·DNS 성공만으로 고객 서비스 정상화를 판단하지 않는다. 관측값을 시점별로 추적하고, 승인된 계획과 실제 수행 결과를 구분해 Incident Commander에게 보고한다.

## 보관 부속

- [collector-20270308-part1.jsonl](logs/collector-20270308-part1.jsonl)
- [collector-20270308-part2.jsonl](logs/collector-20270308-part2.jsonl)
- [collector-20270308-part3.jsonl](logs/collector-20270308-part3.jsonl)

필드 정의·수집 범위는 [데이터 사전](../DATA_DICTIONARY.md)을 참조합니다. 부속은 문서와 함께 읽되 기간·상태·적용 대상을 확인합니다. 자료 미확보는 확인 불가로 기록합니다.

END DOC-INF-02
