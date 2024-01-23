# Write your code for lab 8C (remove) here.
from cal_ui import *


def remove(name: str, day: int, month: str, start: str) -> None:
    """Removes a booked appointment"""
    d = new_day(day)
    mon = new_month(month)
    start_time = new_time_from_string(start)
    cal_year = get_calendar(name)
    cal_month = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_month, d)

    if is_booked_from(cal_day, start_time):
        new_cal_day = remove_appointment(cal_day, start_time)
        new_cal_month = (cm_plus_cd(cal_month, new_cal_day))
        new_cal_year = cy_plus_cm(cal_year, new_cal_month)
        insert_calendar(name, new_cal_year)
        print("The appointment was removed")
    else:
        print("No appointment during that time exists")


def remove_appointment(cal_day, start_time):
    test = cal_day.appointments
    day = test.copy()
    for i in day:
        if ts_start(app_span(i)) == start_time:
            day.remove(i)
            return new_calendar_day(cd_day(cal_day), day)


create("Jayne")
book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
show("Jayne", 20, "sep")
remove("Jayne", 20, "sep", "20:00")
book("Jayne", 20, "sep", "15:00", "16:00", "Return loot")
show("Jayne", 20, "sep")