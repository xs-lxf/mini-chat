from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.chat_schema import ChatRequest
from app.services.chat_service import chat
from app.utils.logger import logger

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/")
async def chat_endpoint(request: ChatRequest):
    stream = chat(request.message)

    def generate():
        full_response = ""
        for chunk in stream:
            if chunk:
                full_response += chunk
                yield chunk

        logger.info(f"AI 响应完成，长度: {len(full_response)} 字符")

    return StreamingResponse(generate(), media_type="text/plain")