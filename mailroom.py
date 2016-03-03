# _*_ coding: utf-8 _*_

# try:
# 	input = raw_input
# except NameError:
# 	pass


donor = {"Tim": "200", "Jim": "10.90"}


def mailroom():
    start_input = """Hello! Press 'Q' to quit.
    Would you like to Send a Thank You(1), or Create a Report(2)?\n
    """
    start = input(start_input)
    while start not in ("1", "2"):
        start = input(start_input)
        continue
    if start == "1":
        thank_you()
    else:
        send_report()


def thank_you():
    print(u"thanks")


def send_report():
    print(u"report")


mailroom()
# thank_you()
