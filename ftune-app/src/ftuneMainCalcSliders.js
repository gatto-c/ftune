import React, { useState } from "react";
import "rc-slider/assets/index.css";
import MainCalcSliderGroup from "./ftuneMainCalcSliderGroup.js";

export default function MainCalcSliders() {
  const [springStiffness, setSpringStiffness] = useState(0);
  const [springStiffnessFBias, setSpringStiffnessFBias] = useState(0);
  const [springStiffnessRBias, setSpringStiffnessRBias] = useState(0);
  const [damperStiffness, setDamperStiffness] = useState(0);
  const [damperStiffnessFBias, setDamperStiffnessFBias] = useState(0);
  const [damperStiffnessRBias, setDamperStiffnessRBias] = useState(0);
  const [dampingRatio, setDampingRatio] = useState(0);
  const [overallBalance, setOverallBalance] = useState(0);
  const [antiRollBar, setAntiRollBar] = useState(0);

  return (
    <div className="main-calc-sliders-container">
      <MainCalcSliderGroup
        title="Spring Stiffness"
        mainValue={springStiffness}
        mainValueSetter={setSpringStiffness}
        mainValueStep={10}
        mainLabelLeft="Softer"
        mainLabelRight="Stiffer"
        fbiasValue={springStiffnessFBias}
        fbiasValueSetter={setSpringStiffnessFBias}
        rbiasValue={springStiffnessRBias}
        rbiasValueSetter={setSpringStiffnessRBias}
      />

      <MainCalcSliderGroup
        title="Damper Stiffness"
        mainValue={damperStiffness}
        mainValueSetter={setDamperStiffness}
        mainValueStep={10}
        mainLabelLeft="Softer"
        mainLabelRight="Stiffer"
        fbiasValue={damperStiffnessFBias}
        fbiasValueSetter={setDamperStiffnessFBias}
        rbiasValue={damperStiffnessRBias}
        rbiasValueSetter={setDamperStiffnessRBias}
      />

      <MainCalcSliderGroup
        title="Damping"
        mainValue={dampingRatio}
        mainValueSetter={setDampingRatio}
        mainValueStep={1}
        mainLabelLeft="Bumpy"
        mainLabelRight="Smooth"
      />

      <MainCalcSliderGroup
        title="Overall Balance"
        mainValue={overallBalance}
        mainValueSetter={setOverallBalance}
        mainValueStep={1}
        mainLabelLeft="Understeer"
        mainLabelRight="Oversteer"
      />

      <MainCalcSliderGroup
        title="Anti-Roll Bar"
        mainValue={antiRollBar}
        mainValueSetter={setAntiRollBar}
        mainValueStep={1}
        mainLabelLeft="Understeer"
        mainLabelRight="Oversteer"
      />
    </div>
  );
}
