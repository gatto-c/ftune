import React, { useState } from "react";
import Slider from "rc-slider";
import "rc-slider/assets/index.css";

export default function MainCalcSliders() {
  // eslint-disable-next-line no-unused-vars
  const [springStiffnessSlider, setSpringStiffnessSlider] = useState(50);
  const [springStiffness, setSpringStiffness] = useState(0);

  const updateSpringStiffnessSlider = (value) => {
    setSpringStiffnessSlider(value);
    const springValue = Math.round(((value - 50) / (100 / 2)) * 300);
    setSpringStiffness(springValue);
  };

  return (
    <div className="main-calc-sliders-container">
      <div>
        Spring Stiffness: {springStiffness}
        <div className="slider-container">
          <p>Softer</p>
          <Slider
            className="slider"
            onChange={updateSpringStiffnessSlider}
            startPoint={50}
            value={springStiffnessSlider}
          />
          <p>Stiffer</p>
        </div>
      </div>

      <div>Damper Stiffness</div>
      <div>Overall Balance</div>
      <div>Anti-Roll Bar</div>
    </div>
  );
}
