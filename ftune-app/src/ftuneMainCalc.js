import React, { createContext, useReducer } from "react";
import { dataCarInputs, dataCarOutputs } from "./ftuneDataContext.js";
import VehicleInfo from "./ftuneVehicleInfo.js";
import MainOutputs from "./ftuneMainOutputs.js";
import MainCalcSliders from "./ftuneMainCalcSliders.js";
// import ReducerForm from "./reducerForm.js";

export const CarDataContext = createContext();

export default function MainCalcs() {
  const carIOReducer = (state, { type, payload }) => {
    console.log(">>cir, state:", state, ", type:", type, ", payload:", payload);
    return { ...state, [type]: payload };
  };

  const [carInputsState, carInputsDispatch] = useReducer(
    carIOReducer,
    dataCarInputs
  );

  const carInputs = {
    state: carInputsState,
    dispatch: carInputsDispatch,
  };

  const [carOutputsState, carOutputsDispatch] = useReducer(
    carIOReducer,
    dataCarOutputs
  );

  const carOutputs = {
    state: carOutputsState,
    dispatch: carOutputsDispatch,
  };

  const mainData = {
    carInputs: carInputs,
    carOutputs: carOutputs,
  };

  return (
    <div>
      <p>Main Calcs</p>
      <div className="main-calcs">
        <CarDataContext.Provider value={mainData}>
          <VehicleInfo />
          <MainOutputs />
          <MainCalcSliders />
        </CarDataContext.Provider>
      </div>
    </div>
  );
}
