from selenium import webdriver


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    """

    :param context:
    :param scenario:
    """
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature) -> object:
    context.driver.delete_all_cookies()
    context.driver.quit()
