import React, { useState, useEffect, useRef } from "react";
import styled from "styled-components";

import { TaskModel } from "api";
import { transparentize } from "polished";

import { IconButton } from "../icons/Icon";
import { slate100, black } from "../constants";

import { Button } from "./Button";

const Container = styled.div<{ hasFocus: boolean }>`
  display: flex;
  justify-content: space-between;
  align-items: center;
  align-self: stretch;
  user-select: none;
  border-radius: 4px;
  cursor: pointer;
  padding: 5px 5px 5px 10px;
  gap: 5px;

  &:hover {
    background-color: ${slate100};
  }

  transition: all 100ms ease-in-out;
  outline-style: solid;
  outline-width: 2px;
  outline-color: #6366f100;
  outline-offset: 4px;

  ${(props) =>
    props.hasFocus &&
    `
    background-color: ${slate100};

    outline-style: solid;
    outline-width: 2px;
    outline-color: #6366f1ff;
    outline-offset: 2px;
  `}
`;

const Text = styled.input<{ isCompleted: boolean }>`
  font-family: Comfortaa;
  font-size: 15px;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
  letter-spacing: -0.333px;
  flex-grow: 1;

  background-color: transparent;
  border: none;
  margin: 0;
  padding: 0;
  width: auto;
  outline: none;

  ${(props) => props.isCompleted && `color: ${transparentize(0.5, black)}`}
`;

export interface TaskListItemProps {
  task: TaskModel;
  onToggleComplete?: () => void;
  onDelete?: () => void;
  onEdit?: (newName: string) => void;
}

export const TaskListItem = ({
  task,
  onToggleComplete,
  onDelete,
  onEdit,
}: TaskListItemProps) => {
  const ref = useRef<HTMLInputElement>(null);
  const [hasFocus, setFocus] = useState(false);

  useEffect(() => {
    if (document.hasFocus() && ref.current?.contains(document.activeElement)) {
      setFocus(true);
    }
  }, []);

  return (
    <Container hasFocus={hasFocus}>
      <Text
        ref={ref}
        onFocus={() => setFocus(true)}
        onBlur={() => setFocus(false)}
        isCompleted={Boolean(task.completed)}
        value={task.name}
        onChange={(e) => onEdit?.(e.target.value)}
      />
      <Button variant="danger" onClick={onDelete}>
        Delete
      </Button>
      <IconButton
        onClick={onToggleComplete}
        type={task.completed ? "circle.checked" : "circle"}
      />
    </Container>
  );
};
