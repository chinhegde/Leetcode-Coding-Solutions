# https://leetcode.com/problems/drop-missing-data/
# 2883. Drop Missing Data

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = ['name'], axis = 0)