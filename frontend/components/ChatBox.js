import { useState, useRef, useEffect } from "react"; 
import axios from "axios";
import styles from "./ChatBox.module.css";

export default function ChatBox() {
  const [username, setUsername] = useState("");
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [joined, setJoined] = useState(false);

  const chatEndRef = useRef(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages]);

  const handleSend = async () => {
    if (!message) return;

    setMessages([...messages, { sender: username, text: message }]);
    const userMessage = message;
    setMessage("");

    try {
      const res = await axios.post("http://localhost:8000/message", {
        username,
        message: userMessage
      });
      setMessages(prev => [...prev, { sender: "AI", text: res.data.reply }]);
    } catch (err) {
      setMessages(prev => [...prev, { sender: "AI", text: "Error generating reply" }]);
      console.error(err);
    }
  };

  return (
    <div className={styles.pageWrapper}>
      {/* Project Title & Description */}
      <h1 className={styles.projectTitle}>
        AI Chat Agent with LiveKit API and Memory-Enhanced Contextual Conversations
      </h1>


      {/* Join Chat Section */}
      {!joined ? (
        <div className={styles.joinContainer}>
          <input
            type="text"
            placeholder="Enter username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <button onClick={() => setJoined(true)}>Join Chat</button>
        </div>
      ) : (
        /* Chat Container */
        <div className={styles.chatContainer}>
          <div className={styles.chatBox}>
            {messages.length === 0 ? (
              <div className={styles.welcome}>
                <h2>Welcome to AI Chat Agent!</h2>
                <p>Start the conversation by typing a message below.</p>
              </div>
            ) : (
              messages.map((m, i) => (
                <div
                  key={i}
                  className={`${styles.message} ${m.sender === "AI" ? styles.aiMessage : styles.userMessage}`}
                >
                  <img
                    src={m.sender === "AI" ? "/ai-icon.jpg" : "/user-icon.png"}
                    alt={m.sender}
                    className={styles.avatar}
                  />
                  <div className={styles.messageText}>{m.text}</div>
                </div>
              ))
            )}
            <div ref={chatEndRef} />
          </div>
          <div className={styles.inputContainer}>
            <input
              type="text"
              placeholder="Type a message..."
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleSend()}
            />
            <button onClick={handleSend}>Send</button>
          </div>
        </div>
      )}
    </div>
  );
}
