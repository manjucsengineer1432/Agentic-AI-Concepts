from google import genai
client=genai.Client()
response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents=input("Ask anything ?\n")
)
print(response.text)
print()
print("Usage ")
print(response.usage_metadata)