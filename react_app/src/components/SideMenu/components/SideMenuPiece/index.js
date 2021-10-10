import React from 'react';
import './index.scss';

const SideMenuPiece = ({name, title}) => {
  return (
    <div className="piece">
      <span className="piece__name">{name}</span>
      <h2 className="piece__title">{title}</h2>
      <div className="piece__circle"></div>
    </div>
  );
};

export default SideMenuPiece;