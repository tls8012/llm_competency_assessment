**왜 좋았는지:** CSV의 필터·조인·합계를 회수하고 모호한 전표 출처를 재조회해 정정했다.  
**어떻게 해야 좋은지:** 합계뿐 아니라 파일·행 키·상태·revision과 제외 조건을 확인 가능한 형태로 남긴다.  
**어떻게 실전에 적용할 수 있는지:** 보고서 작성 전에 원장 추출표를 만들고, 핵심 합계와 출처 키를 별도 집계로 대조한다.

**범위별 평가:** 주요 합계·직원/패키지 값은 제작자 Python 대조에 통과했고, 최초 전표 ID 범위는 2회차에 정정했습니다. 전체 시험이 아닌 추출 연습이므로 97.50점은 이 기록의 점수가 아닙니다. [판정 사유와 한계](EVALUATION.md#v2-review)를 확인하세요.

# v2 자료 탐색 — 실제 입력·응답 기록

실행일 2026-10-13. 같은 gpt-5.6-terra 서브에이전트를 재사용한 별도 자료 추출 연습입니다. 앞선 v1.0.0 시험은 종료 상태로 유지했습니다. 응시자 역할의 상위 Codex와 Terra 모두 앞선 문제를 알고 있었으므로 블라인드 평가가 아닙니다. 전체 시험·브라우저 실행·시간 측정·독립 채점도 아닙니다.

이번에는 시험용 LLM이 원본 CSV에서 기간·상태·revision·키를 적용해 입력값을 회수했습니다. 첫 응답의 주요 합계와 직원/패키지 값은 제작자의 별도 Python 검산과 일치했습니다. 다만 전표 ID 범위에 누락·모호함이 있어 재조회·수정 요청을 보냈습니다. 원문을 사후 교체하지 않았습니다.

**자료 버전:** 이 기록이 포함된 Git commit의 company/ 원본과 데이터 사전을 참조하세요. 1회차 중 회사 문서의 양식 확장이 진행 중이었고, 2회차에 변경된 권한·예산 결재·효력 문서를 재확인했습니다. M02에 사용한 CSV 수치·키는 이 두 회차 사이 변경하지 않았습니다. 원시 부속 체크섬은 [파일 목록](../../company/MANIFEST.json)에 있습니다.

기록 범위는 실제 호출 문구, 입력 파일 전체, 모델의 최종 응답 전체입니다. 숨은 내부 추론과 도구 이벤트 전체는 포함하지 않습니다. 도구 사용 여부에 대한 모델의 보고와 제작자 검산은 구별합니다.

## 01회차

실제 호출 문구:

~~~~~text
authoring/work/m02-v2-retrieval/01-prompt.txt의 전체 내용을 새 v2 자료 탐색 연습 입력으로 읽고 수행하세요. 응답 전체를 같은 폴더의 01-response.md에 저장하고 동일 내용으로 응답하세요. 앞선 v1 시험의 최종 제출은 수정하지 않습니다.
~~~~~

입력 전체:

~~~~~text
앞선 v1.0.0 시험은 종료 상태로 유지한다. 이것은 새 v2.0.0 자료의 탐색 확인용 별도 연습이며 전체 시험이나 독립 채점이 아니다. 이전 숫자를 기억해서 답하지 말고 지금 파일을 실제로 읽고 추출하라.

자료 위치는 llm_competency_assessment. README.md, handbook/COMPANY.md, scenarios/M02.md와 company/ 아래 관련 문서·부속만 읽는다. GRADE.md, examples/, docs/QUALITY.md, authoring/ 제작 코드와 검산 결과는 읽지 않는다. 응답 기록을 위한 이 prompt 파일은 예외다. 도구 계산은 사용할 수 있고 실제 사용한 필터/계산과 수동 해석을 구분한다.

M02 초기 주간 계획을 조사해줘. 먼저 필수 문서와 연결 부속을 찾고, 이번 주의 유효 승인 예산과 미승인 전망, 현금 기준비용, 승인 인력풀의 직원별 검증 스킬·기존 배정·휴가·추가 가용시간, 각 패키지의 현금·스킬 소요·의무·가치점수를 CSV 원본에서 추출해줘. 원장에 다른 주차·원가센터·신청/초안·이력 등이 있으니 어느 키와 필터로 제외하거나 결합했는지 설명해줘. 출처 파일과 확인에 사용한 레코드 식별키를 적어줘. 표 행·파일 접근이 잘렸거나 누락되면 그대로 표시하고 숫자를 기억으로 채우지 마.

패키지를 추천하거나 조합 최적화, 브리핑, 임원 문답까지 진행하지는 마. 이번 목적은 새로운 원본 자료에서 의사결정 입력값을 재구성할 수 있는지 확인하는 것이다. 이 연습은 인간의 블라인드 시험·시간 측정이 아니고 같은 Terra 에이전트를 재사용하므로 이전 문제를 이미 알고 있다.

응답 전체를 authoring/work/m02-v2-retrieval/01-response.md에 UTF-8로 저장하고 동일 본문으로 응답하라. 다른 파일은 수정하지 말고 내부 추론을 기록하지 마.
~~~~~

응답 전체(편집 없음):

~~~~~markdown
# M02 v2.0.0 초기 주간 계획 — 원본 자료 탐색 결과

이것은 v2.0.0 원본 자료의 탐색·추출 연습입니다. 앞선 v1.0.0 시험의 최종 제출은 수정하지 않았고, 패키지 추천·조합 최적화·브리핑·임원 문답은 수행하지 않았습니다.

## 접근 범위와 원본 상태

확인한 필수 진입 문서는 `README.md`, `handbook/COMPANY.md`, `scenarios/M02.md` 및 M02 필수 DOC 12개입니다. 연결 부속으로 아래 CSV를 실제 열어 헤더와 전체 레코드 수를 확인했습니다. 모두 UTF-8 CSV이며 파일 자체의 행 잘림은 없었습니다.

| 부속 파일 | 전체 레코드 수 | 이번 추출의 용도 |
|---|---:|---|
| `company/people/exports/employee_directory.csv` | 36 | 계약시간 |
| `company/people/exports/skills_register.csv` | 108 | 유효 VERIFIED 스킬 |
| `company/people/exports/resource_allocations.csv` | 1,296 | 기존 승인 배정 |
| `company/people/exports/leave_requests.csv` | 648 | 최신 revision의 승인 휴가 |
| `company/people/exports/pool_authorizations.csv` | 8 | AX-POOL 승인 인력 |
| `company/people/exports/standard_cost_rates.csv` | 324 | 표준원가가 현금 추가 항목이 아님을 확인 |
| `company/projects/exports/investment_register.csv` | 54 | 패키지 의무·가치 |
| `company/projects/exports/resource_requirements.csv` | 81 | 패키지별 스킬 소요 |
| `company/projects/exports/package_cost_estimates.csv` | 108 | 패키지별 추가 현금 |
| `company/finance/exports/operating_journal.csv` | 1,331 | AX-POOL 기준비용 |
| `company/finance/exports/budget_workflow.csv` | 108 | 승인 예산·미승인 전망 |

필드 의미, 상태 및 revision 해석은 `company/DATA_DICTIONARY.md`로 확인했습니다. 현금 기준비용에는 `DOC-FIN-01`의 정의에 따라 내부 표준원가를 다시 더하지 않았습니다.

## 적용 필터와 결합 키

도구로 PowerShell `Import-Csv` 필터·집계를 실제 실행했습니다. 수동 해석은 DOC의 효력·상태 규칙을 적용한 부분입니다.

| 대상 | 사용 키·필터 | 제외한 범위·이유 |
|---|---|---|
| 계획 주 | `week_start = 2027-03-08` | 다른 8개 주차는 이번 주가 아니므로 제외 |
| 투자 풀 | `pool_id = AX-POOL`, `status = APPROVED`, `valid_from ≤ 2027-03-08 ≤ valid_to` | 명부 밖 직원은 DOC-HR-04상 추가 가용 인력으로 사용할 수 없음 |
| 직원·스킬 | `employee_id` 조인; `status = VERIFIED`, `valid_from ≤ 계획 주`, `valid_to` 공란 또는 계획 주 이후 | SELF_REPORTED·만료 인증 제외 |
| 기존 배정 | `week_start = 2027-03-08`, `status = APPROVED`, 직원별 `allocation_id` 행의 `hours` 합계 | DRAFT·REJECTED 및 다른 주차 제외; 한 직원의 여러 행을 모두 합산 |
| 휴가 | 대상 주·직원 후 `request_id`별 최대 `revision`만 선택, 그 행이 `APPROVED`일 때만 `hours` 합산 | 과거 revision, REQUESTED·CANCELLED 제외; 원시 16행 중 유효 승인 최신 행은 4행 |
| 예산 | `week_start = 2027-03-08`, `cost_center = AX-POOL`; `APPROVED`, CFO 서명, `effective_from` 존재 | DRAFT 및 SUPERSEDED revision, 다른 원가센터·주차 제외 |
| 기준비용 | `week_start = 2027-03-08`, `cost_center = AX-POOL`, `entry_type = BASELINE`, `status = POSTED`; `account`별 `net_amount` 부호 합계 | DRAFT 분개, 다른 entry type·원가센터·주차 제외. POSTED 환입은 음수로 포함 |
| 패키지 | 세 원장을 `(week_start, package_id)`로 결합; 카탈로그 `APPROVED_CATALOG`, 비용 `APPROVED_ESTIMATE`, 요구 `ALL_REQUIRED` | 다른 주차 패키지·비승인 카탈로그/견적 제외. 카탈로그 승인은 착수 승인이 아님 |

## 유효 승인 예산과 미승인 전망

| 구분 | 금액 USD | 원본 레코드 키 | 판정 |
|---|---:|---|---|
| 유효 승인 상한 | 28,000 | `budget_workflow.csv`: `BUD-AX-POOL-2027-03-08`, revision 2 | `APPROVED`, signatory `CFO`, `effective_from=2027-03-08`; 적용 |
| 미승인 전망 | 31,000 | 같은 `document_id`, revision 3 | `DRAFT`, signatory·effective_from 공란; 제외 |
| 대체된 과거본 | 27,000 | 같은 `document_id`, revision 1 | `SUPERSEDED`; 제외 |

이는 DOC-FIN-02의 AX-POOL 효력 기준 및 DOC-FIN-03의 미서명 초안 배제 규칙을 적용한 결과입니다. DOC-POL-01에 따라 최신 작성 초안에는 승인 효력을 부여하지 않았습니다.

## AX-POOL 현금 기준비용

필터를 통과한 `POSTED/BASELINE` 전표는 71행입니다. `net_amount`를 계정별로 실제 합산했습니다.

| 계정 | 의미 | 합계 USD | 전표 수 | 확인 레코드 키 |
|---|---|---:|---:|---|
| 6100 | 배부 급여 | 12,000 | 36 | `GL-01188`~`GL-01220` 및 `GL-012xx`의 6100 POSTED 36행 |
| 6200 | 공통 도구·기본 클라우드 | 3,000 | 20 | `GL-01221`~`GL-01255`의 6200 POSTED 20행; `GL-01255` 환입 −150 포함 |
| 6300 | 계약 운영·당직 | 5,000 | 15 | `GL-01239`~`GL-01253`의 6300 POSTED 15행 |
| 합계 | 기준비용 | **20,000** | **71** | 필터: AX-POOL / 2027-03-08 / BASELINE / POSTED |

`GL-01256`은 같은 주·원가센터의 `DRAFT` 6200 USD 900이므로 제외했습니다. 내부 급여 6100은 이미 이 USD 20,000에 포함됩니다. `standard_cost_rates.csv`의 `usd_per_hour`는 DOC-HR-03에서 분석용 표준원가로 정의되며, 현금 기준비용에 추가하지 않았습니다.

## 승인 인력풀: 스킬·기존 배정·휴가·추가 가용시간

풀 승인 키는 8명 모두 `pool_authorizations.csv`의 `AX-POOL / APPROVED / COO-POOL-0305 / 2027-03-08~2027-03-12`입니다. 추가 가용시간은 `weekly_contract_hours − APPROVED 기존 배정 합계 − 최신 APPROVED 휴가 합계`로 실제 계산했습니다.

| 직원 | 유효 VERIFIED 스킬·record_id | 계약 h | APPROVED 기존 배정 h·allocation_id | 최신 APPROVED 휴가 h·request/revision | 추가 가용 h |
|---|---|---:|---|---|---:|
| EMP-01 | BE · `SKL-0002` | 40 | 24 · `AL-01153, AL-01154, AL-01155` | 0 · — | 16 |
| EMP-02 | DATA · `SKL-0005` | 40 | 24 · `AL-01157, AL-01158, AL-01159` | 0 · — | 16 |
| EMP-03 | SRE · `SKL-0008` | 40 | 24 · `AL-01161, AL-01162, AL-01163` | 0 · — | 16 |
| EMP-04 | QA · `SKL-0011` | 40 | 24 · `AL-01165, AL-01166, AL-01167` | 0 · — | 16 |
| EMP-05 | BE · `SKL-0014` | 40 | 24 · `AL-01169, AL-01170, AL-01171` | 4 · `PTO-2027-03-08-EMP-05:r2` | 12 |
| EMP-06 | DATA · `SKL-0017` | 40 | 24 · `AL-01173, AL-01174, AL-01175` | 4 · `PTO-2027-03-08-EMP-06:r2` | 12 |
| EMP-07 | SRE · `SKL-0020` | 40 | 24 · `AL-01177, AL-01178, AL-01179` | 4 · `PTO-2027-03-08-EMP-07:r2` | 12 |
| EMP-08 | QA · `SKL-0023` | 40 | 24 · `AL-01181, AL-01182, AL-01183` | 4 · `PTO-2027-03-08-EMP-08:r2` | 12 |

스킬은 사람 이름이 아닌 `employee_id`로 조인했습니다. 상태·기간 필터 후 위 8개의 VERIFIED 스킬 레코드만 배정 자격으로 사용했습니다.

## 주간 패키지 카탈로그·스킬 소요·현금

아래 값은 `week_start=2027-03-08`로 세 프로젝트 원장을 `(week_start, package_id)`로 결합해 추출했습니다. 비용은 각 패키지의 `environment`와 `vendor_service` 두 `APPROVED_ESTIMATE` 행을 합산했습니다.

| 패키지 | 프로젝트 | 의무 / 가치점수 | 카탈로그 키 | 모든 스킬 소요·요구 키 | 현금 USD·비용 레코드 |
|---|---|---|---|---|---:|
| A | PRJ-01 | CONTRACT / 0점 | `2027-03-08:A` | BE 16h; QA 8h · `A:BE`, `A:QA` | 2,000 · `A:environment=1,000`, `A:vendor_service=1,000` |
| B | PRJ-03 | CONTRACT / 0점 | `2027-03-08:B` | SRE 16h; QA 8h · `B:SRE`, `B:QA` | 2,500 · `B:environment=1,250`, `B:vendor_service=1,250` |
| C | PRJ-02 | OPTIONAL / 8점 | `2027-03-08:C` | DATA 16h · `C:DATA` | 2,000 · `C:environment=1,000`, `C:vendor_service=1,000` |
| D | PRJ-04 | OPTIONAL / 6점 | `2027-03-08:D` | DATA 12h · `D:DATA` | 1,000 · `D:environment=500`, `D:vendor_service=500` |
| E | PRJ-06 | OPTIONAL / 7점 | `2027-03-08:E` | SRE 12h · `E:SRE` | 1,500 · `E:environment=750`, `E:vendor_service=750` |
| F | PRJ-07 | OPTIONAL / 9점 | `2027-03-08:F` | BE 12h; QA 8h · `F:BE`, `F:QA` | 1,800 · `F:environment=900`, `F:vendor_service=900` |

카탈로그 상태는 여섯 행 모두 `APPROVED_CATALOG`, 요구 상태는 모두 `ALL_REQUIRED`, 비용 상태는 모두 `APPROVED_ESTIMATE`입니다. 이는 심의·견적에 사용할 수 있다는 상태일 뿐, 신규 패키지의 착수 승인은 아닙니다.

## 누락·한계

- 이번 탐색은 현재 주의 초기 원본 레코드만 대상으로 했습니다. 시험 중 이벤트 델타나 앞선 v1 대화의 수치를 가져오지 않았습니다.
- 필수 DOC와 그 연결 부속의 본문·헤더·레코드 수 및 필요한 행은 확인했습니다. M02 선택 자료(DOC-HR-05, DOC-FIN-04, DOC-FIN-05, DOC-PRJ-01)와 무관 부서 자료는 읽지 않았습니다.
- 위 값은 의사결정 입력 추출 결과이며 패키지 선택, 배정안, 최적화, 브리핑 또는 승인 결론을 포함하지 않습니다.
~~~~~

## 02회차

실제 호출 문구:

~~~~~text
authoring/work/m02-v2-retrieval/02-prompt.txt의 전체 내용을 이번 입력으로 읽고 수행하세요. 응답 전체를 같은 폴더의 02-response.md에 저장하고 동일 내용으로 응답하세요. 이전 응답은 수정하지 않습니다.
~~~~~

입력 전체:

~~~~~text
추출된 주요 수치와 직원·패키지 값은 별도 Python 검산 결과와 일치한다. 다만 6100 전표 출처에 GL-01188~GL-01220 및 GL-012xx라고 적은 것은 재현 가능한 정확한 키 목록이 아니다. 내가 같은 조건으로 조회하니 GL-01185, GL-01186, GL-01187도 있었다. 6200의 연속 범위 GL-01221~GL-01255에는 다른 계정의 행도 끼어 있으므로 필터 없이 그대로 가져갈 수 없는 표현이다.

원본 operating_journal.csv를 다시 읽고 6100/6200/6300 각각의 정확한 연속 ID 구간 또는 개별 ID 목록, 수량, 부호 합계를 제시해줘. 환입 +150/-150과 DRAFT 900의 포함·제외를 개별 키로 확인해줘. 이전 응답은 고치지 말고 이 회차에 수정 근거를 남겨줘. 외부 채팅의 기억이 아닌 이번 파일 조회 결과로만 답해줘.

제작 중이던 회사 문서 양식도 정리되어 DOC-ORG-02, DOC-FIN-06, DOC-POL-01이 이제 섹션/결재 양식으로 확장되었다. 이 세 파일을 다시 읽고 앞서 사용한 승인·효력 해석이 바뀌는지도 확인해줘. 새로운 정답 계산이나 패키지 선택은 하지 않아도 된다.

응답 전체를 authoring/work/m02-v2-retrieval/02-response.md에 저장하고 동일 내용으로 응답하라. 다른 파일 및 앞선 v1 시험 제출은 수정하지 마.
~~~~~

응답 전체(편집 없음):

~~~~~markdown
# M02 v2.0.0 전표 키 정정 근거 및 결재 문서 재확인

이번 회차에 `company/finance/exports/operating_journal.csv`를 다시 읽고 다음 필터를 실제 적용했습니다.

`week_start=2027-03-08` AND `cost_center=AX-POOL` AND `entry_type=BASELINE` AND `status=POSTED`

이 결과는 앞선 응답의 범위형 전표 표현을 대체하는 정정 근거입니다. 앞선 응답 파일은 수정하지 않았습니다.

## 계정별 정확한 전표 키·수량·부호 합계

| 계정 | POSTED BASELINE 수량 | 정확한 연속 ID 구간 | 부호 있는 `net_amount` 합계 USD |
|---|---:|---|---:|
| 6100 | 36 | `GL-01185–GL-01220` | 12,000.00 |
| 6200 | 20 | `GL-01221–GL-01238`, `GL-01254–GL-01255` | 3,000.00 |
| 6300 | 15 | `GL-01239–GL-01253` | 5,000.00 |
| 합계 | 71 | 위 3개 계정의 필터 통과 행 | **20,000.00** |

6100은 `GL-01185`부터 `GL-01220`까지 36개 ID가 빠짐없이 연속입니다. 6200은 두 구간으로 분리되며, `GL-01239–GL-01253`은 6300 계정이므로 6200의 연속 범위에 포함하면 안 됩니다. 6300은 `GL-01239–GL-01253`의 15개 ID가 연속입니다.

## 환입과 초안의 개별 확인

| entry_id | account | status | net_amount USD | reference | 처리 |
|---|---:|---|---:|---|---|
| `GL-01254` | 6200 | POSTED | +150.00 | `ADJ-2027-03-08` | 6200 부호 합계에 포함 |
| `GL-01255` | 6200 | POSTED | −150.00 | `REV-ADJ-2027-03-08` | POSTED 환입으로 6200 부호 합계에 포함 |
| `GL-01256` | 6200 | DRAFT | +900.00 | `BATCH-2027-03-08` | DRAFT이므로 제외 |

따라서 `GL-01254`와 `GL-01255`는 각각 +150과 −150으로 모두 유효 전표이며 서로 상쇄됩니다. `GL-01256`은 같은 주·원가센터·계정이지만 DRAFT이므로 기준비용에 들어가지 않습니다. 이 처리는 DOC-FIN-01의 POSTED 기준과 `net_amount` 부호 합산 규칙에 따릅니다.

## 확장된 결재·정책 문서 재확인

이번 회차에 `company/organization/DOC-ORG-02.md`, `company/finance/DOC-FIN-06.md`, `company/policies/DOC-POL-01.md`의 현재 본문을 다시 읽었습니다. 세 문서는 섹션과 기록 양식이 추가됐지만, 앞서 적용한 승인·효력 해석은 바뀌지 않았습니다.

| 문서 | 이번에 확인한 추가 구조 | M02 해석에 미치는 영향 |
|---|---|---|
| DOC-ORG-02 | 역할별 권한·제한, 승인란(요청 번호/결정권자/승인·반려/일시) | Portfolio Analyst는 배분안을 제안하고 승인 전 실행을 확정할 수 없음. 동일 승인 예산 내 재배분은 COO, 증액은 CFO 권한이라는 해석 유지. 빈 승인란은 승인 증거가 아님. |
| DOC-FIN-06 | 현재 기준·제안 총액·기준 대비 차이·필수 의무·위험·결재자·결재 전 행동의 요청 표, COO/CFO/고객 계약 변경 상태란 | 유효 상한 내 패키지 교체는 COO 승인, 증액은 CFO 서면 승인이 필요하다는 해석 유지. 상태란이 비어 있으면 승인·서명 미취득이므로 집행 확정으로 표현할 수 없음. |
| DOC-POL-01 | 적용 대상·효력→승인 규정→유효 승인 계획→관측→의견·초안의 순서 및 검토 기록 양식 | AX-POOL의 유효 승인 revision 2를 적용하고 DRAFT revision 3을 제외한 해석 유지. 최신 초안이나 양식 확장 자체가 효력을 만들지 않음. |

따라서 이번 파일 조회와 확장 문서 재확인으로 예산·효력·권한에 관한 기존 추출 판단은 유지됩니다. 새 정답 계산, 패키지 선택, 배정안 또는 승인 결론은 생성하지 않았습니다.
~~~~~
