import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


# Columns with non-numerical values
categorical_columns = ['RCONSC', 'SEX', 'RSLEEP', 'RATRIAL', 'RCT', 'RVISINF', 'RHEP24',
                       'RASP3', 'RDEF1', 'RDEF2', 'RDEF3', 'RDEF4', 'RDEF5', 'RDEF6', 'RDEF7', 'RDEF8', 'STYPE', 'RDATE', 'RXASP', 'RXHEP',
                       'DASP14', 'DASPLT', 'DLH14', 'DMH14', 'DSCH', 'DCAA', 'DDIAGISC', 'DRSUNK', 'DALIVE',
                       'FDENNIS', 'FPLACE', 'FAP', 'FOAC', 'COUNTRY', 'CMPLASP', 'CMPLHEP']


class MultiColumnLabelEncoder:
    def __init__(self, columns=None):
        self.columns = categorical_columns  # array of column names to encode

    def fit(self, X, y=None):
        return self  # not relevant here

    def transform(self, X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        print(self.columns)
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname, col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)
