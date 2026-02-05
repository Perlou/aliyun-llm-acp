"""
Week 3 Project 2: 智能客服 Agent
阿里云大模型ACP认证备考 - 阶段二实践项目

技术栈: Function Calling + Agent + 多轮对话
覆盖考点: Agent (12%) + 应用开发 (16%) + Prompt (24%)

运行前请设置:
export DASHSCOPE_API_KEY="your_api_key"
"""

import os
import json
from datetime import datetime
from openai import OpenAI

API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL) if API_KEY else None


# ============================================================
# Step 1: 意图分类
# ============================================================
def step1_intent_classification():
    """意图分类设计"""
    print("=" * 60)
    print("Step 1: 意图分类")
    print("=" * 60)

    intent_prompt = """你是一个智能客服意图分类器。

将用户输入分类为以下类别之一：
- 查询订单: 询问订单状态、物流信息、发货时间
- 退款退货: 申请退款、退货、换货
- 产品咨询: 询问产品功能、规格、价格
- 账户问题: 登录、注册、密码、账户信息
- 投诉建议: 投诉服务、提出建议
- 其他: 不属于以上类别

只输出类别名称，不要解释。

用户输入: {input}
类别:"""

    test_inputs = [
        "我的订单123456什么时候发货？",
        "这个商品支持7天无理由退货吗？",
        "手机的电池容量是多少？",
        "我忘记密码了怎么办？",
        "你们的客服态度太差了！",
        "今天天气怎么样？",
    ]

    print("\n📋 意图分类测试:\n")

    if client:
        for text in test_inputs:
            response = client.chat.completions.create(
                model="qwen-max",
                messages=[
                    {"role": "user", "content": intent_prompt.format(input=text)}
                ],
                temperature=0,  # 分类任务用低温度
            )
            intent = response.choices[0].message.content.strip()
            print(f"  [{intent:8}] {text}")
    else:
        print("  ⚠️ 需要 API Key 运行实际分类")
        print("\n  预期结果:")
        expected = ["查询订单", "退款退货", "产品咨询", "账户问题", "投诉建议", "其他"]
        for text, intent in zip(test_inputs, expected):
            print(f"  [{intent:8}] {text}")


# ============================================================
# Step 2: 工具定义 (Function Calling)
# ============================================================
def step2_tool_definition():
    """工具定义"""
    print("\n" + "=" * 60)
    print("Step 2: 工具定义 (Function Calling)")
    print("=" * 60)

    print("""
📊 工具定义格式:

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "query_order",
            "description": "查询订单状态和物流信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "订单号"
                    }
                },
                "required": ["order_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "apply_refund",
            "description": "申请退款",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string", "description": "订单号"},
                    "reason": {"type": "string", "description": "退款原因"}
                },
                "required": ["order_id", "reason"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_product_info",
            "description": "查询产品信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string", "description": "产品名称"}
                },
                "required": ["product_name"]
            }
        }
    }
]
```
""")
    return get_tools()


def get_tools():
    """返回工具定义"""
    return [
        {
            "type": "function",
            "function": {
                "name": "query_order",
                "description": "查询订单状态和物流信息",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "订单号"}
                    },
                    "required": ["order_id"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "apply_refund",
                "description": "申请退款",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "订单号"},
                        "reason": {"type": "string", "description": "退款原因"},
                    },
                    "required": ["order_id", "reason"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_product_info",
                "description": "查询产品信息",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {"type": "string", "description": "产品名称"}
                    },
                    "required": ["product_name"],
                },
            },
        },
    ]


# ============================================================
# Step 3: 工具执行 (模拟)
# ============================================================
def execute_tool(name: str, arguments: dict) -> str:
    """执行工具调用 (模拟)"""

    if name == "query_order":
        order_id = arguments.get("order_id", "unknown")
        return json.dumps(
            {
                "order_id": order_id,
                "status": "已发货",
                "logistics": "顺丰快递",
                "tracking_no": "SF1234567890",
                "estimated_arrival": "2天后",
            },
            ensure_ascii=False,
        )

    elif name == "apply_refund":
        order_id = arguments.get("order_id", "unknown")
        reason = arguments.get("reason", "")
        return json.dumps(
            {
                "order_id": order_id,
                "refund_id": f"RF{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "status": "已提交",
                "message": f"退款申请已提交，原因：{reason}，预计1-3个工作日处理",
            },
            ensure_ascii=False,
        )

    elif name == "get_product_info":
        product = arguments.get("product_name", "")
        return json.dumps(
            {
                "product_name": product,
                "price": "2999元",
                "specs": "128GB存储/8GB内存",
                "battery": "5000mAh",
                "warranty": "1年保修",
            },
            ensure_ascii=False,
        )

    return json.dumps({"error": "未知工具"})


