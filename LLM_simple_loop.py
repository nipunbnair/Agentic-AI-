from openai import OpenAI
import os

# Initialize OpenAI client (uses OPENAI_API_KEY from environment)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Choose a GPT model
model_id = "gpt-4o-mini"   # fast + cheap
# model_id = "gpt-4.1"     # higher quality

while True:
    # Query to send to GPT
    query = input("👤 Enter your query (or 'quit' to exit): ")
    # Check if user wants to quit
    if query.lower() == "quit":
        print("Goodbye!")
        break

    try:
        print("🤖 System call")

        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "user", "content": query}
            ],
            max_tokens=1024
        )

        output = response.choices[0].message.content

        print(f"👤 Query: {query}")
        print(f"\nResponse:\n{output}")

    except Exception as e:
        print(f"Error calling OpenAI: {e}")



