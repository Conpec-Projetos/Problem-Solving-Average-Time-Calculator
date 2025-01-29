import math
from dataclasses import dataclass

@dataclass
class ProblemSolverEfficiency:
    problem_ages: list[int]
    intervals: list[tuple[int, int]] = None
    frequencies: list[int] = None
    goal_in_days: int = 10
    efficiency: float = 0.0

    def sturges_rule(self) -> int:
        n = len(self.problem_ages)
        if (n == 0):
            return 0
        return math.ceil(1 + math.log2(n))
    
    def calculate_intervals_and_frequencies(self) -> None:
        k = self.sturges_rule()
        if (self.problem_ages == []):
            return
        min_age, max_age = min(self.problem_ages), max(self.problem_ages)
        interval_size = math.ceil((max_age - min_age) / k)

        self.intervals = [(min_age + i * interval_size, min_age + (i + 1) * interval_size - 1) for i in range(k)]
        
        self.frequencies = [sum(1 for age in self.problem_ages if a <= age <= b) for (a, b) in self.intervals]

    def weighted_mean_intervals(self) -> float:
        if (not self.intervals or not self.frequencies):
            return 0
        weighted_sum = sum(((a + b) / 2) * f for (a, b), f in zip(self.intervals, self.frequencies))
        total_frequency = sum(self.frequencies)
        return weighted_sum / total_frequency if total_frequency != 0 else 0

    def calculate_efficiency(self) -> float:
        self.calculate_intervals_and_frequencies()
        self.efficiency = round(self.weighted_mean_intervals(), 2)

    def calculate_goal_efficiency_in_percentage(self) -> float:
        if (self.efficiency == 0):
            return 10000
        return self.goal_in_days / self.efficiency * 100

    def display_results(self) -> None:
        self.calculate_efficiency()
        print("Idades dos problemas:", self.problem_ages)
        print("Intervalos:", self.intervals)
        print("Frequências:", self.frequencies)
        print("Média ponderada dos intervalos:", self.efficiency)

        efficiency = round(self.calculate_goal_efficiency_in_percentage(), 2)
        colors = {efficiency > 100: '\033[94m', efficiency == 100: '\033[92m', 70 <= efficiency < 100: '\033[93m'}
        color = colors.get(True, '\033[91m')
        reset_color = '\033[0m'

        print(f"Eficiência: {color}{efficiency}%{reset_color}")