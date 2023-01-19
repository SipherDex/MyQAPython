import requests

#---------------STATUS CODE TESTS--------------#
#-----------------in this file-----------------#


def test_con_1():
    request = requests.get('https://www.google.com')
    assert request.status_code == 200


def test_con_2():
    request = requests.get('https://www.facebook.com')
    assert request.status_code == 200


#--------------------test_req_3 MUST FAIL-------------------#
#i was interested which will be the answer of pytest failure#

def test_con_3():
    request = requests.get('https://www.iamidiot.com')
    assert request.status_code == 200
