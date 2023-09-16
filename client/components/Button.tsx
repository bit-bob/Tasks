import styled from "styled-components";

import {
  slate100,
  slate300,
  indigo100,
  indigo300,
  indigo700,
} from "../constants";

export interface ButtonProps {
  variant?: "primary" | "default";
  disabled?: boolean;
}

export const Button = styled.button<ButtonProps>`
  height: 32px;
  padding: 0 8px;
  font-family: "Chivo", sans-serif;
  font-weight: 400;
  color: ${(props) => {
    switch (props.variant) {
      case "primary":
        return props.disabled ? indigo300 : indigo100;
      default:
        return props.disabled ? slate300 : slate100;
    }
  }};
  background-color: ${(props) => {
    switch (props.variant) {
      case "primary":
        return props.disabled ? indigo100 : indigo700;
      default:
        return slate300;
    }
  }};
  font-size: 14px;
  border: none;
  border-radius: 4px;
  cursor: ${(props) => (props.disabled ? "not-allowed" : "pointer")};
`;
