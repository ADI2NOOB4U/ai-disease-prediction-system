import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split

dataset = {
    "Symptoms": [
        ["fever", "cough", "tiredness"],
        ["headache", "nausea", "dizziness"],
        ["chest pain", "shortness of breath"],
        ["stomach pain", "vomiting", "diarrhea"],
        ["joint pain", "swelling", "stiffness"]
    ],
    "Disease": [
        "Flu",
        "Migraine",
        "Heart Issue",
        "Food Poisoning",
        "Arthritis"
    ]
}

df = pd.DataFrame(dataset)

binarizer = MultiLabelBinarizer()
X = binarizer.fit_transform(df["Symptoms"])
y = df["Disease"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

def predict(symptoms):
    encoded = binarizer.transform([symptoms])
    return model.predict(encoded)[0]

all_symptoms = sorted(list(binarizer.classes_))

print("\nAvailable Symptoms:")
for s in all_symptoms:
    print("-", s)

user_input = input("\nEnter symptoms (comma separated): ").lower().strip()
user_symptoms = [s.strip() for s in user_input.split(",")]

result = predict(user_symptoms)

print("Predicted Disease:", result)
