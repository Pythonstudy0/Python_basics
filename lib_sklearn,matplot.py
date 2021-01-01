import pandas as pd 
import matplotlib.pyplot as plt

dataset=pd.read_csv('Salary_Data.csv')

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1:].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y
                                                ,test_size=0.2
                                                ,random_state=0
                                                )
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)            
y_prd=regressor.predict(x_test) 

# 시각화
plt.scatter(x_test,y_test, color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title("salary vs Experience")
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.legend(['model','actual_values'], shadow='true')
plt.savefig('Salary vs Experience (test v1)')
plt.show()



