"""
Week 2 Day 3-4: 大模型应用开发
阿里云大模型ACP认证备考 - 考试占比 16%

运行: python week2_day3_app_dev.py
"""

import os
from openai import OpenAI

API_KEY = os.getenv("DASHSCOPE_API_KEY", "your_api_key_here")
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
client = (
    OpenAI(api_key=API_KEY, base_url=BASE_URL)
    if API_KEY != "your_api_key_here"
    else None
)


def exercise1_messages():
    """练习1: 消息格式"""
    print("=" * 60)
    print("练习1: 消息格式与角色")
    print("=" * 60)

    print("""
📊 消息角色类型

┌─────────────┬─────────────────────────────────────────────────┐
│ 角色         │ 作用                                           │
├─────────────┼─────────────────────────────────────────────────┤
│ system      │ 系统设定，定义AI角色，贯穿整个对话              │
│ user        │ 用户输入                                        │
│ assistant   │ AI回复，记录历史用于多轮对话                    │
└─────────────┴─────────────────────────────────────────────────┘

messages = [
    {"role": "system", "content": "你是Python助手"},
    {"role": "user", "content": "如何读取JSON？"},
    {"role": "assistant", "content": "使用json模块..."},  # 历史
    {"role": "user", "content": "如何处理编码？"}         # 当前
]
""")


def exercise2_streaming():
    """练习2: 流式输出"""
    print("\n" + "=" * 60)
    print("练习2: 流式 vs 批量输出")
    print("=" * 60)

    print("""
📊 对比

批量 (stream=False):
  请求 ────────[等待]────────→ 完整响应

流式 (stream=True):
  请求 → [token1] → [token2] → ... → [END]
       ↓ 显示    ↓ 显示

代码:
```python
# 流式
stream = client.chat.completions.create(
    model="qwen-max", messages=messages, stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

💡 考点: 流式体验好，delta.content 是增量内容
""")

    if client:
        print("\n🔹 流式演示:")
        stream = client.chat.completions.create(
            model="qwen-max",
            messages=[{"role": "user", "content": "用一句话介绍Python"}],
            stream=True,
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
        print()


def exercise3_conversation():
    """练习3: 多轮对话"""
    print("\n" + "=" * 60)
    print("练习3: 多轮对话管理")
    print("=" * 60)

    print("""
📊 多轮对话实现

核心: 维护 messages 列表，追加 user 和 assistant

```python
class ChatBot:
    def __init__(self, system_prompt):
        self.history = [{"role": "system", "content": system_prompt}]
    
    def chat(self, user_input):
        self.history.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model="qwen-max", messages=self.history
        )
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return reply
```

📊 上下文管理:
  - 截断: 保留最近 N 轮
  - 摘要: 将旧对话总结
  - 滑动窗口: 始终保持 N 条
""")


def exercise4_langchain():
    """练习4: LangChain"""
    print("\n" + "=" * 60)
    print("练习4: LangChain 概念")
    print("=" * 60)

    print("""
📊 LangChain 组件

┌─────────────────────────────────────────────────────────────┐
│ Models    │ LLMs / Chat Models                             │
│ Prompts   │ PromptTemplate                                 │
│ Chains    │ LLMChain / SequentialChain                     │
│ Memory    │ ConversationBufferMemory / SummaryMemory       │
│ Agents    │ 动态工具选择                                    │
└─────────────────────────────────────────────────────────────┘

💡 考点:
  - Chain = Prompt + Model 组合
  - Memory = 对话历史管理
  - Agent = 动态工具选择
""")


def exercise5_dify():
    """练习5: Dify"""
    print("\n" + "=" * 60)
    print("练习5: Dify 平台")
    print("=" * 60)

    print("""
📊 Dify 特点

  🎨 可视化编排 - 拖拽式无代码
  🔌 内置 RAG - 知识库管理
  🤖 Agent 构建 - 工具/插件集成
  🚀 快速部署 - 一键发布 API

适用场景:
  - 快速原型验证
  - 非技术人员使用
  - 复杂工作流编排

💡 对比:
  - Dify: 低代码快速
  - LangChain: 代码级灵活
  - 百炼: 阿里云生态集成
""")


def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║     Week 2 Day 3-4: 大模型应用开发                        ║
║     阿里云大模型ACP认证备考 (16%)                         ║
╚══════════════════════════════════════════════════════════╝
""")
    exercises = {
        "1": exercise1_messages,
        "2": exercise2_streaming,
        "3": exercise3_conversation,
        "4": exercise4_langchain,
        "5": exercise5_dify,
    }

    print("选择: 1.消息格式 2.流式输出 3.多轮对话 4.LangChain 5.Dify 0.全部")
    choice = input("请选择 (0-5): ").strip()

    if choice == "0":
        for f in exercises.values():
            f()
    elif choice in exercises:
        exercises[choice]()

    print("\n✅ Week 2 Day 3-4 完成！")


if __name__ == "__main__":
    main()
