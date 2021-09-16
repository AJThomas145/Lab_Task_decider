import unittest
from src.task_decider import *
from src.task import Task

class TestTaskDecider(unittest.TestCase):

    def setUp(self):
        self.task1 = Task("Wash Dishes", 15)
        self.task2 = Task("Cook Dinner", 30)
        self.task3 = Task("Clean Windows", 45)

    def test_task_1_equals_task_2(self):
        self.assertEqual(True, tasks_match(self.task1, self.task1))

    def test_task_1_does_not_equal_task_2(self):
        self.assertEqual(False, tasks_match(self.task1, self.task2))

    def test_which_task_is_preferred_Wash_Dishes(self):
        self.assertEqual("Wash Dishes", get_preferred_option(self.task1, self.task2))
    
    def test_which_task_is_preferred_Clean_Windows(self):
        self.assertEqual("Clean Windows", get_preferred_option(self.task3, self.task1))

    def test_which_task_is_preferred_Cook_Dinner(self):
        self.assertEqual("Cook Dinner", get_preferred_option(self.task2, self.task3))

    def test_which_task_is_preferred_Wash_Dishes_2(self):
        self.assertEqual("Wash Dishes", get_preferred_option(self.task2, self.task1))

    def test_which_task_is_preferred_Cook_Dinner_2(self):
        self.assertEqual("Cook Dinner", get_preferred_option(self.task3, self.task2))

    def test_which_task_is_preferred_Clean_Windows_2(self):
        self.assertEqual("Clean Windows", get_preferred_option(self.task1, self.task3))

    def test_which_task_is_preferred_tasks_the_same(self):
        self.assertEqual("Wash Dishes", get_preferred_option(self.task1, self.task1))
      
