from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import classification_report 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

random_state = 42

df = pd.read_csv("train.csv")
test = pd.read_csv('test.csv')
test_df = pd.read_csv('test.csv')

df = df.drop(['PassengerId', 'Embarked', 'Ticket'], axis=1)
test_df = test_df.drop(['PassengerId', 'Embarked', 'Ticket'], axis=1)

df['travelling_status'] = df['SibSp'] + df['Parch']
df['travelling_status'] = np.where(df['travelling_status'] == 0, 'alone', 'not alone')

test_df['travelling_status'] = test_df['SibSp'] + test_df['Parch']
test_df['travelling_status'] = np.where(test_df['travelling_status'] == 0, 'alone', 'not alone')

df['Cabin'].fillna('U', inplace = True)
df['Cabin'] = df['Cabin'].map(lambda c: c[0])

test_df['Cabin'].fillna('U', inplace = True)
test_df['Cabin'] = test_df['Cabin'].map(lambda c: c[0])

titles = set()
for name in test_df['Name']:
    titles.add(name.split(',')[1].split('.')[0].strip())
for name in df['Name']:
    titles.add(name.split(',')[1].split('.')[0].strip())

Title_dict = {'Capt':'Officer',
 'Col':'Officer',
 'Don': 'Royalty',
 'Dr':'Officer',
 'Jonkheer':'Royalty',
 'Lady':'Royalty',
 'Major': 'Officer',
 'Master':'Master',
 'Miss':'Miss',
 'Mlle':'Miss',
 'Mme':'Mrs',
 'Mr':'Mr',
 'Mrs':'Mrs',
 'Ms':'Miss',
 'Rev':'Officer',
 'Sir':'Royalty',
 'the Countess':'Royalty'}

def get_titles():
    df['Title'] = df['Name'].map(lambda name: name.split(',')[1].split('.')[0].strip())
    df['Title'] = df.Title.map(Title_dict)
    del df['Name']
    return df

def get_titles_test():
    test_df['Title'] = test_df['Name'].map(lambda name: name.split(',')[1].split('.')[0].strip())
    test_df['Title'] = test_df.Title.map(Title_dict)
    del test_df['Name']
    return test_df

test_df = get_titles_test()

df = get_titles()

X = df.iloc[:,1:]
# X_pred  = test_df.drop("PassengerId", axis=1).copy()
y = df['Survived']

# fill up the na values in age column with the mean of the column,
# bin them into categories.

age_fare_transformer = make_pipeline(
    SimpleImputer(strategy="mean", missing_values=np.nan),
    MinMaxScaler(),
    KBinsDiscretizer(n_bins=9,encode='onehot-dense',strategy='quantile')
    )


categorical_features = ["Sex", "Pclass", "travelling_status", "Cabin", "Title"]

categorical_transformer = OneHotEncoder(handle_unknown="ignore")


preprocessor = ColumnTransformer(
    transformers=[
        ("age_fare_clean", age_fare_transformer, ['Age', 'Fare']),
        ("cat", categorical_transformer, categorical_features),
    ],
    remainder='passthrough')

pipeline = make_pipeline(preprocessor, LogisticRegression(max_iter=300))
pipeline_random_forest = make_pipeline(preprocessor, RandomForestClassifier(n_estimators=70, max_depth=2))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state= random_state)

pipeline.fit(X_train, y_train)
pipeline_random_forest.fit(X_train, y_train)

print("model score: %.3f" % pipeline.score(X_test, y_test))
print("random forest model score: %.3f" % pipeline_random_forest.score(X_test, y_test))

y_pred = pipeline.predict(X_test)
predictions = pipeline.predict(test_df)

# get predictions from the pipeline
print(y_pred)
print(predictions)

# get prediction probabilities from the pipeline 
print(pipeline.predict_proba(X_test)[:, 1])

output = pd.DataFrame({'PassengerID' : test.PassengerId, 'Survived' : predictions})
output['Survived'] = output['Survived'].astype(int)
output.to_csv('final.csv', index=False)

# kaggle 0.77272
