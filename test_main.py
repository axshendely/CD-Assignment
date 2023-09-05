import main


def test_index():
    assert main.index() == f"<h1>Welcome To The END!.<h1>"


def test_info():
    assert main.info() == f"<h1>The One And Only!.<h1>"


def test_me():
    assert main.me() == f"<h1>@********tools.<h1>"
