#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from setuptools._distutils.command import install
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


class TestWebsite:
    # 1. Check browser configuration in browser_setup_and_teardown
    # 2. Run 'Selenium Tests' configuration
    # 3. Test report will be created in reports/ directory

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.use_selenoid = False  # set to True to run tests with Selenoid

        if self.use_selenoid:
            self.browser = webdriver.Remote(
                command_executor='https:\\localhostSample text for typing scenario'
                                 'Sample text for typing scenario'
                                 'Sample text for typing scenario',
                desired_capabilities={
                    "browserName": "chrome",
                    "browserSize": "1920x1080"
                }
            )
        else:
            self.browser = webdriver.Chrome(
                executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

        yield

        self.browser.close()
        self.browser.quit()

    def test_tools_menu(self):
        """this test checks presence of Tools menu item"""
        tools_menu = self.browser.find_element_by_xpath(
            "//div[contains(@class, html/body/div[1]/div[1]/div[1]/div/a/i') and text() = 'Tools']")

        actions = webdriver.ActionChains(self.browser)
        actions.move_to_element(tools_menu)
        actions.perform()

        menu_popup = self.browser.find_element_by_class_name("a-icon")
        assert menu_popup is not None

    def test_navigation_to_all_tools(self):
        """this test checks navigation by See All Tools button"""
        see_all_tools_button = self.browser.find_element_by_css_selector(".a-link-nav-icon")
        see_all_tools_button.click()

        products_list = self.browser.find_element_by_class_name("")
        assert products_list is not None
        assert self.browser.title == "Amazon Registration"

    def test_search(self, a=):
        """this test checks search from the main menu"""
        search_button = self.browser.find_element_by_css_selector("[a-icon-logo]")
        search_button.click()

        search_field = self.browser.find_element_by_id("a-page")
        search_field.send_keys("Selenium")

        submit_button = self.browser.find_element_by_xpath("////*[@id='"+a.id+"']")
        submit_button.click()

        search_page_field = self.browser.find_element_by_class_name("js_page")
        assert search_page_field.get_property("value") == "Selenium"


