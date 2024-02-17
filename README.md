Bank Churn prediction end to end project


Customer bank churn prediction using XGBClassifier model.

Applied various Data preprocessing, Visualization and EDA techniques on the dataset.

Made use of GridSearchCV to find the best parameters for the XGBClassifier model.

n_estimators: The number of boosting rounds or trees to build. It represents the number of sequential trees added to the model. learning_rate: Also known as the step size or shrinkage, it controls the contribution of each tree to the final prediction. Lower values require more trees but can lead to better generalization. max_depth: The maximum depth of each tree. It controls the maximum number of nodes in each tree, influencing the complexity of the model

This notebook was created as a part of 'Binary Classification with a Bank Churn Dataset' competition hosted by Kaggle.com

Given below is the link to the notebook on Kaggle. Please make sure to upvote it if you like it! Thanks :) https://www.kaggle.com/code/myash21/final-bank-churn-xgb

Created a basic flask application which takes input values of various parameters and displays the prediction whether a customer is likely to churn or not.
