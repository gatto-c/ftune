import React, { createContext, useReducer } from "react";
import VehicleInfo from "./ftuneVehicleInfo.js";
import MainOutputs from "./ftuneMainOutputs.js";
import MainCalcSliders from "./ftuneMainCalcSliders.js";
// import ReducerForm from "./reducerForm.js";

export const CarDataContext = createContext();

export default function MainCalcs() {
  const dataCarInputs = {
    weight: "3800",
    front_percent: "55",
    front_arb: "20",
    rear_arb: "20",
    front_aero: "80",
    power_hp: "330",
    hp_per_ton: "0",
  };

  const carInputsReducer = (state, { type, payload }) => {
    console.log(">>cir, state:", state, ", type:", type, ", payload:", payload);
    return { ...state, [type]: payload };
  };

  const [carInputsState, carInputsDispatch] = useReducer(
    carInputsReducer,
    dataCarInputs
  );

  const carInputs = {
    state: carInputsState,
    dispatch: carInputsDispatch,
  };

  return (
    <div>
      <p>Main Calcs</p>
      <div className="main-calcs">
        <CarDataContext.Provider value={carInputs}>
          <VehicleInfo />
          <MainOutputs />
          <MainCalcSliders />
          {/* <ReducerForm /> */}
        </CarDataContext.Provider>
      </div>
    </div>
  );
}
