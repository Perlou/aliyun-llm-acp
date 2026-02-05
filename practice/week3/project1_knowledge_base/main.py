"""
Week 3 Project 1: 企业知识库问答系统
阿里云大模型ACP认证备考 - 阶段二实践项目

技术栈: LlamaIndex + DashScope + RAG
覆盖考点: RAG (24%) + Prompt (24%) + 应用开发 (16%)

运行前请设置:
export DASHSCOPE_API_KEY="your_api_key"

依赖安装:
pip install llama-index llama-index-llms-dashscope llama-index-embeddings-dashscope
"""

import os
from pathlib import Path

# ============================================================
# 配置
# ============================================================
API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
DATA_DIR = Path(__file__).parent / "data"
INDEX_DIR = Path(__file__).parent / "index"


def check_environment():
    """检查环境配置"""
    print("=" * 60)
    print("环境检查")
    print("=" * 60)

    if not API_KEY:
        print("❌ DASHSCOPE_API_KEY 未设置")
        print("   请运行: export DASHSCOPE_API_KEY='your_key'")
        return False
    else:
        print(f"✅ API Key 已配置 ({API_KEY[:8]}...)")

    # 创建数据目录
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✅ 数据目录: {DATA_DIR}")
    print(f"✅ 索引目录: {INDEX_DIR}")

    return True


# ============================================================
# Step 1: 文档准备
# ============================================================
def step1_prepare_documents():
    """准备示例文档"""
    print("\n" + "=" * 60)
    print("Step 1: 准备文档")
    print("=" * 60)

    # 创建示例文档 - 阿里云百炼平台介绍
    docs = {
        "bailian_overview.txt": """
阿里云百炼平台概述

百炼是阿里云推出的一站式大模型应用开发平台，帮助企业和开发者快速构建AI应用。

主要功能包括：
1. 模型服务：提供通义千问系列模型，支持文本生成、对话、代码等能力
2. 知识库：支持文档上传、解析、向量化，构建企业专属知识库
3. 应用构建：零代码/低代码方式快速搭建AI应用
4. 模型微调：支持LoRA等微调方式，定制专属模型
5. Agent开发：通过Assistant API构建智能体应用

百炼平台支持的模型：
- Qwen-Max：最强文本理解和生成能力
- Qwen-Plus：性价比版本
- Qwen-Turbo：快速响应版本
- Qwen-VL：视觉理解模型
- Qwen-Audio：语音处理模型
""",
        "rag_introduction.txt": """
RAG (检索增强生成) 技术介绍

RAG是一种结合检索和生成的技术，通过检索外部知识来增强大模型的回答能力。

RAG的核心流程：
1. 文档解析 (Document Parsing)：将PDF、Word等文档解析为文本
2. 文本切片 (Chunking)：将长文本切分为适合检索的片段
3. 向量化 (Embedding)：将文本转换为向量表示
4. 索引存储 (Indexing)：将向量存入向量数据库
5. 检索 (Retrieval)：根据用户查询检索相关片段
6. 生成 (Generation)：将检索结果与查询一起输入大模型生成回答

RAG的优势：
- 知识可更新：无需重新训练模型
- 可溯源：回答可追溯到原始文档
- 成本低：不需要模型微调
- 减少幻觉：基于真实文档回答

RAG评测指标 (RAGAS)：
- Faithfulness：忠实度，答案是否基于检索内容
- Answer Relevancy：答案相关性
- Context Precision：上下文精确度
- Context Recall：上下文召回率
""",
        "prompt_engineering.txt": """
提示词工程最佳实践

提示词工程是优化大模型输出的关键技术。

System Prompt 设计要素：
1. 角色定义：明确AI的身份和专业领域
2. 任务描述：清晰说明需要完成的具体目标
3. 输出格式：指定回答的格式要求
4. 约束条件：设定限制和边界

常用分隔符：
- ### 用于分隔不同部分
- \"\"\" 用于包裹长文本
- <tag> XML标签用于结构化

提示词安全：
- 使用分隔符隔离用户输入
- 检测提示注入攻击
- 输入输出双重校验

示例 - 客服分类提示词：
你是一个客服意图分类器。
将用户输入分类为：查询订单/退款申请/产品咨询/投诉建议/其他
只输出类别名称，不要解释。
""",
    }

    for filename, content in docs.items():
        filepath = DATA_DIR / filename
        filepath.write_text(content.strip(), encoding="utf-8")
        print(f"✅ 创建文档: {filename}")

    print(f"\n📁 文档目录: {DATA_DIR}")
    return True


