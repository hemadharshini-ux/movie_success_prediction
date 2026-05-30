import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# dataset
data = {
    'budget': [50, 60, 70, 80, 90, 100],
    'screens': [1000, 1500, 2000, 2500, 3000, 3500],
    'rating': [6, 7, 8, 9, 7, 8],
    'success': [0, 0, 1, 1, 0, 1]  # 0 = Flop, 1 = Hit
}

df = pd.DataFrame(data)

X = df[['budget', 'screens', 'rating']]
y = df['success']

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("Model saved!")