import cvxpy as cp
import numpy as np
from tabulate import tabulate  # make sure to install via pip if not already installed


def egalitarian_division(valuations):
    """
    Compute an egalitarian division of resources.
    
    Parameters:
    valuations: numpy array where valuations[i, j] is the value 
                that person i assigns to resource j.
                - i ranges from 0..(n_people-1)
                - j ranges from 0..(n_resources-1)
    
    Returns:
    A string describing the allocation and each person's utility.
    """
    # valuations.shape -> (n_people, n_resources)
    n_people, m_resources = valuations.shape
    
    # Define the decision variables:
    # x[i, j] is the fraction of resource j allocated to person i
    x = cp.Variable((n_people, m_resources), nonneg=True)
    
    # Each person's utility is the sum of their allocated resource fractions 
    # times their valuation of those resources.
    utilities = [cp.sum(cp.multiply(x[i, :], valuations[i, :])) for i in range(n_people)]
    
    # min_utility is a variable representing the smallest utility across all people
    min_utility = cp.Variable()
    
    # Constraints
    constraints = []
    
    # 1) Each resource j must be fully allocated (sum of fractions == 1).
    #    This works regardless of how many people or resources there are.
    for j in range(m_resources):
        constraints.append(cp.sum(x[:, j]) == 1)
    
    # 2) Each person's utility must be at least min_utility.
    for i in range(n_people):
        constraints.append(utilities[i] >= min_utility)
    
    # Objective: maximize the minimum utility
    objective = cp.Maximize(min_utility)
    
    # Solve the problem
    problem = cp.Problem(objective, constraints)
    problem.solve() 
    
    # Extract results
    allocation = x.value          # The matrix of allocated fractions
    min_util_value = min_utility.value
    
    # Validation checks:
    tolerance = 1e-4
    # Check that each resource is fully allocated.
    for j in range(m_resources):
        resource_sum = sum(allocation[i, j] for i in range(n_people))
        assert abs(resource_sum - 1) < tolerance, f"Resource {j+1} not fully allocated: {resource_sum}" 
    
    # Check that each person's utility meets the min_utility constraint.
    for i in range(n_people):
        person_util = sum(allocation[i, j] * valuations[i, j] for j in range(m_resources))
        assert person_util + tolerance >= min_util_value, f"Person {i+1}'s utility {person_util} is below min utility {min_util_value}"

    # return results
        # Build table headers and rows
    table_headers = ["Person"] + [f"Resource {j+1}" for j in range(m_resources)] + ["Total Utility"]
    table_data = []
    for i in range(n_people):
        row = [f"Person {i+1}"]
        for j in range(m_resources):
            row.append(f"{allocation[i, j]:.8f}")
        row.append(f"{utilities[i].value:.8f}")
        table_data.append(row)
    
    alloc_table = tabulate(table_data, headers=table_headers, tablefmt="pretty")
    
    result = f"Egalitarian division found with minimum utility: {min_util_value:.8f}\n"
    result += "Allocation Table:\n" + alloc_table

    return result


if __name__ == "__main__":

    # Example #1: 2 people, 3 resources
    valuations = np.array([
        [81,  19,  1],   # Person 1's valuations
        [70,  1,  29],   # Person 2's valuations
    ])
    
    print("Valuation matrix #1:")
    print(valuations)
    print("\n" + egalitarian_division(valuations))

    
    # Example #2: 4 people, 3 resources
    valuations2 = np.array([
        [9, 20, 11],   # Person 1's valuations
        [12, 18, 10],  # Person 2's valuations
        [14, 17, 9],   # Person 3's valuations
        [10, 15, 20],  # Person 4's valuations
    ])
    
    print("\nValuation matrix #2:")
    print(valuations2)
    print("\n" + egalitarian_division(valuations2))
    
    # Example #3: 3 people, 3 resources
    valuations3 = np.array([
        [15, 25, 10],  # Person 1's valuations
        [20, 10, 30],  # Person 2's valuations
        [25, 40, 5],   # Person 3's valuations
    ])

    
    print("\nValuation matrix #3:")
    print(valuations3)
    print("\n" + egalitarian_division(valuations3))


    # Example #4: 3 people, 4 resources
    valuations4 = np.array([
        [10, 20, 30, 40],  # Person 1's valuations
        [40, 30, 20, 10],  # Person 2's valuations
        [25, 25, 25, 25],  # Person 3's valuations
    ])
    
    print("\nValuation matrix #4:")
    print(valuations4)
    print("\n" + egalitarian_division(valuations4))
