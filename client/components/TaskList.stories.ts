import type { Meta, StoryObj } from "@storybook/react";

import { TaskList } from "./TaskList";

const meta: Meta<typeof TaskList> = {
  component: TaskList,
};

export default meta;
type Story = StoryObj<typeof TaskList>;

export const taskList: Story = {
  args: {
    tasks: [
      {
        id: "0",
        title: "Wash Dishes",
      },
      {
        id: "1",
        title: "Feed Fishes",
      },
      {
        id: "2",
        title: "Profit",
      },
    ],
  },
};
