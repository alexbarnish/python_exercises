#--------------------------------------- Project Info ---------------------------------------#
# Tutorial: 10 Minutes to pandas
# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html


#--------------------------------------- Libraries ---------------------------------------#
import numpy as np
import pandas as pd


#--------------------------------------- Main ---------------------------------------#
# create series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print s

# create date range
dates = pd.date_range('20190404', periods=6)
print dates

# create random date
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print df

# create data frame
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20190404'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'
                    })
print df2
print df2.dtypes

print df.head(2)

print df.tail(2)
print df2.index
print df2.columns