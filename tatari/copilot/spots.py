from datetime import date, datetime, time
import csv
from collections import defaultdict


ROTATIONS = {
    "Morning": {"Start": "6:00 AM", "End": "12:00 PM"},
    "Afternoon": {"Start": "12:00 PM", "End": "4:00 PM"},
    "Prime": {"Start": "3:00 PM", "End": "8:00 PM"},
}
SPOTS_LOCATION = '../spots.csv'


def to_time(time_: str) -> time:
    return datetime.strptime(time_, "%I:%M %p").time()


def to_date(date_: str) -> date:
    return datetime.strptime(date_, "%m/%d/%Y").date()


def get_rotations(spot_time) -> list:
    """Return all rotation names that the spot_time falls into (for overlapping windows).
    If spot_time is not a datetime.time instance, return ['Other'].
    """
    from datetime import time as dt_time
    if not isinstance(spot_time, dt_time):
        return ["Other"]
    matches = []
    for name, window in ROTATIONS.items():
        start = to_time(window["Start"])
        end = to_time(window["End"])
        if start <= spot_time < end or (start > end and (spot_time >= start or spot_time < end)):
            matches.append(name)
    return matches if matches else ["Other"]


def read_spots(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield {
                "date": to_date(row["Date"]),
                "time": to_time(row["Time"]),
                "spend": float(row["Spend"]),
                "views": int(row["Views"])
            }


def cpv_by_rotation_by_day():
    # Nested dict: {date: {rotation: {"spend": x, "views": y}}}
    stats = defaultdict(lambda: defaultdict(lambda: {"spend": 0.0, "views": 0}))
    for spot in read_spots(SPOTS_LOCATION):
        rotations = get_rotations(spot["time"])
        d = spot["date"]
        for rotation in rotations:
            stats[d][rotation]["spend"] += spot["spend"]
            stats[d][rotation]["views"] += spot["views"]

    # Print results
    print("Date       | Rotation  | Spend   | Views | CPV")
    print("-----------|-----------|---------|-------|------")
    for d in sorted(stats):
        for rotation in ROTATIONS:
            spend = stats[d][rotation]["spend"]
            views = stats[d][rotation]["views"]
            cpv = (spend / views) if views else 0
            print(f"{d} | {rotation:<9} | {spend:7.2f} | {views:5d} | {cpv:.4f}")


if __name__ == "__main__":
    cpv_by_rotation_by_day()
