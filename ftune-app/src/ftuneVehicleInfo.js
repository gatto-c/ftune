/* eslint-disable */

import React, { Component, Fragment } from "react";
import DataIOComponent from "./ftuneDataInput.js";
import { CarDataContext } from "./ftuneMainCalc.js";

export default function VehicleInfo() {
  const vehicleInputsDataContext = React.useContext(CarDataContext);
  const state = vehicleInputsDataContext.state;
  const dispatch = vehicleInputsDataContext.dispatch;

  var arr = [
    {
      id: "input_container_weight",
      label: "Weight",
      type: "number",
      inputValue: state.weight,
      metricLabel: "Lbs",
      handleChange: (event) =>
        dispatch({ type: "weight", payload: event.target.value }),
    },
    {
      id: "input_percentage_front_rear",
      label: "% Front",
      type: "number",
      inputValue: state.front_percent,
      metricLabel: "%",
      handleChange: (event) =>
        dispatch({ type: "front_percent", payload: event.target.value }),
    },
    {
      id: "input_arb_front_rear",
      label: "Front ARB",
      type: "number",
      inputValue: state.front_arb,
      metricLabel: "",
      handleChange: (event) =>
        dispatch({ type: "front_arb", payload: event.target.value }),
    },
    {
      id: "input_front_aero",
      label: "Front Aero",
      type: "number",
      inputValue: state.front_aero,
      metricLabel: "Lbs",
      handleChange: (event) =>
        dispatch({ type: "front_aero", payload: event.target.value }),
    },
    {
      id: "input_power_hp",
      label: "Power",
      type: "number",
      inputValue: state.power_hp,
      metricLabel: "HP",
      handleChange: (event) =>
        dispatch({ type: "power_hp", payload: event.target.value }),
    },
    {
      id: "power_hp_per_ton",
      label: "HP / Ton",
      type: "number",
      inputValue: state.hp_per_ton,
      metricLabel: "",
      readOnly: true,
      handleChange: (event) =>
        dispatch({ type: "hp_per_ton", payload: event.target.value }),
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
            inputValue={el.inputValue}
            metricLabel={el.metricLabel}
            readOnly={el.readOnly}
            handleChange={el.handleChange}
          />
        </Fragment>
      ))}
    </div>
  );
}
