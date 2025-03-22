import pandas as pd
from sklearn.model_selection import train_test_split
 
def split_x_y(df:pd.DataFrame,col='Sentence',tar='Sentiment',random_state=42,test_split=0.2):
    x=df[col]
    y=df[tar]
    x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=test_split, random_state=random_state)
    
    return x_train,x_test,y_train,y_test
    
