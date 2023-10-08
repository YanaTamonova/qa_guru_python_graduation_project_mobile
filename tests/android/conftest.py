import allure
import allure_commons
import pytest
from appium import webdriver
import project
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, support
from utils import allure_attaches


@pytest.fixture(scope='function', autouse=True)
def skip_tutorial():
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()


@pytest.fixture(scope='function', autouse=True)
def android_settings():

    with allure.step('init step session'):
        browser.config.driver = webdriver.Remote(
            project.config.remote_url,
            options=project.config.to_driver_options()
        )

    browser.config.timeout = float(project.config.timeout)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
        )

    yield

    allure_attaches.allure_attach_bstack_screenshot()
    allure_attaches.allure_attach_bstack_dump()

    session_id = browser.driver.session_id
    with allure.step(f'tear down app session: {session_id}'):
        browser.quit()

    if project.config.context == 'bstack':
        allure_attaches.attach_bstack_video(session_id)
