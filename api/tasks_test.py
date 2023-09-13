from tasks import Task
from datetime import datetime

class TestTasks:
    def test_success(self):
        a = Task("a", datetime.now())
        b = Task("b", None)
        assert a > b
