# load the iris dataset
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, confusion_matrix
iris = load_iris()

# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target

# splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

# training the model on training set
Gaussian_Navie_Bayes = GaussianNB()
Gaussian_Navie_Bayes.fit(X_train, y_train)

# making predictions on the testing set
y_pred = Gaussian_Navie_Bayes.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)
print("Confusion matrix: \n", confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Model accuracy: ",
      metrics.accuracy_score(y_test, y_pred)*100)
