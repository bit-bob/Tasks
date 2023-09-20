import React, { useState, useEffect, useCallback } from "react";
import { GlobalStyles } from "./GlobalStyles";
import styled from "styled-components";
import { throttle } from "lodash";

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

  const editTaskTitle = (task: TaskModel, newTitle: string) => {
    TasksService.updateTask({
      task_id: task.id,
      name: newTitle,
    });
  };

  // calls editTaskTitle every 2s with the latest changes
  const editTaskTitleThrottled = useCallback(throttle(editTaskTitle, 2000), []);

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
          onEditTaskTitle={(task, newTitle) => {
            setTasks(
              tasks.map((t) => {
                if (task.id !== t.id) {
                  return t;
                }
                return {
                  ...t,
                  name: newTitle,
                };
              }),
            );
            editTaskTitleThrottled(task, newTitle);
          }}
          tasks={tasks}
        />
      )}
    </Container>
  );
};
