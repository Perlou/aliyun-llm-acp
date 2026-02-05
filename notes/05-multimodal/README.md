# 🎨 AI 辅助多模态内容生产

> 📊 **考试占比**: 12% (~12 题)
>
> 🎯 **重要程度**: ⭐⭐⭐

## 📚 知识大纲

### 1. 通义多模态模型系列 ⭐

#### 1.1 Qwen 模型家族

| 模型            | 能力     | 应用场景         |
| --------------- | -------- | ---------------- |
| **Qwen-Max**    | 文本生成 | 对话、写作、代码 |
| **Qwen-VL**     | 视觉理解 | 图像分析、OCR    |
| **Qwen-Audio**  | 语音处理 | 语音识别、理解   |
| **Qwen-VL-Max** | 高阶视觉 | 复杂图像推理     |

#### 1.2 多模态能力

```
视觉能力 (Qwen-VL):
├── 图像描述: 描述图片内容
├── 视觉问答: 回答关于图片的问题
├── OCR: 识别图片中的文字
├── 物体检测: 识别图片中的物体
└── 图表理解: 解读图表数据

音频能力 (Qwen-Audio):
├── 语音识别: 转文字
├── 语音理解: 理解语音内容
└── 音频分析: 理解音频事件
```

### 2. 多模态 API 调用

#### 2.1 Qwen-VL 图像理解

```python
from dashscope import MultiModalConversation

response = MultiModalConversation.call(
    model="qwen-vl-max",
    messages=[{
        "role": "user",
        "content": [
            {"image": "https://example.com/image.jpg"},
            {"text": "请描述这张图片"}
        ]
    }]
)

print(response.output.choices[0].message.content)
```

#### 2.2 本地图片处理

```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 使用 base64 编码
image_base64 = encode_image("local_image.jpg")
messages = [{
    "role": "user",
    "content": [
        {"image": f"data:image/jpeg;base64,{image_base64}"},
        {"text": "图片中有什么？"}
    ]
}]
```

### 3. Agent 智能体 ⭐

#### 3.1 Agent 核心概念

```
Agent = LLM + 工具 + 规划 + 记忆

运行循环 (ReAct):
┌─────────────────────────────────────┐
│  1. 思考 (Thought)                  │
│     分析任务，制定计划               │
│              ↓                      │
│  2. 行动 (Action)                   │
│     选择并调用工具                   │
│              ↓                      │
│  3. 观察 (Observation)              │
│     获取工具返回结果                 │
│              ↓                      │
│  4. 循环直到任务完成                 │
└─────────────────────────────────────┘
```

#### 3.2 工具调用 (Function Calling)

```python
# 定义工具
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "获取指定城市的天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "城市名称"
                }
            },
            "required": ["city"]
        }
    }
}]

# 调用带工具的对话
response = client.chat.completions.create(
    model="qwen-max",
    messages=[{"role": "user", "content": "北京天气怎么样?"}],
    tools=tools,
    tool_choice="auto"
)

# 处理工具调用
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    # 执行工具...
```

### 4. 百炼 Assistant API

#### 4.1 Assistant 架构

```
Assistant = 角色定义 + 知识库 + 插件工具

能力:
├── 对话管理: 多轮对话状态维护
├── 知识检索: RAG 能力
├── 工具调用: 插件执行
└── 记忆管理: 上下文记忆
```

#### 4.2 创建 Assistant

```python
from dashscope import Assistants, Threads, Messages, Runs

# 创建助手
assistant = Assistants.create(
    model="qwen-max",
    name="健康助手",
    instructions="你是一个专业的健康顾问",
    tools=[{"type": "retrieval"}],  # 启用知识检索
    file_ids=["file_xxx"]  # 关联知识库文件
)

# 创建对话线程
thread = Threads.create()

# 发送消息
Messages.create(
    thread_id=thread.id,
    role="user",
    content="什么是健康饮食?"
)

# 运行助手
run = Runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# 获取回复
messages = Messages.list(thread_id=thread.id)
```

### 5. Multi-Agent 多智能体

#### 5.1 多智能体架构

```
Multi-Agent 协作模式:

1. 串行模式:
   Agent A → Agent B → Agent C

2. 并行模式:
   Agent A ↘
            → 汇总 → 输出
   Agent B ↗

3. 层级模式:
   Manager Agent
        ↓
   ┌────┴────┐
   Worker A  Worker B
```

#### 5.2 应用场景

| 场景     | 架构 | Agent 角色               |
| -------- | ---- | ------------------------ |
| 文章撰写 | 串行 | 研究员 → 作者 → 编辑     |
| 代码开发 | 串行 | 架构师 → 开发者 → 测试员 |
| 客服系统 | 层级 | 路由 → 专业客服          |
| 数据分析 | 并行 | 多角度分析 → 汇总        |

### 6. 多模态内容生产

#### 6.1 文本 + 图像联合生成

```python
# 文案 + 配图一体化
pipeline = [
    "用户需求分析",
    "文案生成 (Qwen-Max)",
    "配图提示词生成",
    "图像生成 (通义万相)",
    "内容审核",
    "输出成品"
]
```

#### 6.2 语音助手构建

```python
# 语音助手流程
flow = """
语音输入 → ASR (语音识别)
         → LLM (理解和生成)
         → TTS (语音合成)
         → 语音输出
"""
```

---

## ✅ 知识点自测

1. [ ] Qwen-VL 和 Qwen-Audio 分别处理什么?
2. [ ] Agent 的 ReAct 循环是什么?
3. [ ] Function Calling 的流程?
4. [ ] 百炼 Assistant API 的核心组件?
5. [ ] Multi-Agent 的常见协作模式?

---

## 📝 考点速记卡

```
🔹 Qwen-VL = 视觉理解，Qwen-Audio = 音频处理
🔹 Agent = LLM + Tools + Planning + Memory
🔹 ReAct = Thought → Action → Observation
🔹 Function Calling = 工具定义 + 自动选择 + 执行
🔹 Assistant = 角色 + 知识库 + 插件
🔹 Multi-Agent = 串行/并行/层级协作
```
