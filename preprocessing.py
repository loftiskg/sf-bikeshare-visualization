import pandas as pd

def preprocess_data(csv_filename):
    time_grouped_weekend = pd.read_csv(csv_filename,index_col = 0,parse_dates=True)
    time_grouped_weekend = time_grouped_weekend.sort_values(['name','Hour'])
    workweek = time_grouped_weekend.loc[time_grouped_weekend.Weekend==False,:]
    weekend = time_grouped_weekend.loc[time_grouped_weekend.Weekend==True,:]

    return workweek,weekend
