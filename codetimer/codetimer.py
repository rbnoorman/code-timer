#TODO logische namen en structuur aanbrengen
#TODO main.py bestand maken met daarin CLICK voor command line interface


import json
import os
import shutil
import time

from csv import writer
from datetime import datetime

from playsound import playsound


class CodeTimer:
    """Overall class to manage timer and its behavior."""

    def __init__(self):
        """Initialize timer attributes."""

        # Import settings
        self.settings = json.load(open('codetimer/core/settings.json'))

        # Duration settings
        self.pomodoro = self.settings['pomodoro']
        self.short_break = self.settings['short_break']
        self.long_break = self.settings['long_break']

        # Initial task
        self.task = self.settings['default_task']

        # Stats for picking right timer
        self.last_timer = ""
        self.pomodoro_count = 0
        self.timer_active = True
        self.countdown_active = True
        self.timer_start_time = datetime.now().strftime("%d-%m-%Y %H:%M")


    def main(self):
        """Starts a session, loops over appropriate timers"""

        # Loop for the duration of the session
        while self.timer_active:
            if self.last_timer != "Pomodoro":
                # Run the pomodoro timer
                self.timer_start('Pomodoro', self.pomodoro)
                os.system('clear')
                print("Pomodoro has ended.")
                self.pomodoro_count += 1
                playsound('codetimer/core/knock.wav')
            elif self.pomodoro_count % 4 != 0:
                # If last timer was pomodoro but not the fourth in a row, run a short break
                self.timer_start('Short break', self.short_break)
                os.system('clear')
                print("Pomodoro has ended.")
                print("Short break has ended.")
                playsound('codetimer/core/knock.wav')
            else:
                # After every fourth pomodoro, run a long break
                self.timer_start('Long Break', self.long_break)
                os.system('clear')
                print("Pomodoro has ended.")
                print("Long break has ended.")
                playsound('codetimer/core/knock.wav')

    def timer_start(self, timer_name, duration):
        """Start the timer"""

        # Run the countdown for the timer
        timer = self.timer_countdown(timer_name, duration)

        if not self.countdown_active:
            # Countdown ended by user, store data, reset stats and change active flag to false.
            if timer_name == "Pomodoro":
                time_worked = timer
            else:
                time_worked = 0
            self.timer_end_time = datetime.now().strftime("%d-%m-%Y %H:%M")
            self.timer_log(time_worked)
            self.pomodoro_count = 0
            self.last_timer = ""
            self.timer_active = False
        else:
            # Update stats
            self.last_timer = timer_name

    def timer_countdown(self, timer_name, duration):
        """The countdown visual, iterates for the duration of the timer"""

        while duration:
            try:
                #
                os.system('clear')

                mins, secs = divmod(duration, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)

                print(f"{timer_name} | {timer}\nPress CTRL+C to end session.")
                time.sleep(1)
                duration -= 1
            except KeyboardInterrupt:
                self.countdown_active = False
                time_worked = self.pomodoro - duration
                return time_worked


    def timer_log(self, add_time):
        """Logs the session data in a csv file"""

        total_duration = (self.pomodoro_count * self.pomodoro) + add_time
        data = [
            self.timer_start_time,
            self.timer_end_time,
            self.task,
            self.pomodoro_count,
            total_duration
        ]

        with open('codetimer/core/log.csv', 'a+', newline='') as log:
            writer(log).writerow(data)

if __name__ == "__main__":
    CT = CodeTimer()
    CT.main()
