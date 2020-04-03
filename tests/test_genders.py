
import project1
#import redactor
import pytest
from project1 import redactor


text = 'Gender is the state of being male or female in relation to the social and cultural roles that are considered appropriate for men and women.Gender is the state of being male or female in relation to the social and cultural roles that are considered appropriate for men and women.'
block ='\u2588'
def test_gender():
    (t,g,c) = redactor.redact_genders (text)
    assert  c == 6

    assert len(g) == 4
