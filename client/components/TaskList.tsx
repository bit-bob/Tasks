import React from "react";
import styled from "styled-components";

import { Task } from "../types";
import { TaskListItem } from "./TaskListItem";

const List = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 5px;
`;


export interface TaskListProps {
  tasks: Task[];
}

export const TaskList = ({
  tasks,
}: TaskListProps) => {
  return ( 
    <List>
      { tasks.map(task => <TaskListItem key={task.id} task={task}/>) }
    </List>
  );
};
