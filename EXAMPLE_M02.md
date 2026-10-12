# M02 정석 예시 — 예산·인력 재배분

패키지 v1.0.0 · **학습용 합성 예시** · 실제 응시 기록이나 유일한 정답이 아닙니다.

먼저 [README의 M02](README.md#m02)를 직접 풀어 본 뒤 읽는 것을 권합니다. 응시 중 읽었다면 예시 사용을 기록하세요. 채점자는 이 예시와의 일치 여부로 점수를 매기지 않고 README 원자료·루브릭을 적용합니다. 사용자 요청으로 추가한 공개 학습 자료이며 비공개 정답집이 아닙니다.

이 예시는 KO 분석표와 영어 브리핑·문답을 결합한 MIX 형식입니다. 실제 사용자 대화 원문·실제 수행 시간·모델별 독립 채점 결과는 없습니다. 아래 프롬프트와 임원 답변은 **어떻게 접근할 수 있는지 보여 주는 작성 예시**이며 실행된 대화로 주장하지 않습니다. 이 문서만 제출해서 AI 활용 과정 점수를 받을 수 없습니다.

## 1. 판단 기준과 자료 확인

먼저 계약상 필수 A/B와 기존 운영비를 보존하고, 예산·인력 제약을 충족하는 선택 투자 중 **기대가치점수 합이 큰 안**을 선택하겠습니다. 점수는 매출이나 성공 확률이 아닌 이번 연습의 비교 지표입니다. 실제 사업 위험을 다르게 가중한 실행 가능한 대안도 가능합니다.

- DOC-FIN-02 승인 예산: USD 28,000. DOC-FIN-03의 31,000은 더 최근 버전이어도 미승인 초안이므로 적용하지 않습니다(DOC-POL-01).
- DOC-FIN-01 기준비용: 급여 12,000 + 공통 기본료 3,000 + 기존 운영·당직 5,000 = USD 20,000.
- DOC-PRJ-04 필수 패키지: A 2,000 + B 2,500 = USD 4,500. 따라서 선택 투자에 쓸 수 있는 현금은 28,000 − 20,000 − 4,500 = **USD 3,500**입니다.
- DOC-HR-01/02/04: BE·DATA·SRE·QA 각각 승인 풀 가용량 16+12=28h. A/B를 반영하면 BE 12h, DATA 28h, SRE 12h, QA 12h가 남습니다.
- DOC-HR-03 시간당 원가는 이미 지급하는 급여의 분석용 값입니다. 추가 배정 시간×시간당 원가를 현금 예산에 다시 합산하지 않습니다.

## 2. 초기 권고안

필수 A/B와 선택 E/F를 제안합니다. E/F는 SRE 12h, BE 12h, QA 8h를 요구하고, 필수 배정 뒤 남은 풀에 맞습니다. DATA 가용량이 남더라도 예산이 제한되므로 모든 직원시간을 소진할 필요는 없습니다.

| 패키지 | 내용 | 증분 현금 USD |
|---|---|---|
| A | 계약 납품 작업 | 2000 |
| B | 계약 복구 검증 | 2500 |
| E | 운영 자동화 | 1500 |
| F | 고객 기능 확장 | 1800 |

총액 = 20,000 + 2,000 + 2,500 + 1,500 + 1,800 = **USD 27,800**. 승인 예산 여유는 **USD 200**. 선택 투자 가치점수는 7+9=**16**입니다. “지난 주보다 절감”이라고 표현하지 않습니다. 지난 주 실적 27,400과 업무 구성이 다르므로 현재 의사결정의 적절한 비교 기준이 아닙니다.

| 패키지 | 직원 | 스킬 | 추가 h |
|---|---|---|---|
| A | EMP-01 | BE | 16 |
| A | EMP-04 | QA | 8 |
| B | EMP-03 | SRE | 16 |
| B | EMP-04 | QA | 8 |
| E | EMP-07 | SRE | 12 |
| F | EMP-05 | BE | 12 |
| F | EMP-08 | QA | 8 |

| 직원 | 스킬 | 계약 h | 기존 h | 휴가 h | 추가 h | 총계 h | 남은 h |
|---|---|---|---|---|---|---|---|
| EMP-01 | BE | 40 | 24 | 0 | 16 | 40 | 0 |
| EMP-02 | DATA | 40 | 24 | 0 | 0 | 24 | 16 |
| EMP-03 | SRE | 40 | 24 | 0 | 16 | 40 | 0 |
| EMP-04 | QA | 40 | 24 | 0 | 16 | 40 | 0 |
| EMP-05 | BE | 40 | 24 | 4 | 12 | 40 | 0 |
| EMP-06 | DATA | 40 | 24 | 4 | 0 | 28 | 12 |
| EMP-07 | SRE | 40 | 24 | 4 | 12 | 40 | 0 |
| EMP-08 | QA | 40 | 24 | 4 | 8 | 36 | 4 |

모든 직원은 기존+휴가+추가≤40h입니다. 스킬 총 필요는 BE 28, DATA 0, SRE 28, QA 24h이며 제공 스킬과 일치합니다. 나머지 28명은 가용량 0h라 새 업무를 배정하지 않습니다. 직원별 시간은 작업 간 중복 합산하지 않았습니다.

## 3. 대안 비교와 선택 이유

| 대안 | 총액 USD | 선택 가치 | 판단 |
|---|---:|---:|---|
| A/B + E/F | 27,800 | 16 | 초기 기준에서 권고. 남은 현금은 적지만 필수 업무와 시간 제약 충족 |
| A/B + D/F | 27,300 | 15 | 가치 1점을 포기하면 여유금 500 증가. 데이터 품질을 더 중시하면 합리적인 대안 |
| A/B + C/E | 28,000 | 15 | AI 파일럿 선호를 반영할 수 있으나 여유금 0이며 E/F보다 점수 1 낮음 |
| A/B + C/D | 27,500 | 14 | DATA 투자 집중안. 기술분야 편중과 기대가치 차이를 설명할 필요 |

현재 선택 기준에서의 “최대” 주장을 검증하기 위해 C~F의 2^4=16개 조합을 아래에 모두 비교했습니다. 예산과 모든 스킬 제약을 함께 적용했습니다. 이 표는 다른 전략 목표까지 유일하게 최적임을 뜻하지 않습니다.

| 선택 투자(필수 A/B 별도) | 주간 총액 USD | 가치점수 | 초기 제약 내 실행 |
|---|---|---|---|
| 없음 | 24500 | 0 | 가능 |
| C | 26500 | 8 | 가능 |
| D | 25500 | 6 | 가능 |
| E | 26000 | 7 | 가능 |
| F | 26300 | 9 | 가능 |
| CD | 27500 | 14 | 가능 |
| CE | 28000 | 15 | 가능 |
| CF | 28300 | 17 | 불가 |
| DE | 27000 | 13 | 가능 |
| DF | 27300 | 15 | 가능 |
| EF | 27800 | 16 | 가능 |
| CDE | 29000 | 21 | 불가 |
| CDF | 29300 | 23 | 불가 |
| CEF | 29800 | 24 | 불가 |
| DEF | 28800 | 22 | 불가 |
| CDEF | 30800 | 30 | 불가 |

## 4. 승인·실행 계획

| 시점 | 책임 | 조치 | 착수 조건 |
|---|---|---|---|
| 즉시 | Portfolio Analyst | A/B/E/F 비용·직원표와 비교안 제출 | FIN-02 상한 적용 |
| 착수 전 | HR | 스킬·휴가·시간 검산 확인 | DOC-HR-04/05 조건 유지 |
| 착수 전 | COO | 상한 내 패키지·배정 승인 | 서면 승인 기록 후 실행 |
| 같은 승인 검토 | Product sponsor·Client Executive | C/D 미선택 이유와 차기 재검토 항목 전달 | 새 납기나 미래 승인 약속 금지 |
| 실행 중 조건 변경 시 | Portfolio Analyst→COO/CFO | 비용·시간표 재계산, 영향 받은 작업의 신규 착수 보류 | 증액은 CFO 승인, 필수 A/B 해제는 계약 변경까지 필요 |

이 계획은 **승인 요청안**입니다. COO의 승인이 이미 났다고 쓰지 않습니다. C/D가 이번 주 선택 투자인 점과 기존 서비스는 고정비로 유지되는 점을 구별해 전달합니다. 예상 가치는 추정치이며 미실현 위험을 다음 검토에서 확인합니다.

## 5. 영어 브리핑 예시

> I recommend retaining mandatory packages A and B and selecting E and F for this week. The proposal totals USD 27,800, leaving USD 200 within the approved limit. I have used FIN-02 rather than the newer, unapproved budget draft. The base cost already includes internal salaries, so assigning available staff does not create another payroll charge in this cash forecast.
>
> The proposed assignments require 28 backend hours, 28 SRE hours and 24 QA hours. Each employee remains within their weekly contract after existing commitments and leave. Data engineering capacity remains available; using every available hour is not our objective when cash is constrained.
>
> Under the stated objective of maximizing the supplied expected-value scores, E and F produce 16 points. D and F offer 15 points with USD 700 of headroom, while C and E preserve the AI pilot at 15 points and use the full budget. I compared all optional combinations before making the narrow score-maximization claim. These scores do not guarantee revenue or future outcomes.
>
> I request COO approval for the package selection and staff assignments, with HR confirmation before work begins. C and D would not proceed this week under this proposal; their existing services remain covered by the base cost. If leadership prefers more headroom or a different strategic priority, I can present the corresponding feasible alternative. Any budget or leave change will trigger a recalculation before further commitments. I am not treating this proposal as approved expenditure.

## 6. 임원 3라운드 대응 예시

아래는 가능한 질문·답변의 학습용 예시입니다. 실제 시험에서는 자신의 제출물에 맞는 질문을 받고, 실제 시행한 EVT만 제출 기록에 넣습니다.

**라운드 1 / CFO — “Why not keep the AI pilot, and how strong is your optimality claim?”**

> Keeping C with E is feasible at USD 28,000 and scores 15. E with F scores 16 at USD 27,800. I checked every combination of the four optional packages, but the conclusion is optimal only for the supplied additive score and current constraints. If preserving the AI pilot is an overriding strategic preference, C and E is a valid alternative; I would record that objective change rather than call it a mathematical error.

**라운드 2 / EVT-M02-2 — 승인 예산이 USD 27,000으로 축소.**

새 선택 투자 여력=27,000−20,000−4,500=2,500. 기존 E/F는 800 초과하므로 유지할 수 없습니다. D/E를 선택하면 총액 **27,000**, 점수 **13**, 추가 DATA 12h와 SRE 12h가 필요합니다. A/B는 유지하고 D=EMP-06 DATA 12h, E=EMP-07 SRE 12h로 배정할 수 있습니다. 기존 F 배정은 제거하고 전체 표를 교체합니다.

> With the reduced cap, I withdraw the E/F proposal and recommend D/E, subject to the revised allocation approval. The total is USD 27,000. A and B remain protected. I would release the proposed F assignments, allocate D to EMP-06 and retain E with EMP-07. This uses all available cash, so any further constraint change requires another review.

**라운드 3 / EVT-M02-3 — EMP-07 휴가 4h 추가, 가용량 8h. 27,000 상한 유지.**

SRE 총 가용량은 16+8=24h가 됩니다. B 16h와 E 12h의 합 28h를 충족하지 못하므로 D/E도 불가합니다. B를 다른 직원에게 일부 분할해도 총량 부족 4h는 사라지지 않습니다. 선택 투자 F만 고르면 총액 **26,300**, 여유 **700**, 점수 **9**이며 시간 제약을 충족합니다. A/B/F 배정은 초기안에서 E만 제거한 표와 같습니다. C 단독은 8점, D 단독은 6점이며 C/D·D/F 등은 축소 예산을 넘습니다.

> The leave change reduces total SRE capacity to 24 hours. B and E together require 28, so moving hours between SRE employees cannot solve the shortage. I would withdraw E and recommend F as the optional package under the current cap. The revised total is USD 26,300 with USD 700 remaining. A and B remain mandatory, and the revised plan still needs allocation approval. I would update the budget, staff table and briefing together so the final submission reflects both events.

위 최종안은 이벤트 후 조건에서의 안입니다. 초기 E/F를 원래 조건에서 틀렸다고 소급 평가하지 않습니다. 원안·수정안·변경 이유를 구분하는 것이 핵심입니다.

## 7. AI 협업·검증의 예시

다음은 실제 대화 기록이 아닌 사용할 수 있는 요청의 예입니다.

1. “FIN-02/03과 POL-01에서 효력 있는 예산을 구별하고 근거를 보여줘. 배분안은 아직 만들지 마.”
2. “HR-01/02/04로 스킬별 가용량을 재계산하고, 기존 투입과 휴가를 모두 차감했는지 확인해줘.”
3. “필수 A/B를 유지한 상태에서 C~F 조합의 현금·시간 제약을 비교해줘. 비용에 내부 급여를 중복해서 넣지 마.”
4. “내 A/B/E/F 표를 독립적으로 검산하고, 실행 불가능하거나 승인되지 않은 약속이 있으면 지적해줘.”
5. “두 EVT를 누적 적용한 최종안에서 예산·스킬 총량·직원별 용량을 다시 확인해줘. 변경 전 판단과 구분해줘.”

계산 결과를 표·자료와 직접 대조하고 선택을 확정하는 실제 사용자 행동이 있어야 과정 증거가 됩니다. 이 예시를 읽은 사실이나 위 문구를 복사한 횟수만으로 과정 역량이 입증되지 않습니다.

## 검증 범위

이 예시의 조합표와 직원 배정표는 로컬 Python 생성기로 산출됩니다. 초기안과 두 이벤트 이후의 예산·시간·최대 기대점수 주장은 제작 검증에서 각각 재계산합니다. 검증 결과·미검증 한계는 README의 품질 기록에 따릅니다. 실제 외부 모델의 점수나 사용자 수행시간을 이 문서로 대신하지 않습니다.
