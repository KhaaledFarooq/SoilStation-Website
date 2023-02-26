import React from "react";
import "./services.css";
import emoji_01 from "../../Images/Imoji_01.png";
import Card from "../Card/Card";
// import HeartEmoji from "../../img/heartemoji.png";
// import Glasses from "../../img/glasses.png";
// import Humble from "../../img/humble.png";
// import { themeContext } from "../../Context";
// import { motion } from "framer-motion";
// import Resume from './resume.pdf';

const Services = () => {
  return (
    <div className="services" id="services">
      <div className="awesome">
        <span>My Awesome</span>
        <span>services</span>
        <spane>
          Lorem ispum is simpley dummy text of printing of printing Lorem
          <br />
          ispum is simpley dummy text of printing
        </spane>
        <button className="button s-button">Download CV</button>
        <div className="blur s-blur1" style={{ background: "#ABF1FF94" }}></div>

        <div className="cards"></div>
      </div>
      <div className="cards">
        <div>
          <img src={emoji_01} alt="" width={50} height={40} />

          <Card emoji={emoji_01} />
          {/* emoji={emoji_01} */}
          {/* heading={"Desing"}
           detail={"Figma, Sketch, Photoshop, Adobe, Adobe xd"} */}
        </div>
      </div>
    </div>
  );
};

export default Services;
