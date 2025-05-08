from datetime import date, datetime, time


ROTATIONS = {
    "Morning": {"Start": "6:00 AM", "End": "12:00 PM"},
    "Afternoon": {"Start": "12:00 PM", "End": "4:00 PM"},
    "Prime": {"Start": "3:00 PM", "End": "8:00 PM"},
}
SPOTS_LOCATION = 'spots.csv'


def to_time(time_: str) -> time:
    return datetime.strptime(time_, "%I:%M %p").time()


def to_date(date_: str) -> date:
    return datetime.strptime(date_, "%m/%d/%Y").date()


def get_rotations():
    '''Given a time, return the associated rotations.'''
    ...
