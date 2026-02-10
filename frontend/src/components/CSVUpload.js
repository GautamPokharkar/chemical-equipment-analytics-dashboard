import axios from "axios";
import { useState } from "react";

function CSVUpload({ onDataReceived, onUploadStart, isLoading }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file || isLoading) return;

    onUploadStart?.();

    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(
      "http://127.0.0.1:8000/api/upload/",
      formData
    );

    onDataReceived(response.data);
  };

  return (
    <div className="upload-bar">
      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
        className="file-input"
      />

      <button
        onClick={handleUpload}
        className="upload-btn"
        disabled={!file || isLoading}
      >
        {isLoading ? "Uploading..." : "Upload CSV"}
      </button>
    </div>
  );
}

export default CSVUpload;
