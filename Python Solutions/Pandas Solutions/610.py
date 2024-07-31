import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:

    triangle['triangle'] = ["Yes" if (row['z'] + row['y'] > row['x'] and row['x'] + row['z'] > row['y'] and row['x'] + row['y'] > row['z']) else "No" for i, row in triangle.iterrows()]

    return triangle
    