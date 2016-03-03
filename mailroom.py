# _*_ coding: utf-8 _*_


donor = {"Tim": "200", "Jim": "10.90"}

start_input = """Hello! Press 'Q' to quit.
Would you like to Send a Thank You(1), or Create a Report(2)?\n
"""
start = input(start_input)


def mailroom(starting):
    if starting == 1:
        thank_you()
    elif starting == 2:
        send_report()
    else:
        while starting not in ["1", "2"]:
            start = input(start_input)


def thank_you():
    print("thanks")


def send_report():
    print("report")


mailroom(start)
# thank_you()
