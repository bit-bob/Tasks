import React from "react";
import styled from "styled-components";
import { useAutoAnimate } from "@formkit/auto-animate/react";

import { TaskModel } from "api";

import { TaskListItem } from "./TaskListItem";

const List = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 4px 0px 0px 0px;
  gap: 4px;
`;

export interface TaskListProps {
  tasks: TaskModel[];
  onToggleComplete?: (task: TaskModel) => void;
  onDelete?: (task: TaskModel) => void;
  onEditTaskTitle?: (task: TaskModel, newTitle: string) => void;
}

export const TaskList = ({
  tasks,
  onToggleComplete,
  onDelete,
  onEditTaskTitle,
}: TaskListProps) => {
  const [animationParent] = useAutoAnimate();
  return (
    <List ref={animationParent}>
      {tasks.map((task) => (
        <TaskListItem
          onToggleComplete={() => onToggleComplete?.(task)}
          onDelete={() => onDelete?.(task)}
          onEdit={(newName) => onEditTaskTitle?.(task, newName)}
          key={task.id}
          task={task}
        />
      ))}
    </List>
  );
};
