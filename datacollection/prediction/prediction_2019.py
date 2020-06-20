import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, log_loss
import sqlite3
import os

train_df_1 = pd.read_csv('input/balanced-2014-2017.csv')
train_df_2 = pd.read_csv('input/balanced-2018.csv')

train_df = pd.concat([train_df_1, train_df_2])

predict_df = pd.read_csv('input/balanced-2019.csv')

train_df = train_df.dropna(subset=['player1_elo_rating','player2_elo_rating'])

train_df = train_df.drop(['match_id','date','player1_id','player2_id','player1_rank','player2_rank','player1_rank_points','player2_rank_points'], axis=1)

train_df['elo_rating_diff'] = train_df['player1_elo_rating'] - train_df['player2_elo_rating']

train_df = train_df.drop(['player1_elo_rating','player2_elo_rating'], axis=1)

predict_df = predict_df.dropna(subset=['player1_elo_rating','player2_elo_rating'])

predict_df = predict_df.drop(['match_id','date','player1_id','player2_id','player1_rank','player2_rank','player1_rank_points','player2_rank_points'], axis=1)

predict_df['elo_rating_diff'] = predict_df['player1_elo_rating'] - predict_df['player2_elo_rating']

predict_df = predict_df.drop(['player1_elo_rating','player2_elo_rating'], axis=1)

print(train_df.columns.values)

X_train = train_df.drop("won", axis=1)
Y_train = train_df["won"]
X_predict = predict_df.drop('won', axis=1).copy()
Y_predict = predict_df['won']

# Logistic Regression

logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
Y_pred = logreg.predict(X_predict)

Y_pred_proba = logreg.predict_proba(X_predict)

print(classification_report(Y_predict, Y_pred))
print(log_loss(Y_predict, Y_pred_proba))

predict_df_info = pd.read_csv('input/balanced-2019.csv')
predict_df_info = predict_df_info.dropna(subset=['player1_elo_rating','player2_elo_rating'])

prediction_player1_proba = []
prediction_player2_proba = []

for predictions in Y_pred_proba:
    prediction_player1_proba.append(predictions[1])
    prediction_player2_proba.append(predictions[0])

prediction_df = pd.DataFrame({
            'match_id': predict_df_info['match_id'],
            'player1_id': predict_df_info['player1_id'],
            'player2_id': predict_df_info['player2_id'],
            'player1_proba': prediction_player1_proba,
            'player2_proba': prediction_player2_proba
        })
    
recordsList = []
    
for index, row in prediction_df.iterrows():
    recordsList.append((row['player1_proba'], row['player2_proba'], row['match_id'], row['player1_id'], row['player2_id']))

BASE_DIR = os.path.abspath('../../')
db_file = os.path.join(BASE_DIR, 'db.sqlite3')
db_file

try:
    sqliteConnection = sqlite3.connect(db_file)
    cursor = sqliteConnection.cursor()
    print("Successfully connected to database")
    
    # create query
    query = """INSERT INTO api_prediction 
        (player1_proba, 
        player2_proba, 
        match_id, 
        player1_id, 
        player2_id) 
        VALUES(?, ?, ?, ?, ?)"""
    # insert in database
    cursor.executemany(query, recordsList)
    sqliteConnection.commit()
    print("Total", cursor.rowcount, "records inserted successfully in database")
except sqlite3.Error as error:
    print(error)
finally:
    if(sqliteConnection):
        sqliteConnection.close()
        print("database connection closed")

