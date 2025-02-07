from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': 'Vai tu māki Latviešu Valodu?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)