import unittest
from src.task import Task

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task1 = Task("Wash Dishes", 15)
        self.task2 = Task("Cook Dinner", 30)
        self.task3 = Task("Clean Windows", 45)

    def test_task_has_description(self):
        self.assertEqual("Wash Dishes", self.task1.name)

    def test_task_has_duration(self):
        self.assertEqual(15, self.task1.duration)