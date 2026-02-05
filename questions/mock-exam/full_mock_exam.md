# 📝 阿里云大模型 ACP 全真模拟试卷

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

### 1. 关于大模型 temperature 参数，以下说法正确的是：

A. temperature 越高，输出越确定  
B. temperature=0 时输出随机  
C. temperature 越高，输出越有创意性  
D. temperature 不影响输出

---

### 2. RAG 的全称是：

A. Real-time AI Generation  
B. Retrieval-Augmented Generation  
C. Rapid Answer Generator  
D. Random Access Gateway

---

### 3. LoRA 微调的主要优势是：

A. 效果比全参数微调更好  
B. 训练参数量少，资源需求低  
C. 不需要任何训练数据  
D. 推理速度更快

---

### 4. 以下哪个不是 System Prompt 的组成部分？

A. 角色定义  
B. 用户历史对话  
C. 输出格式要求  
D. 行为约束

---

### 5. RAGAS 评测中 Faithfulness 衡量的是：

A. 检索速度  
B. 答案是否基于检索内容  
C. 模型大小  
D. 用户满意度

---

### 6. 流式输出 stream=True 的主要作用是：

A. 压缩数据  
B. 边生成边返回，降低首字延迟  
C. 加快推理速度  
D. 节省 token

---

### 7. Function Calling 中工具执行结果应使用哪个 role 返回？

A. user  
B. assistant  
C. tool  
D. system

---

### 8. 提示注入攻击的防护方法不包括：

A. 使用分隔符隔离用户输入  
B. 增加 temperature 值  
C. 关键词检测  
D. 声明忽略用户指令

---

### 9. chunk_overlap 参数的作用是：

A. 增加检索数量  
B. 保持切片边界的上下文连续性  
C. 加快切片速度  
D. 减少存储空间

---

### 10. ReAct 循环的核心步骤是：

A. Read → Execute → Act  
B. Thought → Action → Observation  
C. Request → Response → Retry  
D. Receive → Analyze → Complete

---

### 11. 以下哪个场景最适合使用 RAG？

A. 改变模型输出风格  
B. 基于企业私有文档问答  
C. 学习新的推理能力  
D. 处理多模态输入

---

### 12. 训练时 loss 震荡不稳定，最可能的原因是：

A. 学习率太高  
B. 学习率太低  
C. 数据量太大  
D. epochs 太少

---

### 13. 多轮对话的正确做法是：

A. 只发送最新消息  
B. 保存并发送完整对话历史  
C. 每次重新设定 system prompt  
D. 删除 assistant 回复

---

### 14. Qwen-VL 模型的主要能力是：

A. 语音识别  
B. 图像理解与视觉问答  
C. 代码生成  
D. 文本翻译

---

### 15. 大模型输出虚假引用属于：

A. 有害内容  
B. 隐私泄露  
C. 偏见歧视  
D. 幻觉问题

---

### 16. LangChain Memory 组件的作用是：

A. 存储模型权重  
B. 管理对话历史  
C. 缓存 API 响应  
D. 保存密码

---

### 17. 以下哪个是阿里云身份访问管理服务？

A. KMS  
B. RAM  
C. ActionTrail  
D. OSS

---

### 18. 微调数据集的常见格式是：

A. CSV  
B. JSONL  
C. XML  
D. SQL

---

### 19. similarity_top_k 参数的含义是：

A. 相似度阈值  
B. 返回最相似的 k 个文档  
C. 最多处理 k 个查询  
D. 使用 k 个模型

---

### 20. Assistant API 中 Run 的特点是：

A. 同步执行  
B. 需要轮询状态直到完成  
C. 不需要 Thread  
D. 立即返回结果

---

### 21. 什么是混合检索 (Hybrid Search)？

A. 多个模型并行  
B. 结合稀疏和稠密检索  
C. 多知识库检索  
D. 多语言检索

---

### 22. 对于意图分类任务，最合适的 temperature 是：

A. 0  
B. 0.7  
C. 1.0  
D. 1.5

---

### 23. 过拟合的表现是：

A. 训练 loss 高，验证 loss 低  
B. 训练 loss 低，验证 loss 高  
C. 两者都高  
D. 两者都低

---

### 24. 四层安全防护中，RLHF 属于：

A. 输入层  
B. 模型层  
C. 输出层  
D. 运营层

---

### 25. BM25 属于哪种检索方法？

A. 稠密检索  
B. 稀疏检索  
C. 混合检索  
D. 图检索

---

### 26. tool_choice="auto" 表示：

