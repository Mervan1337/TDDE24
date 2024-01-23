# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT
from cal_ui import *
from cal_booking import *
from lab8a import *
from lab8b import *

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def app_start(app) -> Time:
    return ts_start(app.span)


def app_end(app) -> Time:
    return  ts_end(app.span)


def app_span(app) -> TimeSpan:
    return app.span


def time_spans_max_span(ts1, ts2) -> TimeSpan:
    min1 = min(
        t_number(ts_start(ts1)),  #
        t_number(ts_start(ts2))
    )
    min2 = max(
        t_number(ts_end(ts1)),  #
        t_number(ts_end(ts2))
    )
    t1 = new_time(new_hour(min1 // 60), new_minute(min1 % 60))
    t2 = new_time(new_hour(min2 // 60), new_minute(min2 % 60))
    return new_time_span(t1, t2)


def cd_tss(cd) -> list:
    time_spans = []
    for app in cd.appointments:
        app_ts = app_span(app)
        time_spans.append(app_ts)
    return time_spans


def t_in_ts(t, ts) -> bool :
    start = ts_start(ts)
    end = ts_end(ts)
    start_num = t_number(start)
    end_num = t_number(end)
    t_num = t_number(t)
    if start_num < t_num < end_num:
        return True
    return False


def t_number(t) -> int:
    return time_hour_number(t) * 60 + time_minute_number(t)


def t_to_string(t) -> str:
    hour = str(time_hour_number(t))
    min = str(time_minute_number(t))

    if len(hour) == 1:
        hour = "0"+hour
    if len(min) == 1:
        min = "0"+min

    return f"{hour}:{min}"


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    ensure_type(start, Time)
    ensure_type(end, Time)
    ensure_type(cal_day, CalendarDay)
    spans = new_time_span_seq()
    new_start = start
    tss = cd_tss(cal_day)
    if tss:
        for ts in tss:
            if not t_in_ts(start, ts):
                ts__end = ts_start(ts)
                if not time_equals(new_start, ts__end):
                    new_ts = new_time_span(new_start, ts__end)
                    spans = tss_plus_span(spans, new_ts)
            new_start = ts_end(ts)
            if t_number(new_start) >= t_number(end):
                break
        if not t_number(new_start) >= t_number(end):
            spans = tss_plus_span(spans, new_time_span(new_start, end))
    else:
        time_span = new_time_span(new_start, end)
        spans = tss_plus_span(spans, time_span)
    return spans


def show_free(cal_name, day, mon, str_start, str_end):
    start = new_time_from_string(str_start)
    end = new_time_from_string(str_end)
    day = new_day(day)
    mon = new_month(mon)
    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_month, day)
    free = free_spans(cal_day, start, end)
    for ts in tss_iter_spans(free):
        show_ts(ts)

create("Jayne")
book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
book("Jayne", 20, "sep", "14:00", "16:00", "Escape with loot")


show_free("Jayne", 20, "sep", "08:00", "19:00")
