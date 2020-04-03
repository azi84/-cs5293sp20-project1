import pytest
import project1
from project1 import redactor

c="""Biologically, a child is a person between birth and puberty,[1][2] or between the developmental period of baby and puberty.Common meanings for kid is 
young baby how can talk and walk """

def test_concept():
    (t, con, co) = redactor.redact_concepts (c, ['child'])
    assert  co == 4
  
