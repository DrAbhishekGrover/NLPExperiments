Write a python code to implement Naive Bayes and Logistic Regression from first principles
(without using ML library) for Movie review classification. The structure of the code is as follows:

(a) Function clean_text(text): Takes a raw text and implements preprocessing on it. The
following pre-processing task need to be implemented: normalization, special character
and stop word removal.

(b) Split the dataset into training and test set with a split ratio of 0.2. Ensure that both
training and test set have representations from both classes proportional to original set.

(c) To generate features from documents use a BagofWords (BoW) model.

(d) Implement a class MyNB: To implement a Naive Bayes Model. The class should have
functions fit and predict.

(e) Implement a class MyLogR: To implement a Logistic Regression Model. The class
should have functions fit and predict.

(f) The code should print test accuracy from both the models.
