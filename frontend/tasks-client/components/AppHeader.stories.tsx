import React from "react";
import type { Meta, StoryObj } from "@storybook/react";

import { AppHeader, AppHeaderTitle } from "./AppHeader";
import { PlayingPill } from "./PlayingPill";
import { InlineEdit } from "./InlineEdit";
import { Button } from "./Button";

const meta: Meta<typeof AppHeader> = {
  component: AppHeader,
  tags: ["autodocs"],
};

export default meta;
type Story = StoryObj<typeof AppHeader>;

export const simpleAppHeader: Story = {
  args: {
    title: "tasks",
    actions: null,
  },
};

export const appHeaderWithAction: Story = {
  args: {
    title: "tasks",
    actions: <Button variant="default">Action</Button>,
  },
};

export const appHeaderWithPlayingPill: Story = {
  args: {
    title: "Wash Dishes",
    actions: <PlayingPill started playing />,
  },
};

export const appHeaderWithEditableTitle: Story = {
  args: {
    title: (
      <InlineEdit
        value="Wash Dishes"
        as={AppHeaderTitle as any}
        onChange={async () => {}}
      />
    ),
    actions: <PlayingPill started playing />,
  },
};
