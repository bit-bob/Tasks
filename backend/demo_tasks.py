import json
import logging
import sys
from datetime import datetime, timezone
from enum import Enum
from typing import Generator, List, Optional

from tasks import Task, TaskList

if __name__ == "__main__":
    # setup logs
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


class EnumWithTitle(Enum):
    @property
    def title(self):
        return self.name.title().replace("_", " ")


class DemoTaskEventType(EnumWithTitle):
    CREATE = 0
    START = 1
    PAUSE = 2
    COMPLETE = 3
    DROP = 4


class DemoTaskEvent:
    def __init__(
        self,
        date_args: Optional[List[int]] = None,
        type: Optional[DemoTaskEventType] = None,
    ) -> None:
        if self._type is None:
            self._type = type

        if date_args is None:
            self._date = None
        else:
            self._date = datetime(*date_args, tzinfo=timezone.utc)

    def __str__(self) -> str:
        return f"Event({'type=' + self._type.name if self._type is not None else ''} date={self._date})"

    @property
    def date(self) -> Optional[datetime]:
        return self._date

    @property
    def is_create(self) -> bool:
        return self._type == DemoTaskEventType.CREATE

    @property
    def is_start(self) -> bool:
        return self._type == DemoTaskEventType.START

    @property
    def is_pause(self) -> bool:
        return self._type == DemoTaskEventType.PAUSE

    @property
    def is_complete(self) -> bool:
        return self._type == DemoTaskEventType.COMPLETE

    @property
    def is_drop(self) -> bool:
        return self._type == DemoTaskEventType.DROP

    @property
    def is_in_future(self) -> bool:
        if self.date is None:
            return False

        now = datetime.now().replace(tzinfo=timezone.utc)
        return self.date > now


class DemoTaskEventStart(DemoTaskEvent):
    _type = DemoTaskEventType.START


class DemoTaskEventPause(DemoTaskEvent):
    _type = DemoTaskEventType.PAUSE


class DemoTaskEventComplete(DemoTaskEvent):
    _type = DemoTaskEventType.COMPLETE


class DemoTaskEventDrop(DemoTaskEvent):
    _type = DemoTaskEventType.DROP


class DemoTaskStatus(EnumWithTitle):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETE = 3
    ON_HOLD = 4


class RepetitionCycle(EnumWithTitle):
    DAILY = 1
    WEEKLY = 7
    MONTHLY = 30


class Priority(EnumWithTitle):
    ON_HOLD = 1
    WAITING = 2
    LOW = 4
    MEDIUM = 8
    HIGH = 16


class DemoTask:
    def __init__(
        self,
        name: str,
        children: Optional[List["DemoTask"]] = None,
        events: Optional[List[DemoTaskEvent]] = None,
        repetition: Optional[RepetitionCycle] = None,
        blocked_by: Optional[List[str]] = None,
        priority: Optional[Priority] = None,
    ) -> None:
        self._name = name

        self._parents = []
        self._children = children
        if self._children is not None:
            for child in self._children:
                child._parents.append(self)

        self._events = events
        self._repetition = repetition
        self._blocked_by = blocked_by
        self._priority = priority

    def __str__(self) -> str:
        return f"{self.path} ({self.status.name})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def parents(self) -> List["DemoTask"]:
        return self._parents

    @property
    def children(self) -> Optional[List["DemoTask"]]:
        return self._children

    @property
    def repetition(self) -> Optional[RepetitionCycle]:
        return self._repetition

    @property
    def status(self) -> DemoTaskStatus:
        if self.priority == Priority.ON_HOLD:
            return DemoTaskStatus.ON_HOLD

        if self._events is None or len(self._events) == 0:
            return DemoTaskStatus.NOT_STARTED

        last_started = self.last_started_event
        if last_started is not None:
            if last_started.is_in_future:
                return DemoTaskStatus.ON_HOLD

        last_completed = self.last_completed_date
        if last_completed is not None:
            if self.repetition is None:
                return DemoTaskStatus.COMPLETE

            now = datetime.now().replace(tzinfo=timezone.utc)
            time_delta = now - last_completed
            if time_delta.days < self.repetition.value:
                return DemoTaskStatus.COMPLETE

        return DemoTaskStatus.IN_PROGRESS

    @property
    def is_on_hold(self) -> bool:
        return self.status == DemoTaskStatus.ON_HOLD

    @property
    def is_not_started(self) -> bool:
        return self.status == DemoTaskStatus.NOT_STARTED

    @property
    def is_in_progress(self) -> bool:
        return self.status == DemoTaskStatus.IN_PROGRESS

    @property
    def is_complete(self) -> bool:
        return self.status == DemoTaskStatus.COMPLETE

    @property
    def is_waiting(self) -> bool:
        return self.priority == Priority.WAITING

    @property
    def last_started_event(self) -> Optional["DemoTaskEvent"]:
        if self._events is not None and len(self._events) > 0:
            for event in reversed(self._events):
                if event.is_start:
                    return event

    @property
    def last_started_date(self) -> Optional[datetime]:
        last_started_event = self.last_started_event
        if last_started_event is not None:
            return last_started_event.date

    @property
    def last_completed_event(self) -> Optional["DemoTaskEvent"]:
        if self._events is not None and len(self._events) > 0:
            for event in reversed(self._events):
                if event.is_complete:
                    return event

    @property
    def last_completed_date(self) -> Optional[datetime]:
        last_completed_event = self.last_completed_event
        if last_completed_event is not None:
            return last_completed_event.date

    @property
    def path(self) -> str:
        if self._parents is None or len(self._parents) == 0:
            return f"{self.name}"
        else:
            return f"{' - '.join([p.path for p in self._parents])} - {self.name}"

    @property
    def is_blocked(self) -> bool:
        return self._blocked_by is None

    @property
    def priority(self) -> Priority:
        if self._priority is not None:
            return self._priority

        if self.parents is not None:
            for parent in self.parents:
                return parent.priority

        return Priority.MEDIUM


