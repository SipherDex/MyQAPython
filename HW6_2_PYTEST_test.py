import requests
#------------REQUEST CONTENT TESTS-------------#
#-----------------in this file-----------------#


def test_req_1():
    req = requests.get('https://ukr.net')
    assert 'Access denied' in req.text


#----------------test_con_2 MUST FAIL----------------#
#i was interested which will be the answer of failure#
#---wrong test data IP 255.255.255.255 was entered---#

def test_req_2():
    req = requests.get('https://ukr.net')
    assert 'IP: 255.255.255.255' in req.text


#---------Was not able to parse req variable into true json format, so it's actually string--------#
#--------------test_con_3 MUST FAIL IF MORE THAN 2-3 REQUESTS WAS USED IN 15 MINUTES---------------#

def test_req_3():
    req = requests.get('https://api.tomorrow.io/v4/timelines?location=40.75872069597532,-73.98529171943665&fields=temperature&timesteps=1h&units=metric&apikey=OLah5KRynq7gTk5gQwKDvIu42RbaS32N')
    myjson = req.text
    assert "data" in myjson