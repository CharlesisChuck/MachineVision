import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, svm, model_selection
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-999999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
#print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)




#y = np.array(df['label'])
#x = preprocessing.scale(x)#probally skip if speed was important
#X = X[:-forecast_out+1] #because we won't have a label, but we already dropped the labels

x = np.array(df.drop(['label'],1))
x = preprocessing.scale(x)
#x = x[:-forecast_out]
x_lately = x[-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])
y = np.array(df['label'])



#print(len(x),len(y))

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
#clf = svm.SVR()
#clf = svm.SVR(kernel='poly')
clf.fit(x_train, y_train)
accuracy = clf.score(x_test,y_test)

print(accuracy)

forecast_set = clf.predict(x_lately)

print(forecast_set, accuracy, forecast_out)


