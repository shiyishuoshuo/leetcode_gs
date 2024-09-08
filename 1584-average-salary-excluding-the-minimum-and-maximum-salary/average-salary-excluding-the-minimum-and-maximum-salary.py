class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary, max_salary = min(salary), max(salary)
        total_salary = sum(salary)

        return (total_salary - min_salary- max_salary) / (len(salary) - 2)
        