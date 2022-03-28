from app.util import format_input


def test() -> None:
    input = "1, 2, 3, 4, 5"
    output = format_input(input)

    assert [i.isdigit() for i in output]