# ============================================================
# Step 2: 构建索引
# ============================================================
def step2_build_index():
    """构建向量索引"""
    print("\n" + "=" * 60)
    print("Step 2: 构建向量索引")
    print("=" * 60)

    if not API_KEY:
        print("⚠️ 需要 API Key，跳过实际构建")
        print_index_concept()
        return None

    try:
        from llama_index.core import (
            VectorStoreIndex,
            SimpleDirectoryReader,
            Settings,
            StorageContext,
            load_index_from_storage,
        )
        from llama_index.llms.dashscope import DashScope
        from llama_index.embeddings.dashscope import DashScopeEmbedding

        # 配置模型
        Settings.llm = DashScope(model_name="qwen-max", api_key=API_KEY)
        Settings.embed_model = DashScopeEmbedding(
            model_name="text-embedding-v2", api_key=API_KEY
        )

        print("✅ 模型配置完成: qwen-max + text-embedding-v2")

        # 检查是否已有索引
        if (INDEX_DIR / "docstore.json").exists():
            print("📦 发现已有索引，正在加载...")
            storage_context = StorageContext.from_defaults(persist_dir=str(INDEX_DIR))
            index = load_index_from_storage(storage_context)
            print("✅ 索引加载完成")
        else:
            # 读取文档
            print("📖 正在读取文档...")
            documents = SimpleDirectoryReader(str(DATA_DIR)).load_data()
            print(f"✅ 读取了 {len(documents)} 个文档")

            # 构建索引
            print("🔨 正在构建向量索引...")
            index = VectorStoreIndex.from_documents(documents)

            # 持久化
            index.storage_context.persist(persist_dir=str(INDEX_DIR))
            print(f"✅ 索引已保存到: {INDEX_DIR}")

        return index

    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print(
            "   请运行: pip install llama-index llama-index-llms-dashscope llama-index-embeddings-dashscope"
        )
        return None


def print_index_concept():
    """打印索引概念说明"""
    print("""
📊 向量索引构建流程:

┌─────────────────────────────────────────────────────────────┐
│ 1. 读取文档                                                  │
│    SimpleDirectoryReader(data_dir).load_data()              │
├─────────────────────────────────────────────────────────────┤
│ 2. 文本切片 (自动)                                           │
│    默认 chunk_size=1024, chunk_overlap=20                   │
├─────────────────────────────────────────────────────────────┤
│ 3. 向量化                                                    │
│    使用 DashScopeEmbedding (text-embedding-v2)             │
├─────────────────────────────────────────────────────────────┤
│ 4. 构建索引                                                  │
│    VectorStoreIndex.from_documents(documents)               │
├─────────────────────────────────────────────────────────────┤
│ 5. 持久化                                                    │
│    index.storage_context.persist(persist_dir)               │
└─────────────────────────────────────────────────────────────┘
""")


# ============================================================
# Step 3: 问答查询
# ============================================================
def step3_query(index=None):
    """问答查询"""
    print("\n" + "=" * 60)
    print("Step 3: 问答查询")
    print("=" * 60)

    if index is None:
        print("⚠️ 索引未构建，展示查询概念")
        print_query_concept()
        return

    # 创建查询引擎
    query_engine = index.as_query_engine(
        similarity_top_k=3,  # 检索 top 3 相关片段
    )

    # 测试查询
    test_questions = [
        "百炼平台有哪些主要功能？",
        "RAG的核心流程是什么？",
        "如何设计好的System Prompt？",
    ]

    for q in test_questions:
        print(f"\n❓ 问题: {q}")
        print("-" * 50)
        response = query_engine.query(q)
        print(f"💡 回答: {response}")


