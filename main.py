from typing import List


class Task():

    # should be sorted by date completed
    _instances = []

    def __init__(self, name, repeats_seconds: int = 0) -> None:
        self.name = name
        self._repeats_seconds = repeats_seconds

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)

    def add_instance(self, due: int) -> None:
        t = TaskInstance(due, self)
        self._instances.append(t)

    def instances(self) -> List['TaskInstance']:
        return self._instances

    def last_instance(self) -> None:
        return self._instances[-1]


class TaskInstance():

    _task = None

    def __init__(self, due: int, task: Task) -> None:
        self._due = due
        self._task = task

    def __str__(self) -> str:
        return f"due: {self._due}"

    def __repr__(self) -> str:
        return str(self)


class Tasks():

    _tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        self._tasks.append(task)

    def __str__(self) -> str:
        rv = ""

        if self._tasks:

            rv += "Tasks:\n"

            task_instances = [t.instances() for t in self._tasks]
            for task in self._tasks:

                rv += f"\n - {task}"

                instances = task.instances()
                for instance in instances:

                    rv += f"\n   - {str(instance)}"

            return rv
        return ""


if __name__ == "__main__":
    a = Task("beep")
    a.add_instance(1)

    b = Task("boop")

    brush_teeth_task = Task('brush teeth', 28800)
    brush_teeth_task.add_instance(2)

    tasks = Tasks()
    tasks.add_task(a)
    tasks.add_task(b)
    tasks.add_task(brush_teeth_task)

    print(a)
    print(b)
    print(brush_teeth_task)
    print(tasks)
