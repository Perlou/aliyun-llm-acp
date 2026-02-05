# 📅 阿里云大模型 ACP 认证学习计划

> 建议总备考周期：**4-5 周**（基于已完成 llm-course 的基础）

## 🎯 学习原则

1. **重点突破**: 提示词工程 + RAG 占 48%，是重中之重
2. **理论 + 实践**: 每个模块配合百炼平台实操
3. **刷题巩固**: 每完成一个模块进行专项练习
4. **模拟考试**: 考前进行 2-3 次完整模拟

---

## 📆 第一阶段：知识梳理 (第 1-2 周)

### Week 1：核心模块 (48% 考点)

#### Day 1-2: 提示词工程 (24%)

**学习内容**:

- [ ] 提示词框架与要素
  - 角色定义、任务描述、输出格式
  - 分隔符使用（###、"""、---）
- [ ] 系统角色提示词 (System Prompt)
- [ ] 提示词模板设计
- [ ] 实战场景
  - 意图分类
  - 文档审阅
  - 内容生成

**实践任务**:

```python
# 在百炼平台完成:
1. 调用通义千问 API，测试不同 temperature 效果
2. 设计一个多轮对话的 System Prompt
3. 实现一个意图分类的 Prompt
```

**参考资源**:

- 百炼平台 Prompt 最佳实践
- [notes/01-prompt-engineering/README.md](./notes/01-prompt-engineering/README.md)
- [practice/week1/week1_day1_prompt_engineering.py](./practice/week1/week1_day1_prompt_engineering.py)

---

#### Day 3-5: 检索增强生成 RAG (24%)

**学习内容**:

- [ ] RAG 核心概念与架构
- [ ] RAG 四大核心要素
  - 文件解析 (Document Parsing)
  - 文本切片 (Text Chunking)
  - 段落召回 (Retrieval)
  - 重排序 (Re-ranking)
- [ ] LlamaIndex 构建 RAG 应用
- [ ] RAG 召回优化
  - 句子窗口检索 (Sentence Window)
  - 自动合并检索 (Auto-Merge)
- [ ] RAG 评测体系 (RAGAS)
  - Faithfulness
  - Answer Relevancy
  - Context Precision
  - Context Recall

**实践任务**:

```python
# 使用 LlamaIndex + 百炼:
1. 搭建基础 RAG 应用
2. 实现不同 Chunking 策略对比
3. 使用 RAGAS 评测 RAG 效果
```

**参考资源**:

- 百炼知识库功能文档
- [notes/02-rag/README.md](./notes/02-rag/README.md)
- [practice/week1/week1_day3_rag.py](./practice/week1/week1_day3_rag.py)

---

### Week 2：进阶模块 (52% 考点)

#### Day 1-2: 大模型微调 (16%)

**学习内容**:

- [ ] 微调的作用与适用场景
- [ ] 微调 vs Prompt Engineering vs RAG
- [ ] 常用微调算法
  - LoRA / QLoRA
  - Full Fine-tuning
- [ ] 微调数据集构建
  - 数据格式要求
  - 数据质量控制
- [ ] 微调参数详解
  - Learning Rate
  - Epochs
  - Batch Size
- [ ] 模型评测指标

**实践任务**:

```python
# 在百炼平台:
1. 了解微调任务创建流程
2. 准备微调数据集格式
3. 理解微调参数配置
```

**参考资源**: [practice/week2/week2_day1_finetuning.py](./practice/week2/week2_day1_finetuning.py)

---

#### Day 3-4: 应用开发基础 (16%)

**学习内容**:

- [ ] 大模型 API 调用
  - OpenAI 兼容 API 格式
  - 核心参数: model, temperature, top_p, max_tokens
- [ ] 批量生成 vs 流式生成
- [ ] 消息格式与对话历史管理
- [ ] LangChain 基础
  - Chain 概念
  - Memory 管理
- [ ] Dify 平台使用

**实践任务**:

```python
# 代码实践:
1. 实现流式输出对话
2. 使用 LangChain 构建简单 Chain
3. 体验 Dify 低代码开发
```

