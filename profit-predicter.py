#importing required modules
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import  numpy
from sklearn.preprocessing import OneHotEncoder

#loading the dataset using pandas
dataset=pandas.read_csv('50_Startups.csv')

#setting features and predictor
y=dataset['Profit']
x=dataset[['R&D Spend','Administration','Marketing Spend']]

#creating model using liner regression()
model=LinearRegression()

#converting string to numeric using label encoder
state=dataset['State']
label=LabelEncoder()
state_label=label.fit_transform(state)
state_label=state_label.reshape(-1,1)

#performing onehot encoding
state_ohe=OneHotEncoder()
state_ohe_final=state_ohe.fit_transform(state_label)
#converting it into an array
dump=state_ohe_final.toarray()
final_state=dump[ : ,0:2]

#splitting data for  training and testing 
x_train,x_test,y_train,y_test=train_test_split(x_final,y,test_size=0.30)

#training model
model.fit(x_train,y_train)

#For Testing the model
model.coef_
y_pre=model.predict(x_test)
#Running program to take imput from user and perform model prediction
stop=input("Enter a to stop and click any other to continue")
while(True):
    if(stop=='a'):
        print("you choose to stop")
        break
    else:
        rd=float(input("enter r&d"))
        adm=float(input("enter administration"))
        mar=float(input("enter Marketingspend"))
        state=input("enter state")
        s1=0
        s2=0
        if state=='California':
            s1=0
        if state=='Florida':
             s2=1
        t_final=[[rd,adm,mar,s1,s2]]
        res=model.predict(t_final)
        print("Predicted value,",res)
