# _*_ coding: utf-8 _*_

# try:
# 	input = raw_input
# except NameError:
# 	pass


donor = {"Tim": [23, 43], "Jim": [37, 65, 23], "Paul": [53, 234, 432]}


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
        send_letter()
    else:
        send_report()


def send_letter():
    """Ask user to choose option: enter name or get list of names."""
    thanks_input = """Please give the full name of the thankee(enter name),
or would you like a list(enter 'list')?\n
    """
    name_or_list = input(thanks_input)
    if name_or_list == "list":
        print("Here are the donors in the list: \n")
        for name in list(donor.keys()):
            print(name)
        send_letter()
    elif name_or_list not in list(donor.keys()):
        add_donor(name_or_list)
    else:
        select_donor(name_or_list)


def add_donor(name_or_list):
    """Add donor name to dict."""
    donor.update({name_or_list: []})
    select_donor(name_or_list)


def select_donor(name_or_list):
    """Ask user how much donor gave, check for int, add amount to dict."""
    try:
        amount = int(input("""How much did they give?\n
    """))
        donor.setdefault(name_or_list, []).append(amount)
        print(donor)
        thank_you(name_or_list)
    except ValueError:
        select_donor(name_or_list)


def thank_you(name_or_list):
    """Send an email to the donor, thanking them."""
    print(("Thank you for you generous donation, {}!\n").format(name_or_list))


def send_report():
    """Generate report."""
    for key, value in list(donor.items()):
        print(("Name: {} | Donated: ${} | Number of Donations: {} | Average Donations: ${} ").format(key, sum(value), len(value), round((sum(value) / len(value)), 2)))
        # print(key, values)
    # print(u"report")


mailroom()
# thank_you()
