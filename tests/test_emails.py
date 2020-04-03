
import project1 
from project1 import redactor
import pytest


e = "The general format of an email address is local-part@domain, and a specific example is jsmith@example.com. An address consists of two parts."

def test_emails():
    (t, em,c) = redactor.redact_emails (e)
    assert  c   == 1
    assert em == [' jsmith@example.com']
    assert t == '''The general format of an email address is local-part@domain, and a specific example is ██████████████████. An address consists of two parts.'''
