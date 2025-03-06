document.addEventListener("DOMContentLoaded", function () {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-btn");
    const apiUrl = window.location.origin + "/get_response";

    function appendMessage(sender, text) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        messageDiv.innerHTML = `<p>${text}</p>`;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function showTyping() {
        const typingDiv = document.createElement("div");
        typingDiv.classList.add("message", "bot");
        typingDiv.id = "typing";
        typingDiv.innerHTML = "<p>Typing...</p>";
        chatBox.appendChild(typingDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function removeTyping() {
        const typingDiv = document.getElementById("typing");
        if (typingDiv) typingDiv.remove();
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;

        appendMessage("user", message);
        userInput.value = "";
        showTyping();

        fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: message })
        })
        .then(response => response.json())
        .then(data => {
            removeTyping();
            appendMessage("bot", data.response);
        })
        .catch(error => {
            removeTyping();
            appendMessage("bot", "Error: Unable to fetch response. Try again later.");
            console.error("Error:", error);
        });
    }

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") sendMessage();
    });
});
