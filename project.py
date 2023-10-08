from typing import Literal
import pydantic_settings
import dotenv
from appium.options.android import UiAutomator2Options
from utils import file


class Config(pydantic_settings.BaseSettings):
    context: Literal['local_emulator', 'local_real', 'bstack'] = 'bstack'

    if context == 'bstack':
        dotenv.load_dotenv(dotenv_path=file.file_path('.env.credentials'))

    timeout: str = '10.0'

    browserstack_userName: str = ''
    browserstack_accessKey: str = ''
    projectName: str = 'Python mobile project - 2'
    buildName: str = 'Python mobile project - 2'
    sessionName: str = 'Python mobile project - 2'
    app: str = 'bs://81624cc90f9c4abaf0fca57b0f93148dd4cf31d4'
    remote_url: str = 'http://hub.browserstack.com/wd/hub'
    deviceName: str = 'Google Pixel 3'
    platformVersion: str = '9.0'
    udid: str = ''
    app_wait_activity: str = 'org.wikipedia.*'

    def to_driver_options(self):
        options = UiAutomator2Options()
        options.set_capability('appWaitActivity', self.app_wait_activity)

        if self.context == 'bstack':
            options.set_capability('app', self.app)
            options.load_capabilities({
                'platformVersion': self.platformVersion,
                'deviceName': self.deviceName,

                'bstack:options': {
                    'userName': self.browserstack_userName,
                    'accessKey': self.browserstack_accessKey
                }
            })

        else:
            options.set_capability('app', file.file_path(self.app))
            options.set_capability('udid', self.udid)

        return options


config = Config(_env_file=dotenv.find_dotenv(f'.env.{Config().context}'))
