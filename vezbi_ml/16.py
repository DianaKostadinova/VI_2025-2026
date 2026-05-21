import os

from sklearn.metrics import accuracy_score

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from msilib import type_binary

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier


from dataset_script import dataset


if __name__ == '__main__':
    P = int(input())
    C = input()
    L = int(input())

    X = [row[:-1] for row in dataset]
    y = [row[-1] for row in dataset]

    X_train = X[:int(P/100*len(X))]
    y_train= y[:int(P / 100 * len(X))]

    X_test = X[int(P / 100 * len(X)):]
    y_test = y[int(P / 100 * len(X)):]

    clf1 = DecisionTreeClassifier(
        criterion=C,
        max_leaf_nodes=L,
        random_state=42,
    )
    clf1.fit(X_train, y_train)
    acc1 = accuracy_score(y_test, clf1.predict(X_test))
    trees = {}
    fish_types = ["Perch","Roach","Bream"]
    for f in fish_types:
        clf = DecisionTreeClassifier(
            criterion=C,
            max_leaf_nodes=L,
            random_state=42,

        )
        y_binary = [1 if label == f else 0 for label in y_train]
        clf.fit(X_train, y_binary)
        trees[f] = clf

    correct = 0
    for i, x in enumerate(X_test):
        true_class = y_test[i]
        all_agree = all(
            trees[fish_class].predict([x])[0] == (1 if fish_class == true_class else 0)
            for fish_class in fish_types
        )
        if all_agree:
            correct += 1

    acc2 = correct / len(y_test)

    print(f"Tochnost so originalniot klasifikator: {acc1}")
    print(f"Tochnost so kolekcija od klasifikatori: {acc2}")