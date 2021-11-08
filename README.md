# Cross Browser Testing with LambdaTest using Python

This repo contains the complete code that is demonstrated in the [Selenium Python Tutorial](https://www.lambdatest.com/blog/selenium-webdriver-tutorial-for-cross-browser-testing/) blog 

# Pre-requisites

1. Visual Studio Code

It is best to use the repo with the Visual Studio (VS) Code IDE. In case you do not have VS Code installed on your machine, please download the same from [VS Code Official Download Link](https://code.visualstudio.com/download). However, you can use the Python IDE of your choice.

2. Tests demonstrated in this Selenium Python tutorial will run on the LambdaTest Selenium Cloud Grid. Hence, you need to first create an account on [LambdaTest](https://wwww.lambdatest.com). Once done, make a note of your user name and access key from [LambdaTest Profile](https://accounts.lambdatest.com/detail/profile) section.

# How to use this repo

Clone the project and perform the below mentioned steps:

1. If you are using `poetry`, install the dependencies along with the creation of virtual environment. Run the following command on the terminal to install the packages mentioned in `pyproject.toml`

```bash
poetry install
```

2. With this, the setup for performing Selenium automation testing with Python is complete. Your user name and access key is available in the [LambdaTest Profile](https://accounts.lambdatest.com/detail/profile) section. Add your LambdaTest user name and access key in the files `tests/test_lambdatest_google.py` and `tests/test_lambdatest_todo.py`.

```python
user_name = "user_name"
app_key = "access_key"
```

3. Run the following command to run the two test scenarios in parallel on the LambdaTest Selenium Grid.

```bash
pytest -s -v -n=2 tests/test_lambdatest_todo.py tests/test_lambdatest_google.py
```

4. Navigate to [LambdaTest Automation Dashboard](https://accounts.lambdatest.com/dashboard) to check the status of the test.

# Additional resources

1. [Detailed Selenium Python Video Tutorial](https://youtu.be/UzkuOACmBpA)
2. [Selenium Python Learning Hub](https://www.lambdatest.com/learning-hub/python-tutorial)


# About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [Selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.