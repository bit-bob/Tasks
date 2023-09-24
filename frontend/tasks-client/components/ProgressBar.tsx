import React from "react";
import styled from "styled-components";

import { transparent, slate100, rose800 } from "../constants";

const Bar = styled.progress`
  width: 100%;

  /* 
  This exists only to break out of the default style
  without actually adding a visible background 
  */
  background-color: ${transparent};

  &::-webkit-progress-bar {
    background-color: ${slate100};
    border-radius: 10px;
  }
  &::-webkit-progress-value {
    background-color: ${rose800};
    border-radius: 10px;
  }
`;

export interface ProgressBarProps {
  progress: number;
}

export const ProgressBar = ({ progress }: ProgressBarProps) => {
  return <Bar max={100} value={progress} />;
};