**参考资源**: [practice/week2/week2_day3_app_dev.py](./practice/week2/week2_day3_app_dev.py)

---

#### Day 5-6: 多模态与 Agent (12%)

**学习内容**:

- [ ] 通义系列多模态模型
  - Qwen-VL (视觉)
  - Qwen-Audio (音频)
- [ ] Multi-Agent 架构
- [ ] 百炼 Assistant API
- [ ] 插件开发与工具调用
- [ ] 个性化语音助手

**实践任务**:

```python
# 在百炼平台:
1. 调用 Qwen-VL 进行图像理解
2. 使用 Assistant API 构建 Agent
3. 实现工具调用 (Function Calling)
```

**参考资源**: [practice/week2/week2_day5_multimodal_agent.py](./practice/week2/week2_day5_multimodal_agent.py)

---

#### Day 7: 伦理与安全 (8%)

**学习内容**:

- [ ] 内容安全问题类型
  - 有害内容
  - 隐私泄露
  - 偏见歧视
- [ ] 合规检测方案
- [ ] 云服务安全基础
- [ ] 大模型安全最佳实践

**参考资源**: [practice/week2/week2_day7_ethics_security.py](./practice/week2/week2_day7_ethics_security.py)

---

## 📆 第二阶段：实践巩固 (第 3 周)

### 综合实践项目

#### Project 1: 企业知识库问答系统

```
技术栈: LlamaIndex + 百炼 + RAG
覆盖考点: RAG、Prompt Engineering、应用开发
```

#### Project 2: 智能客服 Agent

```
技术栈: 百炼 Assistant API + 工具调用
覆盖考点: Agent、多模态、应用开发
```

#### Project 3: 模型部署实践

```
技术栈: vLLM + 函数计算 FC / PAI
覆盖考点: 微调、云上部署
```

---

## 📆 第三阶段：刷题强化 (第 4 周)

### 刷题策略

| 天数    | 任务            | 题量   |
| ------- | --------------- | ------ |
| Day 1-2 | 提示词工程专项  | 50 题  |
| Day 3-4 | RAG 专项        | 50 题  |
| Day 5   | 微调 + 应用开发 | 40 题  |
| Day 6   | 多模态 + 安全   | 30 题  |
| Day 7   | 综合模拟测试    | 100 题 |

### 错题整理

每次刷题后整理错题到 `questions/wrong-answers.md`：

- 错误原因分析
- 正确知识点补充
- 相关知识点串联

---

## 📆 第四阶段：考前冲刺 (考前 3 天)

### Day -3: 知识点速记

- [ ] 复习 `questions/key-points.md`
- [ ] 重点公式和概念背诵

### Day -2: 模拟考试

- [ ] 完成官方模拟测试
- [ ] 计时 120 分钟
- [ ] 整理错题

### Day -1: 查漏补缺

- [ ] 复习错题本
- [ ] 薄弱环节专项复习
- [ ] 调整作息，保证睡眠

---

## ⏰ 每日学习安排建议

```
┌─────────────┬────────────────────────────────┐
│ 时间段       │ 学习内容                        │
├─────────────┼────────────────────────────────┤
│ 上午 2h     │ 理论学习 - 看文档、记笔记         │
│ 下午 2h     │ 实践练习 - 百炼平台动手           │
│ 晚上 1h     │ 刷题巩固 - 专项练习              │
└─────────────┴────────────────────────────────┘
```

---

## 📊 学习进度追踪

在每个章节完成后更新进度:

| 模块       | 进度    | 完成日期   |
| ---------- | ------- | ---------- |
| 提示词工程 | ✅ 完成 | 2026-02-05 |
| RAG        | ✅ 完成 | 2026-02-05 |
| 微调       | ✅ 完成 | 2026-02-05 |
| 应用开发   | ✅ 完成 | 2026-02-05 |
| 多模态     | ✅ 完成 | 2026-02-05 |
| 伦理安全   | ✅ 完成 | 2026-02-05 |
