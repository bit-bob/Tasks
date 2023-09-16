import React from "react";
import styled from "styled-components";
import { useAutoAnimate } from "@formkit/auto-animate/react";

import {
  green300,
  green300Lighter,
  slate100,
  slate100Lighter,
  animateOptions,
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
`;

const IconContainer = styled.div`
  height: 20px;
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
  const [animationParent] = useAutoAnimate(animateOptions);
  return (
    <Pill
      ref={animationParent}
      started={started}
      playing={playing}
      onClick={onPlayPause}
    >
      <IconContainer>
        <Icon type={playing ? "pause.fill" : "play.fill"} />
      </IconContainer>
      {(started || playing) && <span>12:14:01</span>}
    </Pill>
  );
};
