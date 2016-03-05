# unit-testing-training

This repo provides a Python module (`functions.py`) and a corresponding module (`functions_test.py`) containing unit
tests for `functions.py`.

## Setup

After cloning this repo:

```
git clone git@github.com:optimizely/unit-testing-training.git

cd unit-testing-training
```

... run the shell script to install dependencies and create a virtualenv (this will ask for your system password):

```
./setup.sh
```

Then enter your new virtualenv:

```
source .virtualenv/bin/activate
```

And finally run all the Python tests in this repo:

```
python -m unittest discover
```

## Where To Start

Try breaking one of the tests and rerunning the tests. In `functions.py`, change:

```
def add_three_to_value(value):
  return value + 3
```

to

```
def add_three_to_value(value):
  return value + 4
```

Then once again run:

```
python -m unittest discover
```

And you should see something like:

```
======================================================================
FAIL: test_add_three_to_value__with_seven (test_my_functions.MyFunctionsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/username/repos/unit-testing-training/test_my_functions.py", line 15, in test_add_three_to_value__with_seven
    self.assertEqual(10, my_functions.add_three_to_value(7))
AssertionError: 10 != 11

======================================================================
FAIL: test_add_three_to_value__with_ten (test_my_functions.MyFunctionsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/username/repos/unit-testing-training/test_my_functions.py", line 18, in test_add_three_to_value__with_ten
    self.assertEqual(13, my_functions.add_three_to_value(10))
AssertionError: 13 != 14

----------------------------------------------------------------------
Ran 6 tests in 0.002s

FAILED (failures=2)
```

Hopefully that helps makes the setup a bit more concrete. Fiddle freely with the tests!

## More Reading/Viewing

* Rambling presentation on unit testing using this repo: https://drive.google.com/a/optimizely.com/file/d/0B3DMe9ZATniSWnZqdHdFQ3J1T0E/view?usp=sharing
* https://docs.python.org/2/library/unittest.html
* https://docs.python.org/3/library/unittest.mock.html
* https://www.toptal.com/python/an-introduction-to-mocking-in-python
