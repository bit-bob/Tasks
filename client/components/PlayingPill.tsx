import React from "react";
import styled from "styled-components";

import { Icon } from "../icons/Icon";

const Pill = styled.div<{ playing: boolean }>`
  display: inline-flex;
  padding: 4px ${(props) => (props.playing ? "10px" : "4px")};
  align-items: center;
  gap: 6px;
  font-family: "Azeret Mono", monospace;
  background-color: ${(props) => (props.playing ? "#c5f9c7ff" : "#c5f9c700")};
  border-radius: 14px;
  user-select: none;
  cursor: pointer;
  transition: all 100ms ease-in-out;

  &:hover {
    background-color: ${(props) => (props.playing ? "#a3f0a6ff" : "#eeeeeeff")};
  }

  &:active {
    transform: scale(0.95);
  }

  & > span {
    transition: all 100ms ease-in-out;
    opacity: ${(props) => (props.playing ? 1 : 0)};

    overflow-x: hidden;

    ${(props) => !props.playing && `margin-left: -6px; width: 0px;`}
  }
`;

export interface PlayingPillProps {
  playing: boolean;
  onPlayPause?: () => void;
}

export const PlayingPill = ({ playing, onPlayPause }: PlayingPillProps) => {
  return (
    <Pill playing={playing} onClick={onPlayPause}>
      <Icon type={playing ? "pause.fill" : "play.fill"} />
      <span>{"12:14:01"}</span>
    </Pill>
  );
};
