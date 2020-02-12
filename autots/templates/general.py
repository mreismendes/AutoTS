import pandas as pd

general_template_dict = {
 0: {'Model': 'UnobservedComponents',
  'ModelParameters': '{"level": true, "trend": true, "cycle": true, "damped_cycle": true, "irregular": true, "stochastic_trend": true, "stochastic_level": true, "stochastic_cycle": false, "regression_type": null}',
  'TransformationParameters': '{"outlier": "clip3std", "fillNA": "rolling mean", "transformation": "PowerTransformer", "context_slicer": null}',
  'Ensemble': 0},
 1: {'Model': 'UnobservedComponents',
  'ModelParameters': '{"level": true, "trend": false, "cycle": false, "damped_cycle": false, "irregular": false, "stochastic_trend": true, "stochastic_level": true, "stochastic_cycle": false, "regression_type": null}',
  'TransformationParameters': '{"outlier": "clip2std", "fillNA": "rolling mean", "transformation": "RollingMean10", "context_slicer": "6ForecastLength"}',
  'Ensemble': 0},
 2: {'Model': 'ETS',
  'ModelParameters': '{"damped": false, "trend": "additive", "seasonal": null, "seasonal_periods": null}',
  'TransformationParameters': '{"outlier": "remove3std", "fillNA": "median", "transformation": "RollingMean10", "context_slicer": "HalfMax"}',
  'Ensemble': 0},
 3: {'Model': 'VECM',
  'ModelParameters': '{"deterministic": "ci", "k_ar_diff": 1, "regression_type": null}',
  'TransformationParameters': '{"outlier": "remove3std", "fillNA": "ffill", "transformation": "RollingMean100thN", "context_slicer": "HalfMax"}',
  'Ensemble': 0},
 4: {'Model': 'VECM',
  'ModelParameters': '{"deterministic": "colo", "k_ar_diff": 1, "regression_type": null}',
  'TransformationParameters': '{"outlier": null, "fillNA": "fake date", "transformation": "PowerTransformer", "context_slicer": "6ForecastLength"}',
  'Ensemble': 0},
 5: {'Model': 'VARMAX',
  'ModelParameters': '{"order": [2, 0], "trend": [1, 1, 0, 1]}',
  'TransformationParameters': '{"outlier": null, "fillNA": "fake date", "transformation": "PowerTransformer", "context_slicer": null}',
  'Ensemble': 0},
 6: {'Model': 'FBProphet',
  'ModelParameters': '{"holiday": false, "regression_type": null}',
  'TransformationParameters': '{"outlier": null, "fillNA": "fake date", "transformation": null, "context_slicer": null}',
  'Ensemble': 0},
 7: {'Model': 'MedValueNaive',
  'ModelParameters': '{}',
  'TransformationParameters': '{"outlier": null, "fillNA": "fake date", "transformation": null, "context_slicer": null}',
  'Ensemble': 0},
 8: {'Model': 'LastValueNaive',
  'ModelParameters': '{}',
  'TransformationParameters': '{"outlier": null, "fillNA": "fake date", "transformation": null, "context_slicer": null}',
  'Ensemble': 0},
 9: {'Model': 'RollingRegression',
  'ModelParameters': '{"regression_model": "DecisionTree", "holiday": false, "mean_rolling_periods": 7, "std_rolling_periods": 7, "max_rolling_periods": 7, "min_rolling_periods": 7, "ewm_alpha": 0.5, "additional_lag_periods": 7, "polynomial_degree": null, "regression_type": "None"}',
  'TransformationParameters': '{"outlier": "clip2std", "fillNA": "ffill", "transformation": null, "context_slicer": null}',
  'Ensemble': 0},
 10: {'Model': 'RollingRegression',
  'ModelParameters': '{"regression_model": "Adaboost", "holiday": false, "mean_rolling_periods": 10, "std_rolling_periods": 30, "max_rolling_periods": 7, "min_rolling_periods": 7, "ewm_alpha": 0.5, "additional_lag_periods": 7, "polynomial_degree": null, "regression_type": "None"}',
  'TransformationParameters': '{"outlier": null, "fillNA": "ffill", "transformation": "MinMaxScaler", "context_slicer": "6ForecastLength"}',
  'Ensemble': 0},
 11: {'Model': 'RollingRegression',
  'ModelParameters': '{"regression_model": "DecisionTree", "holiday": false, "mean_rolling_periods": 30, "std_rolling_periods": null, "max_rolling_periods": 7, "min_rolling_periods": 7, "ewm_alpha": 0.5, "additional_lag_periods": 7, "polynomial_degree": null, "regression_type": "None"}',
  'TransformationParameters': '{"outlier": null, "fillNA": "ffill", "transformation": "MinMaxScaler", "context_slicer": "10ForecastLength"}',
  'Ensemble': 0}
 }

general_template = pd.DataFrame.from_dict(general_template_dict, orient = 'index')