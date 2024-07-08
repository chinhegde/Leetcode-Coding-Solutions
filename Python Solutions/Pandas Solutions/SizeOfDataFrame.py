# https://leetcode.com/problems/get-the-size-of-a-dataframe/description/
# 2878. Get the Size of a DataFrame

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:

    return list(players.shape)
    