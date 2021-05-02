/* eslint-disable */

import React, { Fragment } from "react";
import DataOutputPairComponent from "./ftuneDataOutputPairs.js";
import { CarDataContext } from "./ftuneMainCalc.js";

export default function MainOutputs() {
  const vehicleOutputsDataContext = React.useContext(CarDataContext);
  const state = vehicleOutputsDataContext.carOutputs.state;
  const dispatch = vehicleOutputsDataContext.carOutputs.dispatch;

  console.log(">>>>>state:", state);

  var arr = [
    {
      title: "Camber (degrees)",
      id1: "output-front-camber",
      label1: "Front",
      value1: state.front_camber_results,
      metricLabel1: "",

      id2: "output-front-camber-ft",
      value2: state.front_camber_fine_tune_results,
      metricLabel2: "",

      id3: "output-rear-camber",
      label3: "Rear",
      value3: state.rear_camber_results,

      metricLabel3: "",
      id4: "output-rear-camber-ft",
      value4: state.rear_camber_fine_tune_results,
      metricLabel4: "",
    },
    {
      title: "Toe (degrees)",
      id1: "output-front-toe",
      label1: "Front",
      value1: state.front_toe_results,
      metricLabel1: "",

      id2: "output-front-toe-ft",
      value2: state.front_toe_fine_tune_results,
      metricLabel2: "",

      id3: "output-rear-toe",
      label3: "Rear",
      value3: state.rear_toe_results,
      metricLabel3: "",

      id4: "output-rear-toe-ft",
      value4: state.rear_toe_fine_tune_results,
      metricLabel4: "",
    },
    {
      title: "Anti-Roll Bar (lbs)",
      id1: "output-front-arb",
      label1: "Front",
      value1: state.front_arb_results,
      metricLabel1: "",

      id2: "output-front-arb-ft",
      value2: state.front_arb_fine_tune_results,
      metricLabel2: "",

      id3: "output-rear-arb",
      label3: "Rear",
      value3: state.rear_arb_results,
      metricLabel3: "",

      id4: "output-rear-arb-ft",
      value4: state.rear_arb_fine_tune_results,
      metricLabel4: "",
    },
    {
      title: "Springs (lbs / inch)",
      id1: "output-front-springs",
      label1: "Front",
      value1: state.front_springs_results,
      metricLabel1: "",

      id2: "output-front-springs-ft",
      value2: state.front_springs_fine_tune_results,
      metricLabel2: "",

      id3: "output-rear-springs",
      label3: "Rear",
      value3: state.rear_springs_results,
      metricLabel3: "",

      id4: "output-rear-springs-ft",
      value4: state.rear_springs_fine_tune_results,
      metricLabel4: "",
    },
    {
      title: "Rebound",
      id1: "output-front-rebound",
      label1: "Front",
      value1: state.front_rebound_results,
      metricLabel1: "",

      id2: "output-front-rebound-ft",
      value2: state.front_rebound_fine_tune_results,
      metricLabel2: "",

      id3: "output-rear-rebound",
      label3: "Rear",
      value3: state.rear_rebound_results,
      metricLabel3: "",

      id4: "output-rear-rebound-ft",
      value4: state.rear_rebound_fine_tune_results,
      metricLabel4: "",
    },
    {
      title: "Bump",
      id1: "output-front-bump",
      label1: "Front",
      value1: state.front_bump_results,
      metricLabel1: "",

      id2: "output-front-bump-ft",
      value2: state.front_bump_fine_tune_results,
      metricLabel2: "",

      id3: "output-rear-bump",
      label3: "Rear",
      value3: state.rear_bump_results,
      metricLabel3: "",

      id4: "output-rear-bump-ft",
      value4: state.rear_bump_fine_tune_results,
      metricLabel4: "",
    },
    {
      title: "Aero (lbs)",
      id1: "output-front-aero",
      label1: "Front",
      value1: state.front_aero_results,
      metricLabel1: "",

      id2: "output-front-aero-ft",
      value2: state.front_aero_fine_tune_results,
      metricLabel2: "",

      id3: "output-rear-aero",
      label3: "Rear",
      value3: state.rear_aero_fine_tune_results,
      metricLabel3: "",

      id4: "output-rear-aero-ft",
      value4: state.rear_aero_fine_tune_results,
      metricLabel4: "",
    },
    {
      title: "Caster (degrees)",
      id1: "output-front-caster",
      label1: "Front",
      value1: state.front_caster_results,
      metricLabel1: "",

      id2: "output-front-caster-ft",
      value2: state.front_caster_fine_tune_results,
      metricLabel2: "",

      showSecondPair: false,
    },
  ];

  return (
    <div className="output-pairs-container">
      {arr.map((el, idx) => (
        <Fragment key={idx}>
          <DataOutputPairComponent
            title={el.title}
            id1={el.id1}
            label1={el.label1}
            value1={el.value1}
            metricLabel1={el.metricLabel1}
            id2={el.id2}
            value2={el.value2}
            metricLabel2={el.metricLabel2}
            id3={el.id3}
            label3={el.label3}
            value3={el.value3}
            metricLabel3={el.metricLabel3}
            id4={el.id4}
            value4={el.value4}
            metricLabel4={el.metricLabel4}
            showSecondPair={el.showSecondPair}
          />
        </Fragment>
      ))}
    </div>
  );
}
