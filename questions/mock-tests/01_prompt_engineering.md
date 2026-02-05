# 提示词工程模拟题 (24% - 30题)

---

## 单选题 (1-20)

### 题目 1

关于大模型的 temperature 参数，以下说法正确的是：

A. temperature 越高，输出越确定  
B. temperature=0 时，每次输出完全随机  
C. temperature 越高，输出越具有创意和多样性  
D. temperature 参数对输出结果没有影响

<details>
<summary>查看答案</summary>

**答案: C**

解析: temperature 控制输出的随机性。temperature=0 时输出确定性最高；temperature 越高，输出越随机、越有创意。

</details>

---

### 题目 2

以下哪个不是 System Prompt 的典型组成部分？

A. 角色定义  
B. 任务描述  
C. 用户的历史对话  
D. 输出格式要求

<details>
<summary>查看答案</summary>

**答案: C**

解析: System Prompt 通常包含角色定义、任务描述、输出格式、约束条件。用户历史对话属于 messages 中的 user/assistant 消息，不是 System Prompt 的组成部分。

</details>

---

### 题目 3

在设计提示词时，使用分隔符（如 ###、\"\"\"）的主要目的是：

A. 让输出更美观  
B. 增加 token 消耗  
C. 区分不同内容部分，防止提示注入  
D. 加快模型响应速度

<details>
<summary>查看答案</summary>

**答案: C**

解析: 分隔符用于清晰区分指令和用户输入，是防止提示注入攻击的基本手段。

</details>

---

### 题目 4

对于意图分类任务，以下 temperature 设置最合适的是：

A. temperature = 0  
B. temperature = 0.7  
C. temperature = 1.0  
D. temperature = 1.5

<details>
<summary>查看答案</summary>

**答案: A**

解析: 分类任务需要确定性输出，应使用 temperature=0 以获得一致的结果。

</details>

---

### 题目 5

以下哪种场景最适合使用 Few-shot Prompting？

A. 需要模型学习全新的知识  
B. 需要模型按照特定格式输出  
C. 需要处理超长文档  
D. 需要实时数据查询

<details>
<summary>查看答案</summary>

**答案: B**

解析: Few-shot 通过提供示例来指导模型输出格式和风格，非常适合需要特定格式输出的场景。

</details>

---

### 题目 6

什么是提示注入攻击（Prompt Injection）？

A. 通过大量请求使系统瘫痪  
B. 用户输入恶意指令试图覆盖系统提示词  
C. 窃取模型的训练数据  
D. 通过 API 获取未授权的功能

<details>
<summary>查看答案</summary>

**答案: B**

解析: 提示注入是指用户在输入中嵌入恶意指令，试图让模型忽略原有的系统提示词，执行攻击者的指令。

</details>

---

### 题目 7

以下哪个不是防止提示注入的有效方法？

A. 使用分隔符隔离用户输入  
B. 增加 temperature 值  
C. 在提示词中声明忽略用户输入中的指令  
D. 对用户输入进行关键词检测

<details>
<summary>查看答案</summary>

**答案: B**

解析: 增加 temperature 只影响输出随机性，对防止注入无效。分隔符、声明、检测都是有效的防护手段。

</details>

---

### 题目 8

关于 top_p 参数，以下说法正确的是：

A. top_p 和 temperature 作用完全相同  
B. top_p=1 时只选择概率最高的 token  
C. top_p 控制从累积概率达到 p 的 token 集合中采样  
D. top_p 值越小，输出越随机

<details>
<summary>查看答案</summary>

**答案: C**

解析: top_p (nucleus sampling) 从累积概率达到 p 的最小 token 集合中采样。top_p=1 包含所有 token，top_p 越小输出越确定。

</details>

---

### 题目 9

在多轮对话中，以下哪个角色用于存储 AI 的历史回复？

A. system  
B. user  
C. assistant  
D. tool

<details>
<summary>查看答案</summary>

**答案: C**

解析: assistant 角色用于记录 AI 的回复，在多轮对话中保存历史回答作为上下文。

</details>

---

### 题目 10

什么是思维链（Chain of Thought, CoT）提示？

