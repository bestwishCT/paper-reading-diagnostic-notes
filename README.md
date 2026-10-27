# 检测无关引用的 precision，为什么不是 citation precision

## 论文问题

ALCE 附录 G.5 同时报告 citation recall/citation precision 的自动判断准确率，以及检测 `insufficient citations` 和 `irrelevant citations` 的 recall/precision。它们的评估对象和分母不同，不能把 66.1% 当成答案引用质量。

## 作者核查后的完整答案

1. **评估对象和分母**：85.1% 和 77.6% 是自动分类器相对人工标注的 accuracy；`insufficient` 的检测为 recall 82.3%、precision 84.2%，`irrelevant` 的检测为 recall 75.6%、precision 66.1%。检测 precision 的分母是“自动判为该正类的项目”，citation precision 的分母是“答案中使用的引用”，两者不是同一个事件。

2. **kappa 不能当 accuracy**：论文还报告 recall/precision 方向的 Cohen kappa 为 0.698/0.525。kappa 校正偶然一致性，不是 69.8%/52.5% 的准确率。

3. **partial support 的方向**：若引用只部分支持句子，NLI 判定可能把它误报为 irrelevant，属于 false positive；不能反写成“把无关引用判成支持”。人工规则可以在整个引用集合足以支持句子时不惩罚部分支持，但论文明确指出当前自动模型不能可靠判断这种情况，因此不能把人工规则说成已经实现的自动指标。

4. **基数不可逆推**：只知道 precision=0.661、recall=0.756，最多得到 FP/TP=1/0.661−1、FN/TP=1/0.756−1；TN 和总样本规模仍有自由度，因此不能唯一恢复混淆矩阵、样本量或所有引用中的无关比例。百分比还存在四舍五入误差。

## 可复算检查卡

设 TP=1000，按上式计算 FP、FN；分别令 TN=0 和 TN=10000。两组 precision、recall 相同，但 accuracy 与无关比例不同。这是教学推导，不是重新运行论文的 NLI 或评测实验。检查顺序是：先写正类，再写 TP/FP/FN 的自然语言事件，最后核对对象、分母和单位。

## 本次阅读记录

本篇使用一次新的 Bohrium `gpt-5-mini` 调用。模型原答保留在竞赛材料中；作者核查后的答案如上。调用输出通过严格的 JSON、题号和证据行范围校验，但机械通过不等于科学答案全部正确。设计者熟悉论文，Codex 参与非盲审计；没有把单次调用宣称为稳定提示增益，也没有声称重新运行论文实验。

论文值：85.1%、77.6%、82.3%、84.2%、75.6%、66.1%、0.698、0.525。作者推导：precision/recall 分母分析、FP 方向解释和欠定性算例。局限：没有原始类别计数、没有独立盲审、没有多 seed 评测，也没有测量部署成本。


## 可独立核验的原文证据

本页故意把评分所需的关键证据直接放在公开正文中，打开单个 README 不依赖材料包。ALCE 附录 G.5（物理页17，印刷页6481）原文要点如下：

- “We evaluate the accuracy of our automatic metrics by treating the human annotations as gold labels.”
- citation recall 的 accuracy 为 85.1%，citation precision 的 accuracy 为 77.6%。
- insufficient citations 的 recall/precision 为 82.3%/84.2%；irrelevant citations 的 recall/precision 为 75.6%/66.1%。
- 由于 NLI 模型不能检测 partial support，irrelevant 检测有相对较高的 false positive rate。

主文物理页8（印刷页6472）第110–116行给出人工 citation precision 协议：先要求句子的 citation recall=1，再要求该引用至少部分支持；物理页9（印刷页6473）第27–33行给出 Cohen’s kappa 0.698/0.525 以及同一组 accuracy。上述页码、表头和上下文来自材料中的编号文本；材料同时保存原始页面图、来源说明、模型原答和逐题核验记录。

## 未改写的模型原答摘录

模型按冻结问题输出 D1–D4 的 JSON，原始文件为 `53-run-output.json`。其中 D3 的核心原答是：设 TP=t，则 FN=t(1/0.756−1)，FP=t(1/0.661−1)；没有 TP、总样本或先验比例，混淆矩阵和所有引用中的 irrelevant 比例不唯一。D4 的核心原答是：人工把 partial support 视为可支持，而 NLI 可能把它判为不支持/irrelevant，因而产生 false positive，不能把自动标签当作无条件真值。

## 作者核验与可复算算例

作者逐题复核了事件方向、正类和分母，并保留原答中的计算。取 TP=1000 时，FN≈322.75、FP≈512.86；将 TP 按任意正整数倍缩放，recall 和 precision 不变，因此绝对样本量不由两项百分比确定。再令 TN=0 与 TN=10000，precision/recall 仍相同，但 accuracy 和无关比例不同，说明后两者也不可逆推。这个算例是教学推导，不是重新运行论文的 NLI 评测。

## 复做入口与材料对应

公开版本包含本页对应的任务、冻结来源、原始请求/响应、验证脚本、离线算例和许可证；材料包中的 `提交说明.md`、`submission.txt` 与本页同属 53 号作品。`53-replay.py` 只做离线 JSON/行号和算例复核，不声称重新运行论文实验。
