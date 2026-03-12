from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)   
'''
response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)
'''
response = client.chat.completions.create(
  model="gpt-4o",
  temperature=1.0,
  messages=[
    {"role": "system", "content": "you are a helpful assistant"},
    {"role": "user", "content": "2022월드컵 우승팀은 어디인가?"},
    {'role': "assistant", "content": "2022년 FIFA 월드컵 우승팀은 아르헨티나입니다."},
  ]
)

print(response.choices[0].message.content)