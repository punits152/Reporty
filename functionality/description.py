from numpy import info
import pandas as pd
import numpy as np

class DataGetter():
    def __init__(self,file_object):
        self.file = file_object
    def get_dataframe(self):
        df = pd.read_csv(self.file)
        return df


class Descriptor():
    def __init__(self,data_frame ):
        # this accepts a data frame object because it increases the speed of execution if we can get the df
        self.df = data_frame

    # These three methods will provide dataframe objects so we have to do some prettfying thing
    # When showing them
    def get_head(self):
        return self.df.head()

    def get_tail(self):
        return self.df.tail()
    
    def get_summary(self):
        return self.df.describe()

    def get_suggestion(self):

        # Prints: Suggestion no 1
        info = self.na_values(self.df)
        for col_name, na_count in info:
            print(f'Column: {col_name} have {na_count} nan values. Which is approximately {np.round((na_count/self.df.shape[0])*100)}% of the data')
        # Why 




    # These are utility functions.
    def na_values(self,df):
        # This will provide the number of na values and the columns name
        cols=[]
        vals=[]
        na = df.isna().sum()
        for col_name, na_count in zip(na.index,na.values):
            if na_count != 0:
                cols.append(col_name)
                vals.append(na_count)
        return zip(cols, vals)

