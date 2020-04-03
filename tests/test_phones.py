import pytest
import project1
from project1 import redactor

p = '''Education Abroad Contact Information
Office Hours
Monday - Friday 8:00 AM to 5:00 PM

Mailing Address
Education Abroad
University of Oklahoma
729 Elm Ave. Room 144
Norman, OK 73019

Phone
Main Phone (405) 325-1693
Fax (405) 325-7387
Emergencies While Abroad (405) 630-5392

Email
Office Email: ea@ou.edu
Emergency Email: helpabroad@ou.edu

Building Location'''

def test_phones():
    (t, ph,c) = redactor.redact_phones (p)
    print (ph)
    assert  c == 3
    assert ph == ['(405) 325-1693', '(405) 325-7387', '(405) 630-5392']
    assert t == '''Education Abroad Contact Information
Office Hours
Monday - Friday 8:00 AM to 5:00 PM

Mailing Address
Education Abroad
University of Oklahoma
729 Elm Ave. Room 144
Norman, OK 73019

Phone
Main Phone █████ ████████
Fax █████ ████████
Emergencies While Abroad █████ ████████

Email
Office Email: ea@ou.edu
Emergency Email: helpabroad@ou.edu

Building Location'''
