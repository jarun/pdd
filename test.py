#!/usr/bin/env python3

'''
pdd test script

Author: Arun Prakash Jana
Email : engineerarun@gmail.com
Home  : https://github.com/jarun/pdd

NOTES:

1. Before raising a PR,
   a. add relevant test cases
   b. run `python3 -m pytest test.py
'''
import pytest
import subprocess

test = [
    ('./pdd.py', '-d', '3', 'jul', '1983', '15', '1', '2014'),               # 1
    ('./pdd.py', '-d', '15', '1', '2014', '3', 'jul', '1983'),               # 2
    ('./pdd.py', '-t', '45:50', '6:17:33'),                                  # 3
    ('./pdd.py', '-t', '6:17:33', '45:50'),                                  # 4
    ('./pdd.py', '-t', '5:80:75', '6:17:33'),                                # 5
    ('./pdd.py', '-t', '6:17:33', '5:80:75'),                                # 6
    ('./pdd.py', '-d', '28', 'FEB', '2000', '1', '2', '3', '--add'),         # 7
    ('./pdd.py', '-d', '28', 'FEB', '2000', '3', '2', '1', '--add'),         # 8
    ('./pdd.py', '-t', '47:71:37', '1:2:63', '--add'),                       # 9
    ('./pdd.py', '-d', '01', 'Mar', '2000', '1', '0', '0', '--sub'),         # 10
    ('./pdd.py', '-d', '01', 'Mar', '2000', '1', '1', '1', '--sub'),         # 11
    ('./pdd.py', '-t', '00:00:00', '0:0:1', '--sub'),                        # 12
    ('./pdd.py', '-t', '25:61:61', '0:0:0', '--sub'),                        # 13
    ('./pdd.py', '-t', '0:0:0', '1:1:1', '--sub'),                           # 14
    ('./pdd.py', '-t', '0:0:0', '25:61:61', '--sub'),                        # 15
]

res = [
    b'30y 6m 12d\n11154d\n',                                              # 1
    b'30y 6m 12d\n11154d\n',                                              # 2
    b'05:31:43\n19903s\n',                                                # 3
    b'05:31:43\n19903s\n',                                                # 4
    b'00:03:42\n222s\n',                                                  # 5
    b'00:03:42\n222s\n',                                                  # 6
    b'Tue 29 Apr 2003\n',                                                 # 7
    b'Tue 01 May 2001\n',                                                 # 8
    b'2 day(s) later, 01:14:40\n177280s\n',                               # 9
    b'Tue 29 Feb 2000\n',                                                 # 10
    b'Sun 31 Jan 1999\n',                                                 # 11
    b'1 day(s) earlier, 23:59:59\n-1s\n',                                 # 12
    b'02:02:01\n93721s\n',                                                # 13
    b'1 day(s) earlier, 22:58:59\n-3661s\n',                              # 14
    b'2 day(s) earlier, 21:57:59\n-93721s\n',                             # 15
]


@pytest.mark.parametrize('item, res', zip(test, res))
def test_output(item, res):
    try:
        out = subprocess.check_output(item, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        # print(e.output)
        assert e.output == res
    else:
        assert out == res
