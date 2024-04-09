import pandas as pd


List = list


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    data_frame = pd.DataFrame(student_data)
    data_frame.columns = ['student_id', 'age']
    return data_frame
