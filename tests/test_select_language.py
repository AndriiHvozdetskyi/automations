import pytest
from itertools import product
from pages.selectpage import SelectPage

# Тест одного селекту
@pytest.mark.parametrize("language_value", ['Python', 'JavaScript', 'Ruby', 'C#', 'Java'])
def test_singleselect(driver, language_value):
    selectpage = SelectPage(driver)
    selectpage.open("https://www.qa-practice.com/elements/select/single_select")
    selectpage.choose_value("id_choose_language", language_value)
    selectpage.click_by_id("submit-id-submit")
    selectpage.check_text_is("result-text", language_value)

# Об'єкти для тесту у мултиселектахpytest
place = ['Sea', 'Mountains', 'Old town', 'Ocean', 'Restaurant']
how_get = ['Car', 'Bus', 'Train', 'Air']
when_want = ['Today', 'Tomorrow', 'Next week']

# Тест мультиселекту з даними
@pytest.mark.parametrize("place, how_get, when_want", list(product(place, how_get, when_want)))
def test_multiselect(driver, place, how_get, when_want):
    selectpage = SelectPage(driver)
    selectpage.open("https://www.qa-practice.com/elements/select/mult_select")
    selectpage.choose_value("id_choose_the_place_you_want_to_go", place)
    selectpage.choose_value("id_choose_how_you_want_to_get_there", how_get)
    selectpage.choose_value("id_choose_when_you_want_to_go", when_want)

    selectpage.click_by_id("submit-id-submit")

    selectpage.check_text_is("result-text", f'to go by {how_get.lower()} to the {place.lower()} {when_want.lower()}')
