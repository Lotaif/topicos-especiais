#import inline as inline
#import matplotlib
#import sklearn

from sklearn.datasets import load_wine


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score

data = load_wine()

label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']


train, test, train_labels, test_labels = train_test_split(features,labels,test_size = 0.25, random_state = 0)

gnb = GaussianNB()

model = gnb.fit(train, train_labels)

preds = gnb.predict(test)

print(accuracy_score(test_labels,preds))


print(preds)
print(test_labels)

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.metrics import confusion_matrix

mat = confusion_matrix(test_labels, preds)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=label_names, yticklabels=label_names)
plt.xlabel('true label')
plt.ylabel('predicted label')

print(mat)
plt.savefig("out.png")