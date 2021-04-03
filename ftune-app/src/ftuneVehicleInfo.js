import React from "react";

export default function VehicleInfo() {
  console.log(">>>>>Vehicle Info...");

  return (
    <div className="vehicle-inputs-container">
      <div className="input-container-title">
        <p>Vehicle Info</p>
      </div>
      <div className="input-container">
        <p className="input-label">Weight</p>
        <input type="text" className="input" id="input_weight" />
        <p className="input-metric">Lbs</p>
      </div>
      <div className="input-container">
        <p className="input-label">% Front</p>
        <input type="text" className="input" id="input_percentage_front_rear" />
        <p className="input-metric">%</p>
      </div>
      <div className="input-container">
        <p className="input-label">Front ARB</p>
        <input type="text" className="input" id="input_arb_front_rear" />
      </div>
      <div className="input-container">
        <p className="input-label">Front Aero</p>
        <input type="text" className="input" id="input_front_aero" />
        <p className="input-metric">Lbs</p>
      </div>
      <div className="input-container">
        <p className="input-label">Power</p>
        <input type="text" className="input" id="input_power_hp" />
        <p className="input-metric">HP</p>
      </div>
      <div className="input-container">
        <p className="input-label">HP / Ton</p>
        <input type="text" className="input" id="power_hp_per_ton" />
      </div>
    </div>
  );
}
