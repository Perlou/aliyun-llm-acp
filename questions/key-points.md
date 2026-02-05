# 📝 重点知识点速记

> 考前最后复习使用，涵盖各模块核心考点

---

## 🎯 1. 提示词工程 (24%)

### 核心概念

```
System Prompt = 角色 + 规范 + 边界
分隔符类型 = ###、"""、---、<tag>
Few-shot = 提供示例引导
Chain of Thought = 展示推理步骤
```

### 参数记忆

```
temperature: 0-2, 控制随机性, 低=确定, 高=创意
top_p: 0-1, 核采样, 通常 0.9
max_tokens: 最大生成长度
一般不同时调整 temperature 和 top_p
```

### 设计原则

```
✅ 明确角色定位
✅ 清晰任务描述
✅ 具体输出格式
✅ 合理约束边界
✅ 使用分隔符防注入
```

---

## 🔍 2. RAG 检索增强 (24%)

### 核心流程

```
文档解析 → 文本切片 → 向量化 → 检索 → 重排序 → 生成
```

### RAG vs 微调

```
RAG: 知识可更新, 可溯源, 成本低
微调: 改变行为风格, 学习新概念, 成本高
```

### 优化策略

```
句子窗口 = 精确检索 + 上下文补充
自动合并 = 小块检索 → 父块返回
混合检索 = 稀疏(BM25) + 稠密(向量)
```

### RAGAS 指标

```
Faithfulness = 答案基于检索内容
Answer Relevancy = 答案回答了问题
Context Precision = 检索结果精确
Context Recall = 检索覆盖完整
```

---

## 🔧 3. 模型微调 (16%)

### 何时微调

```
✅ 特定写作风格
✅ 专业术语理解
✅ 稳定输出格式
❌ 实时知识更新 (用 RAG)
```

### LoRA 核心

```
原理: 低秩矩阵分解, W + ΔW = W + BA
参数: r(秩), lora_alpha(缩放), target_modules
优势: 参数量 ~0.1%, 可插拔
```

### 数据格式

```json
{ "instruction": "任务描述", "input": "输入", "output": "输出" }
```

### 训练参数

```
learning_rate: 1e-5 ~ 5e-5, 过大不稳定
epochs: 3-5, 过多过拟合
batch_size: 4-32, 越大越稳定
```

---

## 💻 4. 应用开发 (16%)

### API 消息角色

```
system: 系统设定, 贯穿对话
user: 用户输入
assistant: AI 回复
```

### 流式 vs 批量

```
stream=True: 逐字返回, 体验好, 适合对话
stream=False: 一次返回, 适合后台处理
```

### LangChain 组件

```
Models: LLMs / Chat Models
Prompts: Template
Chains: 链式调用
Memory: 对话记忆
Agents: 工具调用
```

---

## 🎨 5. 多模态应用 (12%)

### Qwen 模型

```
Qwen-VL: 视觉理解 (图像分析, OCR)
Qwen-Audio: 语音处理 (识别, 理解)
Qwen-Max: 文本生成
```

### Agent 核心

```
Agent = LLM + Tools + Planning + Memory
ReAct = Thought → Action → Observation (循环)
```

### Function Calling

```
1. 定义工具 (name, description, parameters)
2. 模型选择工具
3. 返回 tool_calls
4. 执行工具获取结果
5. 将结果返回模型
```

### Multi-Agent

```
串行: A → B → C
并行: A + B → 汇总
层级: Manager → Workers
```

---

## 🛡️ 6. 伦理与安全 (8%)

### 五大风险

```
1. 有害内容 (暴力/色情/违法)
2. 隐私泄露 (数据泄露)
3. 偏见歧视 (性别/种族)
4. 幻觉问题 (事实错误)
5. 提示注入 (越狱攻击)
```

### 四层防护

```
输入层: 敏感词过滤, 注入检测
模型层: 安全对齐, 拒绝机制
输出层: 内容审核, 脱敏处理
运营层: 人工审核, 日志审计
```

### 云安全要素

```
身份认证 (RAM, MFA)
网络安全 (VPC, 安全组)
数据安全 (加密, KMS)
审计追踪 (ActionTrail)
```

---

## ⚡ 考前速查

### 高频数字

```
temperature: 0-2
top_p: 0-1
LoRA 秩 r: 通常 8
学习率: 1e-5 ~ 5e-5
epochs: 3-5
及格分: 80 分
总题数: 100 题 (单选70 + 多选30)
```

### 高频对比

```
RAG vs 微调: 知识更新 vs 行为改变
Few-shot vs Zero-shot: 有示例 vs 无示例
stream=True vs False: 逐字 vs 一次性
稀疏检索 vs 稠密检索: 精确匹配 vs 语义理解
```

### 关键缩写

```
RAG = Retrieval Augmented Generation
LoRA = Low-Rank Adaptation
RLHF = Reinforcement Learning from Human Feedback
CoT = Chain of Thought
RAGAS = RAG Assessment
```
