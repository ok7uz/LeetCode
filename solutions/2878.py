import pandas as pd


List = list


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players), len(players.columns)]
    