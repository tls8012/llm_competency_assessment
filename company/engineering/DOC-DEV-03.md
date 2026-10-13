# Ledger QA 입력과 관측

LumenArc AX · 애플리케이션 품질 기록 · 내부 공유 (가상 기업의 합성 자료)

| 관리 항목 | 값 |
|---|---|
| 문서 번호 | DOC-DEV-03 |
| 작성 부서/책임 | QA |
| 작성 시각 | 2027-03-08T08:50:00+09:00 |
| 버전 / 상태 | 1.0 / 관측 |
| 효력 | 2027-03-08T08:50:00+09:00 |
| 업무 범위 | PRJ-05 |
| 보관 위치 | company/engineering/DOC-DEV-03.md |

BEGIN DOC-DEV-03

## QA 회귀 실행 기록

contract_cases.json에는 테스트 호출 순서와 v1.5 관측을 보존했다. 각 케이스는 독립 초기화하며 동일 케이스 안에서는 상태가 유지된다. Q2는 최초 요청 뒤의 동일 재시도를 포함한다. 호출 배열은 tenant, request_id, amount_cents, simulate_timeout 순서다.

## 판정 절차

관측 auth_id와 행 수는 명세의 기대값을 뜻하지 않는다. API 명세를 기준으로 기대 결과를 산출한 뒤 비교한다. 케이스별 최초 성공, 동일 retry, timeout 뒤 retry, 같은 키의 다른 금액, tenant 분리를 확인한다.

## 추가 검증 요청

0·음수·비정수 금액 처리, 재시작, 다중 프로세스 경합은 별도 계획에 적는다. 제공된 순차 재현만으로 운영환경 전체의 수정 완료를 선언하지 않는다.

## 보관 부속

- [contract_cases.json](qa/contract_cases.json)

필드 정의·수집 범위는 [데이터 사전](../DATA_DICTIONARY.md)을 참조합니다. 부속은 문서와 함께 읽되 기간·상태·적용 대상을 확인합니다. 자료 미확보는 확인 불가로 기록합니다.

END DOC-DEV-03
