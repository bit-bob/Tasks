import React from "react";
import { GlobalStyles } from "./GlobalStyles";

import { TaskListItem } from "./components/TaskListItem";

export const App = () => {
  return (
    <>
      <GlobalStyles />
      <TaskListItem
        task={{
          id: "0",
          title: "Wash Dishes",
        }}
      />
    </>
  );
};
