import React, { Component, Fragment } from "react";
import DataOutputPairComponent from "./ftuneDataOutputPairs.js";

export default class MainOutputs extends Component {
  render() {
    var arr = [
      {
        title: "Camber",
        id1: "output-front-camber",
        label1: "Front",
        value1: "2.0",
        metricLabel1: "",

        id2: "output-front-camber-ft",
        value2: "2.1",
        metricLabel2: "",

        id3: "output-rear-camber",
        label3: "Rear",
        value3: "3.0",

        metricLabel3: "",
        id4: "output-rear-camber-ft",
        value4: "3.1",
        metricLabel4: "",
      },
      {
        title: "Toe",
        id1: "output-front-toe",
        label1: "Front",
        value1: "2.0",
        metricLabel1: "",

        id2: "output-front-toe-ft",
        value2: "2.1",
        metricLabel2: "",

        id3: "output-rear-toe",
        label3: "Rear",
        value3: "3.0",
        metricLabel3: "",

        id4: "output-rear-toe-ft",
        value4: "3.1",
        metricLabel4: "",
      },
      {
        title: "Anti-Roll Bar",
        id1: "output-front-arb",
        label1: "Front",
        value1: "2.0",
        metricLabel1: "",

        id2: "output-front-arb-ft",
        value2: "2.1",
        metricLabel2: "",

        id3: "output-rear-arb",
        label3: "Rear",
        value3: "3.0",
        metricLabel3: "",

        id4: "output-rear-arb-ft",
        value4: "3.1",
        metricLabel4: "",
      },
      {
        title: "Springs",
        id1: "output-front-springs",
        label1: "Front",
        value1: "2.0",
        metricLabel1: "",

        id2: "output-front-springs-ft",
        value2: "2.1",
        metricLabel2: "",

        id3: "output-rear-springs",
        label3: "Rear",
        value3: "3.0",
        metricLabel3: "",

        id4: "output-rear-springs-ft",
        value4: "3.1",
        metricLabel4: "",
      },
      {
        title: "Rebound",
        id1: "output-front-rebound",
        label1: "Front",
        value1: "2.0",
        metricLabel1: "",

        id2: "output-front-rebound-ft",
        value2: "2.1",
        metricLabel2: "",

        id3: "output-rear-rebound",
        label3: "Rear",
        value3: "3.0",
        metricLabel3: "",

        id4: "output-rear-rebound-ft",
        value4: "3.1",
        metricLabel4: "",
      },
      {
        title: "Bump",
        id1: "output-front-bump",
        label1: "Front",
        value1: "2.0",
        metricLabel1: "",

        id2: "output-front-bump-ft",
        value2: "2.1",
        metricLabel2: "",

        id3: "output-rear-bump",
        label3: "Rear",
        value3: "3.0",
        metricLabel3: "",

        id4: "output-rear-bump-ft",
        value4: "3.1",
        metricLabel4: "",
      },
      {
        title: "Aero",
        id1: "output-front-aero",
        label1: "Front",
        value1: "2.0",
        metricLabel1: "",

        id2: "output-front-aero-ft",
        value2: "2.1",
        metricLabel2: "",

        id3: "output-rear-aero",
        label3: "Rear",
        value3: "3.0",
        metricLabel3: "",

        id4: "output-rear-aero-ft",
        value4: "3.1",
        metricLabel4: "",
      },
      {
        title: "Caster",
        id1: "output-front-caster",
        label1: "Front",
        value1: "2.0",
        metricLabel1: "",

        id2: "output-front-caster-ft",
        value2: "2.1",
        metricLabel2: "",

        showSecondPair: false,
      },
    ];

    return (
      <div className="vehicle-output-pairs-container">
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
}
