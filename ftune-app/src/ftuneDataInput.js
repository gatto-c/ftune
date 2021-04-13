/* eslint-disable no-constant-condition */
import React from "react";
import PropTypes from "prop-types";

export default function DataIOComponent({
  id,
  label,
  type,
  metricLabel,
  readOnly,
}) {
  return (
    <div className="input-container">
      <p className="input-label">{label}</p>
      <input type={type} className="input" id={id} readOnly={readOnly} />
      <p className="input-metric">{metricLabel}</p>
    </div>
  );
}

DataIOComponent.defaultProps = {
  readOnly: false,
};

DataIOComponent.propTypes = {
  id: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  type: PropTypes.string.isRequired,
  metricLabel: PropTypes.string.isRequired,
  readOnly: PropTypes.bool,
};
