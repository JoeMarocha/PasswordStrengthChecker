# PasswordStrengthChecker

Motivations - since my initial topic was AI assisted hacking I decided to do this project as it encompasses both AI and hacking to a certain extent. The project uses Machine learning which is a subset of AI and we know that the strength of a password correlates to the difficulty it takes for hackers to retreive this password through brute force attacks and so on. 

Code explanation 

1. loads the training data from the CSV file using Pandas.
2. It prints the first 5 rows of the dataset for inspection.
3. Features such as length, uppercase, lowercase, digit, and special characters are extracted from the passwords.
4. It prints the last 5 rows of the DataFrame to inspect the extracted features.
5. Features (length, uppercase, lowercase, digit, special characters) and labels (strength) are defined for use in training and testing.
6. The dataset is split into training and testing sets.
7. A Random Forest Classifier model is trained on the training set.
8. Model accuracy is evaluated on the testing set.
9. The script defines a function to extract features from a given password.
10. It prompts the user for a password, extracts its features, and predicts its strength, outputting the result.





