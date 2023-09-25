import type { Meta, StoryObj } from "@storybook/react";

import { InlineEdit } from "./InlineEdit";

const meta: Meta<typeof InlineEdit> = {
  component: InlineEdit,
  tags: ["autodocs"],
};

export default meta;
type Story = StoryObj<typeof InlineEdit>;

export const inlineEdit: Story = {
  args: {
    value: "John Doe",
    onChange: async () => {},
  },
};
