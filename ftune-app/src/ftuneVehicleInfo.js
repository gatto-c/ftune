import React, { Component, Fragment } from "react";
import DataIOComponent from "./ftuneDataInput.js";

export default class VehicleInfo extends Component {
  render() {
    var arr = [
      {
        id: "input-container-title",
        label: "Weight",
        type: "text",
        metricLabel: "Lbs",
      },
      {
        id: "input_percentage_front_rear",
        label: "% Front",
        type: "text",
        metricLabel: "%",
      },
      {
        id: "input_arb_front_rear",
        label: "Front ARB",
        type: "text",
        metricLabel: "",
      },
      {
        id: "input_front_aero",
        label: "Front Aero",
        type: "text",
        metricLabel: "Lbs",
      },
      {
        id: "input_power_hp",
        label: "Power",
        type: "text",
        metricLabel: "HP",
      },
      {
        id: "power_hp_per_ton",
        label: "HP / Ton",
        type: "text",
        metricLabel: "",
        readOnly: true,
      },
    ];

    return (
      <div className="vehicle-inputs-container">
        <div className="input-container-title">
          <p>Vehicle Info</p>
        </div>

        {arr.map((el, idx) => (
          <Fragment key={idx}>
            <DataIOComponent
              id={el.id}
              label={el.label}
              type={el.type}
              metricLabel={el.metricLabel}
              readOnly={el.readOnly}
            />
          </Fragment>
        ))}
      </div>
    );
  }
}
