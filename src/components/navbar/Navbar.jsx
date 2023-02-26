import React from "react";
import "./navbar.css";

const Navbar = () => {
  return (
    <div className="n_wrapper">
      <div className="n_left">
        <div className="n_name">SoilStation</div>
        <span>toggle</span>
      </div>
      <div className="n_right">
        <div className="n_list">
          <ul style={{ listStyleType: "none" }}>
            <li>Home</li>
            <li>Soil</li>
            <li>About</li>
            <li>Contact</li>
          </ul>
        </div>
        <button className="button n_button">Sing Up</button>
      </div>
    </div>
  );
};

export default Navbar;
