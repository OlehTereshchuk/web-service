import React from 'react';
import './index.scss';
import SideMenuPiece from '../SideMenuPiece';

const SideMenuContent = () => {
  return (
    <div className="sidemenucontent">
      <SideMenuPiece name="Метод 1" title="Назва методу" />
      <SideMenuPiece name="Метод 2" title="Назва методу" />
      <SideMenuPiece name="Метод 3" title="Назва методу" />
      <SideMenuPiece name="Метод 4" title="Назва методу" />
    </div>
  );
};

export default SideMenuContent;