def print_query_concept():
    """打印查询概念说明"""
    print("""
📊 RAG 查询流程:

```python
# 创建查询引擎
query_engine = index.as_query_engine(
    similarity_top_k=3,       # 检索数量
    response_mode="compact",  # 响应模式
)

# 执行查询
response = query_engine.query("问题内容")

# 获取源文档
for node in response.source_nodes:
    print(node.text)       # 原文
    print(node.score)      # 相似度分数
```

📊 关键参数:

┌─────────────────────┬─────────────────────────────────────┐
│ 参数                 │ 说明                                │
├─────────────────────┼─────────────────────────────────────┤
│ similarity_top_k    │ 检索返回的文档数量                   │
│ response_mode       │ compact/refine/tree_summarize      │
│ streaming           │ 是否流式输出                        │
└─────────────────────┴─────────────────────────────────────┘
""")


# ============================================================
# Step 4: 高级优化
# ============================================================
def step4_optimization():
    """RAG 优化技术"""
    print("\n" + "=" * 60)
    print("Step 4: RAG 优化技术")
    print("=" * 60)

    print("""
📊 切片优化

```python
from llama_index.core.node_parser import SentenceSplitter

# 自定义切片
splitter = SentenceSplitter(
    chunk_size=512,    # 每个片段大小
    chunk_overlap=50,  # 重叠部分
)
nodes = splitter.get_nodes_from_documents(documents)
```

📊 句子窗口检索 (Sentence Window)

原理: 检索时匹配句子，返回时包含上下文窗口

```python
from llama_index.core.node_parser import SentenceWindowNodeParser

parser = SentenceWindowNodeParser.from_defaults(
    window_size=3,  # 上下文窗口大小
)
```

📊 混合检索 (Hybrid Search)

原理: 结合稀疏检索 (BM25) 和稠密检索 (向量)

```python
# 混合检索得分 = α × sparse + (1-α) × dense
from llama_index.core.retrievers import BM25Retriever

bm25_retriever = BM25Retriever.from_defaults(nodes=nodes)
```

📊 重排序 (Re-ranking)

原理: 对检索结果进行精排

```python
from llama_index.core.postprocessor import SentenceTransformerRerank

rerank = SentenceTransformerRerank(
    model="cross-encoder/ms-marco-MiniLM-L-6-v2",
    top_n=3,
)
query_engine = index.as_query_engine(
    node_postprocessors=[rerank]
)
```
""")


# ============================================================
# 主程序
# ============================================================
def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║     Week 3 Project 1: 企业知识库问答系统                  ║
║     阿里云大模型ACP认证备考 - 阶段二实践                  ║
╚══════════════════════════════════════════════════════════╝
""")

    print("选择运行步骤:")
    print("  1. 环境检查")
    print("  2. 准备文档")
    print("  3. 构建索引")
    print("  4. 问答查询")
    print("  5. 优化技术")
    print("  0. 完整流程")

    choice = input("\n请选择 (0-5): ").strip()

    if choice == "1":
        check_environment()
    elif choice == "2":
        step1_prepare_documents()
    elif choice == "3":
        if check_environment():
            step2_build_index()
    elif choice == "4":
        if check_environment():
            index = step2_build_index()
            step3_query(index)
    elif choice == "5":
        step4_optimization()
    elif choice == "0":
        if check_environment():
            step1_prepare_documents()
            index = step2_build_index()
            step3_query(index)
            step4_optimization()
    else:
        print("无效选择")

    print("\n" + "=" * 60)
    print("✅ Project 1 完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
