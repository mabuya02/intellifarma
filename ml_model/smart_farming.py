import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# import dataset :
url = "https://raw.githubusercontent.com/arzzahid66/Optimizing_Agricultural_Production/master/Crop_recommendation.csv"
df =pd.read_csv(url)






import warnings
warnings.filterwarnings('ignore')

z = df.drop(['label'],axis=1)
z = df.loc[:,z.columns].values
x_df = pd.DataFrame(z)
x_df.head()

#Determine Optimum number of cluster by elbow method
from sklearn.cluster import KMeans
plt.rcParams['figure.figsize'] = (10,4)
wcss = []
for i in range (1,11):
    km = KMeans(n_clusters =i, init= 'k-means++', max_iter=300, n_init=10, random_state=0)
    km.fit(z)
    wcss.append(km.inertia_)
#plot the results
plt.plot(range(1,11), wcss)
plt.title('Elbow Method', fontsize= 15)
plt.xlabel('No. of cluster')
plt.ylabel('wcss')
plt.show()

km = KMeans(n_clusters =4, init= 'k-means++', max_iter=300, n_init=10, random_state=0)
y_means= km.fit_predict(z)

a = df['label']
y_means = pd.DataFrame(y_means)
w = pd.concat([y_means, a], axis=1)
w =w.rename(columns= {0:'cluster'})

#Checking Cluster of each group

for i in range(0,4): #for 4 clusters 0,1,2,3
    print('Crops is cluster', i, w[w['cluster']==i]['label'].unique())
    print('---------------------------------------------------------------------------------------')

# Spliting the dataset for predictive modelling
y=df["label"]
x=df.drop(["label"],axis=1)

print("shape of x :",x.shape)
print("shape of y :",y.shape)

# Creating training and testing sets for validation of results
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

print("shape of x_train :",x_train.shape)
print("shape of x_test :",x_test.shape)
print("shape of y_train :",y_train.shape)
print("shape of y_test : ",y_test.shape)

# Creating predictive model
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
y_predict =model.predict(x_test)

# Evaluating the model performance
from sklearn.metrics import confusion_matrix

# Printing confusion metrics
plt.rcParams['figure.figsize'] =(10, 10)
cm=confusion_matrix(y_test,y_predict)
sns.heatmap(cm,annot=True ,cmap='Wistia')
plt.title('confusion matrix for logistic regression  ',fontsize=15)
plt.show()

df.head(5)

# lets predict real time data
prediction = model.predict((np.array([[74,35,40,26.49,80.15,6,242]])))
print("The best crop predicted is:",prediction)

