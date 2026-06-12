import { useState } from "react";
import axios from "axios";

function App() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Hello! I'm FileMind AI. Ask me to find files, summarize PDFs, or find duplicates.",
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userInput = input;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: userInput,
      },
    ]);

    setInput("");
    setLoading(true);

    try {
      const response = await axios.post(
        "http://localhost:8000/chat",
        {
          message: userInput,
        }
      );

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: response.data.response,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Unable to connect to the FileMind backend.",
        },
      ]);
    }

    setLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  };

  return (
    <div
      style={{
        backgroundColor: "#0f172a",
        minHeight: "100vh",
        color: "white",
        display: "flex",
        justifyContent: "center",
        padding: "30px",
      }}
    >
      <div
        style={{
          width: "900px",
          display: "flex",
          flexDirection: "column",
        }}
      >
        <h1
          style={{
            textAlign: "center",
            marginBottom: "20px",
          }}
        >
          FileMind AI
        </h1>

        <div
          style={{
            flex: 1,
            height: "70vh",
            overflowY: "auto",
            border: "1px solid #334155",
            borderRadius: "10px",
            padding: "20px",
            backgroundColor: "#1e293b",
          }}
        >
          {messages.map((msg, index) => (
            <div
              key={index}
              style={{
                display: "flex",
                justifyContent:
                  msg.role === "user"
                    ? "flex-end"
                    : "flex-start",
                marginBottom: "12px",
              }}
            >
              <div
                style={{
                  maxWidth: "75%",
                  padding: "12px",
                  borderRadius: "12px",
                  backgroundColor:
                    msg.role === "user"
                      ? "#2563eb"
                      : "#475569",
                  whiteSpace: "pre-wrap",
                }}
              >
                {msg.content}
              </div>
            </div>
          ))}

          {loading && (
            <div>
              <em>Thinking...</em>
            </div>
          )}
        </div>

        <div
          style={{
            display: "flex",
            gap: "10px",
            marginTop: "15px",
          }}
        >
          <input
            value={input}
            onChange={(e) =>
              setInput(e.target.value)
            }
            onKeyDown={handleKeyDown}
            placeholder="Ask FileMind..."
            style={{
              flex: 1,
              padding: "12px",
              borderRadius: "8px",
              border: "none",
              fontSize: "16px",
            }}
          />

          <button
            onClick={sendMessage}
            style={{
              padding: "12px 24px",
              backgroundColor: "#2563eb",
              color: "white",
              border: "none",
              borderRadius: "8px",
              cursor: "pointer",
            }}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;