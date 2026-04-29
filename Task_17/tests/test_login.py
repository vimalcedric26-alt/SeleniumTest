from Task_17.pages.login_page import LoginPage

def test_login_logout(setup):
    page = setup
    login = LoginPage(page)

    login.login("vimalcedric26@gmail.com", "Cassy@091124")
    login.close_popup_if_present()
    login.log_out()

