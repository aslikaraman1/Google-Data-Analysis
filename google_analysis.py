import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data=pd.read_csv('googleplaystore.csv')
print(data.head())


print(data.columns)
print(data.shape)
data.columns=data.columns.str.replace(" ","_")
print(data.columns)
print(data.dtypes)


print(data.isnull().sum())
sns.set_theme()
sns.set(rc={"figure.dpi":300, "figure.figsize":(12,9)})
sns.heatmap(data.isnull(), cbar=False)
plt.show()

rating_median=data["Rating"].median()
print(rating_median)
data["Rating"].fillna(rating_median, inplace=True)
data.dropna(inplace=True)
print(data.isnull().sum())
print(data.info())


print(data["Reviews"].describe())
data["Reviews"]=data["Reviews"].astype("int64")
data["Reviews"].describe().round()

print(data["Size"].unique())
data["Size"].replace("M","",regex=True,inplace=True)
data["Size"].replace("k","",regex=True,inplace=True)
print(data["Size"].unique())
size_median=data[data["Size"]!="Varies with device"]["Size"].astype(float).median()
print(size_median)
data["Size"].replace("Varies with device", size_median, inplace=True)
data["Size"]=data["Size"].astype("float")
print(data["Size"].head())
data.Size.describe().round()

print(data["Installs"].unique())
data.Installs=data.Installs.apply(lambda x:x.replace("+",""))
data.Installs=data.Installs.apply(lambda x:x.replace(",",""))
data.Installs=data.Installs.apply(lambda x:int(x))
print(data["Installs"].unique())
print(data["Installs"].dtypes)

print(data["Price"].unique())
data.Price=data.Price.apply(lambda x:x.replace("$",""))
data.Price=data.Price.apply(lambda x:float(x))
print(data["Price"].unique())

print(len(data["Genres"].unique()))
print(data["Genres"].head(10))
data["Genres"] = data["Genres"].str.split(";").str[0]
print(len(data["Genres"].unique()))
print(data["Genres"].unique())
print(data["Genres"].value_counts())
data["Genres"]=data["Genres"].replace("Music & Audio","Music", inplace=True)

print(data["Last_Updated"].head())
data["Last_Updated"] = pd.to_datetime(data["Last_Updated"])
print(data.head())
print(data.dtypes)


data["Type"].value_counts().plot(kind="bar", color ="red")
plt.title("Free & Paid")
plt.show()

sns.boxplot(x = "Type", y = "Rating", data = data)
plt.title("Content rating with their counts")
plt.show()

sns.countplot(y = "Content_Rating", data = data)
plt.title("Content rating with their counts")
plt.show()

sns.boxplot(x = "Content_Rating", y = "Rating", data = data)
plt.title("The content rating & rating", size=20)
plt.show()

sns.scatterplot(data = data, y = "Category", x = "Price")
plt.title("Category & Price", size=20)
plt.show()