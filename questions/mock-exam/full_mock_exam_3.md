# 📝 阿里云大模型 ACP 全真模拟试卷（三）

> ⏱️ 考试时长：120 分钟
>
> 📊 题目总数：100 道 (单选 70 + 多选 30)
>
> ✅ 合格分数：80 分

---

## 📋 考试说明

- 每题 1 分，满分 100 分
- 单选题选错不得分
- 多选题少选得 0.5 分，多选或错选不得分
- 建议时间分配：单选 60 分钟，多选 50 分钟，检查 10 分钟

---

## 第一部分：单选题 (1-70)

### 1. 完整的提示词结构中，"约束 (Constraints)"的作用是：

A. 定义 AI 的身份  
B. 提供参考示例  
C. 设定限制条件和输出边界  
D. 指定要完成的目标

---

### 2. 在 RAG 系统中，Embedding 模型的输出是：

A. 文本摘要  
B. 分类标签  
C. 固定维度的数值向量  
D. 关键词列表

---

### 3. 关于 temperature=0 和 top_p=1 的组合，以下说法正确的是：

A. 输出完全随机  
B. 输出最具创意性  
C. 输出最确定（贪心解码）  
D. 两者相互矛盾无法组合

---

### 4. LoRA 中 r=16 相比 r=8 的影响是：

A. 训练速度更快  
B. 显存需求更小  
C. 适配器表达能力更强，但参数量增加  
D. 效果完全相同

---

### 5. Multi-Agent 中"Manager Agent"角色出现在哪种架构？

A. 串行模式  
B. 并行模式  
C. 层级模式  
D. 随机模式

---

### 6. 以下哪项是稀疏检索相比稠密检索的优势？

A. 语义理解能力更强  
B. 精确关键词匹配效果更好  
C. 不需要预处理  
D. 可处理多模态内容

---

### 7. RAM 服务在大模型应用中的典型用途是：

A. 数据加密  
B. API 访问的身份权限控制  
C. 操作日志记录  
D. 内容审核

---

### 8. XML 标签（如 `<context>...</context>`）在提示词中的作用是：

A. 增加输出 token  
B. 清晰区分不同内容区域，提升模型理解  
C. 加速推理  
D. 替代 API 参数

---

### 9. 混合检索公式中 `alpha * sparse_score + (1 - alpha) * dense_score`，alpha 通常取值：

A. 0  
B. 0.3 ~ 0.5  
C. 1.0  
D. 2.0

---

### 10. 使用 RAG 而非微调的核心理由是：

A. RAG 效果一定更好  
B. RAG 成本低且知识可实时更新  
C. RAG 不需要任何外部数据  
D. RAG 改变模型输出风格更容易

---

### 11. `ConversationChain` 在 LangChain 中自动集成了什么能力？

A. 工具调用  
B. 对话历史记忆  
C. 文档检索  
D. 模型微调

---

### 12. 模型在生成医学建议时给出不存在的药物名称，这最可能是：

A. 偏见歧视  
B. 提示注入  
C. 幻觉问题  
D. 有害内容

---

### 13. `SentenceSplitter` 中 separator 参数控制的是：

A. 向量维度  
B. 文本拆分时使用的分隔符  
C. 检索数量  
D. 模型选择

---

### 14. 以下哪个不属于 API messages 中的标准 role？

A. system  
B. user  
C. admin  
D. assistant

---

### 15. 工具定义中 "required" 字段的作用是：

A. 标记可选参数  
B. 指定调用工具时必须提供的参数  
C. 设置默认值  
D. 控制调用频率

---

### 16. FAISS 的全称中包含的核心功能是：

A. 文本生成  
B. 相似度搜索  
C. 模型训练  
D. 数据清洗

---

### 17. 微调数据中标注错误会导致：

A. 训练更快  
B. 模型学到错误模式，质量下降  
C. 显存需求降低  
D. 输出更多样

---

### 18. 百炼平台中 `app_id` 参数的作用是：

A. 指定模型版本  
B. 标识要调用的具体百炼应用  
C. 设置 API 密钥  
D. 控制输出格式

---

### 19. 自动合并检索中，当多个子块来自同一父块时，系统会：

A. 删除重复子块  
B. 返回父块以提供更完整的上下文  
C. 合并为新文档  
D. 忽略这些子块

---

### 20. `tool_choice="none"` 表示：

A. 强制调用工具  
B. 模型自行决定  
C. 禁止调用任何工具  
D. 调用所有工具

---

### 21. learning_rate 设置过小可能导致：

