import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import OneHotEncoder

FEATURES = [
    "lvef",
    "LA_vol",
    "tr_vel",
    "E",
    "Lat_E",
    "Septal_E",
    "EAratio",
    "avgEeratio",
    "myocardial_dz",
]

MODEL_NN = "models/2022.01.06_03_nn.joblib"
MODEL_NN_CV = "models/2022.01.06_03_nn.joblib"
MODEL_SVC = "models/2021.12.16_svc_clf.joblib"
MODEL_TREE = "models/2021.12.16_tree_clf.joblib"


def preprocess_nn_data(X, y=None):
    numerical_features = [
        "lvef",
        "LA_vol",
        "tr_vel",
        "E",
        "Lat_E",
        "Septal_E",
        "EAratio",
        "avgEeratio",
    ]
    bool_features = ["myocardial_dz"]

    # convert X (which is a df) to numpy matrix
    # myocardial_dz is TRUE or FALSE, so convert this with OHE
    X_np = np.hstack(
        (
            X[numerical_features].to_numpy(),
            OneHotEncoder().fit_transform(X[bool_features]).todense(),
        )
    )

    if y is not None:
        # convert y (which is a df) to np array
        y_np = y["diastolic_fn_2016"].to_numpy()
        # convert to 2D array and transpose to shape (n, 1)
        y_np = y_np[np.newaxis].T
        # one hot encoding
        y_np = OneHotEncoder().fit_transform(y_np).todense()

        return X_np, y_np
    else:
        return X_np

if __name__ == "__main__":

    df = (
        pd.read_csv("2022.01.11_results_alldf_bothnn.csv", index_col=0)
        .head(5)
        .reset_index(drop=True)
    )


    model = joblib.load("../models/2022.01.06_03_nn.joblib")

    x = df[FEATURES]
    x = preprocess_nn_data(x)

    results_df = pd.DataFrame(
        model.predict(x), columns=["nn_norm", "nn_mild", "nn_mod", "nn_sev"]
    )

    pd.concat([df, results_df], axis=1)
