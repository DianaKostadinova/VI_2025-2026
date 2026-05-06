import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from submission_script import *
from dataset_script import dataset

from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    record = list(map(float, input().split()))

    class_0 = [row for row in dataset if row[-1] == '0']
    class_1 = [row for row in dataset if row[-1] == '1']

    split_0 = int(len(class_0) * 0.85)
    split_1 = int(len(class_1) * 0.85)

    train = class_0[:split_0] + class_1[:split_1]
    test = class_0[split_0:] + class_1[split_1:]

    train_X = [[float(x) for x in row[:-1]] for row in train]
    train_Y = [int(row[-1]) for row in train]

    test_X = [[float(x) for x in row[:-1]] for row in test]
    test_Y = [int(row[-1]) for row in test]

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    accuracy = classifier.score(test_X, test_Y)
    pred = classifier.predict([record])
    prob = classifier.predict_proba([record])

    print(accuracy)
    print(pred[0])
    print(prob)

    submit_train_data(train_X, train_Y)
    submit_test_data(test_X, test_Y)
    submit_classifier(classifier)