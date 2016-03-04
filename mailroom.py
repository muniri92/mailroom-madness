# _*_ coding: utf-8 _*_

# try:
# 	input = raw_input
# except NameError:
# 	pass


donor = {"Tim": "200", "Jim": "10.90"}


def mailroom():
    """Ask user to choose an option: Send Letter or Create Report."""
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
    """Ask user to choose option: enter name or get list of names."""
    thanks_input = """Please give the full name of the thankee(enter name),
                     or would you like a list(enter 'list')? """
    name_or_list = input(thanks_input)

    if name_or_list == "list":
        print("Here are the donors in the list: ")
        for name in list(donor.keys()):
            print(name)
        thank_you()
    elif name_or_list not in list(donor.keys()):
        add_donor(name_or_list)
    else:
        select_donor(name_or_list)


def add_donor(name_or_list):
    """Add donor name to dict."""
    print("add donor!")


def select_donor(name_or_list):
    """Ask user how much donor gave, check for int, add amount to dict."""
    try:
        amount = int(input("How much did they give?"))
        print(amount)
    except ValueError:
        select_donor(name_or_list)


def send_report():
    """Generate report."""
    print(u"report")


mailroom()
# thank_you()
