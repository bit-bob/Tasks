import type { Meta, StoryObj } from "@storybook/react";

import { Task, WrappedTaskListItem } from "./TaskListItem";

const meta: Meta<typeof WrappedTaskListItem> = {
  component: WrappedTaskListItem,
};

export default meta;
type Story = StoryObj<typeof WrappedTaskListItem>;

const wait = (ms: number) =>
  new Promise((res) => {
    setTimeout(res, ms);
  });

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

export const taskListItem: Story = {
  args: {
    // playing: false,
    task: {
      id: "0",
      title: "Wash Dishes",
      childTasks: 2,
      events: [],
    },
    getTaskChildren: async (task: Task): Promise<Task[]> => {
      await wait(100 + 1000 * Math.random());
      return new Array(task.childTasks)
        .fill(() => null)
        .map(() => {
          return { ...task, childTasks: getRandomInt(4) };
        });
    },
  },
};
