import csv
import keyboard
import time

time.sleep(5)

with open("names.csv", newline='', encoding="UTF-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        keyboard.write(line['name'])
        time.sleep(2.5)
        keyboard.press_and_release('enter')
        time.sleep(1.5)