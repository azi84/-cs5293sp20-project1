import pytest
import project1
from project1 import redactor

options, args = redactor.findFlag ()
def test_downloadText():
    inputFile_list = redactor.downloadFiles (options, inputFile_list='my.txt')
    assert  inputFile_list == 'my.txt'
