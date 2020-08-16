from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np


class Classificador():

	def __init__(self, path):

		self.dados = pd.read_csv(path, encoding='unicode_escape')
		self.dados["Date"] = pd.to_datetime(self.dados["Date"], format='%Y-%m-%d %H:%M:%S')



	def preprocessing(self):	

		le = LabelEncoder()
		self.dados.IsSpam = le.fit_transform(self.dados.IsSpam)


	def treina_modelo(self, modelo_select):

		X = self.dados.drop(columns = ["Full_Text","Date","IsSpam"])
		y = self.dados.IsSpam


		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,y, test_size=0.3, random_state=42)

		if modelo_select == "random forest": 
			self.modelo = RandomForestClassifier()

		if modelo_select == "decision tree": 
			self.modelo = DecisionTreeClassifier()

		if modelo_select == "support vector classifier":	
			self.modelo = SVC()

		if modelo_select == "kNeighbors classifier":
			self.modelo = KNeighborsClassifier()

		if modelo_select == "adaboost classifier":
			self.modelo = AdaBoostClassifier()

		self.modelo.fit(self.X_train,self.y_train)

	def preve_modelo(self):    

	    self.y_pred = self.modelo.predict(self.X_test)
	    self.class_rep = classification_report(self.y_test,self.y_pred)
	    self.acc_score = accuracy_score(self.y_test,self.y_pred)
	    self.conf_mat = confusion_matrix(self.y_test,self.y_pred)

