from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
import numpy as np
import numpy.linalg as LA
f1 = open("TFIDF/textfile1.txt").read()
f2 = open("TFIDF/textfile2.txt").read()
f3 = open("TFIDF/textfile3.txt").read()
train_set = [f1, f2, f3]  # Documents
test_set = ["What is machine learning"]  # Query
stopWords = stopwords.words('english')

vectorizer = CountVectorizer(stop_words=stopWords)
# print vectorizer
transformer = TfidfTransformer()
# print transformer

trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()
testVectorizerArray = vectorizer.transform(test_set).toarray()
print('Fit Vectorizer to train set', trainVectorizerArray)
print('Transform Vectorizer to test set', testVectorizerArray)
def cx(a, b): return round(np.inner(a, b)/(LA.norm(a)*LA.norm(b)), 3)


for vector in trainVectorizerArray:
    print(vector)
    for testV in testVectorizerArray:
        print(testV)
        cosine = cx(vector, testV)
        print("Cosone sim: ", cosine)

transformer.fit(trainVectorizerArray)
print(transformer.transform(trainVectorizerArray).toarray())
transformer.fit(testVectorizerArray)
tfidf = transformer.transform(testVectorizerArray)
print(tfidf.todense())
