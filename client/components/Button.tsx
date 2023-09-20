import styled from "styled-components";

import {
  slate200,
  slate300,
  slate800,
  indigo200,
  indigo300,
  indigo800,
  rose200,
  rose300,
  rose800,
} from "../constants";

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
        return props.disabled ? indigo300 : indigo200;
      case "danger":
        return props.disabled ? rose300 : rose200;
      default:
        return props.disabled ? slate300 : slate200;
    }
  }};

  background-color: ${(props) => {
    switch (props.variant) {
      case "primary":
        return props.disabled ? indigo200 : indigo800;
      case "danger":
        return props.disabled ? rose200 : rose800;
      default:
        return props.disabled ? slate200 : slate800;
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
