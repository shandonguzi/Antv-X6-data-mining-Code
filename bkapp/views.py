import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# from bkapp.models import Yuanweihua
# from bkapp.models import Graduateincome
# from bkapp.models import Userinfo
import hashlib

from bkapp.common.getData import get_data
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances
from sklearn import preprocessing
from scipy.stats import chi2
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet, LogisticRegression
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.svm import SVC, LinearSVC


# @require_http_methods(["GET"])
# def add_person(request):
#     response = {}
#     try:
#         person_name = request.GET.get('person_name')
#         person = PersonInfo(name=person_name, age=100, wage=11.11)
#         person.save()
#         response['respMsg'] = 'success'
#         response['respCode'] = '000000'
#     except Exception as e:
#         response['respMsg'] = str(e)
#         response['respCode'] = '999999'
#     return JsonResponse(response)
#
#
# @require_http_methods(["GET"])
# def show_persons(request):
#     response = {}
#     try:
#         persons = PersonInfo.objects.filter()
#         response['list'] = json.loads(serializers.serialize("json", persons))
#         response['dataId'] = 1
#         response['respMsg'] = 'success'
#         response['respCode'] = '000000'
#     except Exception as e:
#         response['respMsg'] = str(e)
#         response['respCode'] = '999999'
#     return JsonResponse(response)


# @require_http_methods(["GET"])
# def show_houses(request):
#     response = {}
#     try:
#         houses = RentHouseInfo.objects.filter()
#         response['list'] = json.loads(serializers.serialize("json", houses))
#         response['dataId'] = 2
#         response['respMsg'] = 'success'
#         response['respCode'] = '000000'
#     except Exception as e:
#         response['respMsg'] = str(e)
#         response['respCode'] = '999999'
#     return JsonResponse(response)


@require_http_methods(["GET"])
def show_yuanweihua(request):
    response = {}
    try:
        yuanweihua = get_data(1)
        response['list'] = json.loads(yuanweihua.to_json(orient='records'))
        response['dataId'] = 1
        response['respMsg'] = 'success'
        response['respCode'] = '000000'
    except Exception as e:
        response['respMsg'] = str(e)
        response['respCode'] = '999999'
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_graduateIncome(request):
    response = {}
    try:
        graduateIncome = get_data(2)
        response['list'] = json.loads(graduateIncome.to_json(orient='records'))
        response['dataId'] = 2
        response['respMsg'] = 'success'
        response['respCode'] = '000000'
    except Exception as e:
        response['respMsg'] = str(e)
        response['respCode'] = '999999'
    return JsonResponse(response)


# @require_http_methods(["GET"])
# def show_credit(request):
#     response = {}
#     try:
#         houses = Motioncredit.objects.filter()
#         response['list'] = json.loads(serializers.serialize("json", houses))
#         response['dataId'] = 4
#         response['respMsg'] = 'success'
#         response['respCode'] = '000000'
#     except Exception as e:
#         response['respMsg'] = str(e)
#         response['respCode'] = '999999'
#     return JsonResponse(response)


@csrf_exempt
@require_http_methods(["POST"])
def summary(request):
    """
    2.字段基本统计信息
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    target_col = req["characterColumn"]

    # 统计基本信息
    result = pd.DataFrame()
    for each_column in target_col:
        temp = data[each_column].describe()
        result = pd.concat([result, temp], axis=1)
    result = result.reset_index().rename(columns={'index': 'metrics'})
    print(result)

    return JsonResponse({
            "result": json.loads(result.to_json(orient='records'))
        })


@csrf_exempt
@require_http_methods(["POST"])
def unique_amount(request):
    """
    3.查看唯一值及数量
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    target_col = req["characterColumn"]

    # 统计基本信息
    result = pd.DataFrame(data[target_col].value_counts(sort=True, ascending=True)).reset_index(drop=False)
    result.rename(columns={'index': target_col, target_col: 'amount'}, inplace=True)
    print(result)

    return JsonResponse({
            "result": json.loads(result.to_json(orient='records'))
        })


@csrf_exempt
@require_http_methods(["POST"])
def relation(request):
    """
    4.数据相关性
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    target_col = req["characterColumn"]
    relation_indicator = req["indicator"]

    # 计算相关性矩阵
    result = pd.DataFrame(data[target_col].corr(method=relation_indicator))
    result = result.reset_index().rename(columns={'index': relation_indicator+"相关系数"})
    print(result)

    return JsonResponse({
            "result": json.loads(result.to_json(orient='records'))
        })


@csrf_exempt
@require_http_methods(["POST"])
def filter_loss(request):
    """
    5.过滤缺失值
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    if_checked = req["checked"]

    # 过滤缺失值
    columns_list = data.columns.tolist()
    columns_loss = pd.DataFrame(columns_list, columns=['列名'])
    loss_rows = []
    for each in columns_list:
        sums = data[each].isnull().sum(axis=0)
        loss_rows.append(sums)
    columns_loss['缺失值行数'] = loss_rows
    has_loss_rows = data.isnull().T.any().sum()
    data_drop_loss = data.dropna(how='any', axis=1)

    # 不过滤缺失值
    if not if_checked:
        output = data
    else:
        output = data_drop_loss

    return JsonResponse({
        "output": json.loads(output.to_json(orient='records')),
        "result": json.loads(columns_loss.to_json(orient='records')),
        "has_loss_rows": int(has_loss_rows),
    })


