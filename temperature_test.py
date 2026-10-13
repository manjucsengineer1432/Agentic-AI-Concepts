from google import genai

client = genai.Client()

# prompt = "Give me a creative name for an AI startup."
# prompt="Create a short story about a robot learning to cook."

# temperatures = [0.0, 0.2, 0.7, 1.0, 1.5]

# for temperature in temperatures:
prompt=input("Ask anything \n")
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "system_instruction": """
        Answer in exactly 5 Bullet points.
        "temperature": 1.5
        """
    }
)

print("=" * 50)
# print(f"Temperature: {temperature}")
print("Response:")
print(response.text)