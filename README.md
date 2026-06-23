# Mini Chat API

基于 FastAPI + DeepSeek 的流式聊天 API 后端，支持多轮对话。

## 功能

- 流式输出（SSE）
- 多轮对话历史
- 兼容 OpenAI API 格式

## 快速开始

```bash
# 克隆并进入目录
git clone https://github.com/xs-lxf/mini-chat.git
cd mini-chat

# 创建虚拟环境并安装依赖
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 配置 API Key
cp .env.example .env
# 编辑 .env 填入 DEEPSEEK_API_KEY

# 启动服务
python3 main.py
```

服务启动后访问 http://127.0.0.1:8000/docs 查看 API 文档。

## 环境变量

| 变量名 | 说明 |
|--------|------|
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 |

## 项目结构

```
app/
├── api/           # 路由层
│   ├── chat.py
│   └── __init__.py
├── schemas/       # 数据模型
│   ├── chat_schema.py
│   └── __init__.py
├── services/      # 业务逻辑
│   ├── chat_service.py
│   └── __init__.py
└── utils/         # 工具
    ├── logger.py
    └── __init__.py
main.py            # 入口
requirements.txt   # 依赖
pyproject.toml     # 项目配置
```

## 技术栈

- **框架**: FastAPI + Uvicorn
- **AI**: DeepSeek Chat API (兼容 OpenAI SDK)
- **验证**: Pydantic v2
