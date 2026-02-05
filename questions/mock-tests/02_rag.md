# RAG 检索增强生成模拟题 (24% - 30题)

---

## 单选题 (1-20)

### 题目 1

RAG 的全称是什么？

A. Real-time AI Generation  
B. Retrieval-Augmented Generation  
C. Recursive Attention Generator  
D. Random Access Gateway

<details>
<summary>查看答案</summary>

**答案: B**

解析: RAG = Retrieval-Augmented Generation，即检索增强生成。

</details>

---

### 题目 2

以下哪个不是 RAG 流程的核心步骤？

A. 文档解析 (Document Parsing)  
B. 模型微调 (Fine-tuning)  
C. 向量检索 (Retrieval)  
D. 文本切片 (Chunking)

<details>
<summary>查看答案</summary>

**答案: B**

解析: RAG 核心步骤：解析→切片→向量化→检索→生成。微调是独立的模型优化方法，不属于 RAG 流程。

</details>

---

### 题目 3

关于 chunk_size 参数，以下说法正确的是：

A. chunk_size 越大，检索精度越高  
B. chunk_size 越小，上下文越完整  
C. chunk_size 需要根据文档特点调整  
D. chunk_size 不影响检索效果

<details>
<summary>查看答案</summary>

**答案: C**

解析: chunk_size 需权衡：太大可能引入噪音，太小可能丢失上下文。应根据文档类型和任务调整。

</details>

---

### 题目 4

RAGAS 评测体系中，Faithfulness 指标衡量的是：

A. 检索结果与问题的相关性  
B. 答案是否基于检索到的内容  
C. 检索结果的召回率  
D. 答案的语法正确性

<details>
<summary>查看答案</summary>

**答案: B**

解析: Faithfulness（忠实度）评估答案是否忠实于检索到的上下文，防止模型编造信息。

</details>

---

### 题目 5

以下哪种场景最适合使用 RAG？

A. 需要改变模型的回答风格  
B. 需要基于企业私有文档回答问题  
C. 需要模型学习新的推理能力  
D. 需要处理多模态输入

<details>
<summary>查看答案</summary>

**答案: B**

解析: RAG 适合私有知识库问答，知识可更新、可溯源。改变风格用微调，推理能力需要训练。

</details>

---

### 题目 6

关于向量检索，以下说法正确的是：

A. 只能使用精确匹配  
B. 基于语义相似度进行检索  
C. 不需要预处理文档  
D. 检索速度比关键词检索慢

<details>
<summary>查看答案</summary>

**答案: B**

解析: 向量检索（稠密检索）基于语义相似度，可以理解同义词和语义关系，不限于精确匹配。

</details>

---

### 题目 7

什么是混合检索 (Hybrid Search)？

A. 同时使用多个模型  
B. 结合稀疏检索和稠密检索  
C. 在多个知识库中检索  
D. 使用多种语言检索

<details>
<summary>查看答案</summary>

**答案: B**

解析: 混合检索结合 BM25（稀疏）和向量检索（稠密），取两者优势：精确匹配 + 语义理解。

</details>

---

### 题目 8

chunk_overlap 参数的作用是：

A. 增加检索数量  
B. 保持切片边界的上下文连续性  
C. 加快切片速度  
D. 减少存储空间

<details>
<summary>查看答案</summary>

**答案: B**

解析: overlap 使相邻切片有重叠部分，避免重要信息在切片边界丢失。

</details>

---

### 题目 9

以下哪个是 RAG 相对于模型微调的优势？

A. 可以改变模型的核心能力  
B. 知识可以实时更新  
C. 不需要任何计算资源  
D. 输出更加稳定

<details>
<summary>查看答案</summary>

**答案: B**

解析: RAG 的知识在外部文档中，可随时更新，无需重新训练模型。微调后知识固化在模型权重中。

</details>

---

### 题目 10

RAGAS 的 Context Precision 衡量的是：

A. 生成答案的准确性  
B. 检索结果中相关内容的排序质量  
C. 模型的推理能力  
D. 用户问题的清晰度

<details>
<summary>查看答案</summary>

**答案: B**

解析: Context Precision 评估检索返回的文档中相关内容是否排在前面，反映检索的精确度。

</details>

---

### 题目 11

句子窗口检索 (Sentence Window Retrieval) 的原理是：

A. 只检索单个句子  
B. 检索时匹配句子，返回时包含上下文窗口  
C. 将所有句子合并后检索  
D. 按窗口大小滑动检索

<details>
<summary>查看答案</summary>

**答案: B**

解析: 句子窗口技术：用句子做嵌入检索（精确），返回时带上周围上下文（完整），兼顾精度和完整性。

</details>

---

### 题目 12

以下哪个不是影响 RAG 效果的因素？

A. 切片策略  
B. Embedding 模型质量  
C. 用户的网络速度  
D. 检索返回的文档数量

<details>
<summary>查看答案</summary>

**答案: C**

解析: 切片、嵌入模型、检索数量都影响效果。用户网络只影响延迟，不影响回答质量。

</details>

---

### 题目 13

什么是重排序 (Re-ranking)？

A. 重新排列文档的段落  
B. 对初步检索结果进行精细排序  
C. 重新索引所有文档  
D. 改变文档的存储顺序

<details>
<summary>查看答案</summary>

**答案: B**

解析: Re-ranking 对初检结果用更精细的模型重新打分排序，提高最终返回结果的相关性。

</details>

---

### 题目 14

RAG 系统中，Embedding 模型的作用是：

A. 生成最终回答  
B. 将文本转换为向量表示  
C. 解析 PDF 文档  
D. 对回答进行评分

<details>
<summary>查看答案</summary>

**答案: B**

