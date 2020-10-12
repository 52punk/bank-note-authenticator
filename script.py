# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:29:33 2020

@author: Pankaj Kumar Sah
@LinkedIn: https://www.linkedin.com/in/pankaj-sah-b7aa39186/
@Github: https://github.com/52punk

"""
import pandas as pd
import numpy as np
df=pd.read_csv('BankNoteAuthentication.csv')

X=df.iloc[:,:-1]
y=df.iloc[:,-1]

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

### Implement Random Forest classifier
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)

score
import pickle
pickle_out=open("bank_note_new.pkl", "wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()