A. 必须调用工具  
B. 禁止调用工具  
C. 模型自行决定是否调用  
D. 随机调用

---

### 27. 以下哪个不是 LangChain 核心组件？

A. Chain  
B. Memory  
C. Vector Database  
D. Prompt Template

---

### 28. QLoRA 相比 LoRA 的改进是：

A. 更大的 rank  
B. 结合 4-bit 量化降低显存  
C. 训练更快  
D. 效果更好

---

### 29. 句子窗口检索的原理是：

A. 只检索句子  
B. 检索匹配句子，返回包含上下文窗口  
C. 合并所有句子  
D. 按窗口滑动

---

### 30. 以下哪个场景不适合提示词工程解决？

A. 文本分类  
B. 内容摘要  
C. 实时股票查询  
D. 代码解释

---

### 31. max_tokens 参数影响的是：

A. 请求数量  
B. 生成内容的最大长度  
C. 对话历史长度  
D. API 密钥有效期

---

### 32. 重排序 (Re-ranking) 的作用是：

A. 重新排列段落  
B. 对初步检索结果进行精细排序  
C. 重新索引文档  
D. 改变存储顺序

---

### 33. 层级 Multi-Agent 适合的场景是：

A. 简单顺序任务  
B. 独立并行任务  
C. 需要协调调度的复杂任务  
D. 单一功能重复

---

### 34. 数据收集阶段的合规要求是：

A. 加密存储  
B. 获得用户同意  
C. 定期清理  
D. 安全传输

---

### 35. Few-shot Prompting 适用于：

A. 学习全新知识  
B. 按特定格式输出  
C. 处理超长文档  
D. 实时数据查询

---

### 36. Embedding 模型的作用是：

A. 生成回答  
B. 将文本转换为向量  
C. 解析 PDF  
D. 评分回答

---

### 37. ConversationBufferMemory 的特点是：

A. 只保留最近 N 轮  
B. 保存所有对话历史  
C. 历史摘要  
D. 关键词过滤

---

### 38. LoRA 中 r 参数表示：

A. 学习率  
B. 低秩矩阵的秩  
C. 训练轮数  
D. 批次大小

---

### 39. 以下哪个不是 Agent 的组成部分？

A. LLM  
B. Tools  
C. Memory  
D. Database

---

### 40. presence_penalty 参数的作用是：

A. 惩罚已出现的 token，增加多样性  
B. 惩罚频繁 token  
C. 控制长度  
D. 控制温度

---

### 41. 阿里云百炼 API 的 base_url 是：

A. api.openai.com  
B. dashscope.aliyuncs.com/compatible-mode/v1  
C. api.azure.com  
D. localhost:8000

---

### 42. ActionTrail 服务的功能是：

A. 模型部署  
B. 操作审计  
C. 数据加密  
D. 负载均衡

---

### 43. warmup_ratio 的作用是：

A. GPU 预热  
B. 训练初期学习率逐步增大  
C. 数据加载  
D. 模型预热

---

### 44. 以下哪个是 RAG 的优势？

A. 改变核心能力  
B. 知识可实时更新  
C. 不需要计算资源  
D. 输出更稳定

---

### 45. Thread 在 Assistant API 中的作用是：

A. 管理 API 密钥  
B. 存储对话历史  
C. 定义模型参数  
D. 配置工具列表

---

### 46. top_p 参数控制的是：

A. 只选最高概率 token  
B. 从累积概率达到 p 的集合中采样  
C. 输出最大长度  
D. 采样温度

---

### 47. 模型输出性别歧视内容属于：

A. 有害内容  
B. 隐私泄露  
C. 偏见歧视  
D. 幻觉

---

### 48. Dify 平台的特点是：

A. 需要深厚编程基础  
B. 可视化低代码构建  
C. 只支持 GPT  
D. 仅用于训练

---

### 49. 自动合并检索的优势是：

A. 删除重复  
B. 小块检索，返回时合并为大块  
C. 合并知识库  
D. 压缩存储

---

### 50. 思维链 (CoT) 提示的作用是：

A. 串联多个模型  
B. 引导模型分步骤推理  
C. 使用多个模板  
D. 分段发送提示词

---

### 51. 以下哪个不是 RAGAS 指标？

A. Faithfulness  
B. Answer Relevancy  
C. Model Accuracy  
D. Context Precision

---

### 52. API Key 的正确存储方式是：

A. 硬编码  
B. 环境变量  
C. 前端 JavaScript  
D. 用户输入

---

### 53. epochs 参数控制的是：

