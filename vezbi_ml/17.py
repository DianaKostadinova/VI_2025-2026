import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler

from dataset_script import dataset


if __name__ == '__main__':
    C = int(input())
    P = int(input())
    new_dataset = []
    for row in dataset:
        new_feature = row[0] + row[-2]
        new_row = [new_feature] + list(row[1:10]) + [row[-1]]
        new_dataset.append(new_row)


    X_good = [row[:-1] for row in new_dataset if row[-1] == 'good' ]
    y_good = [row[-1] for row in new_dataset if row[-1] == 'good' ]

    X_bad = [row[:-1] for row in new_dataset if row[-1] == 'bad' ]
    y_bad = [row[-1] for row in new_dataset if row[-1] == 'bad' ]

    if C == 0:
        X_train = X_good[:int(P/100 * len(X_good))] + X_bad[:int(P/100 * len(X_bad))]
        y_train = y_good[:int(P/100 * len(y_good))]+y_bad[:int(P/100 * len(y_bad))]

        X_test = X_good[int(P/100 * len(X_good)):]+X_bad[int(P/100 * len(X_bad)):]
        y_test = y_good[int(P/100 * len(y_good)):]+y_bad[int(P/100 * len(y_bad)):]
    else:
        X_train = X_good[len(X_good) - int(P / 100 * len(X_good)):] + X_bad[len(X_bad) - int(P / 100 * len(X_bad)):]
        y_train = y_good[len(y_good) - int(P / 100 * len(y_good)):] + y_bad[len(y_bad) - int(P / 100 * len(y_bad)):]

        X_test = X_good[:len(X_good) - int(P / 100 * len(X_good))] + X_bad[:len(X_bad) - int(P / 100 * len(X_bad))]
        y_test = y_good[:len(y_good) - int(P / 100 * len(y_good))] + y_bad[:len(y_bad) - int(P / 100 * len(y_bad))]

    clf = GaussianNB()
    clf.fit(X_train, y_train)
    pred1 = clf.predict(X_test)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    clf2 = GaussianNB()
    clf2.fit(X_train, y_train)
    pred2 = clf2.predict(X_test)

    acc1 = accuracy_score(y_test, pred1)
    acc2 = accuracy_score(y_test, pred2)
    print(f"Tochnost so zbir na koloni: {acc1}")
    print(f"Tochnost so zbir na koloni i skaliranje: {acc2}")