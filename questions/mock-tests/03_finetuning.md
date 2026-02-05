# 微调模拟题 (16% - 20题)

---

## 单选题 (1-15)

### 题目 1

LoRA 的全称是什么？

A. Low-Rank Adaptation  
B. Large Range Augmentation  
C. Layer Recursive Algorithm  
D. Learning Rate Adjustment

<details>
<summary>查看答案</summary>

**答案: A**

解析: LoRA = Low-Rank Adaptation，低秩适配，一种参数高效微调方法。

</details>

---

### 题目 2

以下哪个场景最适合使用模型微调？

A. 需要基于私有文档回答问题  
B. 需要模型以特定风格输出  
C. 需要实时更新知识  
D. 需要快速原型验证

<details>
<summary>查看答案</summary>

**答案: B**

解析: 微调适合改变模型行为/风格。私有文档用 RAG，实时知识用工具调用，原型验证用提示词。

</details>

---

### 题目 3

LoRA 微调相比全参数微调的优势是：

A. 可以学习更多知识  
B. 训练参数量少，资源需求低  
C. 推理速度更快  
D. 不需要训练数据

<details>
<summary>查看答案</summary>

**答案: B**

解析: LoRA 只训练低秩矩阵（约 0.1% 参数），大幅降低显存和计算需求。

</details>

---

### 题目 4

微调数据集的常见格式是：

A. CSV  
B. JSONL (instruction/input/output)  
C. XML  
D. SQL

<details>
<summary>查看答案</summary>

**答案: B**

解析: 指令微调通常使用 JSONL 格式，包含 instruction、input、output 字段。

</details>

---

### 题目 5

训练过程中发现验证集 loss 比训练集 loss 高很多，这说明：

A. 模型欠拟合  
B. 模型过拟合  
C. 学习率太低  
D. 数据质量好

<details>
<summary>查看答案</summary>

**答案: B**

解析: 训练 loss 低、验证 loss 高 = 过拟合，模型"记住"了训练数据而非学习规律。

</details>

---

### 题目 6

以下哪个参数控制训练的轮数？

A. learning_rate  
B. epochs  
C. batch_size  
D. temperature

<details>
<summary>查看答案</summary>

**答案: B**

解析: epochs 表示训练完整遍历数据集的次数。

</details>

---

### 题目 7

QLoRA 相比 LoRA 的主要改进是：

A. 使用更大的 rank  
B. 结合 4-bit 量化进一步降低显存  
C. 训练速度更快  
D. 效果更好

<details>
<summary>查看答案</summary>

**答案: B**

解析: QLoRA = LoRA + 4-bit 量化，在消费级 GPU 上也能微调大模型。

</details>

---

### 题目 8

关于微调数据质量，以下说法错误的是：

A. 数据越多效果越好  
B. 数据应该准确无误  
C. 数据应该覆盖多种场景  
D. 应该去除重复数据

<details>
<summary>查看答案</summary>

**答案: A**

解析: 数据质量比数量更重要。少量高质量数据可能比大量低质量数据效果好。

</details>

---

### 题目 9

LoRA 中的 r 参数表示：

A. 学习率  
B. 低秩矩阵的秩  
C. 训练轮数  
D. 批次大小

<details>
<summary>查看答案</summary>

**答案: B**

解析: r (rank) 是低秩分解的秩，常用 8/16/32。r 越大表达能力越强，但参数也越多。

</details>

---

### 题目 10

训练时 loss 震荡不稳定，最可能的原因是：

A. 学习率太高  
B. 学习率太低  
C. 数据量太大  
D. epochs 太少

<details>
<summary>查看答案</summary>

**答案: A**

解析: 学习率过高导致参数更新幅度大，loss 震荡。应降低学习率。

</details>

---

### 题目 11

微调后模型部署的常用方式不包括：

A. vLLM 高性能推理  
B. PAI-EAS 企业级服务  
C. 函数计算 FC  
D. 直接发送模型文件给用户

<details>
<summary>查看答案</summary>

**答案: D**

解析: 模型通过服务方式（API）提供，不会直接发送模型文件。vLLM、PAI、FC 都是部署方式。

</details>

---

### 题目 12

以下哪个不是微调的评测指标？

A. Loss  
B. BLEU  
C. Context Recall  
D. Accuracy

<details>
<summary>查看答案</summary>

**答案: C**

解析: Context Recall 是 RAGAS 的 RAG 评测指标，不用于微调评测。

</details>

---

### 题目 13

关于全参数微调 vs LoRA 微调，以下说法正确的是：

A. 全参数效果一定更好  
B. LoRA 不能用于对话任务  
C. LoRA 可以训练多个适配器切换使用  
D. 全参数微调资源需求更低

<details>
<summary>查看答案</summary>

**答案: C**

解析: LoRA 训练的适配器可以热插拔，一个基础模型可以配合多个 LoRA 适配器切换不同任务。

</details>

---

### 题目 14

微调数据集中，以下哪种数据应该排除？

A. 边界情况  
B. 多样化场景  
C. 低质量或错误的样本  
D. 不同长度的输入

<details>
<summary>查看答案</summary>

**答案: C**

解析: 低质量/错误数据会让模型学到错误模式，应该清洗排除。

</details>

---

### 题目 15

warmup_ratio 参数的作用是：

A. 控制模型预热时间  
B. 训练初期使用较小学习率逐步增大  
C. 设置 GPU 预热  
D. 控制数据加载速度

<details>
<summary>查看答案</summary>

**答案: B**

解析: warmup 让训练初期学习率从小逐渐增大到设定值，避免初期参数剧烈变化。

</details>

---

## 多选题 (16-20)

### 题目 16

以下哪些是 LoRA 微调的特点？（多选）

A. 参数量约为全参数的 0.1%  
B. 适配器可以热插拔  
C. 只能用于特定模型  
D. 降低显存需求

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: LoRA 参数少、可插拔、省显存，适用于大多数 Transformer 模型。

</details>

---

### 题目 17

以下哪些场景适合使用微调？（多选）

A. 需要特定的输出格式和风格  
B. 需要模型理解专业术语  
C. 知识需要频繁更新  
D. 需要稳定的结构化输出

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 风格、专业概念、稳定输出适合微调。频繁更新知识用 RAG 更合适。

</details>

---

### 题目 18

过拟合的解决方法包括？（多选）

A. 减少训练轮数 (epochs)  
B. 增加训练数据  
C. 增加正则化 (weight_decay)  
D. 降低学习率

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: 减少 epochs、增加数据、增加正则化都能缓解过拟合。降低学习率主要解决震荡问题。

</details>

---

### 题目 19

微调数据集应该具备哪些特点？（多选）

A. 准确性  
B. 多样性  
C. 一致性  
D. 数量越多越好

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: 准确、多样、一致是数据质量要求。数量不是越多越好，质量更重要。

</details>

---

### 题目 20

以下哪些是微调和 RAG 的正确对比？（多选）

A. 微调改变模型权重，RAG 不改变  
B. RAG 知识可更新，微调知识固化  
C. 微调成本低于 RAG  
D. RAG 可以溯源，微调不能

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 微调改权重、知识固化、不可溯源；RAG 不改权重、可更新、可溯源。RAG 成本通常更低。

</details>
