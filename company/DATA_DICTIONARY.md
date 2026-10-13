# 반출 자료 데이터 사전

가상 기준시각 2027-03-08 09:00 KST의 합성 반출본입니다. 숫자와 이력은 고정 seed Python 생성기에서 만들었습니다. 실제 회사 데이터가 아닙니다. UTF-8, CSV 첫 행은 헤더, 쉼표 구분, ISO 날짜, 소수점은 점입니다. 공란은 미기록/해당 필드 정의의 열린 종료일이며 숫자 0으로 자동 치환하지 않습니다.

자료는 일부러 여러 기간·업무·상태를 함께 보관합니다. 데이터가 놓인 순서로 최신·승인 여부를 판단하지 않습니다. CSV의 식별키와 로그의 event_id는 출처 표기에 사용할 수 있습니다. 파일 이름과 필터 조건·키를 함께 남겨 같은 근거를 다시 찾을 수 있게 하세요. 전체 파일을 채팅에 그대로 붙이는 대신 도구가 있으면 검색·필터·집계를 LLM에 요청할 수 있습니다. 도구가 없으면 필요한 파일을 순차 첨부하고 누락된 범위를 명시하세요.

같은 파일을 참조하는 문서가 여러 개 있어도 파일을 중복 합산하지 않습니다. 시험 중 EVT로 도입된 변경은 원본 파일을 덮어쓰지 않고 해당 시험 분기의 델타로 관리합니다.

## employee_directory.csv

[company/people/exports/employee_directory.csv](people/exports/employee_directory.csv)

- 행의 의미: employee_id당 현재 인사 마스터 1행
- 범위: 36명, 2027-03-08 기준
- 레코드 수: 36
- `employee_id`: PK; 다른 원장과 ID 조인. 이름 중복 가능
- `weekly_contract_hours`: h/week; 개인 주 계약 총량
- `effective_to`: 빈 값은 열린 종료일

## skills_register.csv

[company/people/exports/skills_register.csv](people/exports/skills_register.csv)

- 행의 의미: 스킬 인증 이력 행
- 범위: 기한 만료·자기신고 포함
- 레코드 수: 108
- `record_id`: PK
- `status`: VERIFIED만 해당 유효기간의 배정 자격. SELF_REPORTED는 신청 상태
- `skill`: BE, DATA, SRE, QA, SEC, PM

## resource_allocations.csv

[company/people/exports/resource_allocations.csv](people/exports/resource_allocations.csv)

- 행의 의미: allocation_id별 업무 예약 1행
- 범위: 9주, 승인/미승인 업무 예약 포함
- 레코드 수: 1296
- `hours`: 주간 예약 h; APPROVED만 확정 배정
- `week_start`: KST 계획 주의 월요일
- `allocation_id`: PK; 직원·기간별 여러 업무 행을 합산
- `status`: APPROVED/DRAFT/REJECTED

## leave_requests.csv

[company/people/exports/leave_requests.csv](people/exports/leave_requests.csv)

- 행의 의미: request_id + revision
- 범위: 9주, 휴가 신청과 승인/취소 이력
- 레코드 수: 648
- `revision`: 동일 request_id의 최대 revision이 현재 상태; 과거 버전을 합산하지 않음
- `hours`: h/week; 최종 APPROVED만 반영, CANCELLED는 휴가 0
- `recorded_at`: 오프셋 있는 업무 기록시각

## standard_cost_rates.csv

[company/people/exports/standard_cost_rates.csv](people/exports/standard_cost_rates.csv)

- 행의 의미: employee_id + week_start
- 범위: 9주 표준 배부 원가
- 레코드 수: 324
- `usd_per_hour`: USD/h 분석용 원가; 현금 예산에 추가 지급 아님

## pool_authorizations.csv

[company/people/exports/pool_authorizations.csv](people/exports/pool_authorizations.csv)

