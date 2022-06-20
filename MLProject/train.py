import mlflow
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from argparse import ArgumentParser


def parse_args() -> tuple[str, float]:
    parser = ArgumentParser()
    parser.add_argument("--kernel", dest="kernel", type=str, default='rbf')
    parser.add_argument("--param_c", dest="param_c", type=float, default=1)
    args = parser.parse_args()

    return args.kernel, args.param_c


if __name__ == '__main__':
    X, y = datasets.load_iris(return_X_y=True, as_frame=True)
    # Используем только часть фичей
    X = X.iloc[:, :2]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    kernel, param_c = parse_args()
    with mlflow.start_run():
        clf = svm.SVC(kernel=kernel, C=param_c)
        clf.fit(X_train, y_train)
        mlflow.sklearn.eval_and_log_metrics(clf, X_train, y_train, prefix="training_")
        mlflow.sklearn.eval_and_log_metrics(clf, X_test, y_test, prefix="val_")
        mlflow.sklearn.log_model(clf, 'model')
