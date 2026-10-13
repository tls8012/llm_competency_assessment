# Pulse 서비스 의존성·데이터 경로 지도

LumenArc AX · 서비스 운영 인계 · 내부 공유 (가상 기업의 합성 자료)

| 관리 항목 | 값 |
|---|---|
| 문서 번호 | DOC-INF-01 |
| 작성 부서/책임 | SRE |
| 작성 시각 | 2027-03-08T08:59:00+09:00 |
| 버전 / 상태 | 2.0 / 승인됨 |
| 효력 | 2027-03-08T08:59:00+09:00 |
| 업무 범위 | PRJ-03 |
| 보관 위치 | company/operations/DOC-INF-01.md |

BEGIN DOC-INF-01

목적
Pulse 서비스 장애 분석과 복구 계획에서 애플리케이션 경로와 데이터 경로를 분리해 확인한다. 의존성 순서는 원인 진단 결과가 아니다.

서비스 경로
Client → DNS → Gateway → API pool → Primary DB. API는 DNS와 Gateway가 정상이라는 사실만으로 healthy 상태가 되지 않는다.

데이터·제어 경로
Replica DB는 Primary 확정 로그를 비동기로 복제한다. Control plane과 DB data plane은 별도 경로이므로 control plane의 상태만으로 data plane 연결을 증명할 수 없다. Gateway/API 설정은 변하지 않았고 데이터 경로 ACL 변경 기록이 있다. 이 기록만으로 ACL과 장애의 인과관계를 확정하지 않는다.

서비스 경계
결제 Ledger(PRJ-05)는 별도 애플리케이션 및 데이터베이스를 사용한다. Ledger를 Pulse 복구 범위에 합치지 않는다.

확인 항목
DNS 해석 ______ / Gateway upstream ______ / API DB 연결 ______ / Primary·Replica 데이터 상태 ______ / 근거·시각 ______. 미확인 항목은 정상으로 간주하지 않는다.

## 보관 부속

이 문서 자체가 관리 원본입니다. 별도 데이터 부속 없음.

필드 정의·수집 범위는 [데이터 사전](../DATA_DICTIONARY.md)을 참조합니다. 부속은 문서와 함께 읽되 기간·상태·적용 대상을 확인합니다. 자료 미확보는 확인 불가로 기록합니다.

END DOC-INF-01
