from datetime import datetime

from tasks import Task


class TestTasks:
    def test_success(self):
        a = Task("a", datetime.now())
        b = Task("b", None)
        assert a > b
