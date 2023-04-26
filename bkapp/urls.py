from django.urls import re_path as url

# from bkapp.views import add_person, show_persons, show_houses, show_credit
from bkapp.views import preprocess_train_test_split, show_yuanweihua, preprocess_replace_value, summary, unique_amount, \
    relation, filter_loss, filter_queer, filter_repeat, sample_similarity, delete_column, digital_coding, \
    type_change, name_change, compute_column, preprocess_fillna, preprocess_sort_by_value, onehot, \
    z_score_regulation, min_max_regulation, logistic_regulation, max_abs_regulation, isometric_dispersion, \
    equal_freq_discretization, kmeans_discretization, kafang_discretization, decision_tree_discretization, \
    PCA_reduce_dim, linear_reduce_dim, linear_regression, lasso_regression, ridge_regression, elastic_net, \
    knn_regression, decision_tree_regression, naive_bayes, linear_SVC, SVM_classification, \
    decision_tree_classification, logistic_regression, knn_classification, show_graduateIncome, test_login_info, \
    log


urlpatterns = [
    url("show_yuanweihua", show_yuanweihua, ),
    url("show_graduateIncome", show_graduateIncome, ),
    url("test_login_info", test_login_info, ),
    url("log", log, ),

    # 2.字段基本统计信息
    url("summary", summary, ),
    # 3.查看唯一值及数量
    url("unique_amount", unique_amount, ),
    # 4.数据相关性
    url("relation", relation, ),
    # 5.过滤缺失值
    url("filter_loss", filter_loss, ),
    # 6.单变量异常值检测
    url("filter_queer", filter_queer),
    # 7.重复值检测
    url("filter_repeat", filter_repeat),
    # 8.样本相似度计算
    url("sample_similarity", sample_similarity),
    # 9.删除列
    url("delete_column", delete_column),
    # 10.训练/测试集划分
    url("preprocess_train_test_split", preprocess_train_test_split, ),
    # 11.数字编码
    url("digital_coding", digital_coding),
    # 13.类型转换
    url("type_change", type_change),
    # 14.列重命名
    url("name_change", name_change),
    # 15.数据列计算
    url("compute_column", compute_column),
    # 16.数据值替换
    url("preprocess_replace_value", preprocess_replace_value, ),
    # 17.缺失值填补
    url("preprocess_fillna", preprocess_fillna, ),
    # 18.数据按列值排序
    url("preprocess_sort_by_value", preprocess_sort_by_value, ),
    # 19.Onehot编码
    url("onehot", onehot, ),
    # 20.Z-Score标准化
    url("z_score_regulation", z_score_regulation, ),
    # 21.Min-Max标准化
    url("min_max_regulation", min_max_regulation, ),
    # 22.Logistic标准化
    url("logistic_regulation", logistic_regulation, ),
    # 23.最大绝对值标准化
    url("max_abs_regulation", max_abs_regulation, ),
    # 24.等距离散化
    url("isometric_dispersion", isometric_dispersion, ),
    # 25.等频离散化
    url("equal_freq_discretization", equal_freq_discretization, ),
    # 26.Kmeans离散化
    url("kmeans_discretization", kmeans_discretization, ),
    # 27.卡方离散化
    url("kafang_discretization", kafang_discretization, ),
    # 28.决策树离散化
    url("decision_tree_discretization", decision_tree_discretization, ),
    # 29.主成分分析
    url("PCA_reduce_dim", PCA_reduce_dim, ),
    # 30.线性判别分析
    url("linear_reduce_dim", linear_reduce_dim, ),
    # 31.线性回归
    url("linear_regression", linear_regression, ),
    # 32.LASSO回归
    url("lasso_regression", lasso_regression, ),
    # 33.岭回归
    url("ridge_regression", ridge_regression, ),
    # 34.弹性网络
    url("elastic_net", elastic_net, ),
    # 35.K近邻回归
    url("knn_regression", knn_regression, ),
    # 36.回归决策树
    url("decision_tree_regression", decision_tree_regression, ),
    # 37.朴素贝叶斯
    url("naive_bayes", naive_bayes, ),
    # 38.线性SVC
    url("linear_SVC", linear_SVC, ),
    # 39.支持向量机
    url("SVM_classification", SVM_classification, ),
    # 40.分类决策树
    url("decision_tree_classification", decision_tree_classification, ),
    # 41.逻辑回归
    url("logistic_regression", logistic_regression, ),
    # 42.K近邻
    url("knn_classification", knn_classification, ),
]
