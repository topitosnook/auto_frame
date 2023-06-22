import subprocess
import os
import pathlib
import platform


def add_drivers_to_path():
    print("Adding webdrivers to path.")
    curr_file_path = pathlib.Path(__file__).parent.absolute()

    if platform.system() == 'Darwin':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'mac')
    elif platform.system() == 'Windows':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'wimdows')
    elif platform.system() == 'Linux':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'linux')
    else:
        raise Exception("Unknown platform. Unable to add webdrivers to path.")

    current_path = os.environ.get('PATH')
    new_path = webdriver_path + ':' + current_path
    os.environ['PATH'] = new_path


if __name__ == '__main__':

    add_drivers_to_path()

    command = f'behave tests --format allure_behave.formatter:AllureFormatter -o ./allure-results'
    print(f"Running command: {command}")

    rs = subprocess.run(command, shell=True)

    if os.path.isdir("allure-results"):
        print('helloworld')
