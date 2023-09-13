from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4


class Task():

    def __init__(
        self,
        name: str,
        completed: Optional[datetime]
    ) -> None:
        self.id = uuid4()
        self.name = name
        self.completed = completed

    def __str__(self) -> str:
        return f"Task {self.id}: {self.name}{' (complete)' if self.completed else ''}"


class TaskList():

    def __init__(self):
        self.tasks = []

    # Create
    def add_task(
        self,
        task: Task,
    ):
        self.tasks.append(task)

    # Read
    def get_tasks(self) -> List[Task]:
        return self.tasks

    def get_task(
        self,
        task_id: UUID,
    ) -> Optional[Task]:
        try:
            for task in self.tasks:
                if task.id == task_id:
                    return task
        except IndexError:
            return
