import React from "react";

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
