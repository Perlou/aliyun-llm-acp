# 应用开发模拟题 (16% - 20题)

---

## 单选题 (1-15)

### 题目 1

在 OpenAI 兼容 API 中，用于定义 AI 角色和行为的消息角色是：

A. user  
B. system  
C. assistant  
D. tool

<details>
<summary>查看答案</summary>

**答案: B**

解析: system 角色用于设定 AI 的角色定位和行为规范，贯穿整个对话。

</details>

---

### 题目 2

stream=True 参数的作用是：

A. 压缩响应数据  
B. 边生成边返回，实现流式输出  
C. 加快模型推理速度  
D. 缓存历史对话

<details>
<summary>查看答案</summary>

**答案: B**

解析: 流式输出让用户在生成过程中就能看到内容，提升体验，降低首字延迟。

</details>

---

### 题目 3

多轮对话中，正确的做法是：

A. 只发送最新一条用户消息  
B. 保存并发送完整的对话历史  
C. 每次重新设定 system prompt  
D. 删除 assistant 的历史回复

<details>
<summary>查看答案</summary>

**答案: B**

解析: 多轮对话需要保存 user 和 assistant 的历史消息，让模型理解上下文。

</details>

---

### 题目 4

以下哪个不是 LangChain 的核心组件？

A. Chain  
B. Memory  
C. Vector Database  
D. Prompt Template

<details>
<summary>查看答案</summary>

**答案: C**

解析: LangChain 核心组件包括 Chain、Memory、Agent、Prompt Template。向量数据库是外部工具集成。

</details>

---

### 题目 5

当对话历史过长时，正确的处理方式是：

A. 直接报错  
B. 截断旧对话或使用摘要  
C. 忽略 system prompt  
D. 增加模型参数

<details>
<summary>查看答案</summary>

**答案: B**

解析: 上下文超限时可以截断保留最近 N 轮，或将历史摘要为一条消息。

</details>

---

### 题目 6

流式输出时，每个 chunk 中的内容字段是：

A. content  
B. delta.content  
C. message.content  
D. text

<details>
<summary>查看答案</summary>

**答案: B**

解析: 流式返回的增量内容在 choices[0].delta.content 中。

</details>

---

### 题目 7

Dify 平台的主要特点是：

A. 需要深厚的编程基础  
B. 可视化低代码构建 AI 应用  
C. 只支持 GPT 模型  
D. 仅用于模型训练

<details>
<summary>查看答案</summary>

**答案: B**

解析: Dify 是低代码平台，通过可视化方式快速搭建 AI 应用，支持多种模型。

</details>

---

### 题目 8

LangChain 中 Memory 组件的作用是：

A. 存储模型权重  
B. 管理对话历史  
C. 缓存 API 响应  
D. 保存用户密码

<details>
<summary>查看答案</summary>

**答案: B**

解析: Memory 自动管理对话上下文，有 Buffer、Summary、Window 等多种实现。

</details>

---

### 题目 9

以下哪种场景适合使用批量生成而非流式生成？

A. 实时聊天机器人  
B. 后台批量处理任务  
C. 语音助手  
D. 客服对话

<details>
<summary>查看答案</summary>

**答案: B**

解析: 后台批量处理不需要即时反馈，批量生成更简单。实时交互场景用流式更好。

</details>

---

### 题目 10

关于 API base_url，使用阿里云百炼时应该设置为：

A. https://api.openai.com/v1  
B. https://dashscope.aliyuncs.com/compatible-mode/v1  
C. https://api.azure.com/v1  
D. https://localhost:8000

<details>
<summary>查看答案</summary>

**答案: B**

解析: 百炼提供 OpenAI 兼容 API，endpoint 是 dashscope.aliyuncs.com/compatible-mode/v1。

</details>

---

### 题目 11

ConversationBufferMemory 的特点是：

A. 只保留最近 N 轮对话  
B. 保存所有对话历史  
C. 将历史对话总结为摘要  
D. 按关键词过滤历史

<details>
<summary>查看答案</summary>

**答案: B**

解析: Buffer 保存全部历史，Window 保留最近 N 轮，Summary 做摘要。

</details>

---

### 题目 12

以下哪个是大模型应用开发中获取 API Key 的正确做法？

A. 直接硬编码在代码中  
B. 从环境变量读取  
C. 存储在前端 JavaScript 中  
D. 用户每次手动输入

<details>
<summary>查看答案</summary>

**答案: B**

解析: API Key 应存储在环境变量或密钥管理服务中，不应硬编码或暴露在前端。

</details>

---

### 题目 13

LangChain 中 Chain 的作用是：

A. 区块链技术  
B. 将 Prompt、Model 等组件串联  
C. 连接多个 API  
D. 加密传输数据

<details>
<summary>查看答案</summary>

**答案: B**

解析: Chain 将 Prompt Template、LLM 等组件串联，形成处理流程。

</details>

---

### 题目 14

max_tokens 参数影响的是：

A. 请求的最大数量  
B. 生成内容的最大长度  
C. 对话历史的长度  
D. API 密钥的有效期

<details>
<summary>查看答案</summary>

**答案: B**

解析: max_tokens 限制模型生成的最大 token 数，控制输出长度和成本。

</details>

---

### 题目 15

以下哪个不是选择流式输出的原因？

A. 降低首字延迟  
B. 提升用户体验  
C. 减少 API 调用成本  
D. 边生成边展示

<details>
<summary>查看答案</summary>

**答案: C**

解析: 流式输出不影响成本（token 数相同），主要优势是体验和首字延迟。

</details>

---

## 多选题 (16-20)

### 题目 16

多轮对话实现需要注意哪些要点？（多选）

A. 保存 user 和 assistant 消息  
B. 保留 system prompt  
C. 处理上下文长度超限  
D. 每轮对话使用新的 API Key

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: 多轮对话需要保存历史、保留 system、处理超限。API Key 不需要每轮更换。

</details>

---

### 题目 17

以下哪些是 LangChain 的 Memory 类型？（多选）

A. ConversationBufferMemory  
B. ConversationSummaryMemory  
C. ConversationWindowMemory  
D. ConversationDatabaseMemory

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: Buffer（全保存）、Summary（摘要）、Window（滑窗）是常用 Memory 类型。

</details>

---

### 题目 18

流式输出适用于哪些场景？（多选）

A. 实时聊天  
B. 语音助手（即时反馈）  
C. 后台数据处理  
D. 交互式问答

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 需要即时反馈的交互场景适合流式。后台处理不需要，批量更方便。

</details>

---

### 题目 19

以下哪些是 Dify 平台的功能？（多选）

A. 可视化应用搭建  
B. 知识库管理  
C. 模型训练  
D. 一键发布 API

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: Dify 支持可视化搭建、知识库、发布。模型训练需要专门的训练平台。

</details>

---

### 题目 20

上下文长度超限的处理策略包括？（多选）

A. 截断保留最近 N 轮  
B. 将历史对话总结为摘要  
C. 增大模型 max_tokens  
D. 按重要性筛选保留

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 截断、摘要、筛选都是处理超限的方法。max_tokens 控制输出长度，不控制输入。

</details>
