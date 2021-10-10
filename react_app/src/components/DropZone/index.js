import React, { useRef } from "react";
import "./index.scss";
import { FileDrop } from "react-file-drop";
import dropImage from "../../assets/drop-file.svg";
import searchImage from "../../assets/search.svg";
import fileImage from "../../assets/file.svg";
import cn from "classnames";

const DropZone = ({ setFile, file }) => {
  const fileInputRef = useRef(null);

  const onFileInputChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    setFile(file);
  };

  const onTargetClick = () => {
    fileInputRef.current.click();
  };

  return (
    <FileDrop
      // onFrameDragEnter={(event) => console.log("onFrameDragEnter", event)}
      // onFrameDragLeave={(event) => console.log("onFrameDragLeave", event)}
      // onFrameDrop={(event) => console.log("onFrameDrop", event)}
      // onDragOver={(event) => console.log("onDragOver", event)}
      // onDragLeave={(event) => console.log("onDragLeave", event)}
      onDrop={(files, event) => setFile(files[0])}
      className={cn("file-drop", {
        "file-drop__selected": file,
      })}
    >
      {file ? (
        <>
          <img className="file-drop__image" src={fileImage} alt="drop" />
          <span className="file-drop__text">{file.name}</span>
        </>
      ) : (
        <>
          <img className="file-drop__image" src={dropImage} alt="drop" />
          <span className="file-drop__text">Перетягніть файл</span>
        </>
      )}
      <div
        className={cn("file-drop__button", {
          "file-drop__button--selected": file,
        })}
        onClick={onTargetClick}
      >
        {!file && <img src={searchImage} alt="search" />}
        {file ? "Обрати інший файл" : "Обрати файл"}
        <input
          onChange={onFileInputChange}
          ref={fileInputRef}
          type="file"
          accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
          className="file-drop__hidden"
        />
      </div>
    </FileDrop>
  );
};

export default DropZone;
