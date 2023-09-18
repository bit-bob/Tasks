import styled from "styled-components";

import {
  white,
  slate100,
  slate300,
  indigo100,
  indigo300,
  indigo700,
  rose50,
  rose400,
  rose700,
  slate900,
} from "./constants";

export interface ButtonProps {
  variant?: "primary" | "danger" | "default";
  disabled?: boolean;
}

export const Button = styled.button<ButtonProps>`
  font-family: Comfortaa;
  font-size: 15px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  letter-spacing: -0.333px;

  padding: 10px;

  color: ${(props) => {
    switch (props.variant) {
      case "primary":
        return props.disabled ? indigo300 : indigo100;
      case "danger":
        return props.disabled ? rose50 : white;
      default:
        return props.disabled ? slate300 : slate100;
    }
  }};

  background-color: ${(props) => {
    switch (props.variant) {
      case "primary":
        return props.disabled ? indigo100 : indigo700;
      case "danger":
        return props.disabled ? rose400 : rose700;
      default:
        return slate900;
    }
  }};

  border: none;
  border-radius: 8px;
  cursor: ${(props) => (props.disabled ? "not-allowed" : "pointer")};

  transition: all 100ms ease-in-out;
  &:active:not(:disabled) {
    transform: scale(0.95);
  }
`;