解析: Embedding 模型将文本编码为向量（数值表示），实现语义相似度计算。

</details>

---

### 题目 15

similarity_top_k 参数的含义是：

A. 相似度阈值  
B. 返回最相似的 k 个文档  
C. 最多处理 k 个查询  
D. 使用 k 个模型进行检索

<details>
<summary>查看答案</summary>

**答案: B**

解析: similarity_top_k 指定检索返回相似度最高的 k 个文档片段。

</details>

---

### 题目 16

以下哪种切片策略最适合结构化文档（如技术手册）？

A. 固定字符数切片  
B. 按语义边界切片  
C. 随机切片  
D. 不进行切片

<details>
<summary>查看答案</summary>

**答案: B**

解析: 结构化文档应按语义边界（如章节、段落）切片，保持内容完整性。

</details>

---

### 题目 17

RAG 中的"幻觉"问题通常指：

A. 检索速度过慢  
B. 模型编造不在检索结果中的信息  
C. 文档解析失败  
D. 向量存储空间不足

<details>
<summary>查看答案</summary>

**答案: B**

解析: 即使有检索结果，模型仍可能编造信息。Faithfulness 指标就是用于检测这个问题。

</details>

---

### 题目 18

自动合并检索 (Auto-Merging Retrieval) 的优势是：

A. 自动删除重复文档  
B. 小块精确检索，返回时合并为大块保持完整性  
C. 自动合并多个知识库  
D. 自动压缩存储空间

<details>
<summary>查看答案</summary>

**答案: B**

解析: Auto-Merging 用小块做检索（精确），如果多个小块来自同一父块则合并返回（完整上下文）。

</details>

---

### 题目 19

BM25 属于哪种检索方法？

A. 稠密检索  
B. 稀疏检索  
C. 混合检索  
D. 图检索

<details>
<summary>查看答案</summary>

**答案: B**

解析: BM25 是基于词频的稀疏检索方法，依赖精确关键词匹配。向量检索是稠密检索。

</details>

---

### 题目 20

以下哪个是 RAG Answer Relevancy 指标衡量的内容？

A. 检索结果的数量  
B. 答案是否正确回答了用户的问题  
C. 检索的速度  
D. 文档的更新频率

<details>
<summary>查看答案</summary>

**答案: B**

解析: Answer Relevancy 评估生成的答案与用户问题的相关程度。

</details>

---

## 多选题 (21-30)

### 题目 21

RAG 的核心流程包括哪些步骤？（多选）

A. 文档解析  
B. 文本切片  
C. 模型微调  
D. 向量检索

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: RAG 流程：解析→切片→向量化→检索→生成。微调是独立技术，不属于 RAG。

</details>

---

### 题目 22

以下哪些因素会影响文本切片的效果？（多选）

A. chunk_size 大小  
B. chunk_overlap 重叠度  
C. 文档的语言  
D. 切片策略（按句子/段落/语义）

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 切片大小、重叠度、策略都直接影响效果。语言可能影响分词，但不是主要因素。

</details>

---

### 题目 23

RAGAS 评测框架包含哪些指标？（多选）

A. Faithfulness  
B. Answer Relevancy  
C. Context Precision  
D. Model Accuracy

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: RAGAS 四大指标：Faithfulness、Answer Relevancy、Context Precision、Context Recall。

</details>

---

### 题目 24

以下哪些是 RAG 相对于纯 LLM 的优势？（多选）

A. 知识可更新  
B. 回答可溯源  
C. 降低幻觉风险  
D. 完全消除错误

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: RAG 优势：知识可更新、可引用来源、基于检索减少幻觉。但不能完全消除错误。

</details>

---

### 题目 25

以下哪些技术可以优化 RAG 的检索效果？（多选）

A. 句子窗口检索  
B. 混合检索  
C. 重排序  
D. 增加 temperature

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: 句子窗口、混合检索、重排序都是检索优化技术。temperature 影响生成，与检索无关。

</details>

---

### 题目 26

选择 RAG 而不是微调的场景包括？（多选）

A. 知识需要频繁更新  
B. 需要引用信息来源  
C. 需要改变模型输出风格  
D. 成本预算有限

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 知识更新、溯源需求、成本考虑都适合 RAG。改变输出风格需要微调。

</details>

---

### 题目 27

以下哪些是常见的向量数据库？（多选）

A. Milvus  
B. MySQL  
C. Pinecone  
D. FAISS

<details>
<summary>查看答案</summary>

**答案: A, C, D**

解析: Milvus、Pinecone、FAISS 都是向量数据库/库。MySQL 是关系型数据库。

</details>

---

### 题目 28

以下哪些情况需要调整 chunk_size？（多选）

A. 检索结果不相关  
B. 回答缺少必要上下文  
C. 存储空间不足  
D. 检索到的内容有太多噪音

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 不相关可能需要调小；缺上下文需要调大；噪音多需要调小。存储空间是运维问题。

</details>

---

### 题目 29

混合检索结合了哪些检索方式的优势？（多选）

A. BM25  
B. 向量检索  
C. 图检索  
D. SQL 查询

<details>
<summary>查看答案</summary>

**答案: A, B**

解析: 混合检索 = BM25（稀疏，精确匹配）+ 向量检索（稠密，语义理解）。

</details>

---

### 题目 30

以下哪些是 RAG 系统的常见问题？（多选）

A. 检索不到相关文档  
B. 模型忽略检索结果自行编造  
C. 切片导致信息割裂  
D. 检索延迟过高

<details>
<summary>查看答案</summary>

**答案: A, B, C, D**

解析: 这些都是 RAG 常见问题：检索召回差、幻觉、切片不当、延迟高，需要相应优化。

</details>
