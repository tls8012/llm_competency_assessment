# Ledger 원장 반출 기록

LumenArc AX · 애플리케이션 품질 기록 · 내부 공유 (가상 기업의 합성 자료)

| 관리 항목 | 값 |
|---|---|
| 문서 번호 | DOC-DEV-05 |
| 작성 부서/책임 | QA & Client Operations |
| 작성 시각 | 2027-03-08T08:55:00+09:00 |
| 버전 / 상태 | 1.0 / 관측 |
| 효력 | 2027-03-08T08:55:00+09:00 |
| 업무 범위 | PRJ-05 |
| 보관 위치 | company/engineering/DOC-DEV-05.md |

BEGIN DOC-DEV-05

## 고객 운영 대사 전달서 — Ledger ap-1

08:45 KST부터 timeout 뒤 재시도 관련 중복 승인 신고를 조사 중이다. 첨부는 ap-1 shard의 반출 가능한 확정 원장과 서비스 요청 로그다. 여러 tenant의 정상 요청과 재시도, 응답 실패가 함께 있다. 다른 shard 및 일부 요청 로그는 아직 수집되지 않았으므로 전 세계 장애 규모로 확대하지 않는다.

## 대사 키와 금액

물리 원장 행은 row_id로 구분한다. 논리 요청은 tenant와 request_id를 함께 비교한다. 같은 request_id가 다른 tenant에 등장하는 것은 그 자체로 중복이 아니다. 금액 단위는 USD cent이며 달러와 혼동하지 않는다. 응답 timeout과 확정 원장 반영은 별도 상태다.

## 처리 의뢰 양식

조사자는 의심 논리키, 관련 row_id, 요청로그 시각, 관측 금액, 불확실성, 담당자, 고객 조정 상태를 적는다. 확인 전 삭제·환불을 일괄 실행하지 않는다. 격리·대사와 애플리케이션 rollback을 구분한다. 원시 고객 식별정보는 이 합성 반출본에 포함하지 않는다.

## 보관 부속

- [authorization_ledger.csv](exports/authorization_ledger.csv)
- [authorize-service.log](logs/authorize-service.log)

필드 정의·수집 범위는 [데이터 사전](../DATA_DICTIONARY.md)을 참조합니다. 부속은 문서와 함께 읽되 기간·상태·적용 대상을 확인합니다. 자료 미확보는 확인 불가로 기록합니다.

END DOC-DEV-05
