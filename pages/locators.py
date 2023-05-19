from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    BUTTON_NEW_AC = (By.XPATH, '//*[@id="root"]/div/div/div[4]/form/div/a')
    INPUT_NEW_EMAIL = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[1]/input')
    INPUT_NEW_PASS = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[3]/div[1]/div[1]/input')
    SECOND_NEW_PASS = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[3]/div[2]/div[1]/input')
    EYE_FIRST_OPEN = (By.XPATH, '//*[@id="root"]/div/div/div[1]/form/div[3]/div[1]/div[1]/div/svg/use')
    EYE_FIRST_CLOSE = (By.XPATH, '//*[@id="root"]/div/div/div[1]/form/div[3]/div[1]/div[1]/div/svg/use')
    EYE_SECOND_OPEN = (By.XPATH, '//*[@id="root"]/div/div/div[1]/form/div[3]/div[2]/div[1]/div/svg/use')
    EYE_SECOND_CLOSE = (By.XPATH, '//*[@id="root"]/div/div/div[1]/form/div[3]/div[2]/div[1]/div/svg/use')
    BUTTON_NEXT = (By.XPATH, '//*[@id="root"]/div/div/div[1]/form/div[5]/a')
    INPUT_EMAIL = (By.XPATH, '//*[@id="root"]/div/div/div[4]/form/fieldset/div[1]/div[1]/input')
    INPUT_PASSWORD = (By.XPATH, '//*[@id="password"]')
    BUTTON_OK = (By.XPATH, '//*[@id="root"]/div/div/div[4]/form/div/div/button')
    BUTTON_LOSE_PASS = (By.XPATH, '//*[@id="root"]/div/div/div[4]/form/div/a')
    BUTTON_SIGNIN = (By.XPATH, '//*[@id="root"]/div/div/div[1]/form/div[5]/a')
    BUTTON_NE = (By.XPATH, '//*[@id="root"]/div/div/div[4]/form/div/div/button')