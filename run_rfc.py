import mlflow
import numpy as np
# from mlflow.utils.mlflow_tags import MLFLOW_RUN_NAME

# const
EXP_NAME = 'iris'
model_name = 'rfc'
model_param_dict = {'max_depth': 20}
feat_list = ['a', 'b', 'c']

mlflow.set_experiment(EXP_NAME)

# Run Nameの指定と、パラメータ・特徴の記録
# mlflow.set_tag(MLFLOW_RUN_NAME, TASK_NAME)  # Run Nameを指定
mlflow.log_param('model_name', model_name)  # LigtGBMのパラメータを記録
mlflow.log_param('model_params', model_param_dict)  # LigtGBMのパラメータを記録
mlflow.log_param('Features', feat_list)  # 使った特徴を記録

###
# 中略 LightGBMで学習する
##

# cvscoreの保存
scores = [0.8, 0.83, 0.85, 0.79, 0.88]
dic = dict()
for i, score in enumerate(scores):
    dic[f'fold{i+1}'] = score
mlflow.log_metrics(dic)  # 各foldのsocreを記録
mlflow.log_metric('cv_score', np.mean(scores))  # 各foldのscoreの平均を記録

# ビジュアライズしたpngファイルを記録
# mlflow.log_artifact('importance.png')  # feature importanceを記録
