import pytest
import sys
import os
from pages.login_page import LoginPage

def test_login_valid(setup):

    page = setup

    login = pages(page)

    login.navigate("https://opensource-demo.orangehrmlive.com/")

    login.login("Admin", "admin123")

    assert "OrangeHRM" in login.get_title()