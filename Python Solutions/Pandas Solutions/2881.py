# https://leetcode.com/problems/create-a-new-column/
# 2881. Create a New Column

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees['bonus'] = employees['salary']*2
    return employees