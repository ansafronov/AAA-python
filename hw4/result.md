# Результаты запуска
## issue-01
```
% python3 -m doctest -o NORMALIZE_WHITESPACE -v issue_01.py
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('$O$')
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: '$'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   2 tests in morse.encode
2 tests in 3 items.
2 passed and 0 failed.
Test passed.
```

## issue-02
```
% python3 -m pytest -v issue_02.py
=============================================== test session starts ================================================
platform darwin -- Python 3.8.9, pytest-7.1.3, pluggy-1.0.0 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/a.safronov/Yandex.Disk.localized/Учеба/AAA/Python AAA/hw4
collected 3 items

issue_02.py::test_decode[... --- ...-SOS] PASSED                                                             [ 33%]
issue_02.py::test_decode[.- -. -.. .-. . -.-- .-----ANDREY1] PASSED                                          [ 66%]
issue_02.py::test_decode[..--- ..... -..-. ----- ..... -..-. ..--- ----- ----- .-----25/05/2001] PASSED      [100%]

================================================ 3 passed in 0.01s =================================================
```

## issue-03
```
% python3 -m unittest issue_03.py
....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

## issue-04
```
% python3 -m pytest -v issue_04.py
=============================================== test session starts ================================================
platform darwin -- Python 3.8.9, pytest-7.1.3, pluggy-1.0.0 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/a.safronov/Yandex.Disk.localized/Учеба/AAA/Python AAA/hw4
collected 6 items

issue_04.py::test_strings_input PASSED                                                                       [ 16%]
issue_04.py::test_from_dict PASSED                                                                           [ 33%]
issue_04.py::test_empty PASSED                                                                               [ 50%]
issue_04.py::test_double PASSED                                                                              [ 66%]
issue_04.py::test_case_sensitive PASSED                                                                      [ 83%]
issue_04.py::test_one_input PASSED                                                                           [100%]

================================================ 6 passed in 0.01s =================================================
```

## issue-05
```
% python3 -m pytest -v issue_05.py
=============================================== test session starts ================================================
platform darwin -- Python 3.8.9, pytest-7.1.3, pluggy-1.0.0 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/a.safronov/Yandex.Disk.localized/Учеба/AAA/Python AAA/hw4
collected 3 items                                                                                                                                                                                                                                                                                                      

issue_05.py::test_get_year_dashs PASSED                                                                                                                                                                                                                                                                          [ 33%]
issue_05.py::test_get_year_dots PASSED                                                                                                                                                                                                                                                                           [ 66%]
issue_05.py::test_get_year_space PASSED                                                                       [100%]

================================================ 6 passed in 0.01s =================================================
```