# https://leetcode.com/problems/big-countries/

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    return world[(world['population'] >= 25000000) | (world['area'] >= 3000000)][['name', 'population', 'area']]