import os
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

resp = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=300,
            temperature=1.0,
            system="You are a concise assistant. Answer in 2 senetences",
            messages=[{"role": "user", "content":"Explain what a token is to a Java engineer."}],)

print(resp.content[0].text)
print(resp.usage)