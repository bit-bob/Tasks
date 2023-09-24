import {
  TasksApi,
  TaskModel,
  Configuration,
} from "api";
import { useState, useCallback, useEffect } from "react";
import { AppHeader } from "../components/AppHeader";
import { TaskList } from "../components/TaskList";
import { GlobalStyles } from "../GlobalStyles";
import { throttle } from "lodash";
import styled from "styled-components";

const config = new Configuration({ basePath: "http://localhost:8000" });
const TasksService = new TasksApi(config);

const Container = styled.div`
  display: flex;
  flex-direction: column;
  gap: 4px;
`;

export default function Home() {
  const [tasks, setTasks] = useState<TaskModel[] | null>(null)

  const refresh = () => TasksService.getTasks().then(response => response.tasks).then(setTasks)

  useEffect(() => {
    refresh()
  }, [])

  const editTaskTitle = (task: TaskModel, newTitle: string) => {
    TasksService.updateTask({
      updateTaskRequest: {
        taskId: task.id,
        name: newTitle,
      },
    }).then(refresh);
  };

  // calls editTaskTitle every 2s with the latest changes
  const editTaskTitleThrottled = useCallback(throttle(editTaskTitle, 2000), []);

  return (
    <Container>
      <GlobalStyles />
      <AppHeader title="Tasks" />
      {!tasks ? (
        "Loading..."
      ) : (
        <TaskList
          onToggleComplete={(task) => {
            TasksService.toggleTaskComplete({
              toggleTaskCompleteRequest: {
                taskId: task.id,
                completed: task.completed ? null : new Date(),
              },
            }).then(refresh);
          }}
          onDelete={(task) => {
            console.log(task);
            TasksService.deleteTask({
              deleteTaskRequest: {
                taskId: task.id,
              },
            }).then(refresh);
          }}
          onEditTaskTitle={(task, newTitle) => {
            setTasks(tasks.map((t) => {
              if (task.id !== t.id) {
                return t;
              }
              return {
                ...t,
                name: newTitle,
              };
            }))
            editTaskTitleThrottled(task, newTitle);
          }}
          tasks={tasks}
        />
      )}
    </Container>
  );
}