tasks_task = DemoTask(
    "Make the Tasks App",
    children=[
        DemoTask(
            "Plan",
            repetition=RepetitionCycle.DAILY,
            events=[
                DemoTaskEventStart([2023, 9, 27, 11, 52]),
                DemoTaskEventPause([2023, 9, 27, 12, 45]),
                DemoTaskEventStart([2023, 9, 28, 12, 30]),
                DemoTaskEventPause([2023, 9, 28, 12, 45]),
                DemoTaskEventStart([2023, 10, 5, 16, 37]),
                DemoTaskEventComplete([2023, 10, 5, 16, 42]),
                DemoTaskEventStart([2023, 10, 10, 12, 32]),
                DemoTaskEventPause([2023, 10, 10, 13, 26]),
                DemoTaskEventStart([2023, 10, 10, 17, 18]),
                DemoTaskEventComplete([2023, 10, 10, 17, 38]),
            ],
            children=[
                DemoTask(
                    "Rewrite demo tasks to take more fields into account",
                    priority=Priority.HIGH,
                    events=[
                        DemoTaskEventStart([2023, 9, 26, 12]),
                        DemoTaskEventPause([2023, 9, 26, 14]),
                        DemoTaskEventStart([2023, 9, 26, 16, 20]),
                        DemoTaskEventPause([2023, 9, 26, 17, 35]),
                        DemoTaskEventStart([2023, 9, 26, 18, 50]),
                        DemoTaskEventPause([2023, 9, 26, 18, 59]),
                        DemoTaskEventStart([2023, 9, 27, 12, 45]),
                        DemoTaskEventPause([2023, 9, 27, 13, 40]),
                        DemoTaskEventStart([2023, 9, 27, 16, 23]),
                        DemoTaskEventPause([2023, 9, 27, 17, 12]),
                        DemoTaskEventStart([2023, 9, 28, 10, 35]),
                        DemoTaskEventPause([2023, 9, 28, 11, 10]),
                        DemoTaskEventStart([2023, 10, 3, 13, 23]),
                        DemoTaskEventPause([2023, 10, 3, 14, 5]),
                        DemoTaskEventStart([2023, 10, 3, 14, 37]),
                        DemoTaskEventPause([2023, 10, 3, 17, 5]),
                        DemoTaskEventStart([2023, 10, 3, 17, 43]),
                        DemoTaskEventPause([2023, 10, 3, 18, 1]),
                        DemoTaskEventStart([2023, 10, 3, 18, 16]),
                        DemoTaskEventPause([2023, 10, 3, 18, 41]),
                    ],
                    children=[
                        DemoTask(
                            "Add tasks as you do them",
                            events=[
                                DemoTaskEventStart([2023, 10, 6, 12]),
                                DemoTaskEventComplete([2023, 10, 6, 12, 25]),
                            ],
                        ),
                        DemoTask(
                            "Split DemoTasks and DemoTaskEvents into different structures so it mirrors the db more closely and makes it easier to see what order events were in",
                            priority=Priority.MEDIUM,
                        ),
                        DemoTask(
                            "Add Dropped Events",
                            events=[
                                DemoTaskEventStart([2023, 10, 5, 13, 41]),
                                DemoTaskEventComplete([2023, 10, 5, 13, 46]),
                            ],
                        ),
                        DemoTask(
                            "Treat Tasks with a start date in the future as On Hold",
                            events=[
                                DemoTaskEventStart([2023, 10, 5, 14, 2]),
                                DemoTaskEventComplete([2023, 10, 5, 14, 46]),
                            ],
                        ),
                        DemoTask(
                            "Make it clearer when tasks are complete or not",
                            events=[
                                DemoTaskEventStart([2023, 10, 5, 15, 53]),
                                DemoTaskEventComplete([2023, 10, 5, 16, 13]),
                            ],
                        ),
                        DemoTask(
                            "Print demo tasks more clearly when this file is run directly",
                            events=[
                                DemoTaskEventStart([2023, 10, 6, 12, 25]),
                                DemoTaskEventComplete([2023, 10, 6, 13, 6]),
                            ],
                        ),
                        DemoTask(
                            "Make Blocked a bool",
                            events=[
                                DemoTaskEventStart([2023, 10, 6, 14, 45]),
                                DemoTaskEventComplete([2023, 10, 6, 14, 50]),
                            ],
                        ),
                        DemoTask(
                            "Add Urgency",
                            priority=Priority.MEDIUM,
                            events=[
                                DemoTaskEventStart([2023, 10, 6, 14, 30]),
                                DemoTaskEventPause([2023, 10, 6, 17, 30]),
                            ],
                        ),
                        DemoTask(
                            "Add Defer Until Events",
                            events=[
                                DemoTaskEventStart([2023, 10, 6, 14, 30]),
                                DemoTaskEventPause([2023, 10, 6, 17, 30]),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "Add Demo Tasks From Notion",
                    children=[
                        DemoTask(
                            "Manually copy tasks",
                            events=[
                                DemoTaskEventStart([2023, 9, 26, 16, 15]),
                                DemoTaskEventPause([2023, 9, 26, 16, 20]),
                                DemoTaskEventStart([2023, 9, 26, 21, 10]),
                                DemoTaskEventPause([2023, 9, 26, 21, 25]),
                                DemoTaskEventStart([2023, 9, 27, 16, 2]),
                                DemoTaskEventPause([2023, 9, 27, 16, 23]),
                                DemoTaskEventStart([2023, 9, 28, 12, 45]),
                                DemoTaskEventPause([2023, 9, 28, 12, 55]),
                                DemoTaskEventStart([2023, 9, 28, 13, 56]),
                                DemoTaskEventPause([2023, 9, 28, 14, 42]),
                                DemoTaskEventStart([2023, 9, 30, 9, 55]),
                                DemoTaskEventPause([2023, 9, 30, 10, 30]),
                                DemoTaskEventStart([2023, 10, 5, 13, 37]),
                                DemoTaskEventPause([2023, 10, 5, 15, 53]),
                            ],
                        ),
                        DemoTask(
                            "Option 1 - CSV Export then Import",
                            priority=Priority.LOW,
                            children=[
                                DemoTask(
                                    "Export your notion tasks to a csv",
                                ),
                                DemoTask(
                                    "Filter your notion tasks to exclude tasks you want to keep in notion",
                                ),
                                DemoTask(
                                    "Store the exported tasks somewhere secure",
                                ),
                                DemoTask(
                                    "Delete exported tasks from notion",
                                ),
                                DemoTask(
                                    "Write a script to import demo tasks from a csv",
                                ),
                            ],
                        ),
                        DemoTask(
                            "Option 2 - Direct Import",
                            priority=Priority.LOW,
                            children=[
                                DemoTask(
                                    "Write a script to get your notion tasks using the api",
                                ),
                                DemoTask(
                                    "Keep track of which tasks have been exported",
                                ),
                                DemoTask(
                                    "Store the exported tasks somewhere secure",
                                ),
                                DemoTask(
                                    "Delete exported tasks from notion",
                                ),
                                DemoTask(
                                    "Make the script import the demo tasks to this app",
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        DemoTask(
            "Commit Something",
            repetition=RepetitionCycle.DAILY,
            priority=Priority.HIGH,
            events=[
                DemoTaskEventStart([2023, 10, 3, 18, 1]),
                DemoTaskEventComplete([2023, 10, 3, 18, 16]),
                DemoTaskEventStart([2023, 10, 5, 16, 15]),
                DemoTaskEventComplete([2023, 10, 5, 16, 42]),
            ],
        ),
        DemoTask(
            "Infrastructure",
            children=[
                DemoTask(
                    "Mobile Apps",
                    priority=Priority.LOW,
                    children=[
                        DemoTask(
                            "Plan",
                            events=[
                                DemoTaskEventStart([2023, 10, 10, 13, 26]),
                                DemoTaskEventPause([2023, 10, 10, 13, 40]),
                            ],
                            children=[
                                DemoTask(
                                    "Make Decisions",
                                    children=[
                                        DemoTask(
                                            "Do we want to run builds daily or only on commits with specific tags?",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        DemoTask(
                            "Setup Capacitor",
                        ),
                        DemoTask(
                            "iOS / Apple",
                            children=[
                                DemoTask(
                                    "Build the app using Firebase",
                                    children=[
                                        DemoTask(
                                            "Build manually",
                                            events=[
                                                DemoTaskEventComplete(
                                                    [2023, 10, 8, 21, 38]
                                                ),
                                            ],
                                        ),
                                        DemoTask(
                                            "Build automatically",
                                            events=[
                                                DemoTaskEventComplete(
                                                    [2023, 10, 8, 21, 38]
                                                ),
                                            ],
                                            children=[
                                                DemoTask(
                                                    "Add the secrets to github so firebase can access the api keys",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                DemoTask(
                                    "Get the IOS App on Helina's phone",
                                    priority=Priority.HIGH,
                                    children=[
                                        DemoTask(
                                            "Create the app in apple",
                                        ),
                                        DemoTask(
                                            "Tell firebase where the app is",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        DemoTask(
                            "Android",
                            children=[
                                DemoTask(
                                    "Build the app using Firebase",
                                    children=[
                                        DemoTask(
                                            "Build manually",
                                            events=[
                                                DemoTaskEventComplete(
                                                    [2023, 9, 25, 21, 49, 53]
                                                ),
                                            ],
                                        ),
                                        DemoTask(
                                            "Build automatically",
                                            children=[
                                                DemoTask(
                                                    "Log into firebase",
                                                    events=[
                                                        DemoTaskEventComplete(
                                                            [2023, 10, 10, 13, 40]
                                                        ),
                                                    ],
                                                ),
                                                DemoTask(
                                                    "Go to the firebase console",
                                                    events=[
                                                        DemoTaskEventComplete(
                                                            [2023, 10, 10, 13, 41]
                                                        ),
                                                    ],
                                                ),
                                                DemoTask(
                                                    "get luke to add helina as a member / owner",
                                                    events=[
                                                        DemoTaskEventComplete(
                                                            [2023, 10, 10, 13, 42]
                                                        ),
                                                    ],
                                                ),
                                                DemoTask(
                                                    "accept the invite",
                                                    events=[
                                                        DemoTaskEventComplete(
                                                            [2023, 10, 10, 13, 42]
                                                        ),
                                                    ],
                                                ),
                                                DemoTask(
                                                    "get luke to make a service account for helina",
                                                    events=[
                                                        DemoTaskEventComplete(
                                                            [2023, 10, 10, 13, 44]
                                                        ),
                                                    ],
                                                ),
                                                DemoTask(
                                                    "get the credentials to distribute the app through firebase, see https://github.com/wzieba/Firebase-Distribution-Github-Action/wiki/FIREBASE_TOKEN-migration",
                                                    events=[
                                                        DemoTaskEventComplete(
                                                            [2023, 10, 10, 13, 44]
                                                        ),
                                                    ],
                                                ),
                                                DemoTask(
                                                    "add the firebase credentials to the github secrets",
                                                    events=[
                                                        DemoTaskEventComplete(
                                                            [2023, 10, 10, 13, 50]
                                                        ),
                                                    ],
                                                ),
                                                DemoTask(
                                                    "add the 'upload artifact to Firebase App Distribution' to the capacitor CI",
                                                    events=[
                                                        DemoTaskEventComplete(
                                                            [2023, 10, 10, 13, 52]
                                                        ),
                                                    ],
                                                ),
                                                DemoTask(
                                                    "Follow https://medium.com/firebase-developers/quickly-distribute-app-with-firebase-app-distribution-using-github-actions-fastlane-c7d8eca18ee0",
                                                    events=[
                                                        DemoTaskEventStart(
                                                            [2023, 10, 10, 13, 52]
                                                        ),
                                                        DemoTaskEventPause(
                                                            [2023, 10, 10, 2, 46]
                                                        ),
                                                        DemoTaskEventPause(
                                                            [2023, 10, 10, 17, 7]
                                                        ),
                                                        DemoTaskEventStart(
                                                            [2023, 10, 10, 17, 18]
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        DemoTask(
                            "Trigger App builds more intentionally, not just every commit",
                            children=[
                                DemoTask(
                                    "Figure out how do we do this",
                                ),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "Setup the staging environment",
                ),
                DemoTask(
                    "Automate release notes",
                    children=[
                        DemoTask(
                            "Figure out how do we do this",
                        ),
                    ],
                ),
                DemoTask(
                    "other cool things",
                ),
            ],
        ),
        DemoTask(
            "Day 0 - CRUD and Complete",
            children=[
                DemoTask(
                    "Create",
                    children=[
                        DemoTask(
                            "Front End",
                            events=[
                                DemoTaskEventComplete([2023, 9, 25, 17, 38]),
                            ],
                        ),
                        DemoTask(
                            "Back End",
                            events=[
                                DemoTaskEventComplete([2023, 9, 25, 16, 50]),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "Read",
                    children=[
                        DemoTask(
                            "Design",
                            events=[
                                DemoTaskEventComplete([2023, 9, 10, 21, 17, 36]),
                            ],
                        ),
                        DemoTask(
                            "Front End",
                            priority=Priority.ON_HOLD,
                        ),
                        DemoTask(
                            "Back End",
                            priority=Priority.ON_HOLD,
                        ),
                    ],
                ),
                DemoTask(
                    "Update",
                    children=[
                        DemoTask(
                            "Front End",
                            children=[
                                DemoTask(
                                    "Make an inline edit component",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 14, 6, 30, 51]),
                                    ],
                                ),
                                DemoTask(
                                    "Use the inline edit component in the task list item component",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 16, 14, 6, 0]),
                                    ],
                                ),
                                DemoTask(
                                    "Link editing the task list item component with the backend update endpoint",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 20, 13, 5]),
                                    ],
                                ),
                            ],
                        ),
                        DemoTask(
                            "Back End",
                            events=[
                                DemoTaskEventComplete([2023, 9, 14, 13, 23, 45]),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "Delete",
                    children=[
                        DemoTask(
                            "Design",
                            priority=Priority.ON_HOLD,
                        ),
                        DemoTask(
                            "Front End",
                            children=[
                                DemoTask(
                                    "Make the 'delete' button component",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 11, 18, 30, 8]),
                                    ],
                                ),
                                DemoTask(
                                    "Link the 'delete' button with the backend delete endpoint",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 20, 11, 53]),
                                    ],
                                ),
                            ],
                        ),
                        DemoTask(
                            "Back End",
                            events=[
                                DemoTaskEventComplete([2023, 9, 20, 11, 53]),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "Complete",
                    children=[
                        DemoTask(
                            "Design",
                            priority=Priority.ON_HOLD,
                        ),
                        DemoTask(
                            "Front End",
                            children=[
                                DemoTask(
                                    "Make the 'complete' button component",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 13, 12, 59, 5]),
                                    ],
                                ),
                                DemoTask(
                                    "Make the 'complete' button toggle on click",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 13, 14, 38]),
                                    ],
                                ),
                                DemoTask(
                                    "Make text more faint when complete in storybook",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 13, 14, 38]),
                                    ],
                                ),
                                DemoTask(
                                    "Make text more faint when complete in the main page",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 13, 14, 52]),
                                    ],
                                ),
                            ],
                        ),
                        DemoTask(
                            "Back End",
                            children=[
                                DemoTask(
                                    "Add 'Complete' endpoint",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 13, 14, 38]),
                                    ],
                                ),
                                DemoTask(
                                    "Sort tasks so completed tasks are at the bottom of the page",
                                    events=[
                                        DemoTaskEventComplete(
                                            [2023, 9, 13, 15, 58, 10]
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "Persist tasks in a Database",
                    children=[
                        DemoTask(
                            "Back End",
                            children=[
                                DemoTask(
                                    "Pick a db",
                                ),
                                DemoTask(
                                    "Make the db and tables",
                                ),
                                DemoTask(
                                    "Write a script to add demo data to the db",
                                ),
                                DemoTask(
                                    "Consider taking database dumps regularly for backups, see https://linuxhint.com/automatically-backup-mysql-database-using-python/",
                                ),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "Add Logging",
                    priority=Priority.HIGH,
                    children=[
                        DemoTask(
                            "Find where else you used logs",
                            events=[
                                DemoTaskEventStart([2023, 9, 30, 9, 48]),
                                DemoTaskEventComplete([2023, 9, 30, 9, 55]),
                            ],
                        ),
                        DemoTask(
                            "Use logs here",
                            children=[
                                DemoTask(
                                    "Add a basic log and check it works when using the app",
                                    events=[
                                        DemoTaskEventStart([2023, 10, 5, 14, 50]),
                                        DemoTaskEventComplete([2023, 10, 5, 14, 56]),
                                    ],
                                ),
                                DemoTask(
                                    "Figure out how to see debug level logs",
                                    events=[
                                        DemoTaskEventStart([2023, 10, 5, 14, 56]),
                                        DemoTaskEventComplete([2023, 10, 5, 15, 10]),
                                    ],
                                ),
                                DemoTask(
                                    "Add logs for each endpoint",
                                    events=[
                                        DemoTaskEventStart([2023, 10, 5, 15, 19]),
                                        DemoTaskEventComplete([2023, 10, 5, 15, 26]),
                                    ],
                                ),
                                DemoTask(
                                    "Increase the time between update requests to capture a more complete change when typing",
                                    events=[
                                        DemoTaskEventStart([2023, 10, 5, 15, 26]),
                                        DemoTaskEventComplete([2023, 10, 5, 15, 41]),
                                    ],
                                ),
                                DemoTask(
                                    "Make logs easier to read",
                                    events=[
                                        DemoTaskEventStart([2023, 10, 5, 16, 22]),
                                        DemoTaskEventComplete([2023, 10, 5, 16, 37]),
                                    ],
                                ),
                                DemoTask(
                                    "Add extra information to logs, see https://gist.github.com/liviaerxin/d320e33cbcddcc5df76dd92948e5be3b",
                                    priority=Priority.LOW,
                                    events=[
                                        DemoTaskEventStart([2023, 10, 6, 14, 6]),
                                        DemoTaskEventComplete([2023, 10, 6, 14, 30]),
                                    ],
                                ),
                                DemoTask(
                                    "Store logs in a text file",
                                    priority=Priority.LOW,
                                    events=[
                                        DemoTaskEventStart([2023, 10, 6, 14, 6]),
                                        DemoTaskEventComplete([2023, 10, 6, 14, 30]),
                                    ],
                                ),
                            ],
                        ),
                        DemoTask(
                            "Test logs by using the app a few times",
                            events=[
                                DemoTaskEventStart([2023, 10, 5, 16, 37]),
                                DemoTaskEventComplete([2023, 10, 5, 16, 42]),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "Fix Bugs",
                    priority=Priority.HIGH,
                    children=[
                        DemoTask(
                            "If you edit a task then immediately complete it, if the update request hasn't been sent to the backend yet, the update doesn't persist",
                        ),
                    ],
                ),
            ],
        ),
        DemoTask(
            "Day 1 - Basic Use",
            children=[
                DemoTask(
                    "Events",
                    priority=Priority.LOW,
                    children=[
                        DemoTask(
                            "Decisions",
                            children=[
                                DemoTask(
                                    "Do we want a calendar?",
                                ),
                                DemoTask(
                                    "Do we want a list in the 'Edit' page?",
                                ),
                                DemoTask(
                                    "Should we let users edit or delete events?",
                                ),
                                DemoTask(
                                    "Do we want to use an event sourcing pattern or something else?",
                                ),
                            ],
                        ),
                        DemoTask(
                            "Design",
                            children=[
                                DemoTask(
                                    "Design an Events Page like in aTimeLogger in figma",
                                    priority=Priority.HIGH,
                                ),
                                DemoTask(
                                    "Design how users will play / pause / complete in figma",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 10, 18, 55, 6]),
                                    ],
                                ),
                                DemoTask(
                                    "Design how users will see event history",
                                    priority=Priority.LOW,
                                ),
                            ],
                        ),
                        DemoTask(
                            "Front End",
                            priority=Priority.ON_HOLD,
                            children=[
                                DemoTask(
                                    "Make a play / pause / playing pill component",
                                    events=[
                                        DemoTaskEventComplete([2023, 9, 10, 18, 55, 6]),
                                    ],
                                ),
                            ],
                        ),
                        DemoTask(
                            "Back End",
                            children=[
                                DemoTask(
                                    "Add 'Events' to the task model",
                                ),
                                DemoTask(
                                    "Add endpoints for 'Events'",
                                    children=[
                                        DemoTask(
                                            "Add a 'Play' endpoint for 'Events'",
                                        ),
                                        DemoTask(
                                            "Add a 'Pause' endpoint for 'Events'",
                                        ),
                                        DemoTask(
                                            "Add a 'Complete' endpoint",
                                        ),
                                        DemoTask(
                                            "Make the 'Complete' endpoint more consistent with the 'Play' and 'Pause' endpoints",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        DemoTask(
                            "Calculate Status based on Events",
                            priority=Priority.ON_HOLD,
                        ),
                    ],
                ),
                DemoTask(
                    "Completed Page",
                    priority=Priority.LOW,
                    children=[
                        DemoTask(
                            "Design",
                            children=[
                                DemoTask(
                                    "Design a 'Completed' page in figma",
                                ),
                                DemoTask(
                                    "Design a navigation bar at the bottom with icons for the 'Tasks' and 'Completed' pages in figma"
                                ),
                            ],
                        ),
                        DemoTask(
                            "Front End",
                            priority=Priority.ON_HOLD,
                            children=[
                                DemoTask(
                                    "Add the 'Completed' page",
                                ),
                                DemoTask(
                                    "Split the structure of the navigation bar to make shared parts more generic",
                                ),
                                DemoTask(
                                    "Add the navigation bar",
                                ),
                            ],
                        ),
                        DemoTask(
                            "Back End",
                            priority=Priority.ON_HOLD,
                        ),
                    ],
                ),
                DemoTask(
                    "Edit Page",
                    priority=Priority.LOW,
                    children=[
                        DemoTask(
                            "Design",
                            children=[
                                DemoTask(
                                    "Design a 'Edit' page in figma",
                                ),
                                DemoTask(
                                    "Design an 'Edit' button in the TaskListItem component in figma"
                                ),
                                DemoTask(
                                    "Design a navigation bar at the top of th page to go back to the tasks list in figma"
                                ),
                            ],
                        ),
                        DemoTask(
                            "Front End",
                            priority=Priority.ON_HOLD,
                            children=[
                                DemoTask(
                                    "Add an 'Edit' button to the TaskListItem component to will open the 'Edit' page",
                                ),
                                DemoTask(
                                    "Add a navigation bar to go back to the main page from the 'Edit' page",
                                ),
                                DemoTask(
                                    "Add the 'Edit' page",
                                ),
                                DemoTask(
                                    "Send the requests the backend endpoint to edit the current task",
                                ),
                            ],
                        ),
                        DemoTask(
                            "Back End",
                            priority=Priority.ON_HOLD,
                        ),
                    ],
                ),
                DemoTask(
                    "Filtering",
                    priority=Priority.LOW,
                    children=[
                        DemoTask(
                            "Descisions",
                            children=[
                                DemoTask("What do we want to filter on?"),
                            ],
                        ),
                        DemoTask(
                            "Filter on status",
                            priority=Priority.ON_HOLD,
                            children=[
                                DemoTask(
                                    "Design",
                                ),
                                DemoTask(
                                    "Front End",
                                ),
                                DemoTask(
                                    "Back End",
                                ),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "Goals",
                    children=[
                        DemoTask(
                            "Design",
                        ),
                        DemoTask(
                            "Front End",
                        ),
                        DemoTask(
                            "Back End",
                        ),
                    ],
                ),
                DemoTask(
                    "Statistics Page",
                    children=[
                        DemoTask(
                            "Page",
                            children=[
                                DemoTask(
                                    "Design",
                                ),
                                DemoTask(
                                    "Front End",
                                ),
                                DemoTask(
                                    "Back End",
                                ),
                            ],
                        ),
                        DemoTask(
                            "Graphs",
                            children=[
                                DemoTask(
                                    "aTimeLogger style graphs",
                                    children=[
                                        DemoTask(
                                            "Design",
                                        ),
                                        DemoTask(
                                            "Front End",
                                        ),
                                        DemoTask(
                                            "Back End",
                                        ),
                                    ],
                                ),
                                DemoTask(
                                    "GitHub / Anki Style completion squares",
                                    children=[
                                        DemoTask(
                                            "Design",
                                        ),
                                        DemoTask(
                                            "Front End",
                                        ),
                                        DemoTask(
                                            "Back End",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                DemoTask(
                    "iPhone Dynamic Island Task Status",
                ),
                DemoTask(
                    "Iphone Widget",
                    children=[
                        DemoTask(
                            "Task Status",
                        ),
                        DemoTask(
                            "Stats",
                        ),
                    ],
                ),
            ],
        ),
        DemoTask(
            "Day ? - Users, Persistence and Settings",
            children=[
                DemoTask(
                    "Make Users",
                ),
                DemoTask(
                    "Add App Wide Settings",
                    priority=Priority.LOW,
                    children=[
                        DemoTask(
                            "Colour Themes",
                        ),
                        DemoTask(
                            "Emojis for Priorities",
                        ),
                    ],
                ),
            ],
        ),
        DemoTask(
            "Day 3 - Everything Else",
            priority=Priority.LOW,
            children=[
                # "Priority": {
                #     "Design": [
                #         "Design how the 'Priority' will be shown in figma",
                #         "Decide whether you want to let users sort tasks manually or if you want it to be calculated based on other fields etc",
                #     ],
                #     "Front End": [
                #         "Add the 'Priority' to the front end components",
                #     ],
                #     "Back End": [
                #         "Add a 'Priority' field to the task model",
                #         "Add the new 'Priority' field to each existing endpoint",
                #         "Sort tasks by the 'Priority' field",
                #     ],
                # },
                # "Urgency": {
                #     "Design": [
                #         "Design how the 'Urgency' will be shown in figma",
                #         "Decide whether you want to let users sort tasks manually or if you want it to be calculated based on other fields etc",
                #     ],
                #     "Front End": [
                #         "Add the 'Urgency' to the front end components",
                #     ],
                #     "Back End": [
                #         "Add a 'Urgency' field to the task model",
                #         "Add the new 'Urgency' field to each existing endpoint",
                #         "Sort tasks by the 'Urgency' field",
                #     ],
                # },
                # "Due Dates": {
                #     "Design": [
                #         "Design the due date input in figma",
                #     ],
                #     "Front End": [
                #         "Add a generic date picker component",
                #         "Add the date picker component to the edit tasks page",
                #         "Send the choice from the date picker component to the 'Update' endpoint",
                #     ],
                #     "Back End": [
                #         "Add a 'Due Date' field to the task model",
                #         "Use the 'Due Date' field in each existing endpoint",
                #         "Sort tasks by the 'Due Date' field",
                #     ],
                # },
                # "Commitment": {
                #     "Design": [
                #         "Consider how you would describe committment to a task, definite, optional, suggestion only?",
                #         "Design how the user would pick a committment level in figma",
                #     ],
                # },
                # "Ordering": {
                #     "Decisions": [
                #         "Decide whether you want to let users sort tasks manually or if you want it to be calculated based on other fields etc",
                #         "Decide whether you want to let users manually input an order or sort graphically",
                #     ],
                #     "Option 1 - Let users set the order manually": {
                #         "Design": [
                #             "Add an input box for the order to figma",
                #         ],
                #         "Front End": [
                #             "Add the 'Ordering' to the front end components",
                #         ],
                #         "Back End": [
                #             "Add an 'Order' field to the task model",
                #             "Add the new 'Order' field to each existing endpoint",
                #             "Sort tasks by the 'Order' field",
                #         ],
                #     },
                #     "Option 2 - Let users set the order by dragging and dropping": {
                #         "Design": [
                #             "Design a handle for dragging tasks in figma",
                #         ],
                #         "Front End": [
                #             "Look into drag and drop libraries like https://react-dnd.github.io/react-dnd/examples/sortable/simple",
                #             "Edit the simple drag and drop sandbox example to make the tasks stay fixed from side to side https://codesandbox.io/s/github/react-dnd/react-dnd/tree/gh-pages/examples_ts/02-drag-around/custom-drag-layer?from-embed=&file=/src/snapToGrid.ts",
                #             "Add drag and drop to the main tasks page",
                #             "Send the resulting position of the drag and drop to the back end endpoints",
                #             "Make sure drag and drop is disabled in the completed tasks page",
                #         ],
                #         "Back End": [
                #             "Add a 'Order' Field to the task model",
                #             "Add the new 'Order' field to each existing endpoint",
                #             "Sort tasks by the 'Order' field",
                #         ],
                #     },
                # },
                # "Repeating Tasks": {
                #     "Decisions": [
                #         "Figure out how you want this to work on the back end",
                #         "Decide whether to have a separation between tasks that can be ignored if you don't do them on schedule, or tasks that persist when ignored",
                #     ],
                #     "Design": [
                #         "Design the 'Repeat Schedule' in figma",
                #     ],
                #     "Front End": [
                #         "Make a 'Repeat Schedule' component",
                #     ],
                #     "Back End": [],
                # },
                # "Parents and Children": {
                #     "Design": [
                #         "Design a task picker in figma",
                #         "Design how to add parents or children to tasks in figma",
                #         "Design how to display parent or child tasks in figma",
                #     ],
                #     "Front End": [
                #         "Make the task picker component",
                #         "Design how to add parents or children to tasks in figma",
                #         "Design how to display parent or child tasks in figma",
                #     ],
                #     "Back End": [
                #         "Decide how to model parents and children in the db",
                #     ],
                # },
                # "Profiling to figure out what parts are slow",
                # "Monitoring to figure out what parts are getting slow or how things are scaling",
                # "General Research": [
                #     "Consider using elasticsearch for read heavy parts of the code",
                #     "Consider using a graph database for relationship heavy parts of the code",
                #     "Read about using recursive queries for relationship heavy parts of the code https://www.postgresql.org/docs/current/queries-with.html",
                #     "Read about using ltree for hierarchy heavy parts of the code https://www.postgresql.org/docs/current/ltree.html",
                # ],
                # }
            ],
        ),
    ],
)


def get_grandchildren(
    task: DemoTask,
):
    if task.children is None:
        yield task
    else:
        for child in task.children:
            yield from get_grandchildren(child)


def ppprint(input: dict) -> None:
    print(json.dumps(input, indent=4, default=lambda o: str(o)))


def get_next_task(
    tasks_included: List[DemoTask],
    priorities_included: Optional[List[Priority]] = None,
    statuses_included: Optional[List[DemoTaskStatus]] = None,
) -> Generator:
    tasks_grouped: dict[DemoTaskStatus, dict[Priority, list[DemoTask]]] = {
        s: {p: [] for p in Priority} for s in DemoTaskStatus
    }

    for demo_task in tasks_included:
        for child in get_grandchildren(demo_task):
            tasks_grouped[child.status][child.priority].append(child)

    for priority in reversed(Priority):
        if priorities_included is not None:
            if priority not in priorities_included:
                continue

        for status in DemoTaskStatus:
            if statuses_included is not None:
                if status not in statuses_included:
                    continue

            printed_heading = False
            for task in tasks_grouped[status][priority]:
                if not printed_heading:
                    heading_body = f"{status.title}"
                    if not task.is_on_hold:
                        heading_body = f"{heading_body}, {priority.title}"
                        if not task.is_waiting:
                            heading_body = f"{heading_body} Priority"

                    logging.debug(f"\n == {heading_body} == ")
                    printed_heading = True

                yield Task(
                    name=""
                    # + task.status.name
                    # + " - "
                    # + task.priority.name
                    # + " - "
                    + task.path,
                    completed=task.last_completed_date
                    if status == DemoTaskStatus.COMPLETE
                    else None,
                )


def populate_demo_tasks(
    task_list: TaskList,
    tasks_included: List[DemoTask],
    priorities_included: Optional[List[Priority]] = None,
    statuses_included: Optional[List[DemoTaskStatus]] = None,
):
    for task in get_next_task(
        tasks_included,
        priorities_included,
        statuses_included,
    ):
        task_list.add_task(task)


demo_tasks = TaskList()


if __name__ == "__main__":
    logging.debug(f"\n\n\n ==== TASKS ({datetime.now():%Y %b %d, %H:%M}) ==== ")
    for task in get_next_task(
        [
            tasks_task,
        ],
        # priorities_included=[
        #     Priority.HIGH,
        #     Priority.MEDIUM,
        #     Priority.LOW,
        #     Priority.WAITING,
        # ],
        # statuses_included=[
        #     DemoTaskStatus.COMPLETE,
        #     DemoTaskStatus.IN_PROGRESS,
        #     DemoTaskStatus.NOT_STARTED,
        #     DemoTaskStatus.ON_HOLD,
        # ],
    ):
        logging.debug(task)

else:
    populate_demo_tasks(
        demo_tasks,
        [
            tasks_task,
        ],
        priorities_included=[
            Priority.HIGH,
            Priority.MEDIUM,
            # Priority.LOW,
            # Priority.WAITING,
            # Priority.ON_HOLD,
        ],
        statuses_included=[
            DemoTaskStatus.NOT_STARTED,
            DemoTaskStatus.IN_PROGRESS,
            # DemoTaskStatus.COMPLETE,
            # DemoTaskStatus.ON_HOLD,
        ],
    )
