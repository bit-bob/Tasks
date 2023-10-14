import { TasksApi, TaskModel, Configuration } from "api";
import { useState, useCallback, useEffect } from "react";
import { AppHeader } from "../components/AppHeader";
import { Button } from "../components/Button";
import { TaskList } from "../components/TaskList";
import { GlobalStyles } from "../GlobalStyles";
import { throttle } from "lodash";
import styled from "styled-components";
import { Haptics, ImpactStyle } from "@capacitor/haptics";
import { StatusBar, Style } from "@capacitor/status-bar";

const { NEXT_PUBLIC_BASE_API_URL: BASE_API_URL = "http://localhost:8000" } =
  process.env;

const config = new Configuration({ basePath: BASE_API_URL });
const TasksService = new TasksApi(config);

const Container = styled.div`
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding-top: 100px;
`;

export default function Home() {
  const [tasks, setTasks] = useState<TaskModel[] | null>(null);

  const refresh = async () => {
    const response = await TasksService.getTasks();
    setTasks(response.tasks);
  };

  useEffect(() => {
    StatusBar.setOverlaysWebView({ overlay: true })
      .then(() => StatusBar.setStyle({ style: Style.Light }))
      .catch(console.warn);
    refresh();
  }, []);

  const editTaskTitle = async (task: TaskModel, newTitle: string) => {
    await TasksService.updateTaskName({
      updateTaskNameRequest: {
        taskId: task.id,
        name: newTitle,
      },
    });
    await refresh();
  };

  // calls editTaskTitle every 8s with the latest changes
  const editTaskTitleThrottled = useCallback(throttle(editTaskTitle, 8000), []);

  return (
    <Container>
      <GlobalStyles />
      <AppHeader
        title="Tasks"
        actions={
          <Button
            variant="default"
            onClick={async () => {
              await TasksService.createTask({
                createTaskRequest: {
                  name: "Unnamed Task",
                },
              });
              await refresh();
            }}
          >
            Add Task
          </Button>
        }
      />
      {!tasks ? (
        "Loading..."
      ) : (
        <TaskList
          onToggleComplete={async (task) => {
            await Haptics.impact({ style: ImpactStyle.Medium });
            await TasksService.updateTaskCompletedDate({
              updateTaskCompletedDateRequest: {
                taskId: task.id,
                completedDate: task.completedDate ? null : new Date(),
              },
            });
            await refresh();
          }}
          onDelete={async (task) => {
            await TasksService.deleteTask({
              deleteTaskRequest: {
                taskId: task.id,
              },
            });
            await refresh();
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
              })
            );
            editTaskTitleThrottled(task, newTitle);
          }}
          tasks={tasks}
        />
      )}
    </Container>
  );
}
