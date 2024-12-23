from typing import Dict, List, Optional


# Constraint class: to define the constraint between variables
class Constraint:
    def __init__(self, variable1: str, variable2: str) -> None:
        self.variable1 = variable1
        self.variable2 = variable2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If both variables have been assigned colors, check if they are different
        if self.variable1 in assignment and self.variable2 in assignment:
            return assignment[self.variable1] != assignment[self.variable2]
        return True  # If one of the variables is not yet assigned, we can't check yet


# CSP class: for solving the constraint satisfaction problem using backtracking
class CSP:
    def __init__(self, variables: List[str], domains: Dict[str, List[str]]) -> None:
        self.variables = variables  # list of variables (regions)
        self.domains = domains      # domain of each variable (possible colors)
        self.constraints = []       # list of constraints

    def add_constraint(self, constraint: Constraint) -> None:
        self.constraints.append(constraint)

    def consistent(self, variable: str, assignment: Dict[str, str]) -> bool:
        # Check if assigning a color to a variable satisfies all constraints
        for constraint in self.constraints:
            # Only check constraints involving the current variable
            if variable == constraint.variable1 or variable == constraint.variable2:
                if not constraint.satisfied(assignment):
                    return False
        return True

    def backtracking_search(self, assignment: Dict[str, str] = {}) -> Optional[Dict[str, str]]:
        # Base case: if the assignment is complete, return the assignment
        if len(assignment) == len(self.variables):
            return assignment

        # Choose an unassigned variable (we can just pick the first unassigned variable)
        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]

        # Try all possible values (colors) for the first unassigned variable
        for value in self.domains[first]:
            # Assign a value to the variable
            local_assignment = assignment.copy()
            local_assignment[first] = value

            # Check if the assignment is consistent
            if self.consistent(first, local_assignment):
                # Recurse to assign values to the remaining variables
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result

        # If no valid assignment found, return None
        return None


# Example usage: Solve the map coloring problem
if __name__ == "__main__":
    # List of regions (variables)
    variables = ["Western Australia", "Northern Territory", "South Australia",
                 "Queensland", "New South Wales", "Victoria", "Tasmania"]

    # Domain for each variable: possible colors
    domains = {variable: ["red", "green", "blue"] for variable in variables}

    # Create a CSP instance
    csp = CSP(variables, domains)

    # Add constraints (neighboring regions must not have the same color)
    csp.add_constraint(Constraint("Western Australia", "Northern Territory"))
    csp.add_constraint(Constraint("Western Australia", "South Australia"))
    csp.add_constraint(Constraint("South Australia", "Northern Territory"))
    csp.add_constraint(Constraint("Queensland", "Northern Territory"))
    csp.add_constraint(Constraint("Queensland", "South Australia"))
    csp.add_constraint(Constraint("Queensland", "New South Wales"))
    csp.add_constraint(Constraint("New South Wales", "South Australia"))
    csp.add_constraint(Constraint("Victoria", "South Australia"))
    csp.add_constraint(Constraint("Victoria", "New South Wales"))
    csp.add_constraint(Constraint("Victoria", "Tasmania"))

    # Solve the CSP using backtracking
    solution = csp.backtracking_search()

    # Print the result
    if solution:
        print("Solution found:")
        for variable, color in solution.items():
            print(f"{variable}: {color}")
    else:
        print("No solution found.")
