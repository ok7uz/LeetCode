import sys


problem_id = sys.argv[1]
solution = open(f'solutions/{problem_id}.py').read()

exec(solution)
