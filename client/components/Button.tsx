import styled from "styled-components";

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
        return props.disabled ? "#BEAFE9" : "#EFECFB";
      default:
        return props.disabled ? "#d6d5d9" : "#343334";
    }
  }};
  background-color: ${(props) => {
    switch (props.variant) {
      case "primary":
        return props.disabled ? "#DDD5F6" : "#653FD7";
      default:
        return "#e4e2e8";
    }
  }};
  font-size: 14px;
  border: none;
  border-radius: 4px;
  cursor: ${(props) => (props.disabled ? "not-allowed" : "pointer")};
`;
