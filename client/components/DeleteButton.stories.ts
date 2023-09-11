import type { Meta, StoryObj } from "@storybook/react";

import { DeleteButton } from "./DeleteButton";

const meta: Meta<typeof DeleteButton> = {
  component: DeleteButton,
};

export default meta;
type Story = StoryObj<typeof DeleteButton>;

export const deleteButton: Story = {
  args: {  },
};
