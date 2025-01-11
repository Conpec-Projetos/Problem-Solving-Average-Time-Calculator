import math
from dataclasses import dataclass

@dataclass
class ProblemSolverEfficiency:
    problem_ages: list[int]
    intervals: list[tuple[int, int]] = None
    frequencies: list[int] = None
    
    def sturges_rule(self) -> int:
        n = len(self.problem_ages)
        return math.ceil(1 + math.log2(n))
    
    def calculate_intervals_and_frequencies(self) -> None:
        k = self.sturges_rule()
        min_age, max_age = min(self.problem_ages), max(self.problem_ages)
        interval_size = math.ceil((max_age - min_age) / k)

        self.intervals = [(min_age + i * interval_size, min_age + (i + 1) * interval_size - 1) for i in range(k)]
        
        self.frequencies = [sum(1 for age in self.problem_ages if a <= age <= b) for (a, b) in self.intervals]
    
    def weighted_mean_intervals(self) -> float:
        weighted_sum = sum(((a + b) / 2) * f for (a, b), f in zip(self.intervals, self.frequencies))
        total_frequency = sum(self.frequencies)
        return weighted_sum / total_frequency if total_frequency != 0 else 0
    
    def calculate_efficiency(self) -> float:
        self.calculate_intervals_and_frequencies()
        return self.weighted_mean_intervals()
    
    def display_results(self) -> None:
        self.calculate_intervals_and_frequencies()
        print("Idades dos problemas:", self.problem_ages)
        print("Intervalos:", self.intervals)
        print("Frequências:", self.frequencies)
        print("Média ponderada dos intervalos:", self.calculate_efficiency())
