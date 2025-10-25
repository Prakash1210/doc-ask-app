import React, { useState } from "react";
import axios from "axios";

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");

  const sendMessage = async () => {
    if (!question.trim()) return;
    const newMsg = { sender: "user", text: question };
    setMessages((prev) => [...prev, newMsg]);
    setQuestion("");

    const res = await axios.post("/api/chat", { query: newMsg.text });
    setMessages((prev) => [...prev, { sender: "bot", text: res.data.answer }]);
  };

  return (
    <div>
      <div style={{ height: "300px", overflowY: "auto", margin: "1rem 0", padding: "1rem", background: "#fff", borderRadius: "8px" }}>
        {messages.map((msg, idx) => (
          <p key={idx} style={{ textAlign: msg.sender === "user" ? "right" : "left" }}>
            <strong>{msg.sender === "user" ? "You" : "DocBot"}:</strong> {msg.text}
          </p>
        ))}
      </div>
      <input
        type="text"
        placeholder="Ask your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={{ width: "70%", padding: "0.5rem" }}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}
