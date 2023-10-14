from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4


class Task:
    def __init__(
        self,
        name: str,
        completed_date: Optional[datetime] = None,
    ) -> None:
        self.id = uuid4()
        self.name = name
        self.completed_date = completed_date
        self.created = datetime.now()

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return str(self)

    def __lt__(
        self,
        other: "Task",
    ):
        if (self.completed_date is None and other.completed_date is None) or (
            self.completed_date == other.completed_date
        ):
            # if both are incomplete or completed at the same time, check created timestamp
            return self.created < other.created

        if self.completed_date is None:
            # if other is complete, other is lt
            return True

        if other.completed_date is None:
            # if self is complete, self is lt
            return False

        # if both are complete, check completed_date
        return self.completed_date < other.completed_date


class TaskList:
    def __init__(self):
        self.tasks = []

    # Create
    def add_task(
        self,
        task: Task,
    ):
        self.tasks.append(task)

    def create_task(
        self,
        name: str,
    ):
        self.tasks.append(Task(name))

    # Read
    def get_tasks(
        self,
        to_sort: bool = True,
    ) -> List[Task]:
        if to_sort:
            return sorted(self.tasks)
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

    # Delete
    def delete_task(
        self,
        task_id: UUID,
    ) -> None:
        self.tasks = [t for t in self.tasks if t.id != task_id]
