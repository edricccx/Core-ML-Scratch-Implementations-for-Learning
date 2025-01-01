import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            y_predicted = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


if __name__ == "__main__":
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([1.2, 1.9, 3.0, 4.2, 5.1])

    model = LinearRegression(learning_rate=0.01, epochs=1000)
    model.fit(X, y)

    predictions = model.predict(X)
    print("Predicted values:", predictions)
    print("True values:", y)
    print("Weights:", model.weights)
    print("Bias:", model.bias)