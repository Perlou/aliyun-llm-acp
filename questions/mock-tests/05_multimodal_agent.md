# 多模态与Agent模拟题 (12% - 20题)

---

## 单选题 (1-15)

### 题目 1

以下哪个是 Qwen-VL 模型的主要能力？

A. 语音识别  
B. 图像理解与视觉问答  
C. 代码生成  
D. 文本翻译

<details>
<summary>查看答案</summary>

**答案: B**

解析: Qwen-VL 是视觉语言模型，能理解图片内容、进行视觉问答、图像描述等。

</details>

---

### 题目 2

ReAct 循环的核心步骤是：

A. Read → Execute → Act → Check  
B. Thought → Action → Observation  
C. Request → Response → Retry  
D. Receive → Analyze → Complete

<details>
<summary>查看答案</summary>

**答案: B**

解析: ReAct = Reasoning + Acting，核心循环：Thought（思考）→ Action（行动）→ Observation（观察）。

</details>

---

### 题目 3

Function Calling 中，model 返回的工具调用信息在哪个字段？

A. content  
B. tool_calls  
C. function_result  
D. action

<details>
<summary>查看答案</summary>

**答案: B**

解析: 当模型决定调用工具时，response.choices[0].message.tool_calls 包含工具调用信息。

</details>

---

### 题目 4

执行完工具后，返回结果给模型时使用的 role 是：

A. user  
B. assistant  
C. tool  
D. function

<details>
<summary>查看答案</summary>

**答案: C**

解析: 工具执行结果以 role="tool" 的消息返回，还需包含 tool_call_id 关联对应的调用。

</details>

---

### 题目 5

百炼 Assistant API 中，Thread 的作用是：

A. 管理 API 密钥  
B. 存储对话历史  
C. 定义模型参数  
D. 配置工具列表

<details>
<summary>查看答案</summary>

**答案: B**

解析: Thread 代表一个对话线程，保存用户和 Assistant 之间的消息历史。

</details>

---

### 题目 6

关于 Assistant API 的 Run，以下说法正确的是：

A. Run 是同步执行的  
B. Run 需要轮询状态直到完成  
C. Run 不需要关联 Thread  
D. 一个 Run 可以无限执行

<details>
<summary>查看答案</summary>

**答案: B**

解析: Run 是异步的，创建后需要轮询 run.status 直到变为 "completed"。

</details>

---

### 题目 7

以下哪种 Multi-Agent 协作模式适合有依赖关系的任务？

A. 并行模式  
B. 串行模式  
C. 层级模式  
D. 随机模式

<details>
<summary>查看答案</summary>

**答案: B**

解析: 串行模式（A → B → C）适合有依赖的任务，前一步输出作为下一步输入。

</details>

---

### 题目 8

tool_choice 参数设置为 "auto" 表示：

A. 必须调用工具  
B. 禁止调用工具  
C. 模型自行决定是否调用工具  
D. 随机调用一个工具

<details>
<summary>查看答案</summary>

**答案: C**

解析: "auto" 让模型根据用户输入自行判断是否需要调用工具。

</details>

---

### 题目 9

以下哪个不是定义 Function 时的必要字段？

A. name  
B. description  
C. parameters  
D. return_type

<details>
<summary>查看答案</summary>

**答案: D**

解析: 工具定义需要 name、description、parameters。return_type 不是标准字段。

</details>

---

### 题目 10

Qwen-Audio 模型的主要能力是：

A. 图像生成  
B. 语音识别与音频理解  
C. 视频生成  
D. 文本摘要

<details>
<summary>查看答案</summary>

**答案: B**

解析: Qwen-Audio 处理音频内容，支持语音识别、语音理解等任务。

</details>

---

### 题目 11

Agent 相比传统 LLM 应用的主要优势是：

A. 更快的响应速度  
B. 更低的成本  
C. 能够使用工具与外部世界交互  
D. 更小的模型体积

<details>
<summary>查看答案</summary>

**答案: C**

解析: Agent 通过工具调用与外部系统交互（查数据库、调 API、执行代码等），扩展了 LLM 能力边界。

</details>

---

### 题目 12

以下哪种场景最适合使用层级 Multi-Agent？

A. 简单的顺序任务  
B. 完全独立的并行任务  
C. 需要协调调度的复杂任务  
D. 单一功能的重复任务

<details>
<summary>查看答案</summary>

**答案: C**

解析: 层级模式有 Manager 负责分发和协调，适合复杂的多角色任务（如智能客服的问题分发）。

</details>

---

### 题目 13

多模态输入时，消息中图片的正确格式是：

A. `{"image": "base64_data"}`  
B. `{"type": "image", "url": "..."}`  
C. `"直接粘贴图片"`  
D. `{"image_path": "/local/path"}`

<details>
<summary>查看答案</summary>

**答案: B**

解析: 多模态内容使用数组格式，包含 type 和对应的数据（url 或 base64）。

</details>

---

### 题目 14

Assistant API 中，工具调用失败时应该：

A. 直接结束对话  
B. 返回 tool 消息说明错误  
C. 重新创建 Assistant  
D. 清空 Thread

<details>
<summary>查看答案</summary>

**答案: B**

解析: 失败时仍需返回 tool 消息（包含错误信息），让 Assistant 知道并可能采取替代方案。

</details>

---

### 题目 15

以下哪个不是 Agent 的典型组成部分？

A. LLM（大语言模型）  
B. Tools（工具）  
C. Memory（记忆）  
D. Database（数据库）

<details>
<summary>查看答案</summary>

**答案: D**

解析: Agent 核心组件：LLM（决策）+ Tools（能力）+ Memory（上下文）+ Planning（规划）。数据库是外部资源。

</details>

---

## 多选题 (16-20)

### 题目 16

Function Calling 的完整流程包括？（多选）

A. 定义工具的 JSON Schema  
B. 调用模型时传入 tools 参数  
C. 解析并执行 tool_calls  
D. 以 role="tool" 返回结果

<details>
<summary>查看答案</summary>

**答案: A, B, C, D**

解析: 完整流程：定义 → 传给模型 → 解析执行 → 返回结果 → 模型生成最终回答。

</details>

---

### 题目 17

以下哪些是 Qwen 系列多模态模型？（多选）

A. Qwen-VL  
B. Qwen-Audio  
C. Qwen-Max  
D. Qwen-Code

<details>
<summary>查看答案</summary>

**答案: A, B**

解析: Qwen-VL（视觉）和 Qwen-Audio（音频）是多模态模型。Qwen-Max 是文本模型。

</details>

---

### 题目 18

Multi-Agent 的常见协作模式包括？（多选）

A. 串行模式  
B. 并行模式  
C. 层级模式  
D. 随机模式

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: 串行（顺序依赖）、并行（独立任务）、层级（集中调度）是三种典型模式。

</details>

---

### 题目 19

Assistant API 的核心组件包括？（多选）

A. Assistant  
B. Thread  
C. Run  
D. Database

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: Assistant（助手定义）、Thread（对话线程）、Run（执行实例）是三大核心组件。

</details>

---

### 题目 20

以下哪些是 Agent 应用的典型场景？（多选）

A. 自动化数据分析  
B. 智能客服（多系统集成）  
C. 纯文本翻译  
D. 代码生成与执行

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: Agent 适合需要工具调用、多步骤、外部交互的场景。纯翻译不需要 Agent。

</details>
