# from google import genai
# client=genai.Client()
# system_instruction=""" 
# You are a Java programming teacher.

# Rules:
# 1.Explain concepts for beginners.
# 2.Use simple language.
# 3.Give real-wolrd analogy.
# 4.Give small Java example.
# """
# user_prompt=input("Enter Anything \n")

# response=client.models.generate_content(
#     model="gemini-3.8-flash",
#     contents=user_prompt,
#     config={
#         "system_instruction":system_instruction
#     }
# )
# print("AI Response\n")
# print(response.text)


# How the model give the output based on the rules set by the system or admin

from google import genai
import time

client = genai.Client()

prompt = input("Enter Anything \n")

for attempt in range(3):

    try:

        print(f"\nAttempt {attempt + 1}...")

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config={
                "system_instruction": """
                Answer in exactly 5 Bullet points.
                You are a Java programming expert.
                Explain concepts clearly for a beginner.
                Give a small Java example.
                """
            }
        )

        print("\nAI Response:\n")
        print(response.text)

        break

    except Exception as e:

        print("\nError:", e)

        if attempt < 2:
            print("Waiting 5 seconds before trying again...")
            time.sleep(5)

        else:
            print("\nThe API is currently unavailable.")
            print("Please try again later.")