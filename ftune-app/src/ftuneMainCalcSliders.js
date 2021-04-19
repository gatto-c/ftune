import React, { useState } from "react";
import Slider from "rc-slider";
import "rc-slider/assets/index.css";
import Button from "@material-ui/core/Button";

export default function MainCalcSliders() {
  // eslint-disable-next-line no-unused-vars
  const [springStiffness, setSpringStiffness] = useState(0);
  const [springStiffnessFBias, setSpringStiffnessFBias] = useState(0);
  const [springStiffnessRBias, setSpringStiffnessRBias] = useState(0);

  const updateSpringStiffness = (value) => {
    setSpringStiffness(value);
    // const springValue = Math.round(((value - 50) / (100 / 2)) * 300);
  };

  const softerSprings = () => {
    if (springStiffness > -300) {
      setSpringStiffness(springStiffness - 10);
    }
  };

  const stifferSprings = () => {
    if (springStiffness < 300) {
      setSpringStiffness(springStiffness + 10);
    }
  };

  const softerSpringFrontBias = () => {
    if (springStiffnessFBias > -300) {
      setSpringStiffnessFBias(springStiffnessFBias - 10);
    }
  };

  const stifferSpringFrontBias = () => {
    if (springStiffnessFBias < 300) {
      setSpringStiffnessFBias(springStiffnessFBias + 10);
    }
  };

  const softerSpringRearBias = () => {
    if (springStiffnessRBias > -300) {
      setSpringStiffnessRBias(springStiffnessRBias - 10);
    }
  };

  const stifferSpringRearBias = () => {
    if (springStiffnessRBias < 300) {
      setSpringStiffnessRBias(springStiffnessRBias + 10);
    }
  };

  const calcSlider = function (title, value, updateFtn, decrFtn, incrFtn) {
    return (
      <div>
        {title}: {value}
        <div className="slider-container">
          <p className="label-left">Softer</p>
          <Button
            variant="contained"
            className="slider-button"
            onClick={decrFtn}
          >
            -
          </Button>
          <Slider
            className="slider"
            onChange={updateFtn}
            startPoint={0}
            min={-300}
            max={300}
            step={10}
            value={value}
          />
          <Button
            variant="contained"
            className="slider-button"
            onClick={incrFtn}
          >
            +
          </Button>
          <p className="label-right">Stiffer</p>
        </div>
      </div>
    );
  };

  const calcAdjuster = function (title, value, decrFtn, incrFtn) {
    return (
      <div>
        {title}
        <div className="slider-container">
          <Button
            variant="contained"
            className="slider-button"
            onClick={decrFtn}
          >
            -
          </Button>
          <p className="calc-adj-value">{value}</p>
          <Button
            variant="contained"
            className="slider-button"
            onClick={incrFtn}
          >
            +
          </Button>
        </div>
      </div>
    );
  };

  return (
    <div className="main-calc-sliders-container">
      {calcSlider(
        "Spring Stiffness",
        springStiffness,
        updateSpringStiffness,
        softerSprings,
        stifferSprings
      )}
      <div className="front-rear-adj">
        {calcAdjuster(
          "Front-Bias",
          springStiffnessFBias,
          softerSpringFrontBias,
          stifferSpringFrontBias
        )}
        {calcAdjuster(
          "Rear-Bias",
          springStiffnessRBias,
          softerSpringRearBias,
          stifferSpringRearBias
        )}
      </div>

      <div>Damper Stiffness</div>
      <div>Overall Balance</div>
      <div>Anti-Roll Bar</div>
    </div>
  );
}
