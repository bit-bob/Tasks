import React from 'react'
import type { Meta, StoryObj } from "@storybook/react";

import { AppHeader } from "./AppHeader";
import { PlayingPill } from './PlayingPill'

const meta: Meta<typeof AppHeader> = {
  component: AppHeader,
};

export default meta;
type Story = StoryObj<typeof AppHeader>;

export const simpleAppHeader: Story = {
  args: {
    title: "tasks",
    actions: null
  },
};

export const appHeaderWithPlayingPill: Story = {
    args: {
      title: "Wash Dishes",
      actions: <PlayingPill started playing />
    },
  };

