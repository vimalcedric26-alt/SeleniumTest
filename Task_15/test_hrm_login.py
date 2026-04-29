import pytest
from Task_15.hrm_login import Login
from Task_15.load_exceldata import ExcelData

filename = "C:/Users/vimal/Desktop/Notes_Guvi/Excel.xlsx"
sheetname = "user_data"


def get_test_data():
    excel = ExcelData(filename, sheetname)
    workbook, worksheet = excel.load_excel_wrkbook()
    data = excel.get_data_(worksheet)
    return data


@pytest.mark.parametrize("row_number, user_data", get_test_data())
def test_login_scenario(setup, row_number, user_data):

    user_login = Login(setup, filename)

    username = user_data[1]
    password = user_data[2]

    actual_result = user_login.login_hrm(user_data, row_number)

    # Logical expected result
    if username == "Admin" and password == "admin123":
        expected_result = "PASS"
    else:
        expected_result = "FAIL"

    assert actual_result == expected_result