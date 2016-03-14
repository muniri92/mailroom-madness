# _*_ coding: utf-8 _*_
"""Test mailroom.py."""
import pytest


TEST_REPO = u"""
   Name: PAUL
   Donated: $53
   Number of Donations: 1
   Average Donations: $53.00
"""

TEST_NAME = [(u"Bob", u"Bob")]

EXAMPLE_REPORT = [({'Paul': [53]}, TEST_REPO)]
EXAMPLE_THANK_YOU = [(u"Paul", u"Thank you for your generous donation, Paul!")]


# ***********************************************************************


@pytest.mark.parametrize('donor, results', EXAMPLE_REPORT)
def test_send_report(donor, results):
    """Run working test."""
    from mailroom import send_report
    assert send_report(donor) == results


@pytest.mark.parametrize('donor, thanks', EXAMPLE_THANK_YOU)
def test_thank_you(donor, thanks):
    """Run working test."""
    from mailroom import thank_you
    assert thank_you(donor) == thanks


@pytest.mark.parametrize('donor, names', TEST_NAME)
def test_add_donor(donor, names):
    """Run working test."""
    from mailroom import add_donor
    assert add_donor(donor) == names


# @pytest.mark.parametrize()
def test_select_error():
    """Test to confirm that ValueError is detected."""
    from mailroom import select_donor
    with pytest.raises(ValueError):
        select_donor(45)
