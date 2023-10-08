import allure
from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.conditions import be
import allure
from allure_commons.types import Severity

pytestmark = [
    allure.label('layer', 'UI test'),
    allure.label('owner', 'ytamonova'),
    allure.feature("Tes documentation")
]


@allure.title('Test 1')
@allure.suite('Suite 1')
@allure.tag('android')
@allure.tag('hometask')
@allure.severity(Severity.CRITICAL)
@allure.story('Search article')
def test_search_article():

    with allure.step("Поиск статьи"):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Python")

    with allure.step("Проверка, что статья найдена"):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text("Python"))


@allure.title('Test 2')
@allure.suite('Suite 1')
@allure.tag('android')
@allure.tag('hometask')
@allure.severity(Severity.CRITICAL)
@allure.story('Search article negative case')
def test_search_article_negative():

    with allure.step("Поиск статьи"):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Selenoid")

    with allure.step("Проверка, что статья не найдена"):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.no.text("Selenoid"))


@allure.title('Test 3')
@allure.suite('Suite 1')
@allure.tag('android')
@allure.tag('hometask')
@allure.severity(Severity.CRITICAL)
@allure.story('Search several articles')
def test_search_several_articles():
    with allure.step("Поиск статьи"):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Python")

    with allure.step("Проверка, что статья найдена"):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text("Python"))

    with allure.step("Переход на статью"):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).second.click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_find_in_article')).click()

    with allure.step("Проверка содержимого статьи"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'General-purpose programming language')
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/find_in_page_match')).should(have.text('1/2'))

    with allure.step('Поиск новой статьи'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/action_mode_close_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_toolbar_button_search')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('java')

    with allure.step("Проверка, что статья найдена"):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.second.should(have.text("Java"))

    with allure.step("Переход на новую статью"):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).second.click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_find_in_article')).click()

    with allure.step("Проверка содержимого статьи"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'object-oriented programming language')
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/find_in_page_match')).should(have.text('1/2'))


@allure.title('Test 4')
@allure.suite('Suite 1')
@allure.tag('android')
@allure.tag('hometask')
@allure.severity(Severity.CRITICAL)
@allure.story('Clear search history')
def test_clear_history():
    with allure.step("Поиск статьи"):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Python")

    with allure.step("Переход на статью"):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).second.click()

    with allure.step('Переход на поиск статьи'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_toolbar_button_search')).click()

    with allure.step('Удаление истории поиска'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/recent_searches_delete_button')).click()
        browser.element((AppiumBy.ID, 'android:id/button1')).click()

    with allure.step('Проверка, что история удалена'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_empty_container')).should(be.present)
