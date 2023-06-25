import base64
import subprocess
import allure
from allure_commons.types import AttachmentType
import os


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        # allure.attach.file('./allure-results', name="Video", attachment_type=allure.attachment_type.MP4)
#
# #-----------------------------------------------------------------------------------------
# # Create a variable to track the screen recording process
# screen_recording_process = None
# # Get the path for the Allure report directory
# allure_report_dir = os.path.join(os.getcwd(), "allure-results")
#
# def before_scenario(context,scenario):
#     global screen_recording_process
#
#     screen_recording_process = start_screen_recording()
#
# def after_scenario(context, scenario):
#     global screen_recording_process
#     stop_screen_recording(screen_recording_process)
#
#
# def start_screen_recording():
#     # Start the screen recording process (replace with your preferred screen recording tool)
#     # Make sure the screen recording tool saves the output file in the current directory
#     screen_recording_command = "<your screen recording command>"
#     screen_recording_process = subprocess.Popen(screen_recording_command, shell=True)
#
#     return screen_recording_process
#
# def stop_screen_recording(screen_recording_process):
#     # Stop the screen recording process
#     screen_recording_process.terminate()
#
#     # Attach the screen recording to Allure report
#     allure.attach.file("<path to the recorded video file>", name="Screen Recording", attachment_type=AttachmentType.MP4)
