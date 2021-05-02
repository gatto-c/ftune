/* eslint-disable */
/* eslint-disable no-constant-condition */
import React from "react";
import PropTypes from "prop-types";
import Input from "@material-ui/core/Input";

export default function DataIOComponent({
  id,
  label,
  type,
  inputValue,
  metricLabel,
  visible,
  readOnly,
  handleChange,
}) {
  if (visible) {
    return (
      <div className="input-container">
        <p className="input-label">{label}</p>
        <Input
          id={id}
          className="input"
          type={type}
          value={inputValue}
          readOnly={readOnly}
          inputProps={{ inputMode: "numeric", pattern: "[0-9]*" }}
          onChange={handleChange}
        />
        <p className="input-metric">{metricLabel}</p>
      </div>
    );
  } else {
    return null;
  }
}

DataIOComponent.defaultProps = {
  readOnly: false,
};

DataIOComponent.propTypes = {
  id: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  type: PropTypes.string.isRequired,
  inputValue: PropTypes.string.isRequired,
  metricLabel: PropTypes.string.isRequired,
  visible: PropTypes.bool,
  readOnly: PropTypes.bool,
  handleChange: PropTypes.func.isRequired,
};
/* eslint-enable */
