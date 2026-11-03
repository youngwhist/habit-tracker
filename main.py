"""Демонстрация трекера привычек."""
from datetime import date

from habits import Habit

if __name__ == "__main__":
    water = Habit("Пить воду")
    for day in (1, 2, 3, 5):
        water.mark(date(2026, 11, day))
    print(water.name, "— отмечено дней:", len(water.done_days))
