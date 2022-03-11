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

df = df.drop(['Cabin', 'Embarked', 'Name', 'Ticket'], axis=1)
test_df = test_df.drop(['Cabin', 'Embarked', 'Name', 'Ticket'], axis=1)

df['travelling_status'] = df['SibSp'] + df['Parch']
df['travelling_status'] = np.where(df['travelling_status'] == 0, 'alone', 'not alone')

test_df['travelling_status'] = test_df['SibSp'] + test_df['Parch']
test_df['travelling_status'] = np.where(test_df['travelling_status'] == 0, 'alone', 'not alone')


X = df[['PassengerId', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch',
       'Fare', 'travelling_status']]
y = df['Survived']

age_fare_transformer = make_pipeline(
    SimpleImputer(strategy="mean", missing_values=np.nan),
    MinMaxScaler(),
    KBinsDiscretizer(n_bins=9,encode='onehot-dense',strategy='quantile')
    )

categorical_features = ["Sex", "Pclass", "travelling_status"]

categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("age_fare_clean", age_fare_transformer, ['Age','Fare']),
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

print(y_pred)
print(predictions)

print(pipeline.predict_proba(X_test)[:, 1])

output = pd.DataFrame({'PassengerID' : test.PassengerId, 'Survived' : predictions})
output['Survived'] = output['Survived'].astype(int)
output.to_csv('final_alt_2.csv', index=False)

# kaggle score 0.78468