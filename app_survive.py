import streamlit as st
import pandas as pd
from pickle import load

def get_features():
    st.title('Survival Analysis')
    st.write ( 'Will this  person Survive?')
    Age = st.sidebar.slider('Age', min_value=0,max_value=100)
    Sex = st.sidebar.radio("Sex:",['Male', 'Female'])
    if Sex =='Male':
      Sex=1
    else:
      Sex=0
    Embarked = st.sidebar.radio("Embarked :",['c','Q','S'])
    if Embarked =='C':
       Embarked = 0
    elif Embarked =='Q':
       Embarked = 1
    else :
       Embarked =2
    Fare        =st.sidebar.number_input("Enter the Fare: ")
    PassengerId =st.sidebar.number_input("Enter the PassengerId : ")
    Pclass	= st.sidebar.radio("Pclass:",['1', '2','3'])	
    SibSp	= st.sidebar.slider('SibSp', min_value=0,max_value=10)
    Parch	=st.sidebar.number_input("Enter the Parch : ")

    inp_data = {'PassengerId': PassengerId,
                'Pclass':Pclass,
                'Sex':Sex,	
                'Age':Age,
                'SibSp':SibSp,
                'Parch':Parch,
	            'Fare':Fare,		
	    	    'Embarked':Embarked
	           }
    new_data=pd.DataFrame(inp_data, index=[0])
    return new_data


loaded_model =load(open('clf_survive.pkl','rb'))
user_data=get_features()

if st.sidebar.button('Submit'):
  result=loaded_model.predict(user_data)
  if result == '0':
     ans= 'Yes, this person will Survive'
  else:
    ans= 'No, this person will not Survive'
  st.write(ans)




