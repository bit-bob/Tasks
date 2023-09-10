import React from "react";
import styled from "styled-components";

import { Icon } from "../icons/Icon";

import { PlayingPill } from "./PlayingPill";

const Container = styled.div<{ level: number }>`
  display: flex;
  justify-content: space-between;
  align-items: center;
  align-self: stretch;
  user-select: none;
  margin-left: ${(props) => props.level * 28}px;
`;

const Details = styled.div`
  display: flex;
  align-items: center;
`;

const Text = styled.span`
  text-align: center;
  font-family: Comfortaa;
  font-size: 15px;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
  letter-spacing: -0.333px;
`;

const DropdownIcon = styled(Icon)<{ isOpen: boolean }>`
  transition: all 100ms ease-in-out;

  transform: rotate(${(props) => (props.isOpen ? "0deg" : "-90deg")});
`;

export interface TaskEvent {
  start: number;
  end: number;
}

export interface Task {
  childTasks: number;
  events: TaskEvent[];
  title: string;
}

export interface TaskListItemProps {
  task: Task;
  level?: number;
}

export const TaskListItem = ({ task, level = 0 }: TaskListItemProps) => {
  const [isOpen, setIsOpen] = React.useState(false);
  const [playing, setPlaying] = React.useState(false);
  return (
    <>
      <Container level={level}>
        <Details>
          <DropdownIcon
            isOpen={isOpen}
            onClick={() => setIsOpen((v) => !v)}
            type="chevron.down"
          />
          <Icon type="circle" />
          <Text>{task.title}</Text>
        </Details>
        <Details>
          <PlayingPill
            playing={playing}
            onPlayPause={() => setPlaying((v) => !v)}
          />
          <Icon type="chevron.right" />
        </Details>
      </Container>
      {isOpen ? (
        <>
          <TaskListItem task={task} level={level + 1} />
          <TaskListItem task={task} level={level + 1} />
        </>
      ) : null}
    </>
  );
};

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 2px;
`;

export const WrappedTaskListItem = (props: TaskListItemProps) => (
  <Wrapper>
    <TaskListItem {...props} />
  </Wrapper>
);
