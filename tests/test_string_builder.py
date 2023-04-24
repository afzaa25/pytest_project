from lib.string_builder import StringBuilder

def test_initially_output_is_an_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""


def test_string_plus_input_equals_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output()== "hello"
    assert string_builder.size() == 5

