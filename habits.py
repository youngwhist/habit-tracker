"""Привычки и отметки выполнения по дням."""
from datetime import date


class Habit:
    """Привычка с множеством дат, когда она выполнена."""

    def __init__(self, name):
        self.name = name
        self.done_days = set()

    def mark(self, day=None):
        """Отмечает выполнение за день (по умолчанию — сегодня)."""
        self.done_days.add(day or date.today())
