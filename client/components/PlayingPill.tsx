import React from "react";
import styled from "styled-components";

import {
  green300,
  green300Lighter,
  slate100,
  slate100Lighter,
} from "../constants";
import { Icon } from "../icons/Icon";

const Pill = styled.div<{ playing: boolean; started: boolean }>`
  display: inline-flex;
  padding: 4px ${(props) => (props.started || props.playing ? "10px" : "4px")};
  align-items: center;
  gap: 6px;
  font-family: "Azeret Mono", monospace;
  background-color: ${(props) => (props.playing ? green300 : slate100)};
  border-radius: 14px;
  user-select: none;
  cursor: pointer;
  transition: all 100ms ease-in-out;

  &:hover {
    background-color: ${(props) =>
      props.playing ? green300Lighter : slate100Lighter};
  }

  &:active {
    transform: scale(0.95);
  }

  & > span {
    transition: all 100ms ease-in-out;
    opacity: ${(props) => (props.started || props.playing ? 1 : 0)};

    overflow-x: hidden;

    ${(props) =>
      !(props.started || props.playing) && `margin-left: -6px; width: 0px;`}
  }
`;

export interface PlayingPillProps {
  started: boolean;
  playing: boolean;
  onPlayPause?: () => void;
}

export const PlayingPill = ({
  started,
  playing,
  onPlayPause,
}: PlayingPillProps) => {
  return (
    <Pill started={started} playing={playing} onClick={onPlayPause}>
      <Icon type={playing ? "pause.fill" : "play.fill"} />
      <span>12:14:01</span>
    </Pill>
  );
};
