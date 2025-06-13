from openai import AsyncOpenAI
import chainlit as cl
from agents import Agent,Runner
from dotenv import load_dotenv


load_dotenv()
#-------------------------------------------------------------------------------
client = AsyncOpenAI()

# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "gpt-4.1-mini",
    "temperature": 0,
    # ... more settings
}

@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot, you always reply in enghlish.",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()