from selenium.webdriver.common.by import By

class BurgersLocators:
    #главная страница
    #кнопка "войти в аккаунт":
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')
    LOGIN_HEADER = (By.XPATH, '//h2[contains(text(),"Вход")]')
    #кнопка "личный кабинет":
    ACCOUNT_BUTTON = [By.XPATH, '//p[contains(text(),"Личный Кабинет")]']
    LOGIN_BUTTON_ON_REGISTRATION_PAGE = (By.XPATH, '//p/a[contains(text(),"Войти")]')
    LOGIN_BUTTON_ON_FORGOT_PASSWORD_PAGE = (By.XPATH, '//p/a[contains(text(),"Войти")]')
    #страница регистрации, поля ввода:
    NAME_INPUT_FIELD = (By.XPATH, '//label[ text()="Имя" ]/parent::div/input')
    EMAIL_INPUT_FIELD = (By.XPATH, '//label[ text()="Email" ]/parent::div/input')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//label[ text()="Пароль" ]/parent::div/input')
    REGISTRATION_BUTTON_ON_REGISTRATION_PAGE = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')
    INCORRECT_PASSWORD_ERROR = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')
    #кнопка "Зарегистрироваться" на странице входа
    REGISTRATION_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")

    #страница входа, поля ввода и кнопка:
    LOGIN_EMAIL_INPUT_FIELD = (By.XPATH, '//input[@name="name"]')
    LOGIN_PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    LOGIN_APPLY_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')

    #Кнопка оформить заказ на главной странице:
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    #личный кабинет:
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]/parent::a')
    LOGO_BUTTON = (By.XPATH, '//nav/div')

    #Выбор бургера:
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]')
    SPACE_SAUCE_NAME = (By.XPATH, '//a[2]/p[contains(text(),"Соус фирменный Space Sauce")]')
    FILLINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]')
    BEEF_FILLING_NAME = (By.XPATH, '//p[contains(text(),"Говяжий метеорит (отбивная)")]')
    BUN_SECTION = (By.XPATH, '//span[text()="Булки"]')
    FLUORESCENT_BUN_NAME = (By.XPATH, '//p[contains(text(),"Флюоресцентная булка R2-D3")]')
