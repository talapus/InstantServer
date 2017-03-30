#!/usr/bin/env python

## @file test_test.py
## @brief This is where a brief description should be

import pytest
import os

# global variables go here
config = '/whatever/whatever:999 '

def setup():
    pass # global setup stuff goes here

@pytest.mark.parametrize(('test_input'), ['start', 'stop', 'restart'])
def test_service(test_input):
	assert os.system('echo ' + test_input) == 0

@pytest.mark.parametrize(("black", "white"), [
    (0, 0),
    (9, 9),
    (99, 99),
	(999, 999),
	(9999, 9999),
	(99999, 99999),
])
def test_thing(black, white):
	assert os.system('echo ') == 0

'''
@pytest.mark.parametrize(('test_input'), ['UTC', 'Local'])
def test_port(test_input):
    pass # not supported yet, so this whole block is commented out


'''
