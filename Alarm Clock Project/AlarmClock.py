import time
import os


def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            play_alarm_sound()
            break
        time.sleep(1)


def play_alarm_sound():
    sound_file = "AlarmSound.mp3"
    if os.path.exists(sound_file):
        os.system(sound_file)
    else:
        print(f"Sound file '{sound_file}' not found. Alarm will be silent.")


alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
set_alarm(alarm_time)
