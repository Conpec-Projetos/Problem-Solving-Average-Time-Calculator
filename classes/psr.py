from dataclasses import dataclass
import pandas as pd
from datetime import datetime
import pytz

@dataclass
class ProblemSolverReader:
    file_path: str
    
    def get_problem_ages_without_curr_date_column(self, desired_status: str) -> list[int]:
        df = pd.read_csv(self.file_path)
        df = df[df['status'] == desired_status]
        
        sp_tz = pytz.timezone('America/Sao_Paulo')
        
        df['start-date'] = pd.to_datetime(df['start-date'], format='%d/%m/%Y')
        df['start-date'] = df['start-date'].dt.tz_localize(sp_tz, ambiguous='NaT')
        
        curr_date = datetime.now(sp_tz)
        
        return (curr_date - df['start-date']).dt.days.tolist()
    
    def get_problem_ages_with_curr_date_column(self, desired_status: str) -> list[int]:
        df = pd.read_csv(self.file_path)
        df = df[df['status'] == desired_status]
        
        sp_tz = pytz.timezone('America/Sao_Paulo')
        
        df['start-date'] = pd.to_datetime(df['start-date'], format='%d/%m/%Y')        
        df['start-date'] = df['start-date'].dt.tz_localize(sp_tz, ambiguous='NaT')
        
        df['current-date'] = pd.to_datetime(df['current-date'], format='%d/%m/%Y')
        df['current-date'] = df['current-date'].dt.tz_localize(sp_tz, ambiguous='NaT')
        
        return (df['current-date'] - df['start-date']).dt.days.tolist()
    
    def display_results(self) -> None:
        print("Idades dos problemas:", self.read_file())