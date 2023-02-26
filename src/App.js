import React from "react";

//import { Footer, Header } from "./containers";
//import { Brand, Navbar } from "./components";
import Navbar from "./components/navbar/Navbar";
// import Footer from "./containers/footer/Footer";
import Intro from "./components/Intro/Intro";
import Footer from "./containers/footer/Footer";
import Services from "./components/Services/Services";
import "./App.css";

export const App = () => {
  return (
    <div className="App">
      <Navbar />
      <Intro />
      <Services />
      <Footer />
    </div>
  );
};
export default App;
