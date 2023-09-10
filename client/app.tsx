import React from "react";
import { GlobalStyles } from "./GlobalStyles";

import { WrappedTaskListItem } from "./components/TaskListItem";

export const App = () => {
  return (
    <>
      <GlobalStyles />
      <WrappedTaskListItem
        task={{
          id: "0",
          title: "Wash Dishes",
          childTasks: 1,
          events: [],
        }}
        getTaskChildren={async () => [
          {
            id: "0",
            title: "Wash Dishes",
            childTasks: 0,
            events: [],
          },
        ]}
      />
    </>
  );
};