A. 学习率  
B. 训练遍历数据集的次数  
C. 批次大小  
D. 温度

---

### 54. 流式输出时增量内容在：

A. content  
B. delta.content  
C. message.content  
D. text

---

### 55. 以下哪个是稠密检索的特点？

A. 精确关键词匹配  
B. 基于语义相似度  
C. 不需要预处理  
D. 速度更慢

---

### 56. Qwen-Audio 的主要能力是：

A. 图像生成  
B. 语音识别与音频理解  
C. 视频生成  
D. 文本摘要

---

### 57. 输出层安全措施是：

A. 频率限制  
B. 用户验证  
C. 敏感内容审核  
D. RLHF

---

### 58. 不是防止提示注入有效方法的是：

A. 分隔符  
B. 增加 temperature  
C. 关键词检测  
D. 声明忽略指令

---

### 59. 上下文超限的处理策略是：

A. 直接报错  
B. 截断或摘要  
C. 忽略 system  
D. 增加参数

---

### 60. Zero-shot 的特点是：

A. 需要多个示例  
B. 不需要示例  
C. 需要微调  
D. 只能简单任务

---

### 61. 微调适合的场景是：

A. 知识频繁更新  
B. 需要特定输出风格  
C. 快速原型验证  
D. 基于文档问答

---

### 62. Answer Relevancy 衡量的是：

A. 检索数量  
B. 答案是否正确回答问题  
C. 检索速度  
D. 更新频率

---

### 63. 以下哪个不是常见向量数据库？

A. Milvus  
B. MySQL  
C. Pinecone  
D. FAISS

---

### 64. 提示词模板的优势是：

A. 减少 API 调用  
B. 提高复用性和一致性  
C. 降低成本  
D. 加快响应

---

### 65. Agent 相比 LLM 的优势是：

A. 更快响应  
B. 更低成本  
C. 能使用工具与外部交互  
D. 更小体积

---

### 66. 批量生成（非流式）适合：

A. 实时聊天  
B. 后台批量处理  
C. 语音助手  
D. 客服对话

---

### 67. Chain 在 LangChain 中的作用是：

A. 区块链  
B. 串联 Prompt、Model 等组件  
C. 连接 API  
D. 加密传输

---

### 68. 微调后部署的方式不包括：

A. vLLM  
B. PAI-EAS  
C. 函数计算  
D. 直接发送模型文件

---

### 69. 数据合规核心原则不包括：

A. 最小必要  
B. 用户同意  
C. 数据越多越好  
D. 加密保护

---

### 70. 串行 Multi-Agent 适合的场景是：

A. 完全独立任务  
B. 有依赖关系的任务  
C. 需要速度最快  
D. 随机任务

---

## 第二部分：多选题 (71-100)

### 71. System Prompt 的常见组成部分包括：（多选）

A. 角色定义  
B. 输出格式要求  
C. 用户个人信息  
D. 行为约束

---

### 72. RAG 核心流程包括：（多选）

A. 文档解析  
B. 文本切片  
C. 模型微调  
D. 向量检索

---

### 73. LoRA 微调的特点包括：（多选）

A. 参数量约为全参数的 0.1%  
B. 适配器可热插拔  
C. 只能用于特定模型  
D. 降低显存需求

---

### 74. 防止提示注入的方法包括：（多选）

A. 分隔符隔离用户输入  
B. 声明忽略用户指令  
C. 关键词检测  
D. 增加 max_tokens

---

### 75. RAGAS 评测指标包括：（多选）

A. Faithfulness  
B. Answer Relevancy  
C. Context Precision  
D. Model Accuracy

---

### 76. 多轮对话需要注意：（多选）

A. 保存 user 和 assistant 消息  
B. 保留 system prompt  
C. 处理上下文超限  
D. 每轮更换 API Key

---

### 77. Function Calling 流程包括：（多选）

A. 定义工具 JSON Schema  
B. 调用时传入 tools 参数  
C. 解析执行 tool_calls  
D. 以 role="tool" 返回结果

---

### 78. 大模型安全风险包括：（多选）

A. 有害内容  
B. 隐私泄露  
C. 偏见歧视  
D. 模型下载慢

---

### 79. 检索优化技术包括：（多选）

A. 句子窗口检索  
B. 混合检索  
C. 重排序  
D. 增加 temperature

---

### 80. LangChain Memory 类型包括：（多选）

A. ConversationBufferMemory  
B. ConversationSummaryMemory  
C. ConversationWindowMemory  
D. ConversationDatabaseMemory

---

### 81. 过拟合解决方法包括：（多选）

