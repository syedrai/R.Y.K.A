from transformers import pipeline

class CyberAI:
    def __init__(self):
        self.chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
        self.rankings = {"Beginner": 0, "Intermediate": 10, "Advanced": 20, "Expert": 30}
        self.user_xp = {}

    def get_rank(self, username):
        xp = self.user_xp.get(username, 0)
        for rank, min_xp in reversed(self.rankings.items()):
            if xp >= min_xp:
                return rank
        return "Beginner"

    def respond(self, username, message):
        points = 5 if any(keyword in message.lower() for keyword in ["phishing", "firewall", "SIEM"]) else 1
        self.user_xp[username] = self.user_xp.get(username, 0) + points
        rank = self.get_rank(username)
        
        ai_response = self.chatbot(message, max_length=100, do_sample=True)[0]['generated_text']
        return {"rank": rank, "response": ai_response}

cyber_ai = CyberAI()
