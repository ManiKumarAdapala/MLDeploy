import streamlit as st
st.title("Iris Data API")
st.write("- By Mani Kumar Adapala")

print("\n")

# Webpage

sl = st.slider('Sepal Length :', 4.3, 7.9, 5.1)
sw = st.slider('Sepal Width :', 2.2, 4.5, 3.5)
pl = st.slider('Petal Length :', 1.0, 6.9, 5.5)
pw = st.slider('Petal Width :', 0.1, 2.5, 2.2)


# Model

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

model = DecisionTreeClassifier()
model.fit(iris.data, iris.target)
k = model.predict([[sl,sw,pl,pw]])

name = iris.target_names[k[0]]

st.title(f'The Flower species is iris "{name}" ')