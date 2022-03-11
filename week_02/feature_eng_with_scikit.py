
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
import pandas as pd


"""
After having the recepie of your model defined from all the experimentation
that you have done, it is time to encapsulate that into a neat pipeline
and use columntransformers to apply your transformations to the data.

Pipelines are usually what is used as the last version of code to be deployed,
not the notebook version
"""



# load data
df = pd.read_csv('data/train.csv', index_col=0)
del df['Ticket']
del df['Cabin']

# split to X, and y
X = df.iloc[:,1:]
y = df['Survived']

# feature engineering for numericals
numeric_features = ["Age", "Fare"]

# create a sequential pipeline 
# output of one step will be input to the next 
numeric_transformer = make_pipeline(
    SimpleImputer(strategy="most_frequent"), 
    StandardScaler()
    )

# feature engineering for categorical
categorical_features = ["Embarked", "Sex", "Pclass"]

# handle unknown means it will ignore nan's if it finds them
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

age = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')

# you can also create custom functions
def name_length(df):
    length = df[df.columns[0]].str.len()
    return length.values.reshape(-1, 1)

# pre-process transformations
# notice here that we include a pipeline for the numeric transformations

# Columns of the original feature matrix that are not specified are dropped 
# from the resulting transformed feature matrix, unless specified in the 
# passthrough keyword

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
        ('name', FunctionTransformer(name_length), ['Name']),
        ('age', age, ['Age'])
    ],
    remainder='passthrough')

# create the model pipeline
pipeline = make_pipeline(preprocessor, LogisticRegression(max_iter=300))

# split data to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state= 42)


# fit the pipeline to training data
pipeline.fit(X_train, y_train)

# calculate the accuracy score from test data
print("model score: %.3f" % pipeline.score(X_test, y_test))

# get predictions from the pipeline
print(pipeline.predict(X_test))

# get prediction probabilities from the pipeline 
print(pipeline.predict_proba(X_test)[:, 1])


"""
There are few limitations of ColumnTransformer;

* ColumnTransformer outputs an array even if we input 
a DataFrame object which makes it difficult to track the columns.
That's why we use them after experimenting and playing around
with ideas ; when we have an exact recepie for the pipeline

* In a ColumnTransformer we cannot apply multiple 
transforms to a single column
"""
