/* eslint-disable no-constant-condition */
import React from "react";
import PropTypes from "prop-types";

export default function DataOutputPairComponent({
  title,
  id1,
  label1,
  value1,
  metricLabel1,
  id2,
  value2,
  metricLabel2,
  id3,
  label3,
  value3,
  metricLabel3,
  id4,
  value4,
  metricLabel4,
  showSecondPair,
}) {
  return (
    <div className="output-group">
      <div className="output-pairs-title">{title}</div>
      <div className="two-pairs-container">
        <div className="output-pair-container">
          <div className="output-pair-main">
            <p className="output-pair-label">{label1}</p>
            <p className="output-pair-text" id={id1}>
              {value1}
            </p>
            <p className="output-metric">{metricLabel1}</p>
          </div>
          <div className="output-pair-main">
            <p className="output-pair-label">after ft</p>
            <p className="output-pair-text-ft" id={id2}>
              {value2}
            </p>
            <p className="output-metric">{metricLabel2}</p>
          </div>
        </div>
        {showSecondPair ? (
          <div className="output-pair-container">
            <div className="output-pair-main">
              <p className="output-pair-label">{label3}</p>
              <p className="output-pair-text" id={id3}>
                {value3}
              </p>
              <p className="output-metric">{metricLabel3}</p>
            </div>
            <div className="output-pair-main">
              <p className="output-pair-label">after ft</p>
              <p className="output-pair-text-ft" id={id4}>
                {value4}
              </p>
              <p className="output-metric">{metricLabel4}</p>
            </div>
          </div>
        ) : null}
      </div>
    </div>
  );
}

DataOutputPairComponent.defaultProps = {
  showSecondPair: true,
};

DataOutputPairComponent.propTypes = {
  title: PropTypes.string.isRequired,
  id1: PropTypes.string.isRequired,
  label1: PropTypes.string.isRequired,
  value1: PropTypes.string.isRequired,
  metricLabel1: PropTypes.string.isRequired,
  id2: PropTypes.string.isRequired,
  value2: PropTypes.string.isRequired,
  metricLabel2: PropTypes.string.isRequired,
  id3: PropTypes.string,
  label3: PropTypes.string,
  value3: PropTypes.string,
  metricLabel3: PropTypes.string,
  id4: PropTypes.string,
  value4: PropTypes.string,
  metricLabel4: PropTypes.string,
  showSecondPair: PropTypes.bool.isRequired,
};
