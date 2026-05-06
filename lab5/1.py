import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from submission_script import *
from dataset_script import dataset

from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

if __name__ == '__main__':
    p = int(input())
    record = input().split()

    split_index = int(len(dataset) * p / 100)

    train = dataset[:split_index]
    test = dataset[split_index:]

    train_X = [row[:-1] for row in train]
    train_Y = [row[-1] for row in train]

    test_X = [row[:-1] for row in test]
    test_Y = [row[-1] for row in test]

    encoder = OrdinalEncoder()
    train_X_enc = encoder.fit_transform(train_X)
    test_X_enc = encoder.transform(test_X)
    record_enc = encoder.transform([record])

    classifier = CategoricalNB()
    classifier.fit(train_X_enc, train_Y)

    accuracy = classifier.score(test_X_enc, test_Y)
    pred = classifier.predict(record_enc)
    prob = classifier.predict_proba(record_enc)

    print(accuracy)
    print(pred[0])
    print(prob)

    submit_train_data(train_X_enc, train_Y)
    submit_test_data(test_X_enc, test_Y)
    submit_classifier(classifier)
    submit_encoder(encoder)