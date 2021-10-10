import React from "react";
import "./index.scss";
import Chart from "react-apexcharts";

const Result = ({ serverData, selectedMethod }) => {
  const series = [
    {
      name: "user data",
      data: serverData.data,
    },
    {
      name: selectedMethod,
      data: serverData[selectedMethod] || serverData.result,
    },
  ];

  const options = {
    chart: {
      type: "line",
      height: 350,
      zoom: {
        enabled: false,
      },
    },
    dropShadow: {
      enabled: true,
      color: "#000",
      top: 18,
      left: 7,
      blur: 10,
      opacity: 0.2,
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      width: [0, 5],
      curve: "straight",
    },
    grid: {
      row: {
        colors: ["#f3f3f3", "transparent"],
        opacity: 0.5,
      },
    },
    xaxis: {
      labels: {
        show: false,
      },
    },
    yaxis: {
      decimalsInFloat: 2,
    },
    markers: {
      size: [7, 0],
    },
  };

  return (
    <div style={{ marginBottom: 35 }}>
      <Chart options={options} series={series} height={350} />
      {serverData?.prediction && serverData?.correlation && (
        <div className="result__wrapper">
          <span className="result__values">
            Передбачення: {serverData.prediction}
          </span>

          <span className="result__values">
            Кореляція: {serverData.correlation}
          </span>
        </div>
      )}
    </div>
  );
};

export default Result;
