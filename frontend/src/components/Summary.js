function Summary({ data }) {
  if (!data) return null;

  const boxStyle = {
    border: "1px solid #ddd",
    borderRadius: "6px",
    padding: "10px 14px",
    marginBottom: "10px",
    backgroundColor: "#fafafa",
  };

  const downloadPDF = () => {
    window.open("http://127.0.0.1:8000/api/report/", "_blank");
  };

  return (
    <div style={{ maxWidth: "400px", marginTop: "20px" }}>
      <h3 style={{ marginBottom: "12px" }}>Summary</h3>

      <div style={boxStyle}>
        <strong>Total Equipment</strong>
        <div>{data.total}</div>
      </div>

      <div style={boxStyle}>
        <strong>Average Flowrate</strong>
        <div>{data.avg_flowrate.toFixed(2)}</div>
      </div>

      <div style={boxStyle}>
        <strong>Average Pressure</strong>
        <div>{data.avg_pressure.toFixed(2)}</div>
      </div>

      <div style={boxStyle}>
        <strong>Average Temperature</strong>
        <div>{data.avg_temperature.toFixed(2)}</div>
      </div>

      <button
        onClick={downloadPDF}
        style={{
          marginTop: "10px",
          padding: "8px 14px",
          cursor: "pointer",
        }}
      >
        Download PDF Report
      </button>
    </div>
  );
}

export default Summary;
