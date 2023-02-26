// import React, { useContext } from "react";
// import "./Intro.css";
// import Vector1 from "../../img/Vector1.png";
// import Vector2 from "../../img/Vector2.png";
// import boy from "../../img/boy.png";
// import glassesimoji from "../../img/glassesimoji.png";
// import thumbup from "../../img/thumbup.png";
// import crown from "../../img/crown.png";
// import FloatinDiv from "../FloatingDiv/FloatingDiv";
// import Github from "../../img/github.png";
// import LinkedIn from "../../img/linkedin.png";
// import Instagram from "../../img/instagram.png";
// import { themeContext } from "../../Context";
// import { motion } from "framer-motion";
// import { Link } from "react-scroll";
import Image_01 from "../../Images/Image_01.jpg";
import React from "react";
import "./intro.css";
const Intro = () => {
  // Transition
  //   const transition = { duration: 2, type: "spring" };

  // context
  //   const theme = useContext(themeContext);
  //   const darkMode = theme.state.darkMode;

  return (
    <div className="Intro" id="Intro">
      {/* left name side */}
      <div className="i_left">
        <div className="i_name">
          {/* yahan change hy darkmode ka */}
          <span>Soil</span>
          <span>What is soil?</span>
          <span>
            Soil is the loose surface material that covers most land. It
            consists of inorganic particles and organic matter. Soil provides
            the structural support to plants used in agriculture and is also
            their source of water and nutrients.
          </span>
        </div>
        <button className="button i_button">Hire me </button>
      </div>
      <div className="i_right">
        <img src={Image_01} alt="" width={650} height={440} />
      </div>
    </div>
  );
};

export default Intro;
