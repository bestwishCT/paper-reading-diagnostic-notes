"""Offline teaching calculation; no model or paper experiment rerun."""
import json
from itertools import product
result=[dict(prompt=p,order=o,role='reported-combination' if (p,o)==('random-explicit','random') else ('baseline' if (p,o)==('original','relevance') else 'not-isolated-here'),accuracy=None) for p,o in product(['original','random-explicit'],['relevance','random'])]
assert sum(x['role']=='not-isolated-here' for x in result)==2

print(json.dumps(result,ensure_ascii=False,indent=2))
