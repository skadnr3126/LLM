from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key= api_key)
pass_messages = [{'role': 'system', 'content' : 'you are a helpful assistent'}]
while True :
    user_input = input("사용자 ")
    pass_messages.append({'role': 'user' , 'content' : user_input})
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.2,
        messages= pass_messages
    )
    ai_response = response.choices[0].message.content
    pass_messages.append({'role':'assistant' ,'content':ai_response })
    print("AI:" + ai_response)



