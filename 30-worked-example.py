"""Offline teaching calculation; no model or paper experiment rerun."""
import json
rows={'VANILLA':[20.6,12.],'ORACLE':[21.2,21.3],'LLaMA':[16.2,3.9],'Top1':[19.1,3.]}
result={'rouge_order':sorted(rows,key=lambda k:rows[k][0],reverse=True),'claim_order':sorted(rows,key=lambda k:rows[k][1],reverse=True),'oracle_minus_vanilla':[round(a-b,1) for a,b in zip(rows['ORACLE'],rows['VANILLA'])],'top1_minus_vanilla':[round(a-b,1) for a,b in zip(rows['Top1'],rows['VANILLA'])]}
assert result['rouge_order']!=result['claim_order']

print(json.dumps(result,ensure_ascii=False,indent=2))