A. 减少 epochs  
B. 增加训练数据  
C. 增加正则化  
D. 降低学习率

---

### 82. Multi-Agent 协作模式包括：（多选）

A. 串行模式  
B. 并行模式  
C. 层级模式  
D. 随机模式

---

### 83. 流式输出适用场景包括：（多选）

A. 实时聊天  
B. 语音助手  
C. 后台处理  
D. 交互式问答

---

### 84. 四层安全防护包括：（多选）

A. 输入层  
B. 模型层  
C. 输出层  
D. 运营层

---

### 85. 选择 RAG 而非微调的场景：（多选）

A. 知识频繁更新  
B. 需要引用来源  
C. 需要改变风格  
D. 成本预算有限

---

### 86. 微调数据集应具备：（多选）

A. 准确性  
B. 多样性  
C. 一致性  
D. 数量越多越好

---

### 87. Qwen 多模态模型包括：（多选）

A. Qwen-VL  
B. Qwen-Audio  
C. Qwen-Max  
D. Qwen-Code

---

### 88. RAG 相对纯 LLM 的优势：（多选）

A. 知识可更新  
B. 回答可溯源  
C. 降低幻觉  
D. 完全消除错误

---

### 89. 阿里云安全服务包括：（多选）

A. RAM  
B. KMS  
C. ActionTrail  
D. 内容安全

---

### 90. 思维链 (CoT) 的特点包括：（多选）

A. 引导展示推理过程  
B. 适合复杂推理  
C. 增加输出 token  
D. 只能用于数学

---

### 91. 影响切片效果的因素：（多选）

A. chunk_size  
B. chunk_overlap  
C. 文档语言  
D. 切片策略

---

### 92. Assistant API 核心组件：（多选）

A. Assistant  
B. Thread  
C. Run  
D. Database

---

### 93. temperature 和 top_p 的特点：（多选）

A. 都影响输出随机性  
B. temperature=0 时最确定  
C. 建议同时调整  
D. 创意写作可用较高值

---

### 94. 提示注入形式包括：（多选）

A. 直接要求忽略指令  
B. 角色扮演绕过  
C. Base64 编码  
D. 正常提问

---

### 95. Dify 平台功能包括：（多选）

A. 可视化搭建  
B. 知识库管理  
C. 模型训练  
D. 一键发布 API

---

### 96. 需要调整 chunk_size 的情况：（多选）

A. 检索结果不相关  
B. 回答缺少上下文  
C. 存储不足  
D. 检索内容噪音多

---

### 97. 微调和 RAG 的对比（正确的是）：（多选）

A. 微调改变权重，RAG 不改变  
B. RAG 知识可更新  
C. 微调成本低于 RAG  
D. RAG 可溯源

---

### 98. Agent 典型应用场景：（多选）

A. 自动化数据分析  
B. 多系统集成客服  
C. 纯文本翻译  
D. 代码生成与执行

---

### 99. 数据合规核心原则：（多选）

A. 最小必要  
B. 用户同意  
C. 加密保护  
D. 尽可能多收集

---

### 100. Few-shot 适用场景：（多选）

A. 需要特定输出格式  
B. 模型理解不准确  
C. 学习全新知识  
D. 保持输出风格一致

---

## 📝 答案速查

<details>
<summary>点击查看全部答案</summary>

**单选题答案 (1-70)**

```
1.C   2.B   3.B   4.B   5.B   6.B   7.C   8.B   9.B   10.B
11.B  12.A  13.B  14.B  15.D  16.B  17.B  18.B  19.B  20.B
21.B  22.A  23.B  24.B  25.B  26.C  27.C  28.B  29.B  30.C
31.B  32.B  33.C  34.B  35.B  36.B  37.B  38.B  39.D  40.A
41.B  42.B  43.B  44.B  45.B  46.B  47.C  48.B  49.B  50.B
51.C  52.B  53.B  54.B  55.B  56.B  57.C  58.B  59.B  60.B
61.B  62.B  63.B  64.B  65.C  66.B  67.B  68.D  69.C  70.B
```

**多选题答案 (71-100)**

```
71.ABD   72.ABD   73.ABD   74.ABC   75.ABC
76.ABC   77.ABCD  78.ABC   79.ABC   80.ABC
81.ABC   82.ABC   83.ABD   84.ABCD  85.ABD
86.ABC   87.AB    88.ABC   89.ABCD  90.ABC
91.ABD   92.ABC   93.ABD   94.ABC   95.ABD
96.ABD   97.ABD   98.ABD   99.ABC   100.ABD
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
