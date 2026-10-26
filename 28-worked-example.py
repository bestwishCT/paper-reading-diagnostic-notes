"""Offline teaching calculation; no model or paper experiment rerun."""
import json
from itertools import product
result=[dict(answer_correct=c,has_citation=h,source_entails=e,citation_recall=int(h and e)) for c,h,e in product([False,True],repeat=3)]
assert any(x['answer_correct'] and not x['citation_recall'] for x in result)

print(json.dumps(result,ensure_ascii=False,indent=2))
