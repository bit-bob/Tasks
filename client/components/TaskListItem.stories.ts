import type { Meta, StoryObj } from "@storybook/react";

import { WrappedTaskListItem } from "./TaskListItem";

const meta: Meta<typeof WrappedTaskListItem> = {
  component: WrappedTaskListItem,
};

export default meta;
type Story = StoryObj<typeof WrappedTaskListItem>;

export const taskListItem: Story = {
  args: {
    // playing: false,
    task: {
      title: "Wash Dishes",
      childTasks: 1,
      events: [],
    },
  },
};
