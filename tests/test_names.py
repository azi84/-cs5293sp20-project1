#import redactor
import pytest
import project1
from project1 import redactor

s = " William Bradley Pitt on December 18th, 1963, in Shawnee, Oklahoma, and was raised in Springfield, Missouri. He is the son of Jane Etta (Hillhouse), a school counselor, and William Alvin Pitt, a truck company manager. He has a younger brother, Douglas (Doug) Pitt, and a younger sister, Julie Pitt."


def test_names():
    t,n,c= redactor.redact_names (s)
    
    # there is 7 name in this file [William Bradley Pitt, Jane Etta, William Alvin Pitt, Douglas, Doug, Pitt, Julie  Pitt]
    assert len(n) == 7 



