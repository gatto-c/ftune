import React, { Component, Fragment } from "react";
import DataIOComponent from "./ftuneDataIO.js";

export default class MainOutputs extends Component {
  render() {
    var arr = [
      {
        id: "output-front-camber",
        label: "Front Camber",
        type: "text",
        metricLabel: "",
        readOnly: true,
      },
      {
        id: "output-front-camber-after",
        label: "after fine-tuning",
        type: "text",
        metricLabel: "",
        readOnly: true,
      },
      {
        id: "output-rear-camber",
        label: "Rear Camber",
        type: "text",
        metricLabel: "",
        readOnly: true,
      },
      {
        id: "output-rear-camber-after",
        label: "after fine-tuning",
        type: "text",
        metricLabel: "",
        readOnly: true,
      },
    ];

    return (
      <div className="vehicle-outputs-container">
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
