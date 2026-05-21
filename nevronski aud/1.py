from fontTools.misc.classifyTools import Classifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
def read_dataset():
    data =[]
    with open('winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == "":
                break
            parts = line.split(';')

            data.append(list(map(float,parts[:-1])) + parts[-1:])
    return data

if __name__ == '__main__':
    data = read_dataset()
    data_good = [row for row in data if row[-1] == 'good']
    data_bad = [row for row in data if row[-1] == 'bad']

    train = data_good[:int(0.7*len(data_good))] + data_bad[:int(0.7*len(data_bad))]
    val = data_bad[int(0.7*len(data_bad))+1:int(0.8*len(data_bad))] +  data_good[int(0.7*len(data_good))+1:int(0.8*len(data_good))]
    test = data_bad[int(0.8*len(data_bad))+1:]+data_good[int(0.8*len(data_bad))+1:]

    train_X = [row[:-1] for row in train]
    train_y = [row[-1] for row in train]

    val_X = [row[:-1] for row in val]
    val_y = [row[-1] for row in val]

    test_X = [row[:-1] for row in test]
    test_y = [row[-1] for row in test]

    clf1 = MLPClassifier(5,
                          activation='relu',
                          learning_rate_init=0.001,
                          max_iter=500,
                          random_state=0)
    clf2 = MLPClassifier(10,
                         activation='relu',
                         learning_rate_init=0.001,
                         max_iter=500,
                         random_state=0)
    clf3 = MLPClassifier(100,
                         activation='relu',
                         learning_rate_init=0.001,
                         max_iter=500,
                         random_state=0)
    clf1.fit(train_X, train_y)
    clf2.fit(train_X, train_y)
    clf3.fit(train_X, train_y)

    pred1 =clf1.predict(val_X)
    pred2 = clf2.predict(val_X)
    pred3 = clf3.predict(val_X)

    acc1 = accuracy_score(val_y, pred1)
    acc2 = accuracy_score(val_y, pred2)
    acc3 = accuracy_score(val_y, pred3)

    if acc1 > acc2 and acc1 > acc3:
        pred = clf1.predict(test_X)
        acc = accuracy_score(test_y, pred)
        clf = clf1
    elif acc2 > acc1 and acc2 > acc3:
        pred = clf2.predict(test_X)
        acc = accuracy_score(test_y, pred)
        clf = clf2
    else:
        pred = clf3.predict(test_X)
        acc = accuracy_score(test_y, pred)
        clf = clf3

    standard = StandardScaler()
    minmax = MinMaxScaler(feature_range=(-1,1))
    standard.fit(train_X)
    minmax.fit(train_X)
    clf.fit(standard.transform(train_X), standard.transform(train_y))
    
    print('Accuracy: ', acc)
    print('precision: ', pred)

