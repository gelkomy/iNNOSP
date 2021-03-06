'''
This function tries a list of classifiers on the training data. 
The function may perform imbalancing processing to enhance the accuracy.
% 
% /**************************************************************************** 
%  * Job:              binary classification                                  * 
%  * Input:           features dataframe and the output feature y             *
%  * Output:          The output is a dataframe that contains the accuracy of* 
*                     each classifier.                                        * 
%  * Generated on:    Sun, May 28, 2017                                       * 
%  * Generated by:    Gamal                                                   * 
%  * Version:         1                                                       * 
%  ****************************************************************************/ 
'''

'''
############################### required packages ###############################
pip install -U imbalanced-learn

install the xgboost as shown in the following link
https://www.ibm.com/developerworks/community/blogs/jfp/entry/Installing_XGBoost_For_Anaconda_on_Windows?lang=en
'''

import warnings
warnings.filterwarnings('ignore')


import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, ExtraTreesClassifier
#from xgboost import XGBClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
# from sklearn.gaussian_process import GaussianProcessClassifier
# from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
# from sklearn.naive_bayes import GaussianNB
#from sklearn.neural_network import MLPClassifier
# from sklearn.gaussian_process.kernels import RBF
# from imblearn.ensemble import BalanceCascade, EasyEnsemble
from sklearn.tree import DecisionTreeClassifier
# from scipy.stats import skew
from imblearn.over_sampling import SMOTE, ADASYN, RandomOverSampler
# from imblearn.under_sampling import  RandomUnderSampler,  NeighbourhoodCleaningRule,  CondensedNearestNeighbour,  OneSidedSelection, ClusterCentroids
# from imblearn.combine import SMOTETomek, SMOTEENN


def binary_classification(X,y):
    # performing oversampling on the data
    resampler=     SMOTE()
    X, y= resampler.fit_sample(X, y)
    X= pd.DataFrame(X)
    y=pd.DataFrame(y)
    
    x_train, x_test, y_train, y_test= train_test_split(X, y , test_size=.3, random_state=2000)
    
    
    
    #making list of classifiers
    list_of_classifier=[
            GradientBoostingClassifier(learning_rate=0.05, subsample=0.5, max_depth=6, n_estimators=50),
            RandomForestClassifier(n_estimators=50, n_jobs=-1, criterion='gini'),
            RandomForestClassifier(n_estimators=100, n_jobs=-1, criterion='entropy'),
            ExtraTreesClassifier(n_estimators=100, n_jobs=-1, criterion='gini'),
            ExtraTreesClassifier(n_estimators=100, n_jobs=-1, criterion='entropy'),
#           XGBClassifier(),
                                            #SVC(kernel='rbf', C=1, gamma=1, probability=True) ,
            KNeighborsClassifier(),
#                                                                            GaussianProcessClassifier(1.0 * RBF(1.0), warm_start=True,n_jobs=-1),
                                                                                                     #QuadraticDiscriminantAnalysis(),
            #MLPClassifier(hidden_layer_sizes=(6, 6,3 )),
            DecisionTreeClassifier(criterion='entropy'),
            LogisticRegression(),
#GaussianNB()
            ]
    
    #iterate on every classifier
    for clf in list_of_classifier:
        clf.fit(x_train, y_train)
        result=clf.predict(x_test)
        print str(clf.__class__.__name__), accuracy_score(result, y_test)
    
    
