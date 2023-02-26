import React from "react";
import "./footer.css";
import Linkedin from "../../Images/linkedin.png";
import Facebook from "../../Images/facebook.png";
import Github from "../../Images/github.png";
import Instagram from "../../Images/instagram.png";

const Footer = () => {
  const year = new Date().getFullYear();

  return (
    <footer>
      <div className="container">
        <div className="cotent_footer">
          <div className="profil">
            <div className="logo_area">
              <span className="logo_name">SoilStation</span>
            </div>
            <div className="decsc_area">
              <p>
                Soil is the loose surface material that covers most land. It
                consists of inorganic particles and organic matter. Soil
                provides the structural support to plants used in agriculture
                and is also their source of water and nutrients.
              </p>
            </div>
            <div className="social_media">
              <img src={Linkedin} alt="" />
              <img src={Facebook} alt="" />
              <img src={Github} alt="" />
              <img src={Instagram} alt="" />
            </div>
            <div className="n_list">
              <ul style={{ listStyleType: "none" }}>
                <li>Home</li>
                <li>Soil</li>
                <li>About</li>
                <li>Contact</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <hr />
      {`Copyright © Upbeat Code ${year}`}
    </footer>
  );
};

export default Footer;
