"""Offline teaching calculation; no model or paper experiment rerun."""
import json
def check(x):return x['passage_unit']=='words' and x['context_unit']=='tokens' and x['ELI5_corpus']=='Sphere' and x['eval_per_dataset']==1000
good=dict(passage_unit='words',context_unit='tokens',ELI5_corpus='Sphere',eval_per_dataset=1000)
bad=dict(good,passage_unit='tokens',ELI5_corpus='Wikipedia')
result={'valid_config':check(good),'wrong_unit_and_corpus':check(bad),'gold_metadata':good}
assert result['valid_config'] and not result['wrong_unit_and_corpus']

print(json.dumps(result,ensure_ascii=False,indent=2))
