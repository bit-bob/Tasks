import React from "react";
import styled from "styled-components";

import { ChevronDown } from "./ChevronDown";
import { ChevronRight } from "./ChevronRight";
import { Circle } from "./Circle";
import { CircleChecked } from "./CircleChecked";
import { PauseFill } from "./PauseFill";
import { PlayFill } from "./PlayFill";

export type IconComponent = React.ComponentType<React.SVGProps<SVGSVGElement>>;

export const ICON_MAP = {
  "chevron.down": ChevronDown,
  "chevron.right": ChevronRight,
  circle: Circle,
  "circle.checked": CircleChecked,
  "pause.fill": PauseFill,
  "play.fill": PlayFill,
};

export interface IconProps {
  type: keyof typeof ICON_MAP;
  onClick?: () => void;
  className?: string;
}

export const Icon = ({ type, onClick, className }: IconProps) => {
  const Component = ICON_MAP[type];
  return <Component className={className} onClick={onClick} />;
};

const IconButtonContainer = styled.button`
  background-color: transparent;
  border: none;
  padding: 0;
  margin: 0;
  display: flex;
  cursor: pointer;
  border-radius: 100%;

  transition: all 100ms ease-in-out;
  &:active:not(:disabled) {
    transform: scale(0.9);
  }

  &:focus {
    outline-style: solid;
    outline-width: 2px;
    outline-color: #6366f1;
    outline-offset: -2px;
  }
`;

export const IconButton = ({ onClick, ...rest }: IconProps) => {
  return (
    <IconButtonContainer onClick={onClick}>
      <Icon {...rest} />
    </IconButtonContainer>
  );
};
