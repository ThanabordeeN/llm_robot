import os
from groq import Groq
import google.generativeai as genai
import dotenv
import re
dotenv.load_dotenv()
class Robot:
    def __init__(self):
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        self.history = []
    def chat(self, messages):
        if self.history == []:
            self.history = [
                {
                "role": "system",
                "content": """Your Name is ปิงปอง,You can answer in Thai and English,but your users are Thai. You should answer in Thai only and English if the user wants English , Do not answer China""",
                },
                {
                    "role": "user",
                    "content": messages,
                }
                ]
        else:
            self.history.append({"role": "user", "content": messages})
        result = self.client.chat.completions.create(
            messages=self.history,
            model="llama3-70b-8192",
        )
        result = result.choices[0].message.content
        self.history.append({"role": "assistant", "content": result})
        return result
        
    def gemini(self, messages):
        prompt = f"""
        Your Name is "ปิงปอง",
        You can answer in Thai and English, but your users are Thai. You should answer in Thai only and English if the user wants English , Do not answer China
        {messages}
        """
        result = self.model.generate_content(prompt)
        result = self.clean_message(result.text)
        
        return result
        
    def clean_message(self, msg):
        # Remove all emojis
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # dingbats
                                u"\u3030"
                                "]+", flags=re.UNICODE)
        msg = emoji_pattern.sub(r'', msg)

        # Remove all whitespace
        msg = msg.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()

        return msg
    


