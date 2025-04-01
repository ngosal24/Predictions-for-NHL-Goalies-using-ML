# Predictions For NHL Goalies using Machine Learning


Our code is listed in the order of execution as follows:

(1) formingdb.py (forms and outputs our database to a csv file)

      - required libaries: pandas
      - command to run: python3 formingdb.py
      - input files: (12_13.csv, 13_14.csv, 14_15.csv, 15_16.csv, 17_18.csv, 18_19.csv, 19_20.csv, 20_21.csv, 21_22.csv, 22_23.csv)
      - files produced: 'data.csv' - our concatenated database containing the full ten years of goalie statistics
     
(2) mlmodel.py (creates, trains and validates our machine learning model, then looks at feature importance)

      - required libraries: pandas, sklearn
      - command to run: python3 mlmodel.py
      - input files: 'data.csv' (from last file)
      - files produced: none

(3) linreg.py (investigates correlation between particular statistics and next_sv_pct using linear regression, then plots)

      - required libraries: pandas, numpy, matplotlib, sklearn
      - command to run: python3 linreg.py
      - input files: 'data.csv'
      - files produced: none (none in code, as plt.show() is used, but extracted plot figures for report from this code)

(4) corrtest.py (further investigates correlation using pearsonr test from scipy)

      - required libraries: pandas, scipy
      - command to run: python3 corrtest.py
      - input files: 'data.csv'
      - files produced: none