- 행의 의미: employee_id + pool_id + 유효기간
- 범위: 이번 주 승인된 투자 인력 풀
- 레코드 수: 8
- `status`: 배정 변경 자체는 별도 COO 승인 필요

## operating_journal.csv

[company/finance/exports/operating_journal.csv](finance/exports/operating_journal.csv)

- 행의 의미: entry_id별 부호 있는 순비용 분개
- 범위: 9주·여러 원가센터·초안/확정·취소분개 포함
- 레코드 수: 1331
- `net_amount`: USD, 비용 양수/환입 음수. 전표 취소는 반대 부호 새 POSTED 행
- `cost_center`: AX-POOL은 주간 투자 관리 범위; CORP-*는 별도 지역 운영 장부
- `entry_type`: BASELINE 고정 운영 예약, ACTUAL_VARIABLE 과거 패키지 지출, ACTUAL 기타 실적
- `status`: POSTED만 유효; DRAFT는 미전기
- `reference`: batch/조정 증빙 참조; 합계 행 없음

## budget_workflow.csv

[company/finance/exports/budget_workflow.csv](finance/exports/budget_workflow.csv)

- 행의 의미: document_id + revision
- 범위: 9주 결재 문서 이력; 신규 초안도 함께 반출
- 레코드 수: 108
- `status`: APPROVED이고 적용 기간/서명 유효인 버전만 집행 근거. 최신 초안이 승인 버전을 대체하지 않음
- `ceiling_usd`: USD 주간 총액 상한
- `effective_from`: 빈 값은 효력 미발생

## investment_register.csv

[company/projects/exports/investment_register.csv](projects/exports/investment_register.csv)

- 행의 의미: week_start + package_id
- 범위: 주별 검토 대상 패키지 카탈로그; 실행 승인은 별도
- 레코드 수: 54
- `value_points`: 무단위 추정 가치점수, 현금/매출 아님
- `obligation`: CONTRACT는 기존 계약 의무
- `status`: 카탈로그 승인은 패키지 실행 승인 아님

## resource_requirements.csv

[company/projects/exports/resource_requirements.csv](projects/exports/resource_requirements.csv)

- 행의 의미: week_start + package_id + skill
- 범위: 주별 업무에 필요한 스킬시간
- 레코드 수: 81
- `hours`: h, 모든 행 충족 필요; 동일 스킬은 승인 풀 내 분담 가능

## package_cost_estimates.csv

[company/projects/exports/package_cost_estimates.csv](projects/exports/package_cost_estimates.csv)

- 행의 의미: week_start + package_id + cost_item
- 범위: 주별 복수 비용 항목; 세금 제외
- 레코드 수: 108
- `incremental_cash`: USD 추가 현금. 패키지별 모든 항목 합산; 급여 원가 제외

## work_items.csv

[company/projects/exports/work_items.csv](projects/exports/work_items.csv)

- 행의 의미: snapshot_at + project_id + task_id
- 범위: 9주·7개 프로젝트 정기 스냅샷
- 레코드 수: 756
- `remaining_days`: 기본 인력이 확보된 남은 영업일; 작업시간 h와 다름
- `predecessors`: 같은 snapshot/project 내 task_id; ; 구분
- `workstream`: 납품 계약 작업과 내부 운영 backlog 구분
- `status`: OPEN/BACKLOG; 진척률은 납기 계산 대신 사용 불가

## collector-20270308-part1.jsonl

[company/operations/logs/collector-20270308-part1.jsonl](operations/logs/collector-20270308-part1.jsonl)

- 행의 의미: 수집 이벤트 1행; event_id 재전송 가능
- 범위: 07:00~09:00 KST 여러 프로젝트/환경. 수신 순서로 저장
- 레코드 수: 6039
- `event_at`: ISO8601 offset; 시간대 정규화 필요
- `ingested_at`: 수집 도착 시각; 사건 발생 시각 아님
- `event_id`: 재전송 시 동일 ID. 서로 다른 ID는 합치지 않음
- `trace_id`: 누락은 미기록; 장애 없음 의미 아님
- `signal`: 관측 신호; telemetry heartbeat는 고객 서비스 정상 판정 아님
- `environment`: prod/staging/dev를 구분

