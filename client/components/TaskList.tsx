import React from "react";
import styled from "styled-components";

import { TaskModel } from "../../api-types/models/TaskModel";

import { TaskListItem } from "./TaskListItem";

const List = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 5px;
`;

export interface TaskListProps {
  tasks: TaskModel[];
  onToggleComplete?: (task: TaskModel) => void;
}

export const TaskList = ({ tasks, onToggleComplete }: TaskListProps) => {
  return (
    <List>
      {tasks.map((task) => (
        <TaskListItem
          onToggleComplete={() => onToggleComplete?.(task)}
          key={task.id}
          task={task}
        />
      ))}
    </List>
  );
};
