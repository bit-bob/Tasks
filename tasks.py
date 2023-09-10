from typing import List, Dict
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
        return str(self.as_dict())

    def as_dict(self):
        return {
            'name': self.name,
            'events': [
                {
                    'start': e.start,
                    'end': e.end,
                } for e in self.events
            ]
        }

    def start_event(
        self,
        start: datetime,
    ):
        self.events.append(TaskEvent(start))

    def stop_event(
        self,
        end: datetime,
    ):
        self.events[-1].end = end


class TaskList():

    def __init__(self):
        self.tasks = []

    def get_tasks_as_dicts(self) -> List[Dict]:
        return [t.as_dict() for t in self.tasks]

    # Create
    def add_task(
        self,
        name: str,
    ):
        self.tasks.append(Task(name))

    # Read
    def get_task_as_dict(
        self,
        task_id: int,
    ) -> List[Dict]:
        try:
            task = self.tasks[task_id]
            return [task.as_dict()]
        except IndexError:
            return []

    def get_task(
        self,
        task_id: int,
    ) -> List[Task]:
        try:
            return [self.tasks[task_id]]
        except IndexError:
            return []

    # Update
    # Delete
