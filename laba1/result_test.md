```bash
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
metadata: {'Python': '3.8.10', 'Platform': 'Linux-5.4.0-89-generic-x86_64-with-glibc2.29', 'Packages': {'pytest': '6.2.3', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'cov': '2.11.1', 'metadata': '1.11.0', 'html': '3.1.1', 'Faker': '9.7.1'}}
rootdir: /home/nikel/dev/University/TaDS/laba1
plugins: cov-2.11.1, metadata-1.11.0, html-3.1.1, Faker-9.7.1
collecting ... collected 161 items

test_calculation.py::test_lower_salary_range PASSED                      [  0%]
test_calculation.py::test_higher_salary_range PASSED                     [  1%]
test_calculation.py::test_absence_first_param PASSED                     [  1%]
test_calculation.py::test_absence_second_param PASSED                    [  2%]
test_calculation.py::test_absence_last_param PASSED                      [  3%]
test_calculation.py::test_absence_several_params PASSED                  [  3%]
test_calculation.py::test_correct_param[data0] PASSED                    [  4%]
test_calculation.py::test[-5080-0.2--5] PASSED                           [  4%]
test_calculation.py::test[69999-1.0--5] PASSED                           [  5%]
test_calculation.py::test[70000-1.9--5] PASSED                           [  6%]
test_calculation.py::test[312540-2.0--5] PASSED                          [  6%]
test_calculation.py::test[750000-2.4--5] PASSED                          [  7%]
test_calculation.py::test[750001-2.5--5] PASSED                          [  8%]
test_calculation.py::test[1000000-2.9--5] PASSED                         [  8%]
test_calculation.py::test[1000000-3.0-6] PASSED                          [  9%]
test_calculation.py::test[750001-3.4-6] PASSED                           [  9%]
test_calculation.py::test[750000-3.5-6] PASSED                           [ 10%]
test_calculation.py::test[312540-3.9-6] PASSED                           [ 11%]
test_calculation.py::test[70000-4.0-6] PASSED                            [ 11%]
test_calculation.py::test[69999-5.0-6] PASSED                            [ 12%]
test_calculation.py::test[-5080-5.7-6] PASSED                            [ 13%]
test_calculation.py::test[-5080-5.0-7] PASSED                            [ 13%]
test_calculation.py::test[69999-4.0-7] PASSED                            [ 14%]
test_calculation.py::test[70000-3.9-7] PASSED                            [ 14%]
test_calculation.py::test[312540-3.5-7] PASSED                           [ 15%]
test_calculation.py::test[750000-3.4-7] PASSED                           [ 16%]
test_calculation.py::test[750001-3.0-7] PASSED                           [ 16%]
test_calculation.py::test[1000000-5.7-7] PASSED                          [ 17%]
test_calculation.py::test[1000000-0.2-9] PASSED                          [ 18%]
test_calculation.py::test[750001-1.0-9] PASSED                           [ 18%]
test_calculation.py::test[750000-1.9-9] PASSED                           [ 19%]
test_calculation.py::test[312540-2.9-9] PASSED                           [ 19%]
test_calculation.py::test[70000-2.5-9] PASSED                            [ 20%]
test_calculation.py::test[69999-2.4-9] PASSED                            [ 21%]
test_calculation.py::test[-5080-2.0-9] PASSED                            [ 21%]
test_calculation.py::test[-5080-2.4-10] PASSED                           [ 22%]
test_calculation.py::test[69999-2.5-10] PASSED                           [ 22%]
test_calculation.py::test[70000-2.9-10] PASSED                           [ 23%]
test_calculation.py::test[312540-3.0-10] PASSED                          [ 24%]
test_calculation.py::test[750000-0.2-10] PASSED                          [ 24%]
test_calculation.py::test[750001-5.7-10] PASSED                          [ 25%]
test_calculation.py::test[1000000-5.0-10] PASSED                         [ 26%]
test_calculation.py::test[1000000-4.0-12] PASSED                         [ 26%]
test_calculation.py::test[750001-2.0-12] PASSED                          [ 27%]
test_calculation.py::test[750000-3.9-12] PASSED                          [ 27%]
test_calculation.py::test[312540-1.0-12] PASSED                          [ 28%]
test_calculation.py::test[70000-3.4-12] PASSED                           [ 29%]
test_calculation.py::test[69999-3.5-12] PASSED                           [ 29%]
test_calculation.py::test[-5080-1.9-12] PASSED                           [ 30%]
test_calculation.py::test[-5080-3.5-13] PASSED                           [ 31%]
test_calculation.py::test[69999-3.4-13] PASSED                           [ 31%]
test_calculation.py::test[70000-3.0-13] PASSED                           [ 32%]
test_calculation.py::test[312540-5.7-13] PASSED                          [ 32%]
test_calculation.py::test[750000-5.0-13] PASSED                          [ 33%]
test_calculation.py::test[750001-4.0-13] PASSED                          [ 34%]
test_calculation.py::test[1000000-2.4-13] PASSED                         [ 34%]
test_calculation.py::test[1000000-1.9-14] PASSED                         [ 35%]
test_calculation.py::test[750001-3.9-14] PASSED                          [ 36%]
test_calculation.py::test[750000-2.9-14] PASSED                          [ 36%]
test_calculation.py::test[312540-2.5-14] PASSED                          [ 37%]
test_calculation.py::test[70000-0.2-14] PASSED                           [ 37%]
test_calculation.py::test[69999-2.0-14] PASSED                           [ 38%]
test_calculation.py::test[-5080-1.0-14] PASSED                           [ 39%]
test_calculation.py::test[-5080-2.9-15] PASSED                           [ 39%]
test_calculation.py::test[69999-3.0-15] PASSED                           [ 40%]
test_calculation.py::test[70000-5.7-15] PASSED                           [ 40%]
test_calculation.py::test[312540-2.4-15] PASSED                          [ 41%]
test_calculation.py::test[750000-4.0-15] PASSED                          [ 42%]
test_calculation.py::test[750001-5.0-15] PASSED                          [ 42%]
test_calculation.py::test[1000000-3.5-15] PASSED                         [ 43%]
test_calculation.py::test[1000000-1.0-17] PASSED                         [ 44%]
test_calculation.py::test[750001-0.2-17] PASSED                          [ 44%]
test_calculation.py::test[750000-2.0-17] PASSED                          [ 45%]
test_calculation.py::test[312540-1.9-17] PASSED                          [ 45%]
test_calculation.py::test[70000-5.0-17] PASSED                           [ 46%]
test_calculation.py::test[69999-3.9-17] PASSED                           [ 47%]
test_calculation.py::test[-5080-3.4-17] PASSED                           [ 47%]
test_calculation.py::test[-5080-2.5-21] PASSED                           [ 48%]
test_calculation.py::test[69999-1.9-21] PASSED                           [ 49%]
test_calculation.py::test[70000-2.0-21] PASSED                           [ 49%]
test_calculation.py::test[312540-0.2-21] PASSED                          [ 50%]
test_calculation.py::test[750000-1.0-21] PASSED                          [ 50%]
test_calculation.py::test[750001-3.5-21] PASSED                          [ 51%]
test_calculation.py::test[1000000-2.5-17] PASSED                         [ 52%]
test_calculation.py::test[1000000-3.4-21] PASSED                         [ 52%]
test_calculation.py::test[750001-2.4-17] PASSED                          [ 53%]
test_calculation.py::test[750000-5.7-17] PASSED                          [ 54%]
test_calculation.py::test[312540-4.0-17] PASSED                          [ 54%]
test_calculation.py::test[70000-2.4-21] PASSED                           [ 55%]
test_calculation.py::test[69999-2.9-17] PASSED                           [ 55%]
test_calculation.py::test[-5080-3.0-17] PASSED                           [ 56%]
test_calculation.py::test[-5080-3.9-21] PASSED                           [ 57%]
test_calculation.py::test[69999-5.7-21] PASSED                           [ 57%]
test_calculation.py::test[70000-3.5-17] PASSED                           [ 58%]
test_calculation.py::test[312540-3.4-9] PASSED                           [ 59%]
test_calculation.py::test[750000-3.0-21] PASSED                          [ 59%]
test_calculation.py::test[750001-2.9-21] PASSED                          [ 60%]
test_calculation.py::test[1000000-3.9-9] PASSED                          [ 60%]
test_calculation.py::test[1000000-2.0-13] PASSED                         [ 61%]
test_calculation.py::test[750001-1.9-13] PASSED                          [ 62%]
test_calculation.py::test[750000-2.5-13] PASSED                          [ 62%]
test_calculation.py::test[312540-5.0-21] PASSED                          [ 63%]
test_calculation.py::test[70000-1.0-13] PASSED                           [ 63%]
test_calculation.py::test[69999-0.2-13] PASSED                           [ 64%]
test_calculation.py::test[-5080-4.0-21] PASSED                           [ 65%]
test_calculation.py::test[-5080-4.0-9] PASSED                            [ 65%]
test_calculation.py::test[-5080-0.2-15] PASSED                           [ 66%]
test_calculation.py::test[-5080-1.0-15] PASSED                           [ 67%]
test_calculation.py::test[-5080-5.0-9] PASSED                            [ 67%]
test_calculation.py::test[-5080-2.5-15] PASSED                           [ 68%]
test_calculation.py::test[-5080-1.9-15] PASSED                           [ 68%]
test_calculation.py::test[-5080-2.0-15] PASSED                           [ 69%]
test_calculation.py::test[-5080-3.9-15] PASSED                           [ 70%]
test_calculation.py::test[-5080-2.9-13] PASSED                           [ 70%]
test_calculation.py::test[-5080-3.0-9] PASSED                            [ 71%]
test_calculation.py::test[-5080-3.4-15] PASSED                           [ 72%]
test_calculation.py::test[-5080-3.5-9] PASSED                            [ 72%]
test_calculation.py::test[-5080-5.7-9] PASSED                            [ 73%]
test_calculation.py::test[-5080-2.4-14] PASSED                           [ 73%]
test_calculation.py::test[-5080-2.4-12] PASSED                           [ 74%]
test_calculation.py::test[-5080-5.7-12] PASSED                           [ 75%]
test_calculation.py::test[-5080-3.5-14] PASSED                           [ 75%]
test_calculation.py::test[-5080-3.4-14] PASSED                           [ 76%]
test_calculation.py::test[-5080-3.0-14] PASSED                           [ 77%]
test_calculation.py::test[-5080-2.9-12] PASSED                           [ 77%]
test_calculation.py::test[-5080-3.9-13] PASSED                           [ 78%]
test_calculation.py::test[-5080-2.0-10] PASSED                           [ 78%]
test_calculation.py::test[-5080-1.9-10] PASSED                           [ 79%]
test_calculation.py::test[-5080-2.5-12] PASSED                           [ 80%]
test_calculation.py::test[-5080-5.0-12] PASSED                           [ 80%]
test_calculation.py::test[-5080-1.0-10] PASSED                           [ 81%]
test_calculation.py::test[-5080-0.2-12] PASSED                           [ 81%]
test_calculation.py::test[-5080-4.0-14] PASSED                           [ 82%]
test_calculation.py::test[-5080-4.0-10] PASSED                           [ 83%]
test_calculation.py::test[-5080-0.2-7] PASSED                            [ 83%]
test_calculation.py::test[-5080-1.0-7] PASSED                            [ 84%]
test_calculation.py::test[-5080-5.0-14] PASSED                           [ 85%]
test_calculation.py::test[-5080-2.5-7] PASSED                            [ 85%]
test_calculation.py::test[-5080-1.9-7] PASSED                            [ 86%]
test_calculation.py::test[-5080-2.0-7] PASSED                            [ 86%]
test_calculation.py::test[-5080-3.9-10] PASSED                           [ 87%]
test_calculation.py::test[-5080-2.9-7] PASSED                            [ 88%]
test_calculation.py::test[-5080-3.0-12] PASSED                           [ 88%]
test_calculation.py::test[-5080-3.4-10] PASSED                           [ 89%]
test_calculation.py::test[-5080-3.5-10] PASSED                           [ 90%]
test_calculation.py::test[-5080-5.7-14] PASSED                           [ 90%]
test_calculation.py::test[-5080-2.4-7] PASSED                            [ 91%]
test_calculation.py::test[-5080-2.4-6] PASSED                            [ 91%]
test_calculation.py::test[-5080-5.7--5] PASSED                           [ 92%]
test_calculation.py::test[-5080-3.5--5] PASSED                           [ 93%]
test_calculation.py::test[-5080-3.4--5] PASSED                           [ 93%]
test_calculation.py::test[-5080-3.0--5] PASSED                           [ 94%]
test_calculation.py::test[-5080-2.9-6] PASSED                            [ 95%]
test_calculation.py::test[-5080-3.9--5] PASSED                           [ 95%]
test_calculation.py::test[-5080-2.0-6] PASSED                            [ 96%]
test_calculation.py::test[-5080-1.9-6] PASSED                            [ 96%]
test_calculation.py::test[-5080-2.5-6] PASSED                            [ 97%]
test_calculation.py::test[-5080-5.0--5] PASSED                           [ 98%]
test_calculation.py::test[-5080-1.0-6] PASSED                            [ 98%]
test_calculation.py::test[-5080-0.2-6] PASSED                            [ 99%]
test_calculation.py::test[-5080-4.0--5] PASSED                           [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED test_calculation.py::test_lower_salary_range
PASSED test_calculation.py::test_higher_salary_range
PASSED test_calculation.py::test_absence_first_param
PASSED test_calculation.py::test_absence_second_param
PASSED test_calculation.py::test_absence_last_param
PASSED test_calculation.py::test_absence_several_params
PASSED test_calculation.py::test_correct_param[data0]
PASSED test_calculation.py::test[-5080-0.2--5]
PASSED test_calculation.py::test[69999-1.0--5]
PASSED test_calculation.py::test[70000-1.9--5]
PASSED test_calculation.py::test[312540-2.0--5]
PASSED test_calculation.py::test[750000-2.4--5]
PASSED test_calculation.py::test[750001-2.5--5]
PASSED test_calculation.py::test[1000000-2.9--5]
PASSED test_calculation.py::test[1000000-3.0-6]
PASSED test_calculation.py::test[750001-3.4-6]
PASSED test_calculation.py::test[750000-3.5-6]
PASSED test_calculation.py::test[312540-3.9-6]
PASSED test_calculation.py::test[70000-4.0-6]
PASSED test_calculation.py::test[69999-5.0-6]
PASSED test_calculation.py::test[-5080-5.7-6]
PASSED test_calculation.py::test[-5080-5.0-7]
PASSED test_calculation.py::test[69999-4.0-7]
PASSED test_calculation.py::test[70000-3.9-7]
PASSED test_calculation.py::test[312540-3.5-7]
PASSED test_calculation.py::test[750000-3.4-7]
PASSED test_calculation.py::test[750001-3.0-7]
PASSED test_calculation.py::test[1000000-5.7-7]
PASSED test_calculation.py::test[1000000-0.2-9]
PASSED test_calculation.py::test[750001-1.0-9]
PASSED test_calculation.py::test[750000-1.9-9]
PASSED test_calculation.py::test[312540-2.9-9]
PASSED test_calculation.py::test[70000-2.5-9]
PASSED test_calculation.py::test[69999-2.4-9]
PASSED test_calculation.py::test[-5080-2.0-9]
PASSED test_calculation.py::test[-5080-2.4-10]
PASSED test_calculation.py::test[69999-2.5-10]
PASSED test_calculation.py::test[70000-2.9-10]
PASSED test_calculation.py::test[312540-3.0-10]
PASSED test_calculation.py::test[750000-0.2-10]
PASSED test_calculation.py::test[750001-5.7-10]
PASSED test_calculation.py::test[1000000-5.0-10]
PASSED test_calculation.py::test[1000000-4.0-12]
PASSED test_calculation.py::test[750001-2.0-12]
PASSED test_calculation.py::test[750000-3.9-12]
PASSED test_calculation.py::test[312540-1.0-12]
PASSED test_calculation.py::test[70000-3.4-12]
PASSED test_calculation.py::test[69999-3.5-12]
PASSED test_calculation.py::test[-5080-1.9-12]
PASSED test_calculation.py::test[-5080-3.5-13]
PASSED test_calculation.py::test[69999-3.4-13]
PASSED test_calculation.py::test[70000-3.0-13]
PASSED test_calculation.py::test[312540-5.7-13]
PASSED test_calculation.py::test[750000-5.0-13]
PASSED test_calculation.py::test[750001-4.0-13]
PASSED test_calculation.py::test[1000000-2.4-13]
PASSED test_calculation.py::test[1000000-1.9-14]
PASSED test_calculation.py::test[750001-3.9-14]
PASSED test_calculation.py::test[750000-2.9-14]
PASSED test_calculation.py::test[312540-2.5-14]
PASSED test_calculation.py::test[70000-0.2-14]
PASSED test_calculation.py::test[69999-2.0-14]
PASSED test_calculation.py::test[-5080-1.0-14]
PASSED test_calculation.py::test[-5080-2.9-15]
PASSED test_calculation.py::test[69999-3.0-15]
PASSED test_calculation.py::test[70000-5.7-15]
PASSED test_calculation.py::test[312540-2.4-15]
PASSED test_calculation.py::test[750000-4.0-15]
PASSED test_calculation.py::test[750001-5.0-15]
PASSED test_calculation.py::test[1000000-3.5-15]
PASSED test_calculation.py::test[1000000-1.0-17]
PASSED test_calculation.py::test[750001-0.2-17]
PASSED test_calculation.py::test[750000-2.0-17]
PASSED test_calculation.py::test[312540-1.9-17]
PASSED test_calculation.py::test[70000-5.0-17]
PASSED test_calculation.py::test[69999-3.9-17]
PASSED test_calculation.py::test[-5080-3.4-17]
PASSED test_calculation.py::test[-5080-2.5-21]
PASSED test_calculation.py::test[69999-1.9-21]
PASSED test_calculation.py::test[70000-2.0-21]
PASSED test_calculation.py::test[312540-0.2-21]
PASSED test_calculation.py::test[750000-1.0-21]
PASSED test_calculation.py::test[750001-3.5-21]
PASSED test_calculation.py::test[1000000-2.5-17]
PASSED test_calculation.py::test[1000000-3.4-21]
PASSED test_calculation.py::test[750001-2.4-17]
PASSED test_calculation.py::test[750000-5.7-17]
PASSED test_calculation.py::test[312540-4.0-17]
PASSED test_calculation.py::test[70000-2.4-21]
PASSED test_calculation.py::test[69999-2.9-17]
PASSED test_calculation.py::test[-5080-3.0-17]
PASSED test_calculation.py::test[-5080-3.9-21]
PASSED test_calculation.py::test[69999-5.7-21]
PASSED test_calculation.py::test[70000-3.5-17]
PASSED test_calculation.py::test[312540-3.4-9]
PASSED test_calculation.py::test[750000-3.0-21]
PASSED test_calculation.py::test[750001-2.9-21]
PASSED test_calculation.py::test[1000000-3.9-9]
PASSED test_calculation.py::test[1000000-2.0-13]
PASSED test_calculation.py::test[750001-1.9-13]
PASSED test_calculation.py::test[750000-2.5-13]
PASSED test_calculation.py::test[312540-5.0-21]
PASSED test_calculation.py::test[70000-1.0-13]
PASSED test_calculation.py::test[69999-0.2-13]
PASSED test_calculation.py::test[-5080-4.0-21]
PASSED test_calculation.py::test[-5080-4.0-9]
PASSED test_calculation.py::test[-5080-0.2-15]
PASSED test_calculation.py::test[-5080-1.0-15]
PASSED test_calculation.py::test[-5080-5.0-9]
PASSED test_calculation.py::test[-5080-2.5-15]
PASSED test_calculation.py::test[-5080-1.9-15]
PASSED test_calculation.py::test[-5080-2.0-15]
PASSED test_calculation.py::test[-5080-3.9-15]
PASSED test_calculation.py::test[-5080-2.9-13]
PASSED test_calculation.py::test[-5080-3.0-9]
PASSED test_calculation.py::test[-5080-3.4-15]
PASSED test_calculation.py::test[-5080-3.5-9]
PASSED test_calculation.py::test[-5080-5.7-9]
PASSED test_calculation.py::test[-5080-2.4-14]
PASSED test_calculation.py::test[-5080-2.4-12]
PASSED test_calculation.py::test[-5080-5.7-12]
PASSED test_calculation.py::test[-5080-3.5-14]
PASSED test_calculation.py::test[-5080-3.4-14]
PASSED test_calculation.py::test[-5080-3.0-14]
PASSED test_calculation.py::test[-5080-2.9-12]
PASSED test_calculation.py::test[-5080-3.9-13]
PASSED test_calculation.py::test[-5080-2.0-10]
PASSED test_calculation.py::test[-5080-1.9-10]
PASSED test_calculation.py::test[-5080-2.5-12]
PASSED test_calculation.py::test[-5080-5.0-12]
PASSED test_calculation.py::test[-5080-1.0-10]
PASSED test_calculation.py::test[-5080-0.2-12]
PASSED test_calculation.py::test[-5080-4.0-14]
PASSED test_calculation.py::test[-5080-4.0-10]
PASSED test_calculation.py::test[-5080-0.2-7]
PASSED test_calculation.py::test[-5080-1.0-7]
PASSED test_calculation.py::test[-5080-5.0-14]
PASSED test_calculation.py::test[-5080-2.5-7]
PASSED test_calculation.py::test[-5080-1.9-7]
PASSED test_calculation.py::test[-5080-2.0-7]
PASSED test_calculation.py::test[-5080-3.9-10]
PASSED test_calculation.py::test[-5080-2.9-7]
PASSED test_calculation.py::test[-5080-3.0-12]
PASSED test_calculation.py::test[-5080-3.4-10]
PASSED test_calculation.py::test[-5080-3.5-10]
PASSED test_calculation.py::test[-5080-5.7-14]
PASSED test_calculation.py::test[-5080-2.4-7]
PASSED test_calculation.py::test[-5080-2.4-6]
PASSED test_calculation.py::test[-5080-5.7--5]
PASSED test_calculation.py::test[-5080-3.5--5]
PASSED test_calculation.py::test[-5080-3.4--5]
PASSED test_calculation.py::test[-5080-3.0--5]
PASSED test_calculation.py::test[-5080-2.9-6]
PASSED test_calculation.py::test[-5080-3.9--5]
PASSED test_calculation.py::test[-5080-2.0-6]
PASSED test_calculation.py::test[-5080-1.9-6]
PASSED test_calculation.py::test[-5080-2.5-6]
PASSED test_calculation.py::test[-5080-5.0--5]
PASSED test_calculation.py::test[-5080-1.0-6]
PASSED test_calculation.py::test[-5080-0.2-6]
PASSED test_calculation.py::test[-5080-4.0--5]
============================= 161 passed in 0.32s ==============================
```