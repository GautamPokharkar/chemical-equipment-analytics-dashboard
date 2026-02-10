import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

function Charts({ data }) {
  if (!data) return null;

  const colors = [
    "#FF6384",
    "#36A2EB",
    "#FFCE56",
    "#4BC0C0",
    "#9966FF",
    "#FF9F40",
  ];
  const chartData = {
    labels: Object.keys(data.type_distribution),
    datasets: [
      {
        data: Object.values(data.type_distribution),
        backgroundColor: colors,
        borderColor: "#ffffff",
        borderWidth: 2,
      },
    ],
  };
  const options = {
    responsive: true,
    maintainAspectRatio: false, 
  };
  return (
    <div
      style={{
        width: "400px",
        height: "400px",
        margin: "20px auto",
      }}
    >
      <Pie data={chartData} options={options} />
    </div>
  );
}

export default Charts;
