from lib.gratitudes import *
# add gratitude to gratitudes list
def test_add_gratitude_to_gratitudes_list():
    gratitude = Gratitudes()
    gratitude.add("Kindness")
    assert gratitude.gratitudes == ["Kindness"]
# adds the gratitude formatted as a string
def test_format_gratitude_to_string():
    gratitude = Gratitudes()
    gratitude.add("Kindness")
    formatted = gratitude.format()
    assert formatted == "Be grateful for: Kindness"

