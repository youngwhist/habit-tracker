"""Статистика по привычкам."""
from datetime import timedelta


def longest_streak(days):
    """Длина самой длинной серии подряд идущих дней."""
    if not days:
        return 0
    best = current = 1
    ordered = sorted(days)
    for prev, cur in zip(ordered, ordered[1:]):
        if cur - prev == timedelta(days=1):
            current += 1
            best = max(best, current)
        else:
            current = 1
    return best
