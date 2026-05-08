import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from submission_script import *
from dataset_script import dataset

from sklearn.ensemble import RandomForestClassifier
import numpy as np

if __name__ == '__main__':

    col_index = int(input().strip())
    n_trees = int(input().strip())
    criterion = input().strip()
    new_input = list(map(float, input().strip().split()))

    data = np.array(dataset)

    data = np.delete(data, col_index, axis=1)

    X = data[:, :-1]
    y = data[:, -1].ravel()

    new_input = np.array(new_input)
    new_input = np.delete(new_input, col_index).reshape(1, -1)

    n = len(X)
    train_size = int(0.85 * n)

    train_X = X[:train_size]
    test_X = X[train_size:]

    train_Y = y[:train_size]
    test_Y = y[train_size:]

    clf = RandomForestClassifier(
        n_estimators=n_trees,
        criterion=criterion,
        random_state=0
    )

    clf.fit(train_X, train_Y)

    accuracy = clf.score(test_X, test_Y)

    pred = clf.predict(new_input)[0]
    probs = clf.predict_proba(new_input)[0]
    print(f"Accuracy: {accuracy}")
    print(pred)
    print(probs)

    submit_train_data(train_X, train_Y.tolist())
    submit_test_data(test_X, test_Y.tolist())
    submit_classifier(clf)