# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
from typing import List, NamedTuple
from cal_abstraction import Time
from cal_output import *

TimeSpanSeq = NamedTuple("TimeSpanSeq", [("TimeSpans", List[TimeSpan])])


# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(time_spans: List[TimeSpan] = None) -> TimeSpanSeq:
    """
    Create and return a new CalendarDay for the given Day of the month,
    with the given appointments.
    """
    if time_spans is None:
        time_spans = []
    else:
        ensure_type(time_spans, List[TimeSpan])
    return TimeSpanSeq(time_spans)


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """Return true iff the given CalendarDay has no appointments."""
    ensure_type(tss, TimeSpanSeq)
    return not tss


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan) -> TimeSpanSeq:
    """
    Returns a copy of the given CalendarDay, where the given Appointment
    has been added in its proper position.
    """
    ensure_type(tss, TimeSpanSeq)
    ensure_type(ts, TimeSpan)

    def add_time_span(ts: TimeSpan, tss: List[TimeSpanSeq]):
        if not tss or time_precedes(
                ts_start(ts), ts_start(tss[0])
        ):
            return [ts] + tss
        else:
            return [tss[0]] + add_time_span(ts, tss[1:])

    return new_time_span_seq(
        add_time_span(ts, tss.TimeSpans)
    )


def tss_iter_spans(tss):
    ensure_type(tss, TimeSpanSeq)
    for time in tss.TimeSpans:
        yield time


def show_time_spans(tss):
    ensure_type(tss, TimeSpanSeq)
    for i in tss.TimeSpans:
        show_ts(i)


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result