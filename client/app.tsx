import React from "react";
import { GlobalStyles } from "./GlobalStyles";

import { WrappedTaskListItem } from "./components/TaskListItem";

export const App = () => {
  return (
    <>
      <GlobalStyles />
      <WrappedTaskListItem
        task={{
          title: "Wash Dishes",
          childTasks: 1,
          events: [],
        }}
      />
    </>
  );
};
