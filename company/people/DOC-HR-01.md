# 직원·스킬·거점

LumenArc AX · 인사 운영 회람 · 내부 공유 (가상 기업의 합성 자료)

| 관리 항목 | 값 |
|---|---|
| 문서 번호 | DOC-HR-01 |
| 작성 부서/책임 | Operations Office |
| 작성 시각 | 2027-03-05T16:00:00+09:00 |
| 버전 / 상태 | 1.0 / 승인됨 |
| 효력 | 2027-03-08T00:00:00+09:00 |
| 업무 범위 | 전사 |
| 보관 위치 | company/people/DOC-HR-01.md |

BEGIN DOC-HR-01

## 인사 마스터 운영 공지

People Operations는 월요일 주간 배정 회의에 맞춰 재직자 디렉터리와 역량 인증 이력을 반출한다. 디렉터리의 이름·거점·부서는 연락과 관리용이며, 투입 자격은 별도 스킬 레지스터에서 확인한다. 동명이인이 있어 이름으로 결합하지 않는다.

## 인증 심사와 배정 자격

배정에 사용할 스킬은 해당 기간에 유효한 VERIFIED 기록이다. 만료된 인증과 본인 신고 단계는 검토 이력으로 보관한다. 자기신고에 팀장이 긍정적인 의견을 남겼더라도 인증을 대신하지 않는다. BE=backend, DATA=data engineering, SRE=cloud reliability, QA=test, SEC=security, PM=project management.

## 정정 요청

누락된 자격을 발견하면 People Operations에 employee_id·인증 기록·요청 기간을 보낸다. 정정 전 자격을 임의로 추정하지 않는다. 계약시간은 인사 마스터, 기존 예약과 휴가는 별도 운영대장에서 조회한다.

## 보관 부속

- [employee_directory.csv](exports/employee_directory.csv)
- [skills_register.csv](exports/skills_register.csv)

필드 정의·수집 범위는 [데이터 사전](../DATA_DICTIONARY.md)을 참조합니다. 부속은 문서와 함께 읽되 기간·상태·적용 대상을 확인합니다. 자료 미확보는 확인 불가로 기록합니다.

END DOC-HR-01
