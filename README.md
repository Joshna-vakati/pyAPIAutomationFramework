# Python API Automation Framework

### Tech stack 
- Python 3.12
- Requests - HTTP Requests
- Pytest - Testing Framework
- Reporting - Allure Report, pytest html
- Test Data - CSV,Excel,Json
- Parallel Execution - x distribute(xdist)

### How to install packages 

- pip
- pip install requests pytest pytest-html faker allure-pytest jsonschema
- pip install pytest-xdist

### how to add the .gitignore file?

copy the content from this to .gitignore file.
https://www.toptal.com/developers/gitignore/api/pycharm+all

### how to run the basic testcase with allure report
pytest (path of the file) --alluredir=allure_result -s