@csrf_exempt
@require_http_methods(["POST"])
def filter_queer(request):
    """
    6.单变量异常值检测
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req['characterColumn']
    method = req['method']
    if_checked = req["checked"]

    final_queer_data = pd.DataFrame()
    # 四分位距过滤
    if method == 'four':
        for each in columns:
            q1 = data[each].quantile(0.25)
            q3 = data[each].quantile(0.75)
            IQR = q3 - q1
            max_num = q3 + 1.5*IQR
            min_num = q1 - 1.5*IQR
            queer_data = data[(data[each] > max_num) | (data[each] < min_num)]
            final_queer_data = final_queer_data.append(queer_data).drop_duplicates()
    # 拉伊达准则过滤
    elif method == 'la':
        for each in columns:
            mean = data[each].mean()
            std = data[each].std()
            max_num = mean + 3*std
            min_num = mean - 3*std
            queer_data = data[(data[each] > max_num) | (data[each] < min_num)]
            final_queer_data = final_queer_data.append(queer_data).drop_duplicates()

    if if_checked:
        output = data.append(final_queer_data).drop_duplicates(keep=False)
    else:
        output = data
    return JsonResponse({
        "queer_data_num": int(final_queer_data.shape[0]),
        "result": json.loads(final_queer_data.to_json(orient='records')),
        "output": json.loads(output.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def filter_repeat(request):
    """
    7.重复值检测
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    if_checked = req["checked"]
    result = data[data.duplicated()]

    # 检测出非重复数据
    if if_checked:
        output = data.drop_duplicates()
    else:
        output = data

    return JsonResponse({
        "repeat_data_num": result.shape[0],
        "result": json.loads(result.to_json(orient='records')),
        "output": json.loads(output.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def sample_similarity(request):
    """
    8.样本相似度计算
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    method = req["similarity"]

    # 计算样本相似度
    if method == 'cos':
        matrix = cosine_similarity(data[columns])
    elif method == 'ou':
        matrix = pairwise_distances(data[columns], metric='euclidean')
    elif method == 'abs':
        matrix = pairwise_distances(data[columns], metric='manhattan')

    # 获取相似度矩阵上三角的前十大数值索引
    top10 = np.triu(matrix, k=1).reshape(-1).argsort()[::-1][:10]
    result = []
    for each in top10:
        result.append([each // matrix.shape[0], each % matrix.shape[0],
                       matrix[each // matrix.shape[0]][each % matrix.shape[0]]])

    column3_name = '余弦距离' if method == 'cos' else ('欧式距离' if method == 'ou' else '绝对值距离')
    result = pd.DataFrame(result, columns=['样本1索引', '样本2索引', column3_name])

    return JsonResponse({
        "result": json.loads(result.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def delete_column(request):
    """
    9.删除列
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]

    # 删除列
    result = data.drop(columns=columns)

    return JsonResponse({
        "result": json.loads(result.to_json(orient='records')),
        "output": json.loads(result.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def preprocess_train_test_split(request):
    """
    10.训练/测试集划分
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    target_col = req["characterColumn"]
    test_size = float(req["testSize"])
    test_size = int(test_size) if test_size > 1.0 else test_size
    random_state = int(req["randomState"])
    is_stratify = req["checked"]
    if 'characterColumn1' in req:
        stratify_col = req["characterColumn1"]

    stratify = None if is_stratify is False else data[stratify_col]

    y = data[target_col]
    X = data.drop(target_col, axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=stratify)

    train_df = pd.concat([X_train, y_train], axis=1)
    test_df = pd.concat([X_test, y_test], axis=1)

    return JsonResponse({
        "train_table": json.loads(train_df.to_json(orient='records')),
        "test_table": json.loads(test_df.to_json(orient='records')),
        "result": {"index_counts": [train_df.shape[0], test_df.shape[0]],
                     "index_cols": ["训练集", "测试集"]},
    })


@csrf_exempt
@require_http_methods(["POST"])
def digital_coding(request):
    """
    11.数字编码
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]

    # 编码
    le = preprocessing.LabelEncoder()
    le_to_num = []
    for each in columns:
        data[each] = le.fit_transform(data[each])
        le_to_num.append(le.classes_)

    le_to_num = pd.DataFrame(list(le_to_num[0]), columns=['取值'])
    le_to_num['编码值'] = [i for i in range(le_to_num.shape[0])]

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(le_to_num.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def type_change(request):
    """
    13.类型转换
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    to_type = req["type"]

    # 类型转换
    data[columns + '_trans'] = data[columns].astype(to_type)

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(data.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def name_change(request):
    """
    14.列重命名
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    new_name = req["newName"]

    # 列重命名
    data.rename(columns={columns: new_name}, inplace=True)

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(data.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def compute_column(request):
    """
    15.数据列计算
    """
    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    compute_type = req["computeType"]
    compute_num = int(req["computeNum"])

    # 列重命名
    if compute_type == 'plus':
        data[columns + '_cal'] = data[columns] + compute_num
    elif compute_type == 'minus':
        data[columns + '_cal'] = data[columns] - compute_num
    elif compute_type == 'multiply':
        data[columns + '_cal'] = data[columns] * compute_num
    elif compute_type == 'divide':
        data[columns + '_cal'] = data[columns] / compute_num
    elif compute_type == 'involution':
        data[columns + '_cal'] = data[columns] ** compute_num
    elif compute_type == 'disinvolution':
        data[columns + '_cal'] = data[columns] ** (1/compute_num)

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(data.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def preprocess_replace_value(request):
    """
    16.数据值替换
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    replace_col = req["characterColumn"]

    replace_methods = req["substituteMethod"]
    to_replace_value = req["bySub"]
    replace_value = req["sub"]

    initialType = data[replace_col].dtype
    data[replace_col] = data[replace_col].astype('str')

    if replace_methods == 'single':
        data.loc[:, replace_col] = data.loc[:, replace_col].replace(to_replace_value, replace_value)
    elif replace_methods == 'list':
        ToReplaceList = to_replace_value.split('[')[1].split(']')[0].split(',')
        ReplaceList = replace_value.split('[')[1].split(']')[0].split(',')
        for i in range(len(ToReplaceList)):
            data.loc[:, replace_col] = data.loc[:, replace_col].replace(ToReplaceList[i], ReplaceList[i])

    data[replace_col] = data[replace_col].astype(initialType)

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(data.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def preprocess_fillna(request):
    """
    17.缺失值填补
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    replace_method = req["fillMethod"]
    if replace_method == 'specific':
        specific_num = float(req["specificNum"])

    # 替换缺失值
    if replace_method == 'mean':
        data[columns] = data[columns].fillna(data[columns].mean())
    elif replace_method == 'median':
        data[columns] = data[columns].fillna(data[columns].median())
    elif replace_method == 'mode':
        data[columns] = data[columns].fillna(data[columns].mode())
    elif replace_method == 'specific':
        data[columns] = data[columns].fillna(specific_num)

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(data.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def preprocess_sort_by_value(request):
    """
    18.数据按列值排序
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    checked = req["checked"]

    # 排序
    data.sort_values(ascending=(True if checked else False), by=columns, inplace=True)

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(data.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def onehot(request):
    """
    19.Onehot编码
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    checked = req["checked"]

    # Onehot编码
    result = pd.get_dummies(data, columns=[columns], drop_first=(True if checked else False))

    return JsonResponse({
        "output": json.loads(result.to_json(orient='records')),
        "result": json.loads(result.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def z_score_regulation(request):
    """
    20.Z-Score标准化
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]

    # 标准化
    result = pd.DataFrame()
    for each in columns:
        data[each] = data[each].astype("float64")
        result = result.append([[each, data[each].mean(), data[each].std()]])
        data[each] = preprocessing.scale(data[each])

    result.rename(columns={0: '特征', 1: '均值', 2: '标准差'}, inplace=True)

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(result.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def min_max_regulation(request):
    """
    21.Min-Max标准化
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    min_num = float(req["minNum"])
    max_num = float(req["maxNum"])

    # 标准化
    for each in columns:
        data[each] = data[each].astype("float64")
        data[each] = (max_num - min_num) * (data[each] - data[each].min()) \
                     / (data[each].max() - data[each].min()) + min_num

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(data.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def logistic_regulation(request):
    """
    22.Logistic标准化
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]

    # 标准化
    for each in columns:
        data[each] = data[each].astype("float64")
        data[each] = 1 / (1 + np.exp((-1) * data[each]))

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(data.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def max_abs_regulation(request):
    """
    23.最大绝对值标准化
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]

    # 标准化
    for each in columns:
        data[each] = data[each].astype("float64")
        data[each] = data[each] / max(abs(data[each]))

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(data.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def isometric_dispersion(request):
    """
    24.等距离散化
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    num_of_duan = req["numOfDuan"]

    # 等距离散化
    temp_temp_interval = pd.DataFrame(pd.cut(data[columns], num_of_duan)).value_counts().index
    temp_interval = temp_temp_interval.sort_values()
    interval_to_num = pd.DataFrame()
    interval_list = []
    for each in temp_interval:
        interval_list.append(each[0])
    interval_to_num[columns] = interval_list
    interval_to_num[columns] = interval_to_num[columns].sort_values(ascending=True)
    interval_to_num["区间取值"] = [i for i in range(num_of_duan)]
    interval_to_num.iloc[0, 0] = pd._libs.Interval(-np.inf, interval_to_num.iloc[0, 0].right)
    interval_to_num.iloc[interval_to_num.shape[0]-1, 0] = \
        pd._libs.Interval(interval_to_num.iloc[interval_to_num.shape[0]-1, 0].left, np.inf)

    # 此处的labels会自动升序赋值，所以只需调整interval_to_num的顺序即可
    data[columns] = pd.cut(data[columns], num_of_duan, labels=[i for i in range(num_of_duan)])

    interval_to_num[columns] = interval_to_num[columns].astype('str')

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(interval_to_num.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def equal_freq_discretization(request):
    """
    25.等频离散化，qcut实现方式可能导致分箱数和设定的不想等，待优化
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    num_of_duan = req["numOfDuan"]

    # def Rank_qcut(vector, K):
    #     quantile = np.array([float(i) / K for i in range(K + 1)])  # Quantile: K+1 values
    #     funBounder = lambda x: (quantile >= x).argmax()
    #     return vector.rank(pct=True).apply(funBounder)

    # 等频离散化
    temp_temp_interval = pd.DataFrame(pd.qcut(data[columns], num_of_duan, duplicates='drop')).value_counts().index
    temp_interval = temp_temp_interval.sort_values()
    interval_to_num = pd.DataFrame()
    interval_list = []
    for each in temp_interval:
        interval_list.append(each[0])
    interval_to_num[columns] = interval_list
    interval_to_num["区间取值"] = [i for i in range(len(interval_list))]
    interval_to_num.iloc[0, 0] = pd._libs.Interval(-np.inf, interval_to_num.iloc[0, 0].right)
    interval_to_num.iloc[interval_to_num.shape[0]-1, 0] = \
        pd._libs.Interval(interval_to_num.iloc[interval_to_num.shape[0]-1, 0].left, np.inf)

    data[columns] = pd.qcut(data[columns], num_of_duan, labels=[i for i in range(len(interval_list))], duplicates='drop')

    interval_to_num[columns] = interval_to_num[columns].astype('str')

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(interval_to_num.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def kmeans_discretization(request):
    """
    26.Kmeans离散化
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    num_of_duan = req["numOfDuan"]

    # Kmeans离散化
    KMeans_model = KMeans(n_clusters=num_of_duan, random_state=0)
    KMeans_model.fit(data[columns].values.reshape(data[columns].shape[0], 1))
    interval_to_num = pd.DataFrame(KMeans_model.cluster_centers_, columns=[columns]).sort_values(columns)
    interval_to_num["区间取值"] = [i for i in range(num_of_duan)]
    interval_to_num[columns] = interval_to_num[columns].rolling(2).mean()
    for i in range(num_of_duan):
        if i == 0:
            interval_to_num.iloc[i, 0] = pd._libs.Interval(-np.inf, interval_to_num.iloc[i+1, 0])
        elif i == num_of_duan-1:
            interval_to_num.iloc[i, 0] = pd._libs.Interval(interval_to_num.iloc[i, 0], np.inf)
        else:
            interval_to_num.iloc[i, 0] = pd._libs.Interval(interval_to_num.iloc[i, 0], interval_to_num.iloc[i+1, 0])

    # 依次赋值
    for i in range(data.shape[0]):
        for _, interval in interval_to_num.iterrows():
            if data.loc[i, columns] in interval[columns]:
                data.loc[i, columns] = interval["区间取值"]
                break
    data[columns] = data[columns].astype("int32")

    interval_to_num[columns] = interval_to_num[columns].astype('str')

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(interval_to_num.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def kafang_discretization(request):
    """
    27.卡方离散化
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    num_of_duan = req["numOfBox"]

    # 卡方离散化相关函数
    def dsct_init(data, var_name_bf, var_name_target, feature_type):
        """
        特征离散化节点初始化：统计各取值的正负样本分布 [正例样本个数，负例样本个数] 并排序
        :param data: DataFrame 输入数据
        :param var_name_bf: str 待分箱变量
        :param var_name_target: str 标签变量（y)
        :param feature_type: 特征的类型：0（连续） 1（离散）
        :return: DataFrame 排好序的各组中正负样本分布 count
        """
        # 统计待离散化变量的取值类型（string or digits)
        # data_type = data[var_name_bf].apply(lambda x: type(x)).unique()
        data_type = []
        var_type = True if str in data_type else False  # 实际取值的类型：false(数字） true(字符）

        # 是否需要根据正例样本比重排序，True：需要，False：不需要
        #                   0（连续）    1（离散）
        #     false（数字）    0              0（离散有序）
        #     true（字符）     ×             1（离散无序）
        if feature_type == var_type:
            ratio_indicator = var_type
        elif feature_type == 1:
            ratio_indicator = 0
            print("特征%s为离散有序数据，按照取值大小排序！" % (var_name_bf))
        elif feature_type == 0:
            exit(code="特征%s的类型为连续型，与其实际取值（%s）型不一致，请重新定义特征类型！！！" % (var_name_bf, data_type))

        # 统计各分箱（group）内正负样本分布[累计样本个数，正例样本个数，负例样本个数]
        count = pd.crosstab(data[var_name_bf], data[var_name_target])
        total = count.sum(axis=1)

        # 排序：离散变量按照pos_ratio排序，连续变量按照index排序
        if ratio_indicator:
            count['pos_ratio'] = count[1].sum(axis=1) * 1.0 / total  # 计算正例比例
            count = count.sort_values('pos_ratio')  # 离散变量按照pos_ratio排序
            count = count.drop(columns=['pos_ratio'])
        else:
            count = count.sort_index()  # 连续变量按照index排序
        return count, ratio_indicator

    def calc_chi2(count, group1, group2):
        """
        根据分组信息（group）计算各分组的卡方值
        :param count: DataFrame 待分箱变量各取值的正负样本数
        :param group1: list 单个分组信息
        :param group2: list 单个分组信息
        :return: 该分组的卡方值
        """
        count_intv1 = count.loc[count.index.isin(group1)].sum(axis=0).values
        count_intv2 = count.loc[count.index.isin(group2)].sum(axis=0).values
        count_intv = np.vstack((count_intv1, count_intv2))
        # 计算四联表
        row_sum = count_intv.sum(axis=1)
        col_sum = count_intv.sum(axis=0)
        total_sum = count_intv.sum()

        # 计算期望样本数
        count_exp = np.ones(count_intv.shape) * col_sum / total_sum
        count_exp = (count_exp.T * row_sum).T

        # 计算卡方值
        chi2 = (count_intv - count_exp) ** 2 / count_exp
        chi2[count_exp == 0] = 0
        return chi2.sum()

    def merge_adjacent_intervals(chi2_list, group):
        """
        根据卡方值合并卡方值最小的相邻分组
        :param chi2_list: list 每个分组的卡方值
        :param group: list 分组信息
        :return: 合并后的分组信息及卡方值
        """
        min_idx = chi2_list.index(min(chi2_list))
        # 根据卡方值合并卡方值最小的相邻分组
        group[min_idx] = group[min_idx] + group[min_idx + 1]
        group.remove(group[min_idx + 1])
        return group

    def Chi_Merge(count, max_interval=6, sig_level=0.05):
        """
        基于ChiMerge的卡方离散化方法
        :param count: DataFrame 待分箱变量各取值的正负样本数
        :param max_interval: int 最大分箱数量
        :param sig_level: 显著性水平(significance level) = 1 - 置信度
        :return: 分组信息（group）
        """
        print("ChiMerge分箱开始：")
        deg_freedom = len(count.columns) - 1  # 自由度(degree of freedom)= y类别数-1
        chi2_threshold = chi2.ppf(1 - sig_level, deg_freedom)  # 卡方阈值
        group = np.array(count.index).reshape(-1, 1).tolist()  # 分组信息

        while len(group) > max_interval:
            # 2. 计算相邻分组的卡方值
            chi2_list = [calc_chi2(count, group[idx], group[idx + 1]) for idx in range(len(group) - 1)]
            print(chi2_list)

            # 3. 合并相似分组
            if min(chi2_list) >= chi2_threshold:
                print("最小卡方值%.3f大于卡方阈值%.3f，分箱合并结束！！！" % (min(chi2_list), chi2_threshold))
                break
            group = merge_adjacent_intervals(chi2_list, group)
        print("ChiMerge分箱完成！！！")
        return group

    # 卡方离散化
    ka_count, _ = dsct_init(data, columns, target_columns, 0)
    ka_group = Chi_Merge(ka_count, max_interval=num_of_duan, sig_level=0.1)

    interval_to_num = pd.DataFrame([0 for i in range(len(ka_group))], columns=[columns])
    interval_to_num["区间取值"] = [i for i in range(len(ka_group))]
    for i in range(len(ka_group)):
        if i == 0:
            interval_to_num.iloc[i, 0] = pd._libs.Interval(-np.inf, ka_group[0][-1])
        elif i == len(ka_group) - 1:
            interval_to_num.iloc[i, 0] = pd._libs.Interval(ka_group[i - 1][-1], np.inf)
        else:
            interval_to_num.iloc[i, 0] = pd._libs.Interval(ka_group[i - 1][-1], ka_group[i][-1])

    # 依次赋值
    for i in range(data.shape[0]):
        for _, interval in interval_to_num.iterrows():
            if data.loc[i, columns] in interval[columns]:
                data.loc[i, columns] = interval["区间取值"]
                break

    data[columns] = data[columns].astype("int32")
    interval_to_num[columns] = interval_to_num[columns].astype('str')

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(interval_to_num.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def decision_tree_discretization(request):
    """
    28.决策树离散化
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    model_type = req["modelType"]
    num_of_box = req["numOfBox"]

    # 构建树模型
    tree_model = DecisionTreeClassifier(max_leaf_nodes=num_of_box-1) if \
        model_type == 'classification' else DecisionTreeRegressor(max_leaf_nodes=num_of_box-1)

    # 决策树离散化
    X = data[columns].values
    tree_model.fit(X.reshape(-1, 1), data[target_columns])
    boundary = []
    n_nodes = tree_model.tree_.node_count
    children_left = tree_model.tree_.children_left
    children_right = tree_model.tree_.children_right
    threshold = tree_model.tree_.threshold
    for i in range(n_nodes):
        if children_left[i] != children_right[i]:  # 获得决策树节点上的划分边界值
            boundary.append(threshold[i])
    boundary.sort()
    new_vals = []
    for val in X:
        if val < boundary[0]:
            new_vals.append(0)
        elif val >= boundary[-1]:
            new_vals.append(len(boundary))
        else:
            for j in range(1, len(boundary)):
                if val >= boundary[j - 1] and val < boundary[j]:
                    new_vals.append(j)
    data[columns] = new_vals
    list_temp = []
    for i in range(len(boundary)):
        if i == 0:
            list_temp.append(pd._libs.Interval(-np.inf, round(boundary[i], 6)))
        else:
            list_temp.append(pd._libs.Interval(round(boundary[i - 1], 6), round(boundary[i], 6)))
    list_temp.append(pd._libs.Interval(round(boundary[-1], 6), np.inf))
    interval_to_num = pd.DataFrame(list_temp, columns=[columns])
    interval_to_num["区间取值"] = [i for i in range(len(boundary)+1)]

    interval_to_num[columns] = interval_to_num[columns].astype('str')

    return JsonResponse({
        "output": json.loads(data.to_json(orient='records')),
        "result": json.loads(interval_to_num.to_json(orient='records')),
    })


@csrf_exempt
@require_http_methods(["POST"])
def PCA_reduce_dim(request):
    """
    29.主成分分析
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    dims = req["numOfDim"]

    # 主成分分析
    pca_model = PCA(n_components=dims)
    new_data = pca_model.fit_transform(data[columns])
    n_components = pca_model.n_components_
    new_data = pd.DataFrame(new_data, columns=['pca_' + str(i) for i in range(n_components)])
    components = pd.DataFrame(pca_model.components_, columns=columns)
    ratios = pd.DataFrame(pca_model.explained_variance_ratio_, columns=['ratios'])

    components = components.reset_index().rename(columns={'index': '主成分'})
    components['主成分'] = ['pca_' + str(i) for i in range(n_components)]

    ratios = ratios.reset_index().rename(columns={'index': '主成分'})
    ratios['主成分'] = ['pca_' + str(i) for i in range(n_components)]

    return JsonResponse({
          "output": json.loads(new_data.to_json(orient='records')),
          "result": json.loads(components.to_json(orient='records')),
          "ratios": json.loads(ratios.to_json(orient='records')),
        })


@csrf_exempt
@require_http_methods(["POST"])
def linear_reduce_dim(request):
    """
    30.线性判别分析
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    dims = req["numOfDim"]

    # 主成分分析
    lda_model = LDA(n_components=dims)
    new_data = lda_model.fit_transform(data[columns], data[target_columns])
    new_data = pd.DataFrame(new_data, columns=['lda_' + str(i) for i in range(dims)])
    new_data[target_columns] = data[target_columns]
    ratios = pd.DataFrame(lda_model.explained_variance_ratio_, columns=['ratios'])

    ratios = ratios.reset_index().rename(columns={'index': '主成分'})
    ratios['主成分'] = ['lda_' + str(i) for i in range(dims)]

    return JsonResponse({
          "result": json.loads(new_data.to_json(orient='records')),
          "output": json.loads(new_data.to_json(orient='records')),
          "ratios": json.loads(ratios.to_json(orient='records')),
        })


@csrf_exempt
@require_http_methods(["POST"])
def linear_regression(request):
    """
    31.线性回归
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    is_intercept = True if req["checked"] else False
    is_normalization = True if req["checked1"] and is_intercept else False

    # 线性回归
    linear_model = LinearRegression(fit_intercept=is_intercept, normalize=is_normalization)
    linear_model.fit(data[columns], data[target_columns])
    coef = pd.DataFrame([linear_model.coef_], columns=columns)
    intercept = linear_model.intercept_

    return JsonResponse({
          "result": json.loads(coef.to_json(orient='records')),
          "intercept": intercept,
          "model": linear_model.get_params(),
        })


@csrf_exempt
@require_http_methods(["POST"])
def lasso_regression(request):
    """
    32.LASSO回归
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    normal_num = req["normalNum"]
    is_intercept = True if req["checked"] else False
    is_normalization = True if req["checked1"] and is_intercept else False

    # LASSO回归
    lasso_model = Lasso(alpha=normal_num, fit_intercept=is_intercept, normalize=is_normalization)
    lasso_model.fit(data[columns], data[target_columns])
    coef = pd.DataFrame([lasso_model.coef_], columns=columns)
    intercept = lasso_model.intercept_

    return JsonResponse({
        "result": json.loads(coef.to_json(orient='records')),
        "intercept": intercept,
        "model": lasso_model.get_params(),
    })


@csrf_exempt
@require_http_methods(["POST"])
def ridge_regression(request):
    """
    33.岭回归
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    normal_num = req["normalNum"]
    is_intercept = True if req["checked"] else False
    is_normalization = True if req["checked1"] and is_intercept else False

    # 线性回归
    ridge_model = Ridge(alpha=normal_num, fit_intercept=is_intercept, normalize=is_normalization)
    ridge_model.fit(data[columns], data[target_columns])
    coef = pd.DataFrame([ridge_model.coef_], columns=columns)
    intercept = ridge_model.intercept_

    return JsonResponse({
        "result": json.loads(coef.to_json(orient='records')),
        "intercept": intercept,
        "model": ridge_model.get_params(),
    })


@csrf_exempt
@require_http_methods(["POST"])
def elastic_net(request):
    """
    34.弹性网络
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    normal_num_1 = req["normalNum"]
    normal_num_2 = req["normalNum1"]
    is_intercept = True if req["checked"] else False
    is_normalization = True if req["checked1"] and is_intercept else False

    # 线性回归
    elastic_net_model = ElasticNet(alpha=normal_num_1, l1_ratio=normal_num_2, fit_intercept=is_intercept, normalize=is_normalization)
    elastic_net_model.fit(data[columns], data[target_columns])
    coef = pd.DataFrame([elastic_net_model.coef_], columns=columns)
    intercept = elastic_net_model.intercept_

    return JsonResponse({
        "result": json.loads(coef.to_json(orient='records')),
        "intercept": intercept,
        "model": elastic_net_model.get_params(),
    })


@csrf_exempt
@require_http_methods(["POST"])
def knn_regression(request):
    """
    35.K近邻回归
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    neighbor_num = req["numberOfNeighbor"]
    weight_type = req["weightType"]
    distance_type = req["distanceType"]

    # K近邻回归
    knn_model = KNeighborsRegressor(n_neighbors=neighbor_num, weights=weight_type, metric=distance_type)
    knn_model.fit(data[columns], data[target_columns])

    result = pd.DataFrame(['邻居个数', '权重计算方式', '距离计算方式'], columns=['参数名称'])
    result['参数取值'] = [neighbor_num, weight_type, distance_type]

    return JsonResponse({
        "result": json.loads(result.to_json(orient='records')),
        "model": knn_model.get_params(),
    })


@csrf_exempt
@require_http_methods(["POST"])
def decision_tree_regression(request):
    """
    36.回归决策树
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    max_depth = req["maxDepth"]
    min_split = req["minSplit"]
    min_leaf = req["minLeaf"]

    # 回归决策树
    decision_tree_regression_model = DecisionTreeRegressor(max_depth=max_depth, min_samples_split=min_split,
                                                           min_samples_leaf=min_leaf)
    decision_tree_regression_model.fit(data[columns], data[target_columns])

    # 返回值
    feature_importance = pd.DataFrame([decision_tree_regression_model.feature_importances_], columns=columns)
    tree = decision_tree_regression_model.tree_
    print(feature_importance)
    print(tree)

    return JsonResponse({
          "result": json.loads(feature_importance.to_json(orient='records')),
          # 待解决的画图问题
          # "tree": tree,
          "model": decision_tree_regression_model.get_params(),
        })


@csrf_exempt
@require_http_methods(["POST"])
def naive_bayes(request):
    """
    37.朴素贝叶斯
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    bayes_type = req["bayesType"]
    smooth = req["smooth"] if bayes_type != "GaussianNB" else None
    prior = req["checked"] if bayes_type != "GaussianNB" else None
    binarization = req["binarization"] if bayes_type == "BernoulliNB" else None

    # 贝叶斯分类器
    if bayes_type == "BernoulliNB":
        bayes_model = BernoulliNB(alpha=smooth, fit_prior=prior, binarize=binarization)
    elif bayes_type == "GaussianNB":
        bayes_model = GaussianNB()
    else:
        bayes_model = MultinomialNB(alpha=smooth, fit_prior=prior)
    bayes_model.fit(data[columns], data[target_columns])

    if bayes_type == "BernoulliNB":
        result = pd.DataFrame(['贝叶斯分类器', '平滑参数', '学习先验概率', '二值化阈值'], columns=['参数名称'])
        result['参数取值'] = [bayes_type, smooth, prior, binarization]
    elif bayes_type == "GaussianNB":
        result = pd.DataFrame(['贝叶斯分类器'], columns=['参数名称'])
        result['参数取值'] = [bayes_type]
    else:
        result = pd.DataFrame(['贝叶斯分类器', '平滑参数', '学习先验概率',], columns=['参数名称'])
        result['参数取值'] = [bayes_type, smooth, prior]

    return JsonResponse({
          "result": json.loads(result.to_json(orient='records')),
          "model": bayes_model.get_params(),
        })


@csrf_exempt
@require_http_methods(["POST"])
def linear_SVC(request):
    """
    38.线性SVC
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    normal_num = req["normalNum"]
    min_converge = req["minConverge"]
    max_iter = req["maxIter"]
    if_intercept = req["checked"]

    # 线性SVC
    svc_model = LinearSVC(C=normal_num, tol=min_converge, max_iter=max_iter, fit_intercept=if_intercept)
    svc_model.fit(data[columns], data[target_columns])

    # 返回值
    coef_index = list(svc_model.classes_)
    coef = pd.DataFrame(svc_model.coef_, index=coef_index, columns=columns)
    intercept = pd.DataFrame([svc_model.intercept_], columns=coef_index)

    coef = coef.reset_index().rename(columns={'index': 'labels'})

    return JsonResponse({
          "coef": json.loads(coef.to_json(orient='records')),
          "result": json.loads(intercept.to_json(orient='records')),
          "model": svc_model.get_params(),
        })


@csrf_exempt
@require_http_methods(["POST"])
def SVM_classification(request):
    """
    39.支持向量机
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    train_max_error = req["trainMaxError"]
    core_function = req["coreFunction"]
    gamma = req["gamma"]
    coef0 = req["coef0"] if core_function != "rbf" else None
    degree = req["degree"] if core_function == "poly" else None
    class_weight = req["classWeight"] if req["classWeight"] != "None" else None

    # 支持向量机
    if core_function == "poly":
        svc_model = SVC(C=train_max_error, kernel=core_function, gamma=gamma, coef0=coef0, degree=degree, class_weight=class_weight)
    elif core_function == "rbf":
        svc_model = SVC(C=train_max_error, kernel=core_function, gamma=gamma, class_weight=class_weight)
    else:
        svc_model = SVC(C=train_max_error, kernel=core_function, gamma=gamma, coef0=coef0, class_weight=class_weight)

    svc_model.fit(data[columns], data[target_columns])

    # 返回值
    n_support_index = list(svc_model.classes_)
    n_support = pd.DataFrame([svc_model.n_support_], columns=n_support_index)
    intercept = pd.DataFrame([svc_model.intercept_], columns=n_support_index)

    return JsonResponse({
          "n_support": json.loads(n_support.to_json(orient='records')),
          "result": json.loads(intercept.to_json(orient='records')),
          "model": svc_model.get_params(),
        })


@csrf_exempt
@require_http_methods(["POST"])
def decision_tree_classification(request):
    """
    40.分类决策树
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    max_depth = req["maxDepth"]
    min_split = req["minSplit"]
    min_leaf = req["minLeaf"]

    # 分类决策树
    decision_tree_classification_model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_split,
                                                           min_samples_leaf=min_leaf)
    decision_tree_classification_model.fit(data[columns], data[target_columns])

    # 返回值
    feature_importance = pd.DataFrame([decision_tree_classification_model.feature_importances_], columns=columns)
    tree = decision_tree_classification_model.tree_
    print(feature_importance)
    print(tree)

    return JsonResponse({
        "result": json.loads(feature_importance.to_json(orient='records')),
        # 待解决的画图问题
        # "tree": tree,
        "model": decision_tree_classification_model.get_params(),
    })


@csrf_exempt
@require_http_methods(["POST"])
def logistic_regression(request):
    """
    41.逻辑回归
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    normal_item = req["normalItem"] if req["normalItem"] != "None" else None
    normal_num = req["normalNum"]
    min_converge = req["minConverge"]
    random_state = req["randomState"]
    class_weight = req["classWeight"] if req["classWeight"] != "None" else None

    # 逻辑回归
    logistic_model = LogisticRegression(penalty=normal_item, C=normal_num, tol=min_converge,
                                        random_state=random_state, class_weight=class_weight, solver="liblinear")
    logistic_model.fit(data[columns], data[target_columns])

    # 返回值
    coef_index = list(logistic_model.classes_)
    coef = pd.DataFrame(logistic_model.coef_, index=coef_index, columns=columns)

    return JsonResponse({
          "result": json.loads(coef.to_json(orient='records')),
          "model": logistic_model.get_params(),
        })


@csrf_exempt
@require_http_methods(["POST"])
def knn_classification(request):
    """
    42.K近邻
    """

    req = json.loads(request.body)
    print(req)

    if 'lastOutput' not in req:
        # 获取dataId
        dataId = req["dataId"]
        # 读取数据
        data = get_data(dataId=dataId)
    else:
        data = pd.DataFrame(req['lastOutput'])

    columns = req["characterColumn"]
    target_columns = req["characterColumn1"]
    neighbor_num = req["numberOfNeighbor"]
    weight_type = req["weightType"]
    distance_type = req["distanceType"]

    # K近邻回归
    knn_model = KNeighborsClassifier(n_neighbors=neighbor_num, weights=weight_type, metric=distance_type)
    knn_model.fit(data[columns], data[target_columns])

    result = pd.DataFrame(['邻居个数', '权重计算方式', '距离计算方式'], columns=['参数名称'])
    result['参数取值'] = [neighbor_num, weight_type, distance_type]

    return JsonResponse({
        "result": json.loads(result.to_json(orient='records')),
        "model": knn_model.get_params(),
    })


@csrf_exempt
@require_http_methods(["POST"])
def test_login_info(request):

    req = json.loads(request.body)
    uname = str(req['username'])
    upass = str(req['password'])
    result = 0

    # 数据库对比
    userinfo = pd.read_csv("./bkapp/database/userInfo.csv", encoding='utf-8')
    print(userinfo)

    # 加盐
    obj = hashlib.md5(b'12334')
    obj.update(upass.encode("utf-8"))
    upass_secret = obj.hexdigest()
    if uname in userinfo['username'].values:
        if (upass_secret == userinfo[userinfo['username'] == uname]['password']).values[0]:
            result = 1

    return JsonResponse({
        "result": result
    })


@csrf_exempt
@require_http_methods(["POST"])
def log(request):

    req = json.loads(request.body)
    uname = str(req['username'])
    upass = str(req['password'])
    confirm = str(req['passwordConfirm'])
    result = 0

    # 数据库对比
    userinfo = pd.read_csv("./bkapp/database/userInfo.csv", encoding='utf-8')
    print(userinfo)

    # 加盐
    obj = hashlib.md5(b'12334')
    obj.update(upass.encode("utf-8"))
    upass_secret = obj.hexdigest()
    if uname not in userinfo['username'].values:
        if upass == confirm:
            userinfo = pd.concat([userinfo, pd.DataFrame([[uname, upass_secret]], columns=['username', 'password'])])
            userinfo.to_csv("./bkapp/database/userInfo.csv", encoding='utf-8', index=False)
            result = 1
    print(userinfo)

    return JsonResponse({
        "result": result
    })