## collector-20270308-part2.jsonl

[company/operations/logs/collector-20270308-part2.jsonl](operations/logs/collector-20270308-part2.jsonl)

- 행의 의미: 수집 이벤트 1행; event_id 재전송 가능
- 범위: 07:00~09:00 KST 여러 프로젝트/환경. 수신 순서로 저장
- 레코드 수: 6038
- `event_at`: ISO8601 offset; 시간대 정규화 필요
- `ingested_at`: 수집 도착 시각; 사건 발생 시각 아님
- `event_id`: 재전송 시 동일 ID. 서로 다른 ID는 합치지 않음
- `trace_id`: 누락은 미기록; 장애 없음 의미 아님
- `signal`: 관측 신호; telemetry heartbeat는 고객 서비스 정상 판정 아님
- `environment`: prod/staging/dev를 구분

## collector-20270308-part3.jsonl

[company/operations/logs/collector-20270308-part3.jsonl](operations/logs/collector-20270308-part3.jsonl)

- 행의 의미: 수집 이벤트 1행; event_id 재전송 가능
- 범위: 07:00~09:00 KST 여러 프로젝트/환경. 수신 순서로 저장
- 레코드 수: 6038
- `event_at`: ISO8601 offset; 시간대 정규화 필요
- `ingested_at`: 수집 도착 시각; 사건 발생 시각 아님
- `event_id`: 재전송 시 동일 ID. 서로 다른 ID는 합치지 않음
- `trace_id`: 누락은 미기록; 장애 없음 의미 아님
- `signal`: 관측 신호; telemetry heartbeat는 고객 서비스 정상 판정 아님
- `environment`: prod/staging/dev를 구분

## replication_inventory.json

[company/operations/exports/replication_inventory.json](operations/exports/replication_inventory.json)

- 행의 의미: snapshot_at + project_id + environment
- 범위: 관측 스냅샷; replay/복구 실행 완료 기록 아님
- 레코드 수: 4


## network-audit.log

[company/operations/logs/network-audit.log](operations/logs/network-audit.log)

- 행의 의미: audit_id당 작업 이벤트
- 범위: 조회·변경 혼재; 장애 원인 진단 결과 없음
- 레코드 수: 181


## authorization_ledger.csv

[company/engineering/exports/authorization_ledger.csv](engineering/exports/authorization_ledger.csv)

- 행의 의미: row_id당 확정 원장 1행
- 범위: ap-1 shard, 03-07~03-08 08:59까지 반출 가능한 행. 전 세계 전체 영향 모집단 아님
- 레코드 수: 12004
- `amount_cents`: USD cent 정수; 100 cents=USD 1
- `row_id`: PK, 물리적으로 다른 행
- `request_id`: tenant와 함께 논리 요청 식별; tenant 경계 유지
- `ingestion_batch`: 수집 범위, 전역 대사 완료를 뜻하지 않음

## authorize-service.log

[company/engineering/logs/authorize-service.log](engineering/logs/authorize-service.log)

- 행의 의미: HTTP/application 요청 이벤트
- 범위: ap-1 일부 요청·재시도·응답 지연 기록; 로그 도착 순서
- 레코드 수: 12002


## authorize_v1_5.py

[company/engineering/source/authorize_v1_5.py](engineering/source/authorize_v1_5.py)

- 행의 의미: 제공되는 최소 재현 모듈
- 범위: 단일 프로세스 순차 호출, 운영 접속 없음
- 레코드 수: 해당 없음


## contract_cases.json

[company/engineering/qa/contract_cases.json](engineering/qa/contract_cases.json)

- 행의 의미: QA 케이스
- 범위: v1.5 회귀 관측; 기대 동작은 API 명세 참조
- 레코드 수: 5
