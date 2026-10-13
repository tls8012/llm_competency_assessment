# 주간 작업 패키지

LumenArc AX · PMO 주간 관리 문서 · 내부 공유 (가상 기업의 합성 자료)

| 관리 항목 | 값 |
|---|---|
| 문서 번호 | DOC-PRJ-04 |
| 작성 부서/책임 | Portfolio Office |
| 작성 시각 | 2027-03-05T16:00:00+09:00 |
| 버전 / 상태 | 1.0 / 승인됨 |
| 효력 | 2027-03-08T00:00:00+09:00 |
| 업무 범위 | PRJ-01~PRJ-07 |
| 보관 위치 | company/projects/DOC-PRJ-04.md |

BEGIN DOC-PRJ-04

## 주간 투자 심의 안건 관리서

Portfolio Office는 투자 카탈로그, 자원 소요, 비용 견적을 각 부서 원장으로 관리한다. package_id가 같아도 다른 주의 안건은 다른 범위다. 주간과 패키지 ID를 함께 사용해 세 원장을 결합한다. 카탈로그의 APPROVED_CATALOG는 심의 자료로 사용할 수 있다는 뜻이며 착수 승인 기록은 아니다.

## 사업 가치와 계약 의무

CONTRACT 항목은 기존 계약 이행 범위이며 OPTIONAL은 선택 투자다. 가치점수는 스폰서가 제출한 추정값으로 현금·매출·확정 효과가 아니다. 점수 합을 비교 기준으로 사용할 때는 그 범위를 밝혀야 한다. 미선택 영향은 고객·운영 담당자와 공유한다.

## 자원 및 비용

패키지는 불가분이며 부분 시행과 부분 가치점수는 인정하지 않는다. 모든 스킬 소요를 충족해야 완료 가능하다. 같은 스킬의 시간은 승인 풀 안 여러 직원이 나눌 수 있다. 비용 견적의 모든 항목을 더하되 내부 표준 인건비는 현금에 다시 가산하지 않는다.

## 결재 제출란

선택 패키지와 보류 패키지, 직원별 배치, 필수 의무 충족, 총액과 여유, 대안 비교, 미확인 위험, 결재자를 요청서에 기록한다. 승인 전 고객에게 착수나 완료를 확약하지 않는다.

## 보관 부속

- [investment_register.csv](exports/investment_register.csv)
- [resource_requirements.csv](exports/resource_requirements.csv)
- [package_cost_estimates.csv](exports/package_cost_estimates.csv)

필드 정의·수집 범위는 [데이터 사전](../DATA_DICTIONARY.md)을 참조합니다. 부속은 문서와 함께 읽되 기간·상태·적용 대상을 확인합니다. 자료 미확보는 확인 불가로 기록합니다.

END DOC-PRJ-04
