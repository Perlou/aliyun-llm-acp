# 💻 大模型应用开发

> 📊 **考试占比**: 16% (~16 题)
>
> 🎯 **重要程度**: ⭐⭐⭐⭐

## 📚 知识大纲

### 1. 大模型 API 基础

#### 1.1 OpenAI 兼容 API 格式

```python
from openai import OpenAI

client = OpenAI(
    api_key="your_api_key",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response = client.chat.completions.create(
    model="qwen-max",
    messages=[
        {"role": "system", "content": "你是一个助手"},
        {"role": "user", "content": "你好"}
    ]
)
```

#### 1.2 核心 API 参数 ⭐

| 参数          | 类型  | 说明         | 常见值                |
| ------------- | ----- | ------------ | --------------------- |
| `model`       | str   | 模型名称     | qwen-max, qwen-plus   |
| `messages`    | list  | 对话历史     | system/user/assistant |
| `temperature` | float | 随机性       | 0-2, 默认 1           |
| `top_p`       | float | 核采样       | 0-1, 默认 1           |
| `max_tokens`  | int   | 最大输出长度 | 按需设置              |
| `stream`      | bool  | 流式输出     | true/false            |
| `stop`        | list  | 停止词       | 自定义                |

#### 1.3 消息角色类型

```python
messages = [
    {
        "role": "system",     # 系统设定，贯穿对话
        "content": "你是医疗助手"
    },
    {
        "role": "user",       # 用户输入
        "content": "什么是感冒？"
    },
    {
        "role": "assistant",  # AI 回复
        "content": "感冒是..."
    }
]
```

### 2. 批量生成 vs 流式生成 ⭐

#### 2.1 批量生成 (Non-streaming)

```python
# 等待完整响应
response = client.chat.completions.create(
    model="qwen-max",
    messages=messages,
    stream=False  # 默认
)

print(response.choices[0].message.content)
```

**特点**:

- 一次性返回完整结果
- 用户需等待完整生成
- 适合后台处理任务

#### 2.2 流式生成 (Streaming)

```python
# 逐字返回
response = client.chat.completions.create(
    model="qwen-max",
    messages=messages,
    stream=True  # 开启流式
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

**特点**:

- 实时逐字返回
- 用户体验更好
- 适合对话交互场景

### 3. 对话历史管理

#### 3.1 多轮对话实现

```python
class ChatBot:
    def __init__(self, system_prompt):
        self.history = [
            {"role": "system", "content": system_prompt}
        ]

    def chat(self, user_input):
        # 添加用户消息
        self.history.append({"role": "user", "content": user_input})

        # 调用 API
        response = client.chat.completions.create(
            model="qwen-max",
            messages=self.history
        )

        # 获取回复
        assistant_msg = response.choices[0].message.content

        # 保存到历史
        self.history.append({"role": "assistant", "content": assistant_msg})

        return assistant_msg
```

#### 3.2 上下文长度管理

```python
def truncate_history(messages, max_tokens=4000):
    """保留最近的消息，避免超出上下文限制"""
    # 保留 system prompt
    system = messages[0] if messages[0]["role"] == "system" else None

    # 从最近的消息开始保留
    truncated = []
    total_tokens = 0

    for msg in reversed(messages[1:]):
        msg_tokens = len(msg["content"]) // 2  # 粗略估算
        if total_tokens + msg_tokens > max_tokens:
            break
        truncated.insert(0, msg)
        total_tokens += msg_tokens

    if system:
        truncated.insert(0, system)

    return truncated
```

### 4. LangChain 基础

#### 4.1 核心组件

```
LangChain 架构:
├── Models (模型层)
│   ├── LLMs: 文本输入 → 文本输出
│   └── Chat Models: 消息输入 → 消息输出
├── Prompts (提示层)
│   ├── PromptTemplate: 提示模板
│   └── ChatPromptTemplate: 对话模板
├── Chains (链路层)
│   ├── LLMChain: 基础链
│   └── SequentialChain: 顺序链
├── Memory (记忆层)
│   ├── ConversationBufferMemory
│   └── ConversationSummaryMemory
└── Agents (代理层)
    └── ReAct Agent
```

#### 4.2 简单 Chain 示例

```python
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Tongyi

# 创建 LLM
llm = Tongyi(model_name="qwen-max")

# 创建模板
prompt = PromptTemplate(
    input_variables=["topic"],
    template="请写一篇关于{topic}的简短介绍"
)

# 创建 Chain
chain = LLMChain(llm=llm, prompt=prompt)

# 运行
result = chain.run(topic="人工智能")
```

#### 4.3 Memory 使用

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

# 对话会自动记住历史
conversation.predict(input="你好")
conversation.predict(input="我刚才说了什么?")
```

### 5. Dify 平台

#### 5.1 Dify 特点

- 可视化低代码开发
- 拖拽式工作流编排
- 内置 RAG 和 Agent
- 多模型管理

#### 5.2 适用场景

- 快速原型开发
- 非技术人员使用
- 复杂工作流编排

### 6. 百炼平台应用开发

#### 6.1 应用类型

| 类型         | 说明           | 适用场景       |
| ------------ | -------------- | -------------- |
| **智能问答** | 基于知识库问答 | 客服、文档助手 |
| **智能体**   | 工具调用能力   | 复杂任务处理   |
| **工作流**   | 多步骤编排     | 业务流程自动化 |

#### 6.2 API 调用示例

```python
from dashscope import Application

response = Application.call(
    app_id="your_app_id",
    prompt="用户问题"
)

print(response.output.text)
```

---

## ✅ 知识点自测

1. [ ] messages 中三种 role 的作用?
2. [ ] 流式生成和批量生成的区别?
3. [ ] temperature 和 top_p 如何影响输出?
4. [ ] LangChain 的核心组件有哪些?
5. [ ] 如何管理对话历史避免超出上下文?

---

## 📝 考点速记卡

```
🔹 role 类型 = system + user + assistant
🔹 stream=True → 逐字返回，体验好
🔹 temperature ↓ = 确定性 ↑
🔹 top_p = 核采样，通常 0.9
🔹 LangChain = Models + Prompts + Chains + Memory
🔹 多轮对话 = 维护 messages 列表
```
