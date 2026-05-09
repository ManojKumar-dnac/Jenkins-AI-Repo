from openai import OpenAI

client = OpenAI()

with open("app.log", "r") as file:
    logs = file.read()

prompt = f"""
You are a DevOps assistant.

Analyze this Jenkins/application log and give:
1. Root cause
2. Possible fix
3. Confidence level

Logs:
{logs}
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)
