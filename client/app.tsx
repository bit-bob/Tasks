import React, { useState, useEffect } from "react";
import { GlobalStyles } from "./GlobalStyles";
import styled from "styled-components";

import { AppHeader } from "./components/AppHeader";
import { TaskList } from "./components/TaskList";

import { OpenAPI, TasksService, TaskModel } from "../api-types";

// TODO: fix to environment variable at build time
OpenAPI.BASE = "http://localhost:3000";

const Container = styled.div`
  display: flex;
  flex-direction: column;
  gap: 4px;
`;

export const App = () => {
  const [tasks, setTasks] = useState<TaskModel[] | null>(null);

  useEffect(() => {
    let cancel = false;
    TasksService.getTasks()
      .then((response) => response.tasks)
      .then((tasks) => {
        if (cancel) {
          // this is run if the data is loaded but the component has been unmounted
          return;
        }
        // this is run when the data is loaded and can be set on the component
        setTasks(tasks);
      });

    // this is run when the component unmounts
    return () => {
      cancel = true;
    };
  }, []);

  return (
    <Container>
      <GlobalStyles />
      <AppHeader title="Tasks" />
      {tasks === null ? (
        "loading..."
      ) : (
        <TaskList
          onToggleComplete={(task) => {
            TasksService.toggleTaskComplete({
              task_id: task.id,
              completed: task.completed ? null : new Date().toISOString(),
            })
              .then(TasksService.getTasks)
              .then((response) => response.tasks)
              .then(setTasks);
          }}
          onDelete={(task) => {
            TasksService.deleteTask({
              task_id: task.id,
            })
              .then(TasksService.getTasks)
              .then((response) => response.tasks)
              .then(setTasks);
          }}
          tasks={tasks}
        />
      )}
    </Container>
  );
};
