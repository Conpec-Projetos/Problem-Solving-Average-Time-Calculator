from classes.pse import ProblemSolverEfficiency
from classes.psr import ProblemSolverReader

problem_ages = ProblemSolverReader(
    "data/mock_problems.csv"
    ).get_problem_ages_with_curr_date_column('solved')

solver_efficiency = ProblemSolverEfficiency(problem_ages)
solver_efficiency.display_results()