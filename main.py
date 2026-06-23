from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.utils.logger import logger

# 创建 FastAPI 应用
app = FastAPI(
    title="Mini Chat API",
    description="一个支持多轮对话和流式输出的 ChatGPT 风格后端",
    version="1.0.0"
)

# 注册路由
app.include_router(chat_router)

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Mini Chat API v1 启动成功！")
    logger.info(f"📖 API 文档: http://127.0.0.1:8000/docs")

@app.get("/")
async def root():
    return {
        "message": "Mini Chat API v1",
        "docs": "/docs",
        "endpoints": {
            "POST /chat": "发送消息，流式返回"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # 开发模式自动重载
    )