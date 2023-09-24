import {
  TasksApi,
  TaskModel,
  GetTasksResponseToJSON,
  GetTasksResponseFromJSONTyped,
  Configuration,
} from "api";
import { useState, useCallback } from "react";
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

interface HomeProps {
  initialTasks: any;
}
export async function getServerSideProps(): Promise<{ props: HomeProps }> {
  return {
    props: {
      initialTasks: GetTasksResponseToJSON(await TasksService.getTasks()),
    },
  };
}

export default function Home({ initialTasks }: HomeProps) {
  const [tasks, setTasks] = useState(
    GetTasksResponseFromJSONTyped(initialTasks, false).tasks
  );

  const refresh = async () =>
    await TasksService.getTasks()
      .then(({ tasks }) => tasks)
      .then(setTasks);

  const editTaskTitle = (task: TaskModel, newTitle: string) => {
    TasksService.updateTask({
      updateTaskRequest: {
        taskId: task.id,
        name: newTitle,
      },
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
