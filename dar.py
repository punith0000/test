import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("C:\\Users\\admin\\Desktop\\mtcars.csv")
# print(df)

df = pd.DataFrame({
    'model' : ['Mazda','Datsun','Hornet','Merc','Mazda'],
    'mpg' : [21,22.8,258,24.4,22],
    'transmission' : [160,108,258,95,180]
})
# print(df)
group = df.groupby('mpg').value_counts()
a = plt.hist(group)
a.show()