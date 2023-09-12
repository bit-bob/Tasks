from typing import List


class Task():

    def __init__(
        self,
        name,
    ) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Task: {self.name}"


class TaskList():

    def __init__(self):
        self.tasks = []

    # Create
    def add_task(
        self,
        name: str,
    ):
        self.tasks.append(Task(name))

    # Read
    def get_tasks(self) -> List[Task]:
        return self.tasks

    def get_task(
        self,
        task_id: int,
    ) -> List[Task]:
        try:
            return [self.tasks[task_id]]
        except IndexError:
            return []
