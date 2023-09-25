import type { Meta, StoryObj } from "@storybook/react";

import { Icon, ICON_MAP } from "./Icon";

const meta: Meta<typeof Icon> = {
  component: Icon,
  tags: ["autodocs"],
  argTypes: {
    type: {
      options: Object.keys(ICON_MAP),
      control: { type: "radio" },
    },
  },
};

export default meta;
type Story = StoryObj<typeof Icon>;

export const icon: Story = {
  args: {
    type: "pause.fill",
  },
};