A. 训练不稳定，loss 震荡  
B. 收敛速度慢，可能欠拟合  
C. 过拟合  
D. 显存溢出

---

### 22. 流式输出中，每个 chunk 的增量内容通过以下路径获取：

A. `response.content`  
B. `chunk.choices[0].delta.content`  
C. `chunk.text`  
D. `chunk.message`

---

### 23. BLEU 指标最适合评估哪类任务？

A. 文本分类  
B. 翻译和文本生成  
C. 情感分析  
D. 命名实体识别

---

### 24. Assistant API 中 Run 的执行方式是：

A. 同步执行，立即返回  
B. 异步执行，需轮询状态  
C. 手动触发每一步  
D. 后台定时执行

---

### 25. 创意写作（如诗歌生成）建议使用的参数设置是：

A. temperature=0  
B. temperature=0.7~1.0  
C. top_p=0.1  
D. max_tokens=10

---

### 26. Answer Relevancy 指标的计算原理是：

A. 答案中事实陈述是否正确  
B. 生成反向问题与原始问题的平均相似度  
C. 检索覆盖度  
D. 答案长度

---

### 27. Qwen-Audio 的核心能力不包括：

A. 语音识别（转文字）  
B. 音频事件分析  
C. 图像分类  
D. 语音内容理解

---

### 28. 以下哪种方式不能有效防范提示注入？

A. 使用分隔符隔离用户输入  
B. 增大 max_tokens 值  
C. 关键词检测  
D. 在 system prompt 中声明忽略用户恶意指令

---

### 29. QLoRA 相比 LoRA 的核心改进在于：

A. 更大的秩 r  
B. 结合 4-bit 量化进一步降低显存需求  
C. 不需要基础模型  
D. 训练速度提升 10 倍

---

### 30. 处理长篇技术论文最适合的切片策略是：

A. 按句子切分  
B. 固定大小切分  
C. 按段落切分  
D. 按单词切分

---

### 31. 用户举报机制属于安全防护的哪一层？

A. 输入层  
B. 模型层  
C. 输出层  
D. 运营层

---

### 32. LangChain 中 `LLMChain` 的基本组成是：

A. LLM + Memory  
B. LLM + PromptTemplate  
C. LLM + VectorStore  
D. LLM + Agent

---

### 33. 使用 DashScope MultiModalConversation 的 content 字段是：

A. 纯文本字符串  
B. 包含 image/text 字典的列表  
C. Base64 编码字符串  
D. 二进制数据

---

### 34. 以下关于 epochs 的说法，正确的是：

A. epochs 越多，效果一定越好  
B. epochs 过多可能导致过拟合  
C. epochs 只影响推理速度  
D. epochs 越少，模型越稳定

---

### 35. 微调中对话格式数据的基本结构是：

A. `{"question": ..., "answer": ...}`  
B. `{"conversations": [{"role": ..., "content": ...}, ...]}`  
C. `{"input": ..., "label": ...}`  
D. `{"text": ...}`

---

### 36. 重排序 (Re-ranking) 通常将初步检索的多少结果精排为 Top 5？

A. Top 5  
B. Top 10  
C. Top 100  
D. 全部

---

### 37. 版权合规在大模型应用中的常见方案是：

A. 增加温度  
B. 来源标注  
C. 加密传输  
D. 频率限制

---

### 38. `Tongyi` 在 LangChain 中代表的是：

A. 向量数据库  
B. 通义系列大模型的 LLM 封装  
C. 提示模板  
D. 内存组件

---

### 39. 以下哪种方式最适合处理对话中 token 数量过多的问题？

A. 删除 system prompt  
B. 使用 ConversationSummaryMemory 压缩历史  
C. 增加 temperature  
D. 减小 max_tokens

---

### 40. 串行模式 Multi-Agent 最适合以下哪种工作流？

A. 多维度数据分析后汇总  
B. 研究员 → 作者 → 编辑  
C. 多个客服同时处理不同用户  
D. 随机分配任务

---

### 41. 以下哪个模型适合处理复杂图像推理任务？

A. Qwen-Max  
B. Qwen-Audio  
C. Qwen-VL-Max  
D. Qwen-Plus

---

### 42. chunk_size 设置过小可能导致：

A. 检索到的内容噪音更多  
B. 单个切片缺少足够的上下文信息  
C. 存储成本骤降  
D. 检索速度变慢

---

### 43. 数据收集阶段"明确告知用途"属于：

A. 最小必要原则  
B. 知情同意原则  
C. 加密保护原则  
D. 定期清理原则

---

### 44. 安全组规则在云安全中的作用是：

