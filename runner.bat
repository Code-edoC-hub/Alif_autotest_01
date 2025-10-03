rmdir /s /q allure-results
pytest test/main.py -s -v --alluredir=allure-results
allure serve allure-results
