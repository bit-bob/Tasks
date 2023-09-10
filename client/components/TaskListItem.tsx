import React, { useEffect } from "react";
import styled from "styled-components";

import { Icon } from "../icons/Icon";

import { PlayingPill } from "./PlayingPill";

const Container = styled.div<{ level: number }>`
  display: flex;
  justify-content: space-between;
  align-items: center;
  align-self: stretch;
  user-select: none;
  margin-left: ${(props) => props.level * 28}px;
  border-radius: 4px;
  cursor: pointer;
  padding: 4px;

  &:hover {
    background-color: #f8f8f8;
  }
`;

const Details = styled.div`
  display: flex;
  align-items: center;
`;

const Text = styled.span`
  text-align: center;
  font-family: Comfortaa;
  font-size: 15px;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
  letter-spacing: -0.333px;
`;

const DropdownIcon = styled(Icon)<{ isOpen: boolean }>`
  transition: all 100ms ease-in-out;

  transform: rotate(${(props) => (props.isOpen ? "0deg" : "-90deg")});
`;

export interface TaskEvent {
  start: number;
  end: number;
}

export interface Task {
  id: string;
  childTasks: number;
  events: TaskEvent[];
  title: string;
}

export interface TaskListItemProps {
  task: Task;
  level?: number;
  getTaskChildren: (task: Task) => Promise<Task[]>;
}

export const TaskListItem = ({
  task,
  level = 0,
  getTaskChildren,
}: TaskListItemProps) => {
  const [isOpen, setIsOpen] = React.useState(false);
  const [playing, setPlaying] = React.useState(false);

  const [childTasks, setChildTasks] = React.useState<Task[] | null>(null);

  useEffect(() => {
    let cancel = false;
    if (isOpen && childTasks === null) {
      // fetch new tasks
      getTaskChildren(task).then((tasks) => {
        if (cancel) {
          return;
        }
        setChildTasks(tasks);
      });
    }
    return () => {
      cancel = true;
    };
  }, [isOpen]);

  return (
    <>
      <Container level={task.childTasks === 0 ? level + 1 : level}>
        <Details>
          {task.childTasks !== 0 && (
            <DropdownIcon
              isOpen={isOpen}
              onClick={() => setIsOpen((v) => (task.childTasks === 0 ? v : !v))}
              type="chevron.down"
            />
          )}
          <Icon type="circle" />
          <Text>{task.title}</Text>
        </Details>
        <Details>
          <PlayingPill
            playing={playing}
            onPlayPause={() => setPlaying((v) => !v)}
          />
          <Icon type="chevron.right" />
        </Details>
      </Container>
      {isOpen ? (
        <>
          {childTasks === null
            ? null
            : childTasks.map((childTask) => (
                <TaskListItem
                  task={childTask}
                  level={level + 1}
                  getTaskChildren={getTaskChildren}
                />
              ))}
        </>
      ) : null}
    </>
  );
};

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 4px;
`;

export const WrappedTaskListItem = (props: TaskListItemProps) => (
  <Wrapper>
    <TaskListItem {...props} />
  </Wrapper>
);
