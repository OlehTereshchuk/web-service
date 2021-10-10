import { Table } from "antd";
import React from "react";
import "antd/dist/antd.css";

const DataTable = ({ serverData, selectedMethod }) => {
  let dataToShow = {};

  for (let key in serverData) {
    if (typeof serverData[key] === "object") dataToShow[key] = serverData[key];
  }

  if (selectedMethod === "smoothing") {
    dataToShow = { data: dataToShow.data, smoothing: dataToShow.smoothing };
  }

  const columns = Object.keys(dataToShow).map((key) => ({
    title: key,
    dataIndex: key,
  }));
  const data = serverData.data.map((item, index) => ({
    key: index,
    ...Object.keys(dataToShow).reduce((acc, key) => {
      acc[key] = serverData[key][index];
      return acc;
    }, {}),
  }));

  return (
    <div style={{ maxHeight: 500, overflowY: "scroll" }}>
      <Table
        columns={columns}
        dataSource={data}
        size="middle"
        pagination={false}
      />
    </div>
  );
};

export default DataTable;
