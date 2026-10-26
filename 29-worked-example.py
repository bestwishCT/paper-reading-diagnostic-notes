"""Offline teaching calculation; no model or paper experiment rerun."""
import json
rows={'ASQA':[[66.6,40.4,73.6,72.5],[75.8,28.4,58.1,58.]],'ELI5':[[57.2,12.,51.1,50.],[25.2,4.4,39.3,39.3]]}
result={k:[round(y-x,1) for x,y in zip(*v)] for k,v in rows.items()}
def comparable(a,b):return a['dataset']==b['dataset'] and a['metric']==b['metric']
result['cross_task_comparison_allowed']=comparable(dict(dataset='ASQA',metric='EM'),dict(dataset='ELI5',metric='Claim'))
assert not result['cross_task_comparison_allowed']

print(json.dumps(result,ensure_ascii=False,indent=2))
