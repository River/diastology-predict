# A Novel Continuous Left Ventricular Diastolic Function Score Using Machine Learning
*River Jiang, Darwin F Yeung, Delaram Behnami, Christina Luong, Michael Y C Tsang, John Jue, Ken Gin, Parvathy Nair, Purang Abolmaesumi, Teresa S M Tsang*

PMID: [35753590](https://pubmed.ncbi.nlm.nih.gov/35753590/)  DOI: [10.1016/j.echo.2022.06.005](https://doi.org/10.1016/j.echo.2022.06.005)

## Abstract

**Background**: Unlike left ventricular (LV) ejection fraction, which provides a precise, reliable, and prognostically valuable measure of systolic function, there is no single analogous measure of LV diastolic function.

**Objectives**: We aimed to develop a continuous score to grade LV diastolic function using machine learning modeling of echocardiographic data.

**Methods**: Consecutive echo studies performed at a tertiary-care center between February 1, 2010, and March 31, 2016, were assessed, excluding studies containing features that would interfere with diastolic function assessment as well as studies in which 1 or more parameters within the contemporary diastolic function assessment algorithm were not reported. Diastolic function was graded based on 2016 American Society of Echocardiography (ASE)/European Association of Cardiovascular Imaging (EACVI) guidelines, excluding indeterminate studies. Machine learning models were trained (support vector machine [SVM], decision tree [DT], XGBoost [XGB], and dense neural network [DNN]) to classify studies within the training set by diastolic dysfunction severity, blinded to the ASE/EACVI classification. The DNN model was retrained to generate a regression model (R-DNN) to predict a continuous LV diastolic function score.

**Results**: A total of 28,986 studies were included; 23,188 studies were used to train the models, and 5,798 studies were used for validation. The models were able to reclassify studies with high agreement to the ASE/EACVI algorithm (SVM, 83%; DT, 100%; XGB, 100%; DNN, 98%). The continuous diastolic function score corresponded well with ASE/EACVI guidelines, with scores of 1.00 ± 0.01 for studies with normal function and 0.74 ± 0.05, 0.51 ± 0.06, and 0.27 ± 0.11 for mild, moderate, and severe diastolic dysfunction, respectively (mean ± 1 SD). A score of <0.91 predicted abnormal diastolic function (area under the receiver operator curve = 0.99), while a score of <0.65 predicted elevated filling pressure (area under the receiver operator curve = 0.99).

**Conclusions**: Machine learning can assimilate echocardiographic data and generate an automated continuous diastolic function score that corresponds well with current diastolic function grading recommendations.

**Keywords**: Artificial intelligence; Diastolic function; Echocardiography; Machine learning.

## Usage

1. Install pip requirements

```sh
python -m pip install -r requirements.txt
```

2. Make an input file (CSV format)

An example row is shown below. This file can contain as many rows as you want. Save this as `example.csv`. 

```csv
lvef,LA_vol,tr_vel,E,Lat_E,Septal_E,EAratio,avgEeratio,myocardial_dz
65.0,32.1428571428571,1.8027756377319943,63.0,5.1,3.7,0.68,14.32,False
```

3. Make predictions through models

```sh
python predict.py --file example.csv
```

This will output the results into `output/YYYY-mm-dd-HHMMSS.csv` for your further analysis.