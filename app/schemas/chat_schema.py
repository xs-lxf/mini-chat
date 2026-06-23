from pydantic import BaseModel


class ChatRequest(BaseModel):
    '''聊天请求的数据模型'''
    message: str
