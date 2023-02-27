import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from datetime import datetime
from pathlib import Path
import argparse


MODEL_NN = "models/2022.01.06_03_nn.joblib"
MODEL_NN_CV = "models/2022.01.06_05cv_nn.joblib"
MODEL_SVC = "models/2021.12.16_svc_clf.joblib"
MODEL_TREE = "models/2021.12.16_tree_clf.joblib"

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

OUTPUT_DIR = "output"

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

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", help="path to input csv file", required=True)
    args = parser.parse_args()

    # load data
    df = pd.read_csv(args.source)
    df = df.reset_index(drop=True)

    # check all columns are present in input
    if not set(FEATURES).issubset(df.columns):
        raise ValueError(f"Input should contain following columns: {','.join(FEATURES)}")

    # preprocess data
    x = df[FEATURES]
    x_nn = preprocess_nn_data(x)

    # load models
    model_svc = joblib.load(MODEL_SVC)
    model_tree = joblib.load(MODEL_TREE)
    model_nn = joblib.load(MODEL_NN)
    model_nn_cv = joblib.load(MODEL_NN_CV)

    # make predictions and save to dataframe
    results_df = pd.DataFrame(
        model_nn.predict(x_nn), columns=["nn_norm", "nn_mild", "nn_mod", "nn_sev"]
    )
    results_df['nn_cv'] = model_nn_cv.predict(x_nn)
    results_df['svc'] = model_svc.predict(x)
    results_df['tree'] = model_tree.predict(x)

    # join results df with input df
    df = pd.concat([df, results_df], axis=1)

    # save as output
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    current_date = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    df.to_csv(f"output/{current_date}.csv", index=False)