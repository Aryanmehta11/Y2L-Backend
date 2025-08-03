import os 
from dotenv import load_dotenv
load_dotenv()
from google import genai

# Initialize the Gemini AI client with the API key from environment variables
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# def generate_linkedin_post(transcript: str) -> str:
#     try:
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=f"Generate a Linkedin Post for this transcript: {transcript}"
#         )
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"
    

def generate_linkedin_post(transcript: str) -> dict:
    try:
        prompt = (
            "You're a professional LinkedIn content strategist.\n"
            "Given the transcript below, your job is to:\n"
            "1. Extract the core ideas as 3–5 concise bullet points for professionals.\n"
            "2. Write a well-crafted LinkedIn post based on the transcript that:\n"
            "- Starts with a strong hook\n"
            "- Is insightful, motivating, and easy to read\n"
            "- Uses short paragraphs and light emoji (if helpful)\n"
            "- Ends with a call to action\n"
            "Avoid casual/slang. Keep it clean and professional.\n\n"
            f"Transcript:\n{transcript}\n\n"
            "Return output in the following format:\n"
            "Bullet Points:\n- Point 1\n- Point 2\n...\n\n"
            "LinkedIn Post:\n<your post here>"
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        output = response.text.strip()

        # Optional: Split output into parts
        bullet_points = ""
        post_text = ""
        if "LinkedIn Post:" in output:
            parts = output.split("LinkedIn Post:")
            bullet_points = parts[0].replace("Bullet Points:", "").strip()
            post_text = parts[1].strip()
        else:
            post_text = output  # fallback if formatting is different

        return {
            "bullet_points": bullet_points,
            "linkedin_post": post_text
        }

    except Exception as e:
        return {
            "bullet_points": "",
            "linkedin_post": f"Error: {str(e)}"
        }


# Example usage of the Gemini AI client
# Uncomment the following lines to test the Gemini AI client directly
# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )
# print(response.text)