A. 将多个模型串联使用  
B. 引导模型分步骤进行推理  
C. 使用多个提示词模板  
D. 将长提示词分段发送

<details>
<summary>查看答案</summary>

**答案: B**

解析: CoT 通过"让我们一步步思考"等引导语，让模型展示推理过程，提高复杂问题的解决能力。

</details>

---

### 题目 11

以下哪个是 Zero-shot Prompting 的特点？

A. 需要提供多个示例  
B. 不需要提供任何示例  
C. 需要对模型进行微调  
D. 只能处理简单任务

<details>
<summary>查看答案</summary>

**答案: B**

解析: Zero-shot 不提供示例，直接描述任务让模型完成。Few-shot 才需要提供示例。

</details>

---

### 题目 12

关于 max_tokens 参数，以下说法错误的是：

A. 控制生成的最大 token 数量  
B. 超过限制后会截断输出  
C. 设置越大生成质量越高  
D. 影响 API 调用成本

<details>
<summary>查看答案</summary>

**答案: C**

解析: max_tokens 控制输出长度上限，与质量无关。适当设置可以控制成本和响应时间。

</details>

---

### 题目 13

设计客服机器人的 System Prompt 时，以下哪项最重要？

A. 使用最新的网络流行语  
B. 明确角色定位和行为边界  
C. 尽可能长的提示词  
D. 包含所有可能的回答模板

<details>
<summary>查看答案</summary>

**答案: B**

解析: 客服机器人需要明确的角色定位（专业客服）和行为边界（什么能做什么不能做），这是核心设计要点。

</details>

---

### 题目 14

以下哪种场景不适合使用大模型提示词工程解决？

A. 文本分类  
B. 内容摘要  
C. 实时股票价格查询  
D. 代码解释

<details>
<summary>查看答案</summary>

**答案: C**

解析: 大模型不能获取实时数据，实时股票价格需要通过 API 或工具调用获取，单纯的提示词工程无法解决。

</details>

---

### 题目 15

关于提示词中的角色扮演，以下说法正确的是：

A. 角色扮演会降低模型性能  
B. 角色扮演可以帮助模型更好地理解任务上下文  
C. 角色扮演只适用于对话场景  
D. 角色扮演必须使用第一人称

<details>
<summary>查看答案</summary>

**答案: B**

解析: 角色扮演（如"你是一个专业的法律顾问"）帮助模型理解应该以什么专业背景和风格回答问题。

</details>

---

### 题目 16

在提示词工程中，"分步骤说明"的主要作用是：

A. 减少 token 消耗  
B. 让模型更容易理解复杂任务  
C. 加快生成速度  
D. 防止模型输出错误

<details>
<summary>查看答案</summary>

**答案: B**

解析: 将复杂任务分解为步骤可以帮助模型更好地理解和执行，提高输出质量。

</details>

---

### 题目 17

以下哪个不是提示词优化的常用技巧？

A. 使用清晰具体的指令  
B. 提供输出格式示例  
C. 增加无关的背景信息  
D. 设定任务边界和约束

<details>
<summary>查看答案</summary>

**答案: C**

解析: 无关的背景信息会增加噪音，降低模型理解准确性。提示词应该简洁且相关。

</details>

---

### 题目 18

关于 presence_penalty 参数，以下说法正确的是：

A. 惩罚已经出现过的 token，增加主题多样性  
B. 惩罚频繁出现的 token  
C. 控制输出的最大长度  
D. 控制采样的温度

<details>
<summary>查看答案</summary>

**答案: A**

解析: presence_penalty 对已出现的 token 施加惩罚，鼓励模型讨论新主题。frequency_penalty 才是惩罚频繁出现的 token。

</details>

---

### 题目 19

什么是"提示词模板"的主要优势？

A. 减少 API 调用次数  
B. 提高代码复用性和一致性  
C. 降低模型成本  
D. 加快模型响应

<details>
<summary>查看答案</summary>

**答案: B**

解析: 模板化的提示词可以复用，确保同类任务使用一致的格式，便于维护和优化。

</details>

---

### 题目 20

以下哪种提示词结构最清晰？

