import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import ChatBox from "./components/ChatBox";

export default function App() {
  const [fileUploaded, setFileUploaded] = useState(false);

  return (
    <div className="container">
      <h1>📚 Doc Ask App</h1>
      {!fileUploaded ? (
        <FileUpload onUpload={() => setFileUploaded(true)} />
      ) : (
        <ChatBox />
      )}
    </div>
  );
}

    