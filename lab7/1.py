import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from submission_script import *
from dataset_script import dataset

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
import numpy as np

if __name__ == '__main__':
    X_percent = int(input().strip())
    criterion = input().strip()

    data = np.array(dataset)

    X = data[:, :-1]
    Y = data[:, -1]

    X_encoder = OrdinalEncoder()
    X_encoded = X_encoder.fit_transform(X)

    Y_encoder = OrdinalEncoder()
    Y_encoded = Y_encoder.fit_transform(Y.reshape(-1, 1))

    n = len(X_encoded)
    train_size = int(n * X_percent / 100)

    X_train = X_encoded[-train_size:]
    X_test = X_encoded[:-train_size]

    y_train = Y_encoded[-train_size:]
    y_test = Y_encoded[:-train_size]

    clf = DecisionTreeClassifier(
        criterion=criterion,
        random_state=0
    )

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    acc = np.mean(y_pred == y_test)
    depth = clf.get_depth()
    leaves = clf.get_n_leaves()

    importances = clf.feature_importances_
    most = int(np.argmax(importances))
    least = int(np.argmin(importances))

    print(f"Depth: {depth}")
    print(f"Number of leaves: {leaves}")
    print(f"Accuracy: {acc}")
    print(f"Most important feature: {most}")
    print(f"Least important feature: {least}")

    submit_train_data(X_train, y_train)
    submit_test_data(X_test, y_test)
    submit_classifier(clf)
    submit_encoder(X_encoder)