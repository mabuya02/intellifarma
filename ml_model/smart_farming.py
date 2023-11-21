

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#for interactivity
from ipywidgets import interact

# import dataset :
url = "https://raw.githubusercontent.com/arzzahid66/Optimizing_Agricultural_Production/master/Crop_recommendation.csv"
df =pd.read_csv(url)

# check the shape of dataset
print("The shape of dataset is :",df.shape)

# find and count missing values
df.isnull().sum()

# lets check crops presents in this dataset
df["label"].value_counts()

df.columns

# checking the summary of all crops
print("average ratio of nitrogen in soil : {0:2f}".format(df["N"].mean()))
print("average ratio of nitrogen in soil : {0:2f}".format(df["P"].mean()))
print("average ratio of nitrogen in soil : {0:2f}".format(df["K"].mean()))
print("average ratio of nitrogen in soil : {0:2f}".format(df["temperature"].mean()))
print("average ratio of nitrogen in soil : {0:2f}".format(df["humidity"].mean()))
print("average ratio of nitrogen in soil : {0:2f}".format(df["ph"].mean()))
print("average ratio of nitrogen in soil : {0:2f}".format(df["rainfall"].mean()))

# lets check the summary of statistics for each of crops
@interact
def summary(crops=list(df["label"].value_counts().index)):
    x=df[df["label"]==crops]
    print("...........................................")
    print("statistics for nitrogen")
    print("minimum nitrogen required :",x["N"].min())
    print("average nitrogen required :",x["N"].mean())
    print("maximum nitrogen required :",x["N"].max())
    print("...........................................")
    print("statistics for phosphorous")
    print("minimum phosphorous required :",x["P"].min())
    print("average phosphorous required :",x["P"].mean())
    print("maximum phosphorous required :",x["P"].max())
    print("...........................................")
    print("statistics for potassium")
    print("minimum potassium required :",x["K"].min())
    print("average potassium required :",x["K"].mean())
    print("maximum potassium required :",x["K"].max())
    print("...........................................")
    print("statistics for temperature")
    print("minimum temperature required :{0:2f}".format(x["temperature"].min()))
    print("average temperature required :{0:2f}".format(x["temperature"].mean()))
    print("maximum temperature required :{0:2f}".format(x["temperature"].max()))
    print("...........................................")
    print("statistics for humidity")
    print("minimum humidity required :{0:2f}".format(x["humidity"].min()))
    print("average humidity required :{0:2f}".format(x["humidity"].mean()))
    print("maximum humidity required :{0:2f}".format(x["humidity"].max()))
    print("...........................................")
    print("statistics for ph")
    print("minimum ph required :{0:2f}".format(x["ph"].min()))
    print("average ph required :{0:2f}".format(x["ph"].mean()))
    print("maximum ph required :{0:2f}".format(x["ph"].max()))
    print("...........................................")
    print("statistics for rainfall")
    print("minimum rainfall required :{0:2f}".format(x["rainfall"].min()))
    print("average rainfall required :{0:2f}".format(x["rainfall"].mean()))
    print("maximum rainfall required :{0:2f}".format(x["rainfall"].max()))

# lets compare the average requirement for each crops with conditions

@interact
def compare(conditions=["N","K","P","temperature","humidity","ph","rainfall"]):
    print("average value for",conditions,"is {0:2f}".format(df[conditions].mean()))
    print("--------------------------------------------------------------")
    print("rice :{0:2f}".format(df[(df["label"]=="rice")][conditions].mean()))
    print("black grams :{0:2f}".format(df[(df["label"]=="black grams")][conditions].mean()))
    print("banana :{0:2f}".format(df[(df["label"]=="banana")][conditions].mean()))
    print("maize :{0:2f}".format(df[(df["label"]=="maize")][conditions].mean()))
    print("chickpea :{0:2f}".format(df[(df["label"]=="chickpea")][conditions].mean()))
    print("kidneybeans :{0:2f}".format(df[(df["label"]=="kidneybeans")][conditions].mean()))
    print("pigeonpeas :{0:2f}".format(df[(df["label"]=="pigeonpeas")][conditions].mean()))
    print("mothbeans :{0:2f}".format(df[(df["label"]=="mothbeans")][conditions].mean()))
    print("lentil:{0:2f}".format(df[(df["label"]=="lentil")][conditions].mean()))
    print("pomegranate :{0:2f}".format(df[(df["label"]=="pomegranate")][conditions].mean()))
    print("grapes :{0:2f}".format(df[(df["label"]=="grapes")][conditions].mean()))
    print("watermelon :{0:2f}".format(df[(df["label"]=="watermelon")][conditions].mean()))
    print("muskmelon :{0:2f}".format(df[(df["label"]=="muskmelon")][conditions].mean()))
    print("apple :{0:2f}".format(df[(df["label"]=="apple")][conditions].mean()))
    print("orange :{0:2f}".format(df[(df["label"]=="orange")][conditions].mean()))
    print("papaya :{0:2f}".format(df[(df["label"]=="papaya")][conditions].mean()))
    print("coconut :{0:2f}".format(df[(df["label"]=="coconut")][conditions].mean()))
    print("cotton :{0:2f}".format(df[(df["label"]=="cotton")][conditions].mean()))
    print("coffee :{0:2f}".format(df[(df["label"]=="coffee")][conditions].mean()))
    print("mungbean :{0:2f}".format(df[(df["label"]=="mungbean")][conditions].mean()))
    print("coffee :{0:2f}".format(df[(df["label"]=="coffee")][conditions].mean()))
    print("mango :{0:2f}".format(df[(df["label"]=="mango")][conditions].mean()))

# Making the function more interactive: compare less average and greater average
@interact
def compare(conditions=["N","P","K","temperature","ph","humidity","rainfall"]):
    print("crops with require greater than average",conditions,'\n')
    print(df[df[conditions]>df[conditions].mean()]["label"].unique())
    print("----------------------------------------------------------------------")
    print("crops wich require less than average",conditions,'\n')
    print(df[df[conditions]<=df[conditions].mean()]["label"].unique())

# Finding interesting facts

print("Some interesting facts")
print("..........................................")
print("crop which requires very high ratio of nitrogen content in soil",df[df["N"]>120]["label"].unique())
print("crop which requires very high ratio of phosphorous content in soil",df[df["P"]>100]["label"].unique())
print("crop which requires very high ratio of potassium content in soil",df[df["K"]>200]["label"].unique())
print("crop which requires very high ratio of temperature content in soil",df[df["temperature"]>40]["label"].unique())
print("crop which requires very low ratio of temperature content in soil",df[df["temperature"]<10]["label"].unique())
print("crop which requires very low ratio of humidity content in soil",df[df["humidity"]<20]["label"].unique())
print("crop which requires very high ratio of ph",df[df["ph"]>9]["label"].unique())
print("crop which requires very low ratio of ph ",df[df["ph"]<4]["label"].unique())
print("crop which requires very high rainfall content in soil",df[df["rainfall"]>200]["label"].unique())

# Understanding which crops can only be grown in summer season, winter season, and rainy season

print("summer crops :")
print(df[(df["temperature"]>30) & (df["humidity"]>50)]["label"].unique())
print("...............................................................")
print("winter crops :")
print(df[(df["temperature"]<20) & (df["humidity"]>30)]["label"].unique())
print("----------------------------------------------------------")
print("Rainy crops :")
print(df[(df["rainfall"]>200) & (df["humidity"]>30)]["label"].unique())

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

