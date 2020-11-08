class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "txtUsername"
        self.password_texbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def enter_username (self, username):
