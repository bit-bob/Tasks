import React from "react";

import { ChevronDown } from "./ChevronDown";
import { ChevronRight } from "./ChevronRight";
import { Circle } from "./Circle";
import { PauseFill } from "./PauseFill";
import { PlayFill } from "./PlayFill";

export const ICON_MAP = {
  "chevron.down": ChevronDown,
  "chevron.right": ChevronRight,
  circle: Circle,
  "pause.fill": PauseFill,
  "play.fill": PlayFill,
};

export interface IconProps {
  type: keyof typeof ICON_MAP;
}

export const Icon = ({ type }: IconProps) => {
  const IconComponent = ICON_MAP[type];
  return <IconComponent />;
};
