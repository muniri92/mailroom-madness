# _*_ coding: utf-8 _*_
"""Mailroom app."""
import sys
# Example dictiontary of names to start.
donor = {u"tim": [23, 43], u"jim": [37, 65, 23], u"paul": [53]}

SEND_REPO = u"""
   Name: {}
   Donated: ${}
   Number of Donations: {}
   Average Donations: ${}
"""

THANK_YOU = u"""Thank you for your generous donation, {}! \n"""

# ***********************************************************************


def mailroom():
    """Ask user to choose an option: Send Letter or Create Report."""
    start_input = u"""Hello! Press 'Q' to quit.
Would you like to Send a Thank You(1), or Create a Report(2)?\n
    """
    start = input(start_input).lower()
    while start not in [u"1", u"2", u"q"]:
        start = input(start_input)
        continue
    if start == u"1":
        send_letter()
        return start
    elif start == u"2":
        send_report(donor)
        return start
    else:
        sys.exit(0)


def send_letter():
    """Ask user to choose option: enter name or get list of names."""
    thanks = """Please give the full name of the thankee(enter name),
or would you like a list(enter 'list')?\n
    """
    while True:
        name_or_list = input(thanks).lower()
        if name_or_list == u"q":
            mailroom()
            break
        elif name_or_list == u"list":
            print(u"Here are the donors in the list: \n")
            for name in list(donor.keys()):
                print(name.upper())
                continue
        elif name_or_list not in list(donor.keys()):
            add_donor(name_or_list)
            select_donor(name_or_list)
            break
        select_donor(name_or_list)
        break


def add_donor(add_name):
    """Add donor name to dictionary."""
    donor.update({add_name: []})
    if add_name in donor:
        return add_name


def select_donor(add_name):
    """Ask user how much donor gave, check for int, add amount to dict."""
    try:
        amount = int(input("How much did they give?\n"))
        donor.setdefault(add_name, []).append(amount)
        thank_you(add_name)
        return amount
    except ValueError:
        select_donor(add_name)


def thank_you(donor):
    """Create an email to the donor, thanking them."""
    thanks = THANK_YOU.format(donor)
    print(thanks)
    return thanks


def send_report(donor):
    """Generate report."""
    result = ""
    for key, value in list(donor.items()):
        sum_val = sum(value)
        len_val = len(value)
        avg_donation = format((sum_val / len_val), '.2f')
        result += SEND_REPO.format(key.upper(), sum_val, len_val, avg_donation)
    print(result)
    return result


if __name__ == '__main__':
    while True:
        mailroom()