A. 密钥轮换  
B. 控制网络入站和出站流量规则  
C. 用户认证  
D. 数据备份

---

### 45. 以下关于 Context Precision 和 Context Recall 的说法正确的是：

A. 两者评估相同维度  
B. Precision 关注检索结果的排序质量，Recall 关注检索内容的完整性  
C. 两者都不使用 Ground Truth  
D. Recall 只评估答案质量

---

### 46. Function Calling 中，模型识别到需要调用工具后，实际执行工具的是：

A. 模型自身  
B. 开发者的应用代码  
C. API 网关  
D. 向量数据库

---

### 47. Perplexity 指标越低表示：

A. 模型越困惑  
B. 模型越差  
C. 模型对数据的预测越好  
D. 训练数据越少

---

### 48. 输入层安全防护不包括：

A. 敏感词过滤  
B. 提示注入检测  
C. 敏感信息脱敏  
D. 用户身份验证

---

### 49. 在 RAG 评测中，如果答案完全基于检索到的内容生成，则 Faithfulness 值为：

A. 0  
B. 0.5  
C. 1.0  
D. 不确定

---

### 50. ASR 在语音助手中的作用是：

A. 语音合成  
B. 语音识别（语音转文字）  
C. 自然语言理解  
D. 文本生成

---

### 51. Adapter 微调方法的参数量约为全参数的：

A. 0.1%  
B. 1%  
C. 3%  
D. 10%

---

### 52. LangChain 中 `ChatPromptTemplate` 和 `PromptTemplate` 的区别是：

A. 没有区别  
B. ChatPromptTemplate 支持多角色消息格式  
C. PromptTemplate 只能用于图像  
D. ChatPromptTemplate 不支持变量

---

### 53. 多模态 API 中，远程图片通过以下方式传入：

A. 上传二进制文件  
B. 提供图片 URL  
C. Base64 编码  
D. FTP 传输

---

### 54. 训练 loss 降低但验证 loss 开始上升，应该：

A. 继续训练更多 epochs  
B. 增大学习率  
C. 早停 (Early Stopping) 以防止过拟合  
D. 增大 batch size

---

### 55. LlamaIndex 中 `VectorStoreIndex.from_documents()` 的核心功能是：

A. 训练模型  
B. 将文档向量化并建立索引  
C. 解析 PDF  
D. 启动 Web 服务

---

### 56. 以下哪种做法违反了数据安全的"目的限制"原则？

A. 仅对经授权的数据进行分析  
B. 将用户对话数据未经同意用于模型训练  
C. 对敏感数据进行脱敏处理  
D. 定期清理过期数据

---

### 57. vLLM 的主要功能是：

A. 模型训练  
B. 大模型高效推理部署  
C. 数据标注  
D. 向量搜索

---

### 58. Prefix Tuning 与 LoRA 的区别是：

A. 两者原理完全相同  
B. Prefix Tuning 在输入前添加可学习向量，LoRA 通过低秩矩阵分解  
C. LoRA 参数量更大  
D. Prefix Tuning 不能用于 Transformer 模型

---

### 59. 欧氏距离在向量检索中衡量的是：

A. 两个向量方向的夹角  
B. 两个向量在空间中的直线距离  
C. 向量的维度数量  
D. 词频统计信息

---

### 60. 合规检测中"行业合规"的保障方案是：

A. 内容审核 API  
B. 数据脱敏  
C. 来源标注  
D. 专业审核

---

### 61. 以下哪个不是 Qwen 多模态模型家族的成员？

A. Qwen-VL  
B. Qwen-Audio  
C. Qwen-VL-Max  
D. Qwen-Code

---

### 62. HierarchicalNodeParser 中 `chunk_sizes=[512, 128]` 表示：

A. 两种独立的切分方式  
B. 父块大小 512 tokens，子块大小 128 tokens  
C. 总共切分为 512+128 个块  
D. 切片重叠为 512 到 128

---

### 63. Dify 平台最适合哪类用户？

A. 只需要命令行操作的专家  
B. 需要可视化低代码快速搭建 AI 应用的用户  
C. 纯做模型训练的研究员  
D. 只使用数据库的 DBA

---

### 64. Context Precision 的计算依据是：

A. Answer vs Question  
B. Context vs Question  
C. Answer vs Context  
D. Context vs Ground Truth

---

### 65. 以下哪个场景最能体现 Agent 相比 LLM 的优势？

A. 简单翻译  
B. 自动查询数据库、调用 API、生成报告  
C. 纯文本摘要  
D. 情感分析

---

