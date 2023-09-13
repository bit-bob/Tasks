from tasks import Task, TaskList
from datetime import datetime, timezone


def populate_demo_tasks(task_list, info):
    for name, completed in info:
        datetime.now().isoformat()
        task_list.add_task(Task(
            name=name,
            completed=completed,
        ))


demo_task_info = [
    (
        'Create Tasks - front end - storybook components - create button',
        None,
    ),
    (
        'Create Tasks - front end - storybook components - create form',
        None,
    ),
    (
        'Create Tasks - back end - endpoints',
        None,
    ),
    (
        'Create Tasks - front end - full implementation',
        None,
    ),
    (
        'Complete Tasks - front end - storybook components - complete button',
        datetime(2023, 9, 13, 12, 59, 5, tzinfo=timezone.utc),
    ),
    (
        'Complete Tasks - front end - storybook components - task text changes',
        datetime(2023, 9, 13, 14, 38, tzinfo=timezone.utc),
    ),
    (
        'Complete Tasks - back end - endpoints',
        datetime(2023, 9, 13, 14, 38, tzinfo=timezone.utc),
    ),
    (
        'Complete Tasks - front end - full implementation - toggle complete button',
        datetime(2023, 9, 13, 14, 38, tzinfo=timezone.utc),
    ),
    (
        'Complete Tasks - front end - full implementation - make text more faint when complete',
        datetime(2023, 9, 13, 14, 52, tzinfo=timezone.utc),
    ),
    (
        'Complete Tasks - front end - full implementation - move completed tasks to the bottom of the page',
        datetime(2023, 9, 13, 15, 58, 10, tzinfo=timezone.utc),
    ),
    (
        'Delete Tasks - front end - storybook components - delete button',
        datetime(2023, 9, 11, 18, 30, 8, tzinfo=timezone.utc),
    ),
    (
        'Delete Tasks - back end - endpoints',
        None,
    ),
    (
        'Delete Tasks - front end - full implementation',
        None,
    ),
    (
        'Update Tasks - front end - storybook components - edit button',
        None,
    ),
    (
        'Update Tasks - back end - endpoints',
        None,
    ),
    (
        'Update Tasks - front end - full implementation',
        None,
    ),
    (
        'Persisting Tasks',
        None,
    ),
    (
        'Task Events',
        None,
    ),
    (
        'Repeating Tasks',
        None,
    ),
    (
        'Parent Tasks',
        None,
    ),
    (
        'Local DB for offline use',
        None,
    ),
]

demo_tasks = TaskList()
populate_demo_tasks(demo_tasks, demo_task_info)
