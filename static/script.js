document.addEventListener("DOMContentLoaded", function() {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");
    const micButton = document.getElementById("mic-button");
    const themeToggle = document.getElementById("theme-toggle");

    // Load saved theme
    if (localStorage.getItem("theme") === "light") {
        document.body.classList.add("light-theme");
    }

    // Theme Toggle Function
    themeToggle.addEventListener("click", function() {
        document.body.classList.toggle("light-theme");

        // Save theme preference
        if (document.body.classList.contains("light-theme")) {
            localStorage.setItem("theme", "light");
        } else {
            localStorage.setItem("theme", "dark");
        }
    });

    function appendMessage(message, isUser = false) {
        const messageDiv = document.createElement("div");
        messageDiv.innerHTML = message;
        messageDiv.style.padding = "10px";
        messageDiv.style.marginBottom = "10px";
        messageDiv.style.borderRadius = "5px";
        messageDiv.style.color = isUser ? "var(--accent-color)" : "var(--text-color)";
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    sendButton.addEventListener("click", function() {
        const message = userInput.value.trim();
        if (message) {
            appendMessage(`You: ${message}`, true);
            userInput.value = "";
            fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => appendMessage(`RYKA: ${data.response}`))
            .catch(error => appendMessage("Error: AI service is unavailable."));
        }
    });

    micButton.addEventListener("click", function() {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = "en-US";
        recognition.start();
        recognition.onresult = function(event) {
            const voiceText = event.results[0][0].transcript;
            userInput.value = voiceText;
        };
    });

    userInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") sendButton.click();
    });
});
