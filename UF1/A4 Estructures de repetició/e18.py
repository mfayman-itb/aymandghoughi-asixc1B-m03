"""
descripción: programa que mostri per pantalla un rellotge, indicant les hores, minuts i segons.
"""
import time

while True:
    for i in range(0, 86400):
        seconds = i % 60
        minutes = int(i / 60) % 60
        hours = int(i / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
        time.sleep(1)
