from datetime import date, datetime, time
from csv import DictReader
from collections.abc import Iterator


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


def get_rotations(a_time:time) -> list[str]:
    """Given a time, return the associated rotations.

    Args:
        a_time (time): _description_

    Returns:
        list[str]: _description_
    """
    matched_rotations = []
    for a_name in ROTATIONS.keys():
        start = to_time(ROTATIONS[a_name]["Start"])
        end = to_time(ROTATIONS[a_name]["End"])
        if start <= a_time < end:
            matched_rotations.append(a_name)
        
    return matched_rotations

def fetch_spots(filename:str) -> Iterator[dict]:
    """Get spots from a CSV file

    Args:
        filename (str): _description_

    Yields:
        dict: _description_
    """
    with open(filename) as open_file:
        file_reader = DictReader(open_file)
        for a_row in file_reader:
            yield a_row

def collect_daily_data(filename:str) -> dict:
    """Collect daily data from the spots CSV file.

    Args:
        filename (str): _description_

    Returns:
        dict: _description_
    """
    daily_data = {}
    for a_row in fetch_spots(filename):
        a_date = to_date(a_row["Date"])
        a_time = to_time(a_row["Time"])
        spend = float(a_row["Spend"])
        views = int(a_row["Views"])
        
        rotations = get_rotations(a_time)
        
        if a_date not in daily_data:
            daily_data[a_date] = {}
        
        for a_rotation in rotations:
            if a_rotation not in daily_data[a_date]:
                daily_data[a_date][a_rotation] = {"Spend": 0.0, "Views": 0}
            daily_data[a_date][a_rotation]["Spend"] += spend
            daily_data[a_date][a_rotation]["Views"] += views
            
    return daily_data

def display_cpv(daily_data:dict):
    """Display CPV by date and rotation

    Args:
        daily_data (dict): _description_
    """
    print("Date, Rotation => CPV")
    for a_date in sorted(daily_data.keys()):
        for a_rotation in sorted(daily_data[a_date].keys()):
            spend = daily_data[a_date][a_rotation]["Spend"]
            views = daily_data[a_date][a_rotation]["Views"]
            if views > 0:
                cpv = spend / views
            else:
                cpv = spend # Technically inf, not sure that's useful
            print(f"{a_date}, {a_rotation} => {cpv:.4f}")

if __name__ == "__main__":
    daily_data = collect_daily_data(SPOTS_LOCATION)
    display_cpv(daily_data)
