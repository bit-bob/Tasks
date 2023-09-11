import type { Meta, StoryObj } from "@storybook/react";

import { PlayingPill } from "./PlayingPill";

const meta: Meta<typeof PlayingPill> = {
  component: PlayingPill,
};

export default meta;
type Story = StoryObj<typeof PlayingPill>;

export const playingPill: Story = {
  args: {
    started: false,
    playing: false,
  },
};
