"""Offline teaching calculation; no model or paper experiment rerun."""
import json
tp=1000.;p=.661;r=.756
fp=tp*(1/p-1);fn=tp*(1/r-1)
result=[dict(tp=tp,fp=fp,fn=fn,tn=tn,precision=tp/(tp+fp),recall=tp/(tp+fn),accuracy=(tp+tn)/(tp+fp+fn+tn),prevalence=(tp+fn)/(tp+fp+fn+tn)) for tn in [0.,10000.]]
assert result[0]['precision']==result[1]['precision'] and result[0]['prevalence']!=result[1]['prevalence']

print(json.dumps(result,ensure_ascii=False,indent=2))
