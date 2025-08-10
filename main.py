from fastapi import FastAPI
from ollama import Client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
)

@app.get("/{content}")
async def root(content: str):
    response = client.chat(model='llama3.2:1b', messages=[
        {
            'role': 'user',
            'content': content,
        },
    ])
    return {"message": response.message.content}