### 66. 事实性检查 (Fact Checking) 属于安全防护的哪一层？

A. 输入层  
B. 模型层  
C. 输出层  
D. 运营层

---

### 67. 函数计算 (Function Compute) 适合部署哪类大模型服务？

A. 需要常驻 GPU 的大规模推理  
B. 轻量级、按需触发的推理服务  
C. 大规模模型训练  
D. 向量数据库管理

---

### 68. LoRA 中 `lora_dropout=0.1` 的作用是：

A. 控制秩的大小  
B. 在适配器层随机丢弃 10% 的神经元以防止过拟合  
C. 设置学习率为 0.1  
D. 控制输出长度

---

### 69. 操作日志和访问日志属于云安全的哪个方面？

A. 身份认证  
B. 网络安全  
C. 数据安全  
D. 审计追踪

---

### 70. 以下关于 Few-shot 和 Zero-shot 的对比，错误的是：

A. Few-shot 提供示例，Zero-shot 不提供  
B. Few-shot 适合需要特定格式输出的任务  
C. Zero-shot 效果一定比 Few-shot 好  
D. Zero-shot 更适合简单直接的任务

---

## 第二部分：多选题 (71-100)

### 71. System Prompt 的最佳实践包括：（多选）

A. 明确角色定位  
B. 定义回答规范和语气  
C. 包含用户对话历史  
D. 设定安全边界

---

### 72. RAG 系统架构的关键环节包括：（多选）

A. 文档库管理  
B. Query 向量化  
C. 相似度匹配  
D. LLM 生成

---

### 73. LoRA 的核心参数包括：（多选）

A. r (秩)  
B. lora_alpha (缩放因子)  
C. lora_dropout  
D. target_modules

---

### 74. 以下属于幻觉问题表现形式的有：（多选）

A. 事实错误  
B. 虚假引用  
C. 不一致回答  
D. 性别歧视

---

### 75. 影响 RAG 检索质量的因素包括：（多选）

A. chunk_size 大小  
B. Embedding 模型的质量  
C. 检索方式（稀疏/稠密/混合）  
D. 模型的 temperature 参数

---

### 76. API 消息中的标准 role 类型包括：（多选）

A. system  
B. user  
C. assistant  
D. tool

---

### 77. 以下属于 RAGAS 评测框架中使用的评估维度的有：（多选）

A. 答案与检索内容的一致性  
B. 答案与问题的相关性  
C. 检索结果的排序质量  
D. 模型推理速度

---

### 78. 稠密检索的实现需要：（多选）

A. Embedding 模型  
B. 向量数据库  
C. 相似度计算  
D. 关键词词典

---

### 79. 提示注入检测的常见方法包括：（多选）

A. 关键词模式匹配  
B. 使用分隔符隔离  
C. 增大 temperature  
D. 安全分类模型判断

---

### 80. Dify 平台的特点包括：（多选）

A. 可视化搭建工作流  
B. 内置 RAG 能力  
C. 支持多模型管理  
D. 必须编写大量代码

---

### 81. 微调训练参数调优建议中，正确的有：（多选）

A. 学习率过大导致 loss 震荡  
B. epochs 过多导致过拟合  
C. batch_size 越大训练越稳定  
D. warmup_ratio=0 是最优选择

---

### 82. 完整的 Function Calling 交互涉及的步骤包括：（多选）

A. 定义工具的 JSON Schema  
B. 模型判断并返回 tool_calls  
C. 开发者执行工具获取结果  
D. 以 role="tool" 将结果返回模型

---

### 83. Qwen-Audio 的能力包括：（多选）

A. 语音识别  
B. 语音内容理解  
C. 音频事件分析  
D. 视频生成

---

### 84. 以下关于 presence_penalty 和 frequency_penalty 的说法正确的有：（多选）

A. presence_penalty 惩罚已出现的 token  
B. frequency_penalty 根据出现频率进行惩罚  
C. 两者都可以增加输出多样性  
D. 两者取值范围为 -2 到 2

---

### 85. 微调数据集需要避免的问题包括：（多选）

A. 重复数据  
B. 标注错误  
C. 格式混乱  
D. 数据泄露

---

### 86. 云服务安全的核心要素包括：（多选）

A. 身份认证  
B. 网络安全  
C. 数据安全  
D. 审计追踪

---

### 87. ReAct 循环的完整步骤包括：（多选）

A. Thought（思考）  
B. Action（行动）  
C. Observation（观察）  
D. Prediction（预测）

---

### 88. 以下哪些是解决欠拟合的有效方法？（多选）

