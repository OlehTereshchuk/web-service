import React, { useState } from "react";
import "./index.scss";
import mainImage from "../../assets/main-image.svg";
import DropZone from "../../components/DropZone";
import Result from "../../components/Result";
import Table from "../../components/Table";
import axios from "axios";
import { notification } from "antd";
import { ExclamationCircleOutlined } from "@ant-design/icons";

const options = [
  {
    id: "linear",
    name: "Лінійний",
    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam amet gravida amet tortor eget mauris.",
  },
  {
    id: "logarithmic",
    name: "Логарифмічний",
    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam amet gravida amet tortor eget mauris.",
  },
  {
    id: "hyperbolic",
    name: "Гіперболічний",
    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam amet gravida amet tortor eget mauris.",
  },
  {
    id: "smoothing",
    name: "Експоненційне згладжування",
    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam amet gravida amet tortor eget mauris.",
  },
  {
    id: "without-three-smoothing",
    name: "Згладжування методом ковзного середнього без ваг за трьома точками",
    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam amet gravida amet tortor eget mauris.",
  },
  {
    id: "without-five-smoothing",
    name: "Згладжування методом ковзного середнього без ваг за п'ятьма точками",
    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam amet gravida amet tortor eget mauris.",
  },
  {
    id: "with-three-smoothing",
    name: "Згладжування методом ковзного середнього з вагами за трьома точками",
    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam amet gravida amet tortor eget mauris.",
  },
  {
    id: "with-five-smoothing",
    name: "Згладжування методом ковзного середнього з вагами за п'ятьма точками",
    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam amet gravida amet tortor eget mauris.",
  },
];

const HomePage = () => {
  const [activeMethod, setActiveMethod] = useState("linear");
  const [serverData, setServerData] = useState(null);
  const [file, setFile] = useState(null);
  const [selectedMethod, setSelectedMethod] = useState("linear");

  const handleRadioCheck = (e) => {
    setActiveMethod(e.target.id);
  };

  const openNotification = () => {
    notification.open({
      message: "Будь ласка оберіть інший файл",
      description:
        "Потрібно вивантажити числовий ряд у форматі .xls",
      icon: <ExclamationCircleOutlined style={{ color: "red" }} />,
    });
  };

  const handleSelectMethod = () => {
    const fileData = new FormData();
    fileData.append("file", file);
    axios
      .post(`http://127.0.0.1:8000/api/${activeMethod}/`, fileData)
      .then((response) => {
        if (response.data.error) return openNotification();
        return response.data;
      })
      .then((data) => {
        setSelectedMethod(activeMethod);
        setServerData(data);
      })
      .catch((error) => console.log(error.message));
  };

  return (
    <div className="homepage">
      <div className="homepage__main">
        <img className="homepage__main-image" src={mainImage} alt="main" />
        <div className="homepage__title-wrapper">
          <h1 className="homepage__title">
            Веб-сервіс для прогнозування на основі вхідних даних
          </h1>
          <p className="homepage__text">
            Простий і загальнодоступний сервіс для аналізу будь-яких даних за
            лічені секунди
          </p>
        </div>
      </div>
      <div className="homepage__main" style={{ padding: "0 100px 0 37px" }}>
        <DropZone setFile={setFile} file={file} />
        <div className="homepage__options">
          <span>Оберіть метод:</span>
          {options.map((option) => (
            <div key={option.id} className="homepage__option">
              <input
                type="radio"
                name="method"
                id={option.id}
                checked={activeMethod === option.id}
                onChange={handleRadioCheck}
              />
              <label htmlFor={option.id}>{option.name}</label>
              {/* <p>{option.text}</p> */}
            </div>
          ))}
          <div className="homepage__button" onClick={handleSelectMethod}>
            Розпочати
          </div>
        </div>
      </div>
      {serverData && (
        <>
          <h1 className="homepage__title">Результати</h1>
          <Result serverData={serverData} selectedMethod={selectedMethod} />
          <Table serverData={serverData} selectedMethod={selectedMethod} />
        </>
      )}
    </div>
  );
};

export default HomePage;
