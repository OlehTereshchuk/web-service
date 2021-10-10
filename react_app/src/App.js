import React from "react";
import { HashRouter } from "react-router-dom";
import { useRoutes } from "./router";
import SideMenu from "./components/SideMenu";

const App = () => {
  const routes = useRoutes();

  return (
    <HashRouter>
      <div className="container">
        {/* <SideMenu /> */}
        {routes}
      </div>
    </HashRouter>
  );
};

export default App;
