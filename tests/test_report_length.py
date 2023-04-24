from lib.report_length import *
def test_report_length():
    result = report_length("Hello Afzaa!")
    assert result == "This string was 12 characters long."
