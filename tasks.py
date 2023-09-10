from typing import List
from datetime import datetime


class TaskEvent():

    def __init__(
        self,
        start: datetime,
    ) -> None:
        self.start = start
        self.end = None

    def __str__(self) -> str:
        return f'{self.start}, {self.end}'


class Task():

    def __init__(
        self,
        name,
    ) -> None:
        self.name = name
        self.events = []

    def __str__(self) -> str:
        return self.name

    def start_event(
        self,
        start: datetime,
    ):
        self.events.append(TaskEvent(start))

    def stop_event(
        self,
        end: datetime,
    ):
        self.events[0].end = end


class TaskList():

    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def get_task(
        self,
        task_id: int,
    ) -> List[Task]:
        try:
            return [self.tasks[task_id]]
        except IndexError:
            return []

    def add_task(
        self,
        name: str,
    ):
        self.tasks.append(Task(name))
