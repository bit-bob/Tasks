import { useState } from "react";
import { TaskModel, TasksService } from "api-types";
import { AppHeader } from 'components/AppHeader'
import { TaskList } from 'components/TaskList'

interface HomeProps {
  initialTodos: TaskModel[];
}

export async function getServerSideProps(): Promise<{ props: HomeProps }> {
  return {
    props: {
      initialTodos: (await TasksService.getTasks()).tasks,
    },
  };
}

export default function Home(props: HomeProps) {
  const [tasks, setTasks] = useState<TaskModel[]>(props.initialTodos);

  const refresh = async () => { 
    console.log('refreshing')
    setTasks((await TasksService.getTasks()).tasks)
    console.log('refreshed')
  };

  return (
    <>
      <AppHeader title="Tasks" />
      <TaskList
        onToggleComplete={async task => {
          const promise = TasksService.toggleTaskComplete({
            task_id: task.id,
            completed: Boolean(task.completed) ? null : new Date().toISOString(),
          })
          console.log(promise.then())
        }}
        tasks={tasks}
      />
    </>
  );
}
