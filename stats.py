from datetime import timedelta
def LongestStreak(days):
    if not days: return 0
    best=current=1
    ordered=sorted(days)
    for prev,cur in zip(ordered,ordered[1:]):
        if cur-prev==timedelta(days=1):
            current+=1
            best=max(best,current)
        else: current=1
    return best
