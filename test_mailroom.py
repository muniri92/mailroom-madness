# _*_ coding: utf-8 _*_
import pytest


SAMPLE_DONOR = {u"Tim": [23, 43]}
# SAMPLE_REPORT =


# @pytest.mark.parametrize("1", "2")
# def test_mailroom():
#     from mailroom import mailroom
#     assert results == True


# @pytest.mark.parametrize()
# def test_send_letter():
#     from mailroom import send_letter
#     assert [[blank]] == result


# @pytest.mark.parametrize()
# def test_add_donor():
#     from mailroom import add_donor
#     assert 1 == result


@pytest.mark.parametrize("dict, result", SAMPLE_DONOR)
def test_send_report(dict, result):
    from mailroom import send_report
    assert result == result
