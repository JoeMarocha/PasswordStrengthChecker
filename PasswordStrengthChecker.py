import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 

#reading the dataset
data = pd.read_csv(r'C:\Users\joema\Desktop\NewPasswordchecker\training.csv')

#this prints out the first 5 rows of the datset for inspection
print(data.head())

#feature extraction
data['length'] = data['password'].str.contains(r'[0-7]').astype(float)
data['uppercase'] = data['password'].str.contains(r'[A-Z]').astype(float)
data['lowercase'] = data['password'].str.contains(r'[a-z]').astype(float)
data['digit'] = data['password'].str.contains(r'\d').astype(float)
data['specialcharacter'] = data['password'].str.contains(r'[^a-zA-Z0-9]').astype(float)

   


# Printing the DataFrame to see a few of the extracted features
print(data.tail())

#defining X and Y for use in training and testing 
feature_columns = ['length', 'uppercase', 'lowercase', 'digit', 'specialcharacter']
X = data[feature_columns]
y = data['strength']

#split data for training and testing 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

#model evaluation
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Function to extract features from a given password
def extract_features(password):
    features = {
        'length': len(password),
        'uppercase': any(char.isupper() for char in password),
        'lowercase': any(char.islower() for char in password),
        'digit': any(char.isdigit() for char in password),
        'specialcharacter': any(not char.isalnum() for char in password)
    }
    return pd.DataFrame([features])

# Prompt user for a password and predict its strength
user_password = input("Enter your password: ")
user_features = extract_features(user_password)

# Ensure the order of columns matches the training data
user_features = user_features[feature_columns].astype(float)


# Predict the strength of the user's password
user_strength_prediction = model.predict(user_features)

print("The strength of the entered password is:", user_strength_prediction)



