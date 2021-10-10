import React, { useState } from "react";
import ReactDOM from "react-dom";
import "./index.scss";
import burgerMenu from "../../assets/burger-menu.svg";
import cross from "../../assets/cross.svg";
import SideMenuContent from "./components/SideMenuContent";

const SideMenu = () => {
  const [isOpened, setIsOpened] = useState(false);
  const [animationNameSlide, setAnimationNameSlide] = useState("");
  const [animationNameFade, setAnimationNameFade] = useState("");

  const openSideMenu = () => {
    document.getElementsByTagName('body')[0].style.overflow = 'hidden';
    setIsOpened(true)
  };

  const closeSideMenu = () => {
    setAnimationNameSlide("slide-close");
    setAnimationNameFade("fade-out");

    setTimeout(() => {
      document.getElementsByTagName('body')[0].style.overflow = 'auto';
      setIsOpened(false);
      setAnimationNameSlide("");
      setAnimationNameFade("");
    }, 250);
  };

  return (
    <div className="sidemenu">
      <img src={burgerMenu} alt="burger menu" onClick={openSideMenu} />
      {isOpened &&
        ReactDOM.createPortal(
          <div
            className="sidemenu__overlay"
            onClick={closeSideMenu}
            style={{ animationName: animationNameFade }}
          >
            <div
              className="sidemenu__wrapper"
              onClick={(e) => e.stopPropagation()}
              style={{ animationName: animationNameSlide }}
            >
              <img
                className="sidemenu__cross"
                src={cross}
                alt="cross icon"
                onClick={closeSideMenu}
              />
              <SideMenuContent />
            </div>
          </div>,
          document.getElementById("side-menu")
        )}
    </div>
  );
};

export default SideMenu;
