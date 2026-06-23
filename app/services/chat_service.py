from collections.abc import Generator

from openai import OpenAI
from dotenv import load_dotenv
import os

from app.utils.logger import logger

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

messages = [
    {
        "role": "system",
        "content": "你是一位专业的 Python 老师，擅长用通俗易懂的方式讲解技术概念。"
    }
]


def chat(message: str) -> Generator[str, None, None]:
    logger.info(f"用户消息: {message}")

    messages.append({"role": "user", "content": message})

    stream = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=True
    )

    logger.info(f"模型: deepseek-chat, 历史消息数: {len(messages)}")

    full_content = ""
    for chunk in stream:
        delta = chunk.choices[0].delta if chunk.choices else None
        content = delta.content if delta and delta.content else ""
        full_content += content
        yield content

    messages.append({"role": "assistant", "content": full_content})
    logger.info(f"助手回复已记录, 历史消息数: {len(messages)}")


def get_messages_count() -> int:
    return len(messages)


def clear_history():
    global messages
    system_prompt = messages[0]
    messages = [system_prompt]
    logger.info("对话历史已清空")