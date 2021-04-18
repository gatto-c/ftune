import React from "react";
import VehicleInfo from "./ftuneVehicleInfo.js";
import MainOutputs from "./ftuneMainOutputs.js";
import MainCalcSliders from "./ftuneMainCalcSliders.js";

export default function MainCalcs() {
  return (
    <div>
      <p>Main Calcs</p>
      <div className="main-calcs">
        <VehicleInfo />
        <MainOutputs />
        <MainCalcSliders />
      </div>
    </div>
  );
}
