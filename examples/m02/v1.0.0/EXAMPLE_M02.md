**왜 좋았는지:** LLM 초안을 원자료·계산·반례로 점검하고, 예산·휴가 변경까지 반영해 실행 가능한 승인 요청안으로 확정했다.  
**어떻게 해야 좋은지:** 목표·출처·제약을 먼저 주고 생성 → 검산 → 오류 수정 → 명시적 채택을 기록하며, 사전 답안 노출도 정확히 밝힌다.  
**어떻게 실전에 적용할 수 있는지:** 회사 원장·로그의 기간·상태·키를 확인한 뒤 보고·발표 초안을 맡기고, 변경 조건과 승인 권한을 재확인해 제출한다.

## 사후 채점 — 기록 원문과 구별

**학습용 우수 사례로 활용할 수 있으나 무결점 정답은 아닙니다. 제작자 사후 채점 97.50/100입니다.** 평가 대상은 v1.0.0의 실제 12회차 기록과 종료 전에 확정한 출력물입니다. 사후 검산은 결과의 정확성을 확인하는 자료이며 당시 응시 과정으로 소급 가점하지 않았습니다.

| 영역 | 배점 | 수준 | 점수 | 원문 근거·채점 사유 |
|---|---:|---:|---:|---|
| 문제 이해·구조화 | 10 | 100% | 10.00 | [02·03·10회차](M02_PROMPT_CHAIN.md#turn-02) — 필수 A/B와 선택 투자를 분리하고, 가치점수 최대화·예산·스킬 의존성을 정했다. |
| 자료 탐색·근거 정확성 | 15 | 100% | 15.00 | [02·03·11·12회차](M02_PROMPT_CHAIN.md#turn-02) — 승인 28,000과 미승인 31,000을 구별하고, 원자료·직원별 중간값·단위를 추적했다. v1 제공자료 범위의 평가다. |
| 규정·제약 적용 | 15 | 100% | 15.00 | [08~12회차](M02_PROMPT_CHAIN.md#turn-08) — 예산 27,000과 추가 휴가를 누적 반영하고 A/B 유지, 초과배정 금지, COO 승인 전 제안 상태를 지켰다. |
| AI 활용·검증 과정 | 15 | 100% | 15.00 | [03·04·10~12회차](M02_PROMPT_CHAIN.md#turn-03) — 다른 합산 경로와 원자료 대조를 요청하고, 금액 차이·SRE 분할 반례·점수 단위·비교 범위를 실제로 확인·수정했다. |
| 대안 비교·의사결정 | 15 | 100% | 15.00 | [02·08·10·12회차](M02_PROMPT_CHAIN.md#turn-02) — 16개 선택 조합과 변경 후 대안을 동일 기준으로 비교했다. 최적은 제공된 가치점수와 허용된 선택지 안에서만 주장했다. |
| 최종 산출물 | 10 | 75% | 7.50 | [12회차](M02_PROMPT_CHAIN.md#turn-12) — 표·브리핑·결재 요청은 일치한다. 다만 EXPORT의 예시 해설 사용 없음은 응시자 역할의 사전 답안 노출을 정확히 공개하지 못해 2.50점 감점했다. |
| 이해관계자 대응 | 10 | 100% | 10.00 | [05~12회차](M02_PROMPT_CHAIN.md#turn-05) — 브리핑 5/5 + 실제 Q&A 5/5. CFO·COO 요구에 선택 이유와 전환 조건을 설명하고 승인 요청으로 마무리했다. |
| 언어·전달 명료성 | 10 | 100% | 10.00 | [05·11·12회차](M02_PROMPT_CHAIN.md#turn-05) — 한국어 표와 영어 전달문을 구분하고 최종본에서 차이·잔액·증액, 가치점수와 USD, 비교 범위를 명확히 했다. |
| **합계** | **100** | — | **97.50** | 제작자 사후 채점; 독립 외부 평가 아님 |

[상세 평가·계산 근거·오류별 판정·개선 프롬프트](../EVALUATION.md)를 함께 읽으세요. 아래 원문 중 “예시 해설·외부 자료 사용: 없음”은 시험용 LLM에 제공한 자료만 설명한 것으로도 읽히지만, 응시자 역할인 상위 Codex는 기존 답안을 알고 있었습니다. 제출 메타정보의 이 불완전한 공개를 감점했습니다. 당시 프롬프트·응답·EXPORT는 사후 수정하지 않았습니다.

---

# M02 학습 예시 — LLM 생성과 응시자의 검증·선택

이 예시에서는 응시자가 리포트나 발표문을 직접 작문하지 않습니다. **gpt-5.6-terra 시험용 LLM이 분석표·브리핑·임원 답변 초안을 생성하고, 상위 Codex가 응시자로서 지시·검증 요청·선택·최종 확정을 수행했습니다.**

[실제 전체 프롬프트·응답 체인](M02_PROMPT_CHAIN.md)에는 가용성 확인부터 종료·제출까지의 회차와 첨부자료가 들어 있습니다. 복사해 사용할 수 있는 입력 예와 실제 응답을 함께 볼 수 있습니다. 체인 안의 응답은 관측 기록이며, 이후의 설명용 모범 문장으로 교체하지 않았습니다.

실행일 2026-10-13. 자료는 v1.0.0 / cc3f50cf9a9e288b237d558d76cac2d3cbc4eb4c입니다. 새 브라우저 ChatGPT에서 수행한 시험이나 실제 사람의 45분 실측·독립 채점이 아닙니다. 응시자 역할의 Codex는 기존 답안을 알고 있었으므로 블라인드 성능 평가로 해석하지 마세요. 내부 추론은 기록 대상이 아닙니다.

## 활용할 입력의 흐름

1. 역할·자료·MIX·시간을 지정하고, 해법 전에 필수 자료 접근 확인을 요청합니다.
2. 목표함수와 계약·승인 제약을 정한 뒤, LLM에 계산과 대안 비교를 맡깁니다.
3. 원자료 대조·별도 재계산·직원별 용량 검증을 요청하고 승인 요청안과 영어 브리핑 생성을 맡깁니다.
4. 생성된 브리핑을 채택해 발표합니다. 임원 질문에는 HELP로 영어 답변 초안을 받아, 근거 확인 후 채택·수정합니다.
5. 변경 조건을 누적 적용한 최종 표·브리핑을 확인하고 FINAL→END→EXPORT로 확정·정리합니다.

직접 작문 대신 무엇을 확인하도록 요청했고 왜 제안을 채택했는지가 핵심입니다. 같은 LLM이 스스로 맞다고 한 것만으로 검증이 끝났다고 보지 않습니다. 모델의 계산 설명과 아래 별도 수치 검토를 구분하세요.

## 실제 생성된 제출 정리

아래는 마지막 EXPORT에 대한 LLM 응답 원문입니다. 생성·확정된 답안을 새로 작문해 바꾸지 않았습니다. 파일 안의 모델명·기록 범위 같은 메타정보도 당시 응답에 해당하며 제작자의 확인은 전체 체인과 검토 기록을 기준으로 합니다.

**기록 해석 보완:** EXPORT의 “예시 해설·외부 자료 사용: 없음”은 시험용 LLM이 EXAM_INPUT만 읽었다는 범위입니다. 응시자 역할인 상위 Codex는 이전 예시를 작성해 알고 있었습니다. 전체 실행을 답안 미노출 시험으로 해석할 수 없습니다. 10회차 최초 호출의 사용 한도 중단과 재시도도 전체 체인에 표시했습니다. 03회차 차이 금액 혼동, 10회차 점수의 USD 열 표기, 11회차 비교 범위 표현은 수정 전후를 모두 남겼습니다.

~~~~~markdown
# submission

## 메타정보

- 시나리오 ID: M02 — Budget & Workforce Restructuring
- 언어 / 제한 시간: MIX / 45분 권장, 실제 소요시간 미측정
- 사용 모델: gpt-5.6-terra
- 응시자: 상위 Codex. 사람의 블라인드 시험이나 ChatGPT 웹 UI 시험이 아닌 LLM 서브에이전트 시뮬레이션.
- 자료 버전: 실행 시 제공된 v1.0.0
- 기준 commit: `cc3f50cf9a9e288b237d558d76cac2d3cbc4eb4c`
- 기록 범위: 실제 입력·응답 파일 전체를 상위 Codex가 별도 보존·조립. 이 제출 정리는 그 원문을 재작성하지 않음.
- 실제 대화 원문 위치·범위: `authoring/work/m02-terra-20261013/01-prompt.txt`~`12-prompt.txt` 및 대응하는 `01-response.md`~`12-response.md`; `transcript.txt`는 이 응답에서 생성하지 않음.
- 예시 해설·외부 자료 사용: 없음. EXAM_INPUT.md에 제공된 자료만 사용.

## 최종 산출물

### 예산·인력 표, 패키지·스킬 검산, 비교 대안, COO 결재 요청

- 제출 상태: 확정 제출
- 확정 근거: 12회차 사용자 `FINAL`
- 작성 주체 확인 수준: AI 생성, 사용자 수정
- 사용자 수정: 비교 대안의 A+B+D 행을 “선택 패키지 하나를 시행하는 세 대안 중 가장 큰 여유를 남기지만”으로 수정해 확정.
- 출처: DOC-HR-01, DOC-HR-02, DOC-HR-03, DOC-HR-04, DOC-PRJ-04, DOC-FIN-01, DOC-FIN-02, DOC-FIN-06, DOC-ORG-02; EVT-M02-2, EVT-M02-3.

#### 누적 적용 조건

| 조건 | 현행 적용 |
|---|---|
| EVT-M02-2 | 승인 총 현금 상한 USD 27,000. DOC-FIN-01 기준비용 USD 20,000과 필수 A/B 유지. |
| EVT-M02-3 | EMP-07 휴가 총 8h, 추가 가용 8h. |
| 제안 상태 | COO 승인 요청안이며 승인된 집행계획이 아님. |

#### 직원별 시간과 배정

추가 가용시간 계산: `주 계약 40h − 기존 투입 − 휴가`.

| 직원 | 스킬 | 기존 h | 휴가 h | 추가 가용 h | 제안 추가 h | 잔여 h | 제안 배정 |
|---|---|---:|---:|---:|---:|---:|---|
| EMP-01 | BE | 24 | 0 | 16 | 16 | 0 | A: BE 16h |
| EMP-02 | DATA | 24 | 0 | 16 | 0 | 16 | — |
| EMP-03 | SRE | 24 | 0 | 16 | 16 | 0 | B: SRE 16h |
| EMP-04 | QA | 24 | 0 | 16 | 16 | 0 | A: QA 8h; B: QA 8h |
| EMP-05 | BE | 24 | 4 | 12 | 12 | 0 | F: BE 12h |
| EMP-06 | DATA | 24 | 4 | 12 | 0 | 12 | — |
| EMP-07 | SRE | 24 | 8 | 8 | 0 | 8 | — |
| EMP-08 | QA | 24 | 4 | 12 | 8 | 4 | F: QA 8h |

#### 패키지·스킬 검산

| 패키지 | 상태 | 현금 USD | 가치점수 | 요구 스킬 | 제안 배정 | 판정 |
|---|---|---:|---:|---|---|---|
| A | 필수 | 2,000 | 0점 | BE 16h, QA 8h | EMP-01 BE 16h; EMP-04 QA 8h | 충족 |
| B | 필수 | 2,500 | 0점 | SRE 16h, QA 8h | EMP-03 SRE 16h; EMP-04 QA 8h | 충족 |
| F | 선택 | 1,800 | 9점 | BE 12h, QA 8h | EMP-05 BE 12h; EMP-08 QA 8h | 충족 |

| 스킬 | A/B/F 수요 h | 제안 배정 h | 새 승인 풀 가용 h | 잔여 h | 판정 |
|---|---:|---:|---:|---:|---|
| BE | 28 | 28 | 28 | 0 | 충족 |
| DATA | 0 | 0 | 28 | 28 | 충족 |
| SRE | 16 | 16 | 24 | 8 | 충족 |
| QA | 24 | 24 | 28 | 4 | 충족 |

E는 SRE 12h가 필요하지만 B 후 SRE 잔여는 8h입니다. EMP-03·EMP-07의 새 합산 SRE 가용 24h보다 B+E 수요 28h가 4h 크므로 E 포함안은 실행 불가입니다.

#### 비용·여유금 검산

| 구분 | 항목 | 현금 USD | 가치점수 |
|---|---|---:|---:|
| 기준비용 | 내부 급여 | 12,000 | — |
| 기준비용 | 공통 도구·클라우드 기본료 | 3,000 | — |
| 기준비용 | 기존 계약 운영·당직 | 5,000 | — |
| 기준비용 소계 |  | 20,000 | — |
| 필수 패키지 | A+B | 4,500 | 0점 |
| 선택 패키지 | F | 1,800 | 9점 |
| 제안 총액 | 20,000 + 4,500 + 1,800 | 26,300 | 9점 |
| 현재 승인 상한 | EVT-M02-2 | 27,000 | — |
| 승인 상한 대비 차이 | 26,300 − 27,000 | −700 | — |
| 미사용 예산 | 27,000 − 26,300 | 700 | — |
| 추가 증액 요청액 |  | 0 | — |

DOC-HR-03 시간당 원가는 분석용 표준원가이며, 내부 급여 USD 12,000은 DOC-FIN-01 기준비용에 포함되어 현금 합계에 다시 더하지 않았습니다.

#### 비교 대안

| 선택안 | 총액 USD | 미사용 예산 USD | 제공 기대가치 | 비교 |
|---|---:|---:|---:|---|
| A+B+F — 권고 | 26,300 | 700 | 9점 | 가능한 조합 중 제공 기대가치 최대. 고객 기능 확장을 선택. |
| A+B+C | 26,500 | 500 | 8점 | AI 수요 파일럿을 유지하지만 F보다 1점 낮음. |
| A+B+D | 25,500 | 1,500 | 6점 | 데이터 품질 개선을 선택하고, 선택 패키지 하나를 시행하는 세 대안 중 가장 큰 여유를 남기지만 가치가 낮음. |
| A+B만 | 24,500 | 2,500 | 0점 | 선택 투자를 모두 연기. |

C+D는 선택 현금 USD 3,000으로 한도를 USD 500 초과하고, D+F는 USD 2,800으로 USD 300 초과합니다. 제공 기대가치의 최대화는 이 비교 범위와 점수에 한정하며 실제 매출 최대 주장이 아닙니다.

#### COO 결재 요청

| 항목 | 승인 요청 내용 |
|---|---|
| 현재 유효 기준 | EVT-M02-2에 따른 승인 총 현금 상한 USD 27,000 |
| 제안 | 필수 A/B 유지, 선택 F; 총액 USD 26,300 |
| 상한 대비 차이 | −USD 700; 미사용 예산 USD 700 |
| 증액 요청 | USD 0 |
| 요청 결재자 | COO — 승인 상한 내 패키지·인력 재배분 승인 |
| 위험·영향 | BE 추가 가용 전부 사용. C·D는 이번 요청안에서 미선택, E는 새 SRE 가용량으로 실행 불가. |
| 결재 전 행동 | COO 승인 전 착수·확정 배정하지 않음. HR이 업데이트된 EMP-07 휴가·계약시간 재확인 후 팀장이 주간 배치 시작. |

### English briefing

- 제출 상태: 확정 제출
- 확정 근거: 12회차 사용자 `FINAL`
- 작성 주체 확인 수준: AI 생성
- 출처: 위와 같음.

**Subject: Revised approval request — weekly allocation A, B, and F**

I am requesting COO approval for a revised weekly allocation of USD 26,300: mandatory packages A and B, plus optional package F. This is a proposal for approval, not an approved execution plan.

The current ceiling is USD 27,000 following the CFO budget change. The USD 20,000 baseline remains fixed, and mandatory A and B require USD 4,500. F adds USD 1,800, leaving USD 700 unspent. Internal salaries are already included in the baseline, so hourly employee cost is not added again.

The second change is EMP-07’s additional leave. Their available SRE capacity is now 8 hours, reducing total approved-pool SRE capacity to 24 hours. B requires 16 SRE hours. That leaves 8 hours, which cannot satisfy E’s 12-hour requirement. Redistributing between EMP-03 and EMP-07 cannot resolve this, because B and E would require 28 SRE hours in total. I therefore removed E from this approval request before execution.

The proposed allocation fully staffs A, B, and F: EMP-01 and EMP-04 cover A; EMP-03 and EMP-04 cover B; EMP-05 and EMP-08 cover F. The allocation uses 28 BE, 16 SRE, and 24 QA hours, all within the updated available capacity.

Among feasible optional choices under the USD 2,500 limit and the updated skill constraints, F has the highest provided expected-value score, 9. C would score 8 and D would score 6. This comparison uses the supplied expected-value scores only; it does not claim actual revenue is maximized. C and D are not selected in this proposal.

I request COO approval for this within-ceiling package and workforce reallocation. Before work begins, HR must reconfirm the updated leave and contract hours. Until that approval and confirmation are complete, no package is authorized to start and no staffing assignment is final.

## 결정·변경 기록

| 턴/시점 | 결정 또는 수정 | 근거 DOC-ID | 변경 이유 | 최종본 반영 |
|---|---|---|---|---|
| 03 | A/B/E/F 승인 요청안과 초안 생성 | FIN-02, PRJ-04, HR-01~04 | 당시 USD 28,000·가용시간 조건에서 제공 기대가치 최대 조합 | EVT 전 판단 기록 |
| 04~05 | 상한 대비 차이와 증액 요청 분리; 초기 영어 브리핑 제출 | FIN-02, FIN-06, ORG-02 | −USD 200과 증액 요청 USD 0을 구분 | 초기 발표 기록 |
| 07~09 | EVT-M02-2 반영, A/B/D/E로 변경 | FIN-01, PRJ-04 | 상한 USD 27,000; 선택 한도 USD 2,500 | EVT-M02-3 전 판단 기록 |
| 09~11 | EVT-M02-3 반영, A/B/F로 변경 | HR-01, HR-02, HR-04, PRJ-04 | EMP-07 가용 8h로 E 불가 | 최종 반영 |
| 12 | A+B+D 비교 문구 한정 수정 | 최종 후보 비교 표 | A+B만의 여유 USD 2,500이 더 큼 | 최종 반영 |

## 이벤트·문답·도움

| 시나리오/EVT-ID | 실제 조건·적용 시점 | 질문 | 답변 또는 원문 위치 | HELP 내용/여부 |
|---|---|---|---|---|
| 초기 발표 | 05회차 | CFO Round 1: E/F의 최고 실행 가능 판단 근거 | 06 도움 초안, 07 채택 답변 | HELP 사용: 16개 조합·제약·한계 답변 초안 |
| EVT-M02-2 | 07회차 Round 2부터 총 상한 USD 27,000; FIN-01·A/B 유지 | 수정 배분과 가치·여유 트레이드오프 | 08 도움 초안, 09 채택 답변 | HELP 사용: D+E 재계산·답변 초안 |
| EVT-M02-3 | 09회차 Round 3부터 EMP-07 추가 휴가 4h, 가용 12→8h; EVT-M02-2 유지 | 수정 배분과 잔여 스킬 검증 | 10 도움 초안, 11 채택 답변 | HELP 사용: SRE 총량·A/B/F 재계산·답변 초안 |

- 계획/실제 Q&A 라운드 수: 3/3. 각 라운드 후속 질문은 시행하지 않음.
- 질문 미시행과 미응답 구분: 세 주질문 모두 응답됨. 후속 질문은 계획상 최대 1회였으나 시행하지 않음.

## 확인 불가·누락

- 실제 소요시간: 미측정. 메시지 수나 시각으로 추정하지 않음.
- 실제 대화 원문: 이 제출 정리는 재작성하지 않음. 상위 Codex가 보존·조립하는 `01-prompt.txt`~`12-prompt.txt`와 `01-response.md`~`12-response.md`가 원문 범위이며, `transcript.txt`는 없음.
- 종료 상태: `FINAL`로 위 산출물을 확정했고, `END`로 시험을 종료함. 이후 새 답안·수정·누락 보충은 생성하지 않음.
~~~~~

## 기존 계산 참고 예시

아래는 이번 실행 전에 제작자가 작성한 계산 설명입니다. 실제 Terra 응답과 구별하는 **참고 부록**이며 채점 정답표나 실제 대화 기록이 아닙니다. 전체 응답 체인을 대체하지 않습니다.

# 참고 부록 — 기존 제작자 계산 설명

패키지 v1.0.0 · **학습용 합성 예시** · 실제 응시 기록이나 유일한 정답이 아닙니다.

먼저 [README의 M02](https://github.com/tls8012/llm_competency_assessment/blob/cc3f50cf9a9e288b237d558d76cac2d3cbc4eb4c/README.md#m02)를 직접 풀어 본 뒤 읽는 것을 권합니다. 응시 중 읽었다면 예시 사용을 기록하세요. 채점자는 이 예시와의 일치 여부로 점수를 매기지 않고 README 원자료·루브릭을 적용합니다. 사용자 요청으로 추가한 공개 학습 자료이며 비공개 정답집이 아닙니다.

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
