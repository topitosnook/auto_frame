import subprocess

if __name__ == '__main__':

    command = f'behave tests --no-capture ' \
              f'--format allure_behave.formatter:AllureFormatter -o ' \
              f'./allure-results'
    print(f"Running command: {command}")

    rs = subprocess.run(command, shell=True)
