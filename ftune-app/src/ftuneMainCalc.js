import React from "react";
import VehicleInfo from "./ftuneVehicleInfo.js";
import MainOutputs from "./ftuneMainOutputs.js";

export default function MainCalcs() {
  return (
    <div>
      <p>Main Calcs</p>
      <div className="main-calcs">
        <VehicleInfo />
        <MainOutputs />
      </div>
    </div>
  );
}