A. 请帮我写一篇关于AI的文章  
B. 你是科技记者，请撰写一篇800字的AI发展趋势文章，包含引言、3个要点和结论  
C. 写文章AI  
D. 请用华丽的词藻写AI

<details>
<summary>查看答案</summary>

**答案: B**

解析: B 包含了角色、任务、长度、结构要求，是最完整清晰的提示词。

</details>

---

## 多选题 (21-30)

### 题目 21

以下哪些是 System Prompt 的常见组成部分？（多选）

A. 角色定义  
B. 输出格式要求  
C. 用户的个人信息  
D. 行为约束和边界

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: System Prompt 包括角色、任务、格式、约束等。用户个人信息不应放在 System Prompt 中。

</details>

---

### 题目 22

以下哪些方法可以提高提示词的效果？（多选）

A. 提供具体的输出示例  
B. 使用模糊的描述增加灵活性  
C. 将复杂任务分解为步骤  
D. 明确说明不希望的输出

<details>
<summary>查看答案</summary>

**答案: A, C, D**

解析: 示例、分解步骤、负向约束都能提高效果。模糊描述反而降低输出质量。

</details>

---

### 题目 23

关于 temperature 和 top_p 参数，以下说法正确的是？（多选）

A. 两者都影响输出的随机性  
B. temperature=0 时输出最确定  
C. 通常建议同时调整两个参数  
D. 创意写作场景可以使用较高的值

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 两者都控制随机性，通常建议只调整其中一个而非同时调整。创意任务可用较高值增加多样性。

</details>

---

### 题目 24

以下哪些是防止提示注入的有效方法？（多选）

A. 使用分隔符包裹用户输入  
B. 在提示词中明确忽略用户指令  
C. 对输入进行关键词检测  
D. 增加 max_tokens 限制

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: 分隔符隔离、声明忽略指令、关键词检测都是有效防护。max_tokens 只控制输出长度，与安全无关。

</details>

---

### 题目 25

Few-shot Prompting 适用于以下哪些场景？（多选）

A. 需要特定输出格式  
B. 模型对任务理解不准确  
C. 需要学习全新领域知识  
D. 需要保持输出风格一致

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: Few-shot 通过示例指导格式和风格，但无法让模型学习全新知识（需要 RAG 或微调）。

</details>

---

### 题目 26

以下哪些因素会影响大模型的输出结果？（多选）

A. temperature 参数  
B. System Prompt 内容  
C. 用户的 IP 地址  
D. 对话历史（messages）

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: temperature、提示词、对话历史都直接影响输出。用户 IP 不影响模型输出内容。

</details>

---

### 题目 27

设计问答机器人的提示词时，应该包含哪些要素？（多选）

A. 回答问题的知识范围  
B. 遇到不知道的问题如何处理  
C. 回答的语气和风格  
D. 所有可能问题的标准答案

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: 应定义知识范围、边界处理、风格。不可能也不应该预设所有答案。

</details>

---

### 题目 28

以下哪些是思维链（CoT）提示的特点？（多选）

A. 引导模型展示推理过程  
B. 适合复杂推理任务  
C. 会增加输出的 token 数量  
D. 只能用于数学问题

<details>
<summary>查看答案</summary>

**答案: A, B, C**

解析: CoT 引导推理过程，适合复杂任务，会增加输出。不限于数学，逻辑推理、问题分析等都可用。

</details>

---

### 题目 29

以下哪些情况需要调整 System Prompt？（多选）

A. 模型输出不符合预期格式  
B. 模型处理了不应该处理的请求  
C. 需要更换底层模型  
D. 用户反馈回答风格不合适

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 格式、边界、风格问题都可以通过调整 Prompt 解决。更换模型可能需要调整提示词，但不是必须的触发因素。

</details>

---

### 题目 30

关于提示词工程与其他技术的关系，以下说法正确的是？（多选）

A. 提示词工程是最低成本的优化方式  
B. 复杂问题可能需要结合 RAG  
C. 提示词工程可以完全替代模型微调  
D. 好的提示词可以显著提升输出质量

<details>
<summary>查看答案</summary>

**答案: A, B, D**

解析: 提示词工程成本最低、可与 RAG 结合、能显著提升质量。但无法完全替代微调（如改变模型行为风格）。

</details>
