# Egalitarian Division Assignment

This repository contains an implementation of an egalitarian division algorithm using CVXPY. The algorithm computes an allocation of resources among several people such that the minimum utility is maximized. Multiple examples are provided to demonstrate different configurations.

## File Overview

- **question_3.py**:  
  Contains the implementation of the `egalitarian_division` function and several example valuation matrices. The function uses convex optimization to determine the best fair allocation, checks the validity of the results, and then outputs a neatly formatted allocation table.

## Dependencies

Make sure you have the following installed:
- [Python 3.x](https://www.python.org/)
- [CVXPY](https://www.cvxpy.org/) (`pip install cvxpy`)
- [NumPy](https://numpy.org/) (`pip install numpy`)
- [Tabulate](https://pypi.org/project/tabulate/) (`pip install tabulate`)

## How to Run

Open a terminal in the repository folder and run:
```
python question_3.py
```

## Sample Output

When you run the script, you will see output similar to the following:

```
Valuation matrix #1:
[[81 19  1]
 [70  1 29]]

Egalitarian division found with minimum utility: 61.91390727
Allocation Table:
+----------+------------+------------+------------+---------------+
|  Person  | Resource 1 | Resource 2 | Resource 3 | Total Utility |
+----------+------------+------------+------------+---------------+
| Person 1 | 0.52980132 | 1.00000000 | 0.00000000 |  61.91390729  |
| Person 2 | 0.47019868 | 0.00000000 | 1.00000000 |  61.91390728  |
+----------+------------+------------+------------+---------------+

Valuation matrix #2:
[[ 9 20 11]
 [12 18 10]
 [14 17  9]
 [10 15 20]]

Egalitarian division found with minimum utility: 12.28070175
Allocation Table:
+----------+------------+------------+------------+---------------+
|  Person  | Resource 1 | Resource 2 | Resource 3 | Total Utility |
+----------+------------+------------+------------+---------------+
| Person 1 | 0.00000000 | 0.61403508 | 0.00000001 |  12.28070175  |
| Person 2 | 0.12280702 | 0.38596492 | 0.38596490 |  12.28070175  |
| Person 3 | 0.87719298 | 0.00000000 | 0.00000000 |  12.28070175  |
| Person 4 | 0.00000000 | 0.00000000 | 0.61403509 |  12.28070175  |
+----------+------------+------------+------------+---------------+

Valuation matrix #3:
[[15 25 10]
 [20 10 30]
 [25 40  5]]

Egalitarian division found with minimum utility: 25.85106380
Allocation Table:
+----------+------------+------------+------------+---------------+
|  Person  | Resource 1 | Resource 2 | Resource 3 | Total Utility |
+----------+------------+------------+------------+---------------+
| Person 1 | 0.00000003 | 0.97872338 | 0.13829787 |  25.85106380  |
| Person 2 | 0.00000000 | 0.00000000 | 0.86170213 |  25.85106386  |
| Person 3 | 0.99999996 | 0.02127662 | 0.00000000 |  25.85106381  |
+----------+------------+------------+------------+---------------+

Valuation matrix #4:
[[10 20 30 40]
 [40 30 20 10]
 [25 25 25 25]]

Egalitarian division found with minimum utility: 43.74999997
Allocation Table:
+----------+------------+------------+------------+------------+---------------+
|  Person  | Resource 1 | Resource 2 | Resource 3 | Resource 4 | Total Utility |
+----------+------------+------------+------------+------------+---------------+
| Person 1 | 0.00000000 | 0.00000000 | 0.12500000 | 1.00000000 |  43.74999998  |
| Person 2 | 1.00000000 | 0.12500000 | 0.00000000 | 0.00000000 |  43.74999998  |
| Person 3 | 0.00000000 | 0.87500000 | 0.87500000 | 0.00000000 |  43.74999998  |
+----------+------------+------------+------------+------------+---------------+

Valuation matrix #5:
[[12  7  3 15]
 [ 4 17 10  6]]

Egalitarian division found with minimum utility: 26.99999983
Allocation Table:
+----------+------------+------------+------------+------------+---------------+
|  Person  | Resource 1 | Resource 2 | Resource 3 | Resource 4 | Total Utility |
+----------+------------+------------+------------+------------+---------------+
| Person 1 | 1.00000000 | 0.00000000 | 0.00000000 | 1.00000000 |  27.00000000  |
| Person 2 | 0.00000000 | 1.00000000 | 1.00000000 | 0.00000000 |  26.99999999  |
+----------+------------+------------+------------+------------+---------------+

Valuation matrix #6:
[[20 10  5 15 30]
 [15 25 10  5 20]
 [30 12 18 22  8]]

Egalitarian division found with minimum utility: 37.16417909
Allocation Table:
+----------+------------+------------+------------+------------+------------+---------------+
|  Person  | Resource 1 | Resource 2 | Resource 3 | Resource 4 | Resource 5 | Total Utility |
+----------+------------+------------+------------+------------+------------+---------------+
| Person 1 | 0.00000001 | 0.00000000 | 0.00000000 | 0.47761193 | 1.00000000 |  37.16417909  |
| Person 2 | 0.14427860 | 1.00000000 | 0.99999999 | 0.00000000 | 0.00000000 |  37.16417909  |
| Person 3 | 0.85572138 | 0.00000000 | 0.00000001 | 0.52238807 | 0.00000000 |  37.16417910  |
+----------+------------+------------+------------+------------+------------+---------------+

Valuation matrix #7:
[[10 20 30 40]
 [40 30 20 10]
 [25 35 30 20]
 [15 25 35 45]]

Egalitarian division found with minimum utility: 37.30569948
Allocation Table:
+----------+------------+------------+------------+------------+---------------+
|  Person  | Resource 1 | Resource 2 | Resource 3 | Resource 4 | Total Utility |
+----------+------------+------------+------------+------------+---------------+
| Person 1 | 0.00000000 | 0.00000000 | 0.00000000 | 0.93264249 |  37.30569948  |
| Person 2 | 0.93264249 | 0.00000000 | 0.00000000 | 0.00000000 |  37.30569948  |
| Person 3 | 0.06735751 | 1.00000000 | 0.02072539 | 0.00000000 |  37.30569948  |
| Person 4 | 0.00000000 | 0.00000000 | 0.97927461 | 0.06735751 |  37.30569948  |
+----------+------------+------------+------------+------------+---------------+
```

## Repository Structure

```
assignment_2/
├── question_3.py
└── README.md
```

## Description

The `egalitarian_division` function in `question_3.py` uses convex optimization (via CVXPY) to solve a fair division problem. For a given valuation matrix (with rows corresponding to persons and columns to resources), the function:
- Sets up the decision variable matrix `x` for allocations.
- Defines each person's utility.
- Adds constraints to ensure that 100% of each resource is allocated and that each person receives a utility at least equal to a variable `min_utility`.
- Maximizes the `min_utility` to ensure an equitable division.
- Validates the solution (ensuring that every resource is fully allocated and each person meets the minimum utility).
- Constructs and prints a nicely formatted table of allocations and total utilities using the `tabulate` module.

Feel free to modify the valuation matrices in the examples to test different scenarios.

Happy coding!