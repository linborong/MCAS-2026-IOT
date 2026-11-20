import numpy as np 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = np.loadtxt("Bank_Customer.csv",skiprows=1,dtype=str,delimiter=',')

'''
Your work
非數值型資料需轉換成數值型資料 (country, gender)
去除掉無意義的特徵類別 (customer_id)
標準化特徵 (StandardScaler)
'''
# pre_data = ...
country = data[:, 2]
gender = data[:, 3]

features = np.column_stack((
    data[:, 1].astype(float),
    (country == "France").astype(int),
    (country == "Germany").astype(int),
    (country == "Spain").astype(int),
    (gender == "Male").astype(int),
    data[:, 4:-1].astype(float),
))

labels = data[:, -1].astype(int)


from sklearn.linear_model import LogisticRegression 
# 決策分類器
clf = LogisticRegression()

x_train, x_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.30, random_state=42, stratify=labels
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

pre_data = np.column_stack((scaler.transform(features), labels))
np.savetxt("Bank_Customer_Preprocessed.csv", pre_data, delimiter=",")

print("Preprocessed:", pre_data.shape)
print("Training:", x_train.shape)
print("Testing:", x_test.shape)
# 使用訓練集來訓練我們的分類器
clf.fit(x_train, y_train)
# 測試資料集中進行預測
pred = clf.predict(x_test)

#print (pred) # 預測分類，即客戶是否流失
#print (y_test) # 分類
print (str(accuracy_score(pred, y_test)*100 ) + "% ")   # 預測精度 