A. 增加训练数据  
B. 增加训练轮次 (epochs)  
C. 使用更大的模型  
D. 减少正则化

---

### 89. 批量生成 (Non-streaming) 的特点包括：（多选）

A. 一次性返回完整结果  
B. 用户需等待完整生成  
C. 适合后台批量处理  
D. 实时逐字返回

---

### 90. 数据存储阶段的安全要求包括：（多选）

A. 加密存储  
B. 访问控制  
C. 定期清理  
D. 公开共享

---

### 91. RAG 和微调可以结合使用的场景包括：（多选）

A. 微调改变输出风格 + RAG 补充知识  
B. 微调学习专业术语 + RAG 提供实时数据  
C. 用 RAG 完全替代微调  
D. 微调行业格式 + RAG 检索行业文档

---

### 92. 以下属于内容合规检测手段的有：（多选）

A. 内容安全 API  
B. 敏感词过滤  
C. 人工审核  
D. 增加训练数据

---

### 93. LoRA 适配器"热插拔"的含义是：（多选）

A. 可以在不重新训练基座模型的情况下使用  
B. 同一基座模型可加载不同任务的适配器  
C. 适配器参数与基座模型完全独立存储  
D. 必须修改基座模型的全部参数

---

### 94. 以下属于 LlamaIndex 提供的组件的有：（多选）

A. SentenceSplitter  
B. SentenceWindowNodeParser  
C. HierarchicalNodeParser  
D. VectorStoreIndex

---

### 95. 选择 Prompt Engineering 而非微调的场景包括：（多选）

A. 快速原型验证  
B. 需要灵活调整输出  
C. 需要学习全新领域概念  
D. 成本预算有限

---

### 96. 百炼 Assistant API 的工作流程包括：（多选）

A. 创建 Assistant  
B. 创建 Thread  
C. 发送 Message  
D. 创建 Run 执行

---

### 97. 模型层安全措施包括：（多选）

A. 安全对齐训练 (RLHF)  
B. 拒绝机制  
C. 内容边界设定  
D. 用户举报

---

### 98. 以下属于百炼平台微调流程步骤的有：（多选）

A. 上传 JSONL 数据集  
B. 选择基础模型  
C. 配置训练参数  
D. 手动实现反向传播

---

### 99. 常用的相似度/距离计算方法包括：（多选）

A. 余弦相似度  
B. 欧氏距离  
C. 内积  
D. 曼哈顿距离

---

### 100. 以下关于 RAG 评测的说法正确的有：（多选）

A. Faithfulness 评估答案与检索内容的一致性  
B. Answer Relevancy 评估答案是否回答了问题  
C. Context Recall 需要 Ground Truth 来计算  
D. 所有指标都不需要 Ground Truth

---

## 📝 答案速查

<details>
<summary>点击查看全部答案</summary>

**单选题答案 (1-70)**

```
1.C   2.C   3.C   4.C   5.C   6.B   7.B   8.B   9.B   10.B
11.B  12.C  13.B  14.C  15.B  16.B  17.B  18.B  19.B  20.C
21.B  22.B  23.B  24.B  25.B  26.B  27.C  28.B  29.B  30.C
31.D  32.B  33.B  34.B  35.B  36.C  37.B  38.B  39.B  40.B
41.C  42.B  43.B  44.B  45.B  46.B  47.C  48.C  49.C  50.B
51.C  52.B  53.B  54.C  55.B  56.B  57.B  58.B  59.B  60.D
61.D  62.B  63.B  64.B  65.B  66.C  67.B  68.B  69.D  70.C
```

**多选题答案 (71-100)**

```
71.ABD   72.ABCD  73.ABCD  74.ABC   75.ABC
76.ABCD  77.ABC   78.ABC   79.ABD   80.ABC
81.ABC   82.ABCD  83.ABC   84.ABCD  85.ABCD
86.ABCD  87.ABC   88.ABCD  89.ABC   90.ABC
91.ABD   92.ABC   93.ABC   94.ABCD  95.ABD
96.ABCD  97.ABC   98.ABC   99.ABCD  100.ABC
```

</details>

---

## 📊 自我评估

| 得分区间 | 评价     | 建议             |
| -------- | -------- | ---------------- |
| 90-100   | 优秀     | 可以考试了！     |
| 80-89    | 良好     | 再巩固薄弱点     |
| 70-79    | 中等     | 重点复习错题     |
| 60-69    | 及格边缘 | 需要系统复习     |
| <60      | 需要加强 | 回顾笔记重新学习 |

---

我的得分：**\_\_\_** 分

错题整理：

-
-
-
