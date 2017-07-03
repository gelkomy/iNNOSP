import warnings

from sklearn.ensemble.forest import RandomForestClassifier

warnings.filterwarnings('ignore')

import pickle
# data=pickle.load(open(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\pkl patient 14\file6_only.pkl','r'))
# data=pickle.load(open(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\pkl patient 14\file6_kalman.pkl','r'))

data=pickle.load(open(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\pkl patient 14\all_files_hp.pkl','r'))
#
# from PrepareYVector import getY
# from PrepareWindowsVector import getWindows
# from feature_basis_selection import feature_basis_selection
# from electrode_selection import electrode_selction
#
# text_file=r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient14\chb14-summary.txt'
# yTimeLine = getY(text_file,6 ,6 )
# y = getWindows(yTimeLine)
#
#
# from numpy import sort
# from xgboost import XGBClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.feature_selection import SelectFromModel
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
# from sklearn.svm import SVC
# import pandas as pd
#
# X= data['FP2-F4']
# Y=y
# # from imblearn.over_sampling import SMOTE
# # resampler=     SMOTE()
# # X, Y= resampler.fit_sample(X, Y)
# # X= pd.DataFrame(X)
# # Y=pd.DataFrame(Y)
#
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=700)
# # fit model on all training data
# model = XGBClassifier()
# model.fit(X_train, y_train)
# # make predictions for test data and evaluate
# y_pred = model.predict(X_test)
# predictions = [round(value) for value in y_pred]
# accuracy = accuracy_score(y_test, predictions)
# print "Accuracy: %.2f%%" % (accuracy * 100.0)
# # Fit model using each importance as a threshold
# thresholds = sort(model.feature_importances_)
# # print "thresholds are" , thresholds
# # print "features importance are ", model.feature_importances_
# l=[]
# for i in range(0,len( model.feature_importances_)):
#     l.append((i, model.feature_importances_[i] ))
#
# l= sorted(l, key=lambda x: x[1], reverse=True)
# # print l[0:9]
# # print "end"
#
#
#
#
#
# max_accuracy=0
# prev_n=10000000000
# for thresh in thresholds:
#     # select features using threshold
#     selection = SelectFromModel(model, threshold=thresh, prefit=True)
#     select_X_train = selection.transform(X_train)
#     # train model
#     selection_model = XGBClassifier()
#     selection_model.fit(select_X_train, y_train)
#     # eval model
#     select_X_test = selection.transform(X_test)
#     y_pred = selection_model.predict(select_X_test)
#     predictions = [round(value) for value in y_pred]
#     accuracy = accuracy_score(y_test, predictions)
#
#     if accuracy> max_accuracy and select_X_train.shape[1]<prev_n:
#         max_accuracy=accuracy
#         selected_cols=selection.get_support()
#         # print(selected_cols)
#         temp=X[X.columns[selected_cols]]
#         print temp.columns
#         # X[X.columns[selected_cols]].to_csv(r'E:\Faculty of Engineering\bioInformatics\Ensemble\Layer 2 Feature Selection\\clinical_data_selected.csv', index=False)
# #        X.to_csv(r'D:\Faculty of Engineering\bioInformatics\METABRIC data set\Data\Clinical_Data_selected.csv', index=False)
#
#     print "Thresh=%.3f, n=%d, Accuracy: %.2f%%" % (thresh, select_X_train.shape[1], accuracy*100.0)
#     prev_n=select_X_train.shape[1]
# #
