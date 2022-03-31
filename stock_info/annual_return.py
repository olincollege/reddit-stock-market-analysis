import pandas as pd




def get_annual_return(path):
    """
    Given a path to a csv containing 1 years worth of data from a stock,
    find the annual return / ROI
    """
    dataframe = pd.read_csv(path)

    start_val = list(dataframe['close'])[0]
    end_val = list(dataframe['close'])[-1]

    roi = ((end_val - start_val) / start_val) * 100

    return roi




