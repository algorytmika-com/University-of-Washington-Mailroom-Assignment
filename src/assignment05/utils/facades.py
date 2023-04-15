import sys
from utils import sendings as s, reports as r

prompt = "\n".join(("Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

def send_thanks():
    s.send_thanks()

def create_report():
    r.create_report()

def exit_program():
    print("Bye!")
    sys.exit() 
