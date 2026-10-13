"""Recompute M02 from the preserved v1 source, not the author's answer generator.

Published use: python recompute.py (writes verification.json alongside the script).
This checks arithmetic and allocations; rubric scores remain an attributed judgment.
"""
import hashlib
import itertools
import json
import re
from pathlib import Path

HERE=Path(__file__).resolve().parent
if (HERE/'work/m02-terra-20261013').exists():
    source=(HERE/'work/m02-terra-20261013/EXAM_INPUT.md').read_text(encoding='utf-8')
    final=(HERE/'work/m02-terra-20261013/12-response.md').read_text(encoding='utf-8')
    out=HERE/'work/m02-grading-verification.json'
else:
    chain=(HERE.parent/'v1.0.0/M02_PROMPT_CHAIN.md').read_text(encoding='utf-8')
    source=chain.split('## 첨부자료 전체',1)[1].split('~~~~~markdown\n',1)[1].split('\n~~~~~',1)[0]+'\n'
    last=chain.split('<a id="turn-12"></a>',1)[1].split('## 첨부자료 전체',1)[0]
    final=last.split('응답 전체(편집 없음):',1)[1].split('~~~~~markdown\n',1)[1].split('\n~~~~~',1)[0]
    out=HERE/'verification.json'

def block(did):return source.split('BEGIN '+did,1)[1].split('END '+did,1)[0]
def table(text):
    result=[]
    for line in text.splitlines():
        if not line.startswith('|'):continue
        cells=[v.strip() for v in line.strip().strip('|').split('|')]
        if all(re.fullmatch('[-:]+',c) for c in cells):continue
        result.append(cells)
    return result

staff={r[0]:{'contract':int(r[1]),'booked':int(r[2]),'leave':int(r[3])} for r in table(block('DOC-HR-02')) if r[0].startswith('EMP-')}
skills={r[0]:r[3] for r in table(block('DOC-HR-01')) if r[0].startswith('EMP-')}
packages={r[0]:{'mandatory':r[3]=='필수','needs':{k:int(v) for k,v in re.findall(r'(BE|DATA|SRE|QA) (\d+)h',r[4])},'cash':int(r[5]),'value':int(r[6])} for r in table(block('DOC-PRJ-04')) if r[0] in list('ABCDEF')}
costrows=table(block('DOC-FIN-01'))
base=sum(int(r[1]) for r in costrows if r[0] in ['내부 급여','공통 도구·클라우드 기본료','기존 계약 운영·당직'])
cap=int(re.search(r'USD ([\d,]+)',block('DOC-FIN-02')).group(1).replace(',',''))
draft=int(re.search(r'USD ([\d,]+)',block('DOC-FIN-03')).group(1).replace(',',''))
budget_event=int(re.search(r'EVT-M02-2:.*?USD ([\d,]+)',source).group(1).replace(',',''))
extra_leave=int(re.search(r'EVT-M02-3:.*?휴가가 (\d+)h 추가',source).group(1))
pool=[f'EMP-{n:02}' for n in range(1,9)]
mandatory=[k for k,v in packages.items() if v['mandatory']]
optional=[k for k,v in packages.items() if not v['mandatory']]

def evaluate(ceiling,leave_delta):
    capacity={k:sum(staff[e]['contract']-staff[e]['booked']-staff[e]['leave']-leave_delta.get(e,0) for e in pool if skills[e]==k) for k in ['BE','DATA','SRE','QA']}
    combos=[]
    for bits in itertools.product([False,True],repeat=len(optional)):
        chosen=mandatory+[k for k,yes in zip(optional,bits) if yes]
        cash=base+sum(packages[k]['cash'] for k in chosen)
        used={s:sum(packages[k]['needs'].get(s,0) for k in chosen) for s in capacity}
        combos.append(dict(packages=''.join(chosen),cash_usd=cash,headroom_usd=ceiling-cash,value_points=sum(packages[k]['value'] for k in chosen),used_hours=used,feasible=cash<=ceiling and all(used[s]<=capacity[s] for s in capacity)))
    feasible=[r for r in combos if r['feasible']]
    best=max(r['value_points'] for r in feasible)
    return dict(ceiling_usd=ceiling,capacity_hours=capacity,feasible_count=len(feasible),optimal=[r for r in feasible if r['value_points']==best],all_combinations=combos)

states={'initial':evaluate(cap,{}),'budget_change':evaluate(budget_event,{}),'budget_and_leave':evaluate(budget_event,{'EMP-07':extra_leave})}
allocations={};used={}
employee_rows=[r for r in table(final.split('#### 직원별 시간과 배정',1)[1].split('#### 패키지·스킬 검산',1)[0]) if r[0].startswith('EMP-')]
assert len(employee_rows)==8
for r in employee_rows:
    eid,skill=r[:2];booked,leave,free,assigned,remainder=map(int,r[2:7]);expected=staff[eid]
    assert skill==skills[eid] and booked==expected['booked'] and leave==expected['leave']+(extra_leave if eid=='EMP-07' else 0)
    assert expected['contract']-booked-leave==free and free-assigned==remainder and remainder>=0
    parts=re.findall(r'([A-F]): (BE|DATA|SRE|QA) (\d+)h',r[7]);assert sum(int(h) for _,_,h in parts)==assigned
    for p,s,h in parts:
        assert s==skill
        used[p,s]=used.get((p,s),0)+int(h)
    allocations[eid]=dict(skill=skill,booked_h=booked,leave_h=leave,assigned_h=assigned,remaining_h=remainder)
for p in 'ABF':assert {s:h for (k,s),h in used.items() if k==p}==packages[p]['needs']
assert all(k in 'ABF' for k,s in used)
assert states['initial']['optimal'][0]['cash_usd']==27800
assert states['budget_change']['optimal'][0]['cash_usd']==27000
assert states['budget_and_leave']['optimal'][0]['cash_usd']==26300
def number(cell):return int(cell.replace(',','').replace('−','-').removesuffix('점'))
cash_table={r[0]:r for r in table(final.split('#### 비용·여유금 검산',1)[1].split('#### 비교 대안',1)[0])}
best=states['budget_and_leave']['optimal'][0]
assert number(cash_table['기준비용 소계'][2])==base
assert number(cash_table['제안 총액'][2])==best['cash_usd']
assert number(cash_table['제안 총액'][3])==best['value_points']
assert number(cash_table['현재 승인 상한'][2])==budget_event
assert number(cash_table['승인 상한 대비 차이'][2])==-best['headroom_usd']
assert number(cash_table['미사용 예산'][2])==best['headroom_usd']
assert number(cash_table['추가 증액 요청액'][2])==0
report=dict(source_normalized_sha256=hashlib.sha256(source.rstrip().encode()).hexdigest(),source_version='v1.0.0 / cc3f50cf9a9e288b237d558d76cac2d3cbc4eb4c',method='Parse the original DOC tables and event text; enumerate 16 optional subsets per state; parse and verify the actual final employee allocation and budget table.',baseline_usd=base,approved_initial_usd=cap,unsigned_forecast_usd=draft,states=states,final_employee_allocation=allocations,all_final_employee_and_package_checks_passed=True,final_budget_table_checks_passed=True,scope='Post-exam arithmetic audit, not evidence of calculations performed by the examinee during the exam. No rubric scores computed by this script.')
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'baseline_usd':base,'best':{k:v['optimal'][0]['packages'] for k,v in states.items()},'final_allocation':'PASS','output':str(out)},ensure_ascii=False))
