from lib.counter import *
def test_counter_initially_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far"