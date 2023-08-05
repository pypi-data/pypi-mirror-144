import pandas as pd
import pandas_datareader as pdr
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from scalecast.Forecaster import Forecaster

models = ('knn','svr','lightgbm','mlp','elasticnet')
level_models = ('arima','hwes','prophet','silverkite')
df = pdr.get_data_fred('HOUSTNSA',start='1900-01-01',end='2021-06-01')
f = Forecaster(y=df['HOUSTNSA'],current_dates=df.index) # to initialize, specify y and current_dates (must be arrays of the same length)

f.set_test_length(12) # specify a test length for your models--it's a good idea to keep this the same for all forecasts
f.generate_future_dates(24) # this will create future dates that are on the same interval as the current dates and it will also set the forecast length
f.add_ar_terms(4) # add AR terms before differencing
f.add_AR_terms((2,12)) # seasonal AR terms
f.diff() # differences the y term and all ar terms to make a series stationary (also supports 2-level integration)
f.add_seasonal_regressors('month',raw=False,sincos=True) # uses pandas attributes: raw=True creates integers (default), sincos=True creates wave functions (not default), dummy=True creates dummy vars (not default)
f.add_seasonal_regressors('year')
f.add_covid19_regressor() # dates are flexible, default is from when disney world closed to when US CDC lifted mask recommendations
f.add_time_trend()
f.add_combo_regressors('t','COVID19') # multiplies regressors together
f.set_validation_length(6) # length, different than test_length, to tune the hyperparameters 

# automatically tune and forecast with a series of models
f.tune_test_forecast(models,feature_importance=True,summary_stats=True) # by default, tuning is not dynamic but testing is

# combine models and run manually specified models of other varieties
f.set_estimator('combo')
f.manual_forecast(how='simple',models=models,determine_best_by='ValidationMetricValue',call_me='avg_diff') # simple average of top_3 models based on performance in validation
f.manual_forecast(how='weighted',models=models,determine_best_by='ValidationMetricValue',call_me='weighted_diff') # weighted average of all models based on metric specified in determine_best_by (default is the validation metric)

# undifference results to bring back orginal series
f.undiff()
f.tune_test_forecast(level_models,feature_importance=True,summary_stats=True) # by default, tuning is not dynamic but testing is

# combine models and run manually specified models of other varieties
f.set_estimator('combo')
f.manual_forecast(how='simple',models=level_models,determine_best_by='ValidationMetricValue',call_me='avg_level') # simple average of top_3 models based on performance in validation
f.manual_forecast(how='weighted',models=level_models,determine_best_by='ValidationMetricValue',call_me='weighted_level')

# plot results
matplotlib.use('QT5Agg')
f.plot(models='all',order_by='LevelTestSetMAPE',print_attr=['LevelTestSetRMSE','LevelTestSetR2','LevelTestSetMAPE','HyperParams','Xvars','models']) # will automatically plot levels for everything
plt.show()
f.plot_test_set(models='all',order_by='LevelTestSetMAPE',include_train=60) # will automatically plot levels for everything
plt.show()
f.plot_fitted(models=models,order_by='LevelTestSetMAPE') # cannot plot fitted values of all models when levels were different during forecasting
plt.show()
f.plot_fitted(models=level_models,order_by='LevelTestSetMAPE')
plt.show()

# export key results
f.export(['model_summaries','lvl_fcsts'],to_excel=True,determine_best_by='LevelTestSetMAPE',excel_name='housing_different_levels_results.xlsx') # export interesting model metrics and forecasts (both level and non-level)
f.all_feature_info_to_excel(excel_name='housing_different_levels_feature_info.xlsx')