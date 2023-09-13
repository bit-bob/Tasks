import type { Meta, StoryObj } from "@storybook/react";

import { TaskListItem } from "./TaskListItem";

const meta: Meta<typeof TaskListItem> = {
  component: TaskListItem,
};

export default meta;
type Story = StoryObj<typeof TaskListItem>;

export const taskListItem: Story = {
  args: {
    task: {
      id: "0",
      name: "Wash Dishes",
      completed: null,
    },
  },
};