# ============================================================
# Step 4: Agent 对话循环
# ============================================================
def step4_agent_conversation():
    """Agent 对话实现"""
    print("\n" + "=" * 60)
    print("Step 4: Agent 对话")
    print("=" * 60)

    if not client:
        print("⚠️ 需要 API Key 运行 Agent")
        print_agent_concept()
        return

    system_prompt = """你是一个专业的智能客服助手。

## 职责
- 帮助用户查询订单状态
- 处理退款退货申请
- 回答产品相关问题

## 规范
- 态度友好专业
- 回答简洁明了
- 必要时使用工具获取信息

## 边界
- 不处理账户安全问题
- 复杂问题转人工客服"""

    messages = [{"role": "system", "content": system_prompt}]
    tools = get_tools()

    print("\n💬 智能客服已启动 (输入 'quit' 退出)\n")

    while True:
        user_input = input("用户: ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            print("👋 感谢使用，再见！")
            break

        messages.append({"role": "user", "content": user_input})

        # 调用模型
        response = client.chat.completions.create(
            model="qwen-max", messages=messages, tools=tools, tool_choice="auto"
        )

        assistant_message = response.choices[0].message

        # 检查是否需要调用工具
        if assistant_message.tool_calls:
            messages.append(assistant_message)

            for tool_call in assistant_message.tool_calls:
                func_name = tool_call.function.name
                func_args = json.loads(tool_call.function.arguments)

                print(f"  🔧 调用工具: {func_name}({func_args})")

                result = execute_tool(func_name, func_args)

                messages.append(
                    {"role": "tool", "tool_call_id": tool_call.id, "content": result}
                )

            # 再次调用获取最终回复
            response = client.chat.completions.create(
                model="qwen-max", messages=messages
            )
            assistant_message = response.choices[0].message

        reply = assistant_message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"客服: {reply}\n")


def print_agent_concept():
    """打印 Agent 概念"""
    print("""
📊 Agent 执行流程 (ReAct):

  用户输入 → Thought (思考)
                ↓
            Action (调用工具)
                ↓
            Observation (获取结果)
                ↓
            判断完成? ─No→ 回到 Thought
                ↓ Yes
            Final Answer

📊 Function Calling 流程:

1. 用户: "查一下订单123456"
2. 模型返回 tool_calls: query_order(order_id="123456")
3. 执行工具，获取结果
4. 将结果以 role="tool" 返回给模型
5. 模型生成最终回答
""")


# ============================================================
# Step 5: 多轮对话管理
# ============================================================
def step5_conversation_management():
    """多轮对话管理"""
    print("\n" + "=" * 60)
    print("Step 5: 多轮对话管理")
    print("=" * 60)

    print("""
📊 上下文管理策略:

```python
class ConversationManager:
    def __init__(self, max_turns=10):
        self.history = []
        self.max_turns = max_turns
    
    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})
        self._truncate_if_needed()
    
    def _truncate_if_needed(self):
        # 保留 system + 最近 N 轮对话
        system = [m for m in self.history if m["role"] == "system"]
        others = [m for m in self.history if m["role"] != "system"]
        
        if len(others) > self.max_turns * 2:
            others = others[-(self.max_turns * 2):]
        
        self.history = system + others
    
    def get_messages(self):
        return self.history
```

📊 摘要策略:

当对话过长时，可以：
1. 截断旧对话
2. 将旧对话总结为一条消息
3. 只保留关键信息 (如订单号、用户需求)

📊 考点:
- 多轮对话需要保存 user 和 assistant 消息
- 上下文过长需要截断或摘要
- system prompt 始终保留
""")


# ============================================================
# 主程序
# ============================================================
def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║     Week 3 Project 2: 智能客服 Agent                      ║
║     阿里云大模型ACP认证备考 - 阶段二实践                  ║
╚══════════════════════════════════════════════════════════╝
""")

    print("选择运行步骤:")
    print("  1. 意图分类")
    print("  2. 工具定义")
    print("  3. Agent 对话 (需要API Key)")
    print("  4. 多轮对话管理")
    print("  0. 全部学习")

    choice = input("\n请选择 (0-4): ").strip()

    if choice == "1":
        step1_intent_classification()
    elif choice == "2":
        step2_tool_definition()
    elif choice == "3":
        step4_agent_conversation()
    elif choice == "4":
        step5_conversation_management()
    elif choice == "0":
        step1_intent_classification()
        step2_tool_definition()
        print_agent_concept()
        step5_conversation_management()

    print("\n" + "=" * 60)
    print("✅ Project 2 完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
