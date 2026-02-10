import { useState } from "react";
import CSVUpload from "./components/CSVUpload";
import Summary from "./components/Summary";
import Charts from "./components/Chart";
import "./App.css";

function App() {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleDataReceived = (receivedData) => {
    setData(receivedData);
    setIsLoading(false);
  };

  const handleUploadStart = () => {
    setIsLoading(true);
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="header-content">
          {/* ✅ UPDATED PROJECT NAME */}
          <h1>Chemical Equipment Analytics Dashboard</h1>
          <p className="subtitle">
            Upload and analyze equipment performance data
          </p>
        </div>
      </header>

      <main className="main-content">
        <div className="upload-section">
          <CSVUpload
            onDataReceived={handleDataReceived}
            onUploadStart={handleUploadStart}
            isLoading={isLoading}
          />
        </div>

        {isLoading && (
          <div className="loading-container">
            <div className="spinner"></div>
            <p>Processing your data...</p>
          </div>
        )}

        {data && !isLoading && (
          <div className="data-container">
            <div className="summary-section">
              <Summary data={data} />
            </div>
            <div className="chart-section">
              <Charts data={data} />
            </div>
          </div>
        )}

        {!data && !isLoading && (
          <div className="empty-state">
            <svg
              width="120"
              height="120"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
            >
              <path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <h3>No Data Yet</h3>
            <p>
              Upload a CSV file to get started with your equipment analysis
            </p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
