from fastapi import FastAPI
from ollama import Client

app = FastAPI()
client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)

#
@app.get("/{content}")
async def root(content: str):
    response = client.chat(model='llama3.2:1b', messages=[
        {
            'role': 'user',
            'content': content,
        },
    ])
    return response.message.content
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}



# print(response.message.content)