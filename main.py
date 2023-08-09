

class Task():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)


class Tasks():

    _tasks = []

    def addTask(self, task: Task) -> None:
        self._tasks.append(task)

    def __str__(self) -> str:
        if self._tasks:
            return ", ".join([str(t) for t in self._tasks])
        return ""


if __name__ == "__main__":
    a = Task("beep")
    b = Task("boop")

    t = Tasks()
    t.addTask(a)
    t.addTask(b)

    print(a)
    print(b)
    print(t)
