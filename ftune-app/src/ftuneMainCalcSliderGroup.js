import React from "react";
import Slider from "rc-slider";
import "rc-slider/assets/index.css";
import Button from "@material-ui/core/Button";
import PropTypes from "prop-types";

export default function MainCalcSliderGroup({
  title,
  mainValue,
  mainValueSetter,
  mainValueStep,
  mainLabelLeft,
  mainLabelRight,
  fbiasValue = null,
  fbiasValueSetter = null,
  rbiasValue = null,
  rbiasValueSetter = null,
}) {
  let showFBias = true;
  if (fbiasValue === null) {
    showFBias = false;
  }

  let showRBias = true;
  if (rbiasValue === null) {
    showRBias = false;
  }

  const softerMainValue = () => {
    if (mainValue > -300) {
      mainValueSetter(mainValue - mainValueStep);
    }
  };

  const stifferMainValue = () => {
    if (mainValue < 300) {
      mainValueSetter(mainValue + mainValueStep);
    }
  };

  const softerFBias = () => {
    if (fbiasValue > -300) {
      fbiasValueSetter(fbiasValue - mainValueStep);
    }
  };

  const stifferFBias = () => {
    if (fbiasValue < 300) {
      fbiasValueSetter(fbiasValue + mainValueStep);
    }
  };

  const softerRBias = () => {
    if (rbiasValue > -300) {
      rbiasValueSetter(rbiasValue - mainValueStep);
    }
  };

  const stifferRBias = () => {
    if (rbiasValue < 300) {
      rbiasValueSetter(rbiasValue + mainValueStep);
    }
  };

  const calcAdjuster = function (title, value, decrFtn, incrFtn) {
    return (
      <div>
        {title}
        <div className="bias-adj-container">
          <Button
            variant="contained"
            className="slider-button"
            onClick={decrFtn}
          >
            -
          </Button>
          <div className="calc-adj-value">{value}%</div>
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
    <div className="main-calc-slider-group">
      <div>
        <div className="group-title">
          <div>{title}:</div>
          <div className="main-value">{mainValue} %</div>
        </div>
        <div className="slider-container">
          <div className="label-button-left">
            <p className="label-left">{mainLabelLeft}</p>
            <Button
              variant="contained"
              className="slider-button"
              onClick={softerMainValue}
            >
              -
            </Button>
          </div>
          <Slider
            className="slider"
            onChange={mainValueSetter}
            startPoint={0}
            min={-300}
            max={300}
            step={mainValueStep}
            value={mainValue}
          />
          <div className="label-button-right">
            <Button
              variant="contained"
              className="slider-button"
              onClick={stifferMainValue}
            >
              +
            </Button>
            <p className="label-right">{mainLabelRight}</p>
          </div>
        </div>
      </div>

      <div className="front-rear-adj">
        {showFBias &&
          calcAdjuster("Front-Bias", fbiasValue, softerFBias, stifferFBias)}
        {showRBias &&
          calcAdjuster("Rear-Bias", rbiasValue, softerRBias, stifferRBias)}
      </div>
    </div>
  );
}

MainCalcSliderGroup.propTypes = {
  title: PropTypes.string.isRequired,
  mainValue: PropTypes.number.isRequired,
  mainValueSetter: PropTypes.func.isRequired,
  mainValueStep: PropTypes.number.isRequired,
  mainLabelLeft: PropTypes.string.isRequired,
  mainLabelRight: PropTypes.string.isRequired,
  fbiasValue: PropTypes.number,
  fbiasValueSetter: PropTypes.func,
  rbiasValue: PropTypes.number,
  rbiasValueSetter: PropTypes.func,
};
