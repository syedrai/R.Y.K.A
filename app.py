from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
API_KEY = "your_api_key"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"response": "Please enter a message."})

    try:
        # Generate AI response
        response = model.generate_content(user_message)
        
        # Format response with lines and spaces
        formatted_response = f"<hr><br>{response.text.replace('. ', '.<br><br>')}<br><hr>"

        return jsonify({"response": formatted_response})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
