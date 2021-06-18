import pandas as pd
import numpy as np


class DataSets:
    @staticmethod
    def add_bias(arr, bias=-1):
        biased_arr = np.ndarray(shape=(arr.shape[0], arr.shape[1] + 1), dtype=float)
        for i in range(0, len(arr)):
            biased_arr[i] = np.append(bias, arr[i])

        return biased_arr

class ANIMAIS:
    df = pd.read_csv("animais.csv")
    df.isna().any()

    input = DataSets.add_bias(np.array((df["pelo_longo"], df["perna_curta"], df["late"])).reshape(-1,3))
    outputs = np.array(list(df["animal"])).reshape(-1, 1)

    output = np.arange(outputs.size, dtype=float).reshape(-1, 1)
    for i in range(outputs.size):
        if outputs[i] == 'cachorro':
            output[i] = 0
        else:
            output[i] = 1
