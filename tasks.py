from typing import List
from uuid import uuid4


class Task():

    def __init__(
        self,
        name: str,
    ) -> None:
        self.id = uuid4()
        self.name = name

    def __str__(self) -> str:
        return f"Task {self.id}: {self.name}"


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
