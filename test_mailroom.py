# _*_ coding: utf-8 _*_
"""Test mailroom.py."""
import pytest


TEST_REPO = u"""
   Name: Paul
   Donated: $719
   Number of Donations: 3
   Average Donations: $239.67
"""


EXAMPLE_REPORT = [({'Paul': [53, 234, 432]}, TEST_REPO)]


# ***********************************************************************


@pytest.mark.parametrize('donor, results', EXAMPLE_REPORT)
def test_send_report(donor, results):
    """Run working test."""
    from mailroom import send_report
    assert send_report(donor) == results
