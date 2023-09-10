import React from "react";

import { PauseFill } from "./PauseFill";
import { PlayFill } from "./PlayFill";

export const ICON_MAP = {
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
