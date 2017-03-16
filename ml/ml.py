

```python
print("hello")
```

    hello



```python
from scipy.spatial.distance import cosine
import pandas as pd
import numpy as np
def run_scipy(s):
    s1 = np.array(pd.read_csv('total/total({}).csv'.format(s),index_col=0)[0:1])
    s2 = np.array(pd.read_csv('total/total({}).csv'.format(s),index_col=0)[1:2])
    cos = cosine(s1, s2)
    return   (1-cos)


def display_range(start, end):
    temp = 0
    for i in range(start, end):
        print(temp,"::", run_scipy(i))
        temp+=1
```


```python
div_ = []
y_div = []
start = 952
end = 1053
mid_point_wo_2 =   (end - start) // 2 
mid_point = mid_point_wo_2+ start 

print(mid_point, len_div)

for i in range(start, mid_point):
    y_div.append(0)
    div_.append([run_scipy(i)])

for i in range(mid_point, end):
    div_.append([run_scipy(i)])
    y_div.append(1)
    
len_div = len(div_)
print("--",len_div)
#print(div_[10], y_div[10])

```

    1002 0
    -- 101



```python
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem
import numpy as np
```


```python
svm = SVC()
x_train, x_test, y_train, y_test = train_test_split(div_, y_div,test_size=0.25, random_state=0 )
```


```python

def evaluate_cross_validation(clf, X, y, K=5):
    # create a k-fold croos validation iterator
    cv = KFold(len(y), K, shuffle=True, random_state=0)
    # by default the score used is the one returned by score method of the estimator (accuracy)
    scores = cross_val_score(clf, X, y, cv=cv)
    print (scores)
    print (("Mean score: {0:.3f} (+/-{1:.3f})").format(np.mean(scores), sem(scores)))
```


```python

#print(x_train, x_test, y_train, y_test )
def train_and_evaluate(clf, X_train, X_test, y_train, y_test):
    clf.fit(X_train, y_train)
    print("Acc train x:", clf.score(X_train, y_train))
    print("Acc test y:",  clf.score(X_test, y_test))
    y_pred = clf.predict(X_test)

    print ("Classification Report:")
    print (metrics.classification_report(y_test, y_pred))
    print ("Confusion Matrix:")
    print (metrics.confusion_matrix(y_test, y_pred))

```


```python
evaluate_cross_validation(svm, x_train, y_train, 5)
```

    [ 0.4         0.33333333  0.4         0.8         0.66666667]
    Mean score: 0.520 (+/-0.090)



```python
train_and_evaluate(svm, x_train, x_test, y_train, y_test)
```

    Acc train x: 0.826666666667
    Acc test y: 0.846153846154
    Classification Report:
                 precision    recall  f1-score   support
    
              0       0.81      0.93      0.87        14
              1       0.90      0.75      0.82        12
    
    avg / total       0.85      0.85      0.84        26
    
    Confusion Matrix:
    [[13  1]
     [ 3  9]]
