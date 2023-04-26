<template>
  <a-row>
    <a-col :span="4">
      <a-layout-sider style="background: #fff">
      <a-menu
          mode="inline"
          :style="{ height: '100%', borderRight: 0, width: menuWidth }"
      >
        <a-sub-menu key="sub1">
          <template #title>
            <span>数据源</span>
          </template>
          <a-menu-item key="1" @click="changePage(1)">读数据表</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub2">
          <template #title>
            <span>数据探索</span>
          </template>
          <a-menu-item key="2" @click="changePage(2)">字段基本信息统计</a-menu-item>
          <a-menu-item key="3" @click="changePage(3)">查看唯一值及数量</a-menu-item>
          <a-menu-item key="4" @click="changePage(4)">数据相关性</a-menu-item>
          <a-menu-item key="5" @click="changePage(5)">缺失值检测</a-menu-item>
          <a-menu-item key="6" @click="changePage(6)">单变量异常值检测</a-menu-item>
          <a-menu-item key="7" @click="changePage(7)">重复值检测</a-menu-item>
          <a-menu-item key="8" @click="changePage(8)">样本相似度计算</a-menu-item>

        </a-sub-menu>
        <a-sub-menu key="sub3">
          <template #title>
            <span>
              筛选与分组
            </span>
          </template>
          <a-menu-item key="9" @click="changePage(9)">列删除</a-menu-item>
          <a-menu-item key="10" @click="changePage(10)">训练/测试集划分</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub4">
          <template #title>
            <span>数据转换</span>
          </template>
          <a-menu-item key="11" @click="changePage(11)">数字编码</a-menu-item>
          <!--            <a-menu-item key="12" @click="changePage(12)">人工数字编码</a-menu-item>-->
          <a-menu-item key="13" @click="changePage(13)">类型转换</a-menu-item>
          <a-menu-item key="14" @click="changePage(14)">列重命名</a-menu-item>
          <a-menu-item key="15" @click="changePage(15)">数据列计算</a-menu-item>
          <a-menu-item key="16" @click="changePage(16)">数据值替换</a-menu-item>
          <a-menu-item key="17" @click="changePage(17)">缺失值填补</a-menu-item>
          <a-menu-item key="18" @click="changePage(18)">数据按列值排序</a-menu-item>

        </a-sub-menu>
        <a-sub-menu key="sub5">
          <template #title>
            <span>特征抽取</span>
          </template>
          <a-menu-item key="19" @click="changePage(19)">OneHot编码</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub6">
          <template #title>
            <span>标准化</span>
          </template>
          <a-menu-item key="20" @click="changePage(20)">Z-Score标准化</a-menu-item>
          <a-menu-item key="21" @click="changePage(21)">Min-Max标准化</a-menu-item>
          <a-menu-item key="22" @click="changePage(22)">Logistic标准化</a-menu-item>
          <a-menu-item key="23" @click="changePage(23)">最大绝对值标准化</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub7">
          <template #title>
            <span>离散化</span>
          </template>
          <a-menu-item key="24" @click="changePage(24)">等距离散化</a-menu-item>
          <a-menu-item key="25" @click="changePage(25)">等频离散化</a-menu-item>
          <a-menu-item key="26" @click="changePage(26)">Kmeans离散化</a-menu-item>
          <a-menu-item key="27" @click="changePage(27)">卡方离散化</a-menu-item>
          <a-menu-item key="28" @click="changePage(28)">决策树离散化</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub8">
          <template #title>
            <span>降维</span>
          </template>
          <a-menu-item key="29" @click="changePage(29)">主成分分析</a-menu-item>
          <a-menu-item key="30" @click="changePage(30)">线性判别分析</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub9">
          <template #title>
            <span>回归</span>
          </template>
          <a-menu-item key="31" @click="changePage(31)">线性回归</a-menu-item>
          <a-menu-item key="32" @click="changePage(32)">LASSO</a-menu-item>
          <a-menu-item key="33" @click="changePage(33)">岭回归</a-menu-item>
          <a-menu-item key="34" @click="changePage(34)">弹性网络</a-menu-item>
          <a-menu-item key="35" @click="changePage(35)">K近邻回归</a-menu-item>
          <a-menu-item key="36" @click="changePage(36)">回归决策树</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub10">
          <template #title>
            <span>分类</span>
          </template>
          <a-menu-item key="37" @click="changePage(37)">朴素贝叶斯</a-menu-item>
          <a-menu-item key="38" @click="changePage(38)">线性SVC</a-menu-item>
          <a-menu-item key="39" @click="changePage(39)">支持向量机</a-menu-item>
          <a-menu-item key="40" @click="changePage(40)">分类决策树</a-menu-item>
          <a-menu-item key="41" @click="changePage(41)">逻辑回归</a-menu-item>
          <a-menu-item key="42" @click="changePage(42)">K近邻</a-menu-item>
        </a-sub-menu>
      </a-menu>
    </a-layout-sider>
    </a-col>
    <a-col :span="20">
      <a-layout style="padding: 0 24px 24px">
      <el-text v-for="(name, key) in id_to_name" style="color: black ;font-size: 30px; margin: 16px; font-weight: bold"
               v-show="pageId == key">
        {{ name }}
      </el-text>

      <a-layout-content :style="{ background: '#F0F2F5', padding: '24px', margin: 0 }">
        <el-space v-if="pageId == 1" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">从已有数据集列表选择数据集读取数据。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 选取数据集：可选参数，可选择不同行业的数据集。</el-text>
          <el-image style="width: 500px; height: 330px; margin-bottom: 30px; margin-left: 130px" :src="photo1_1"/>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出桩返回读取的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">显示数据集基本信息和预览数据。</el-text>
          <el-image :src="photo1_2" style="width: 500px; height: 350px; margin-bottom: 30px; margin-left: 130px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">从平台数据集或用户自己的数据集中选取要分析的数据集。</el-text>
        </el-space>
        <el-space v-if="pageId == 2" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对某些数据字段进行统计分析，并展示相应的信息。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 统计列：选择指定的一个或多个数据字段进行基本信息统计。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回数据字段信息基本统计后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回数据字段信息基本统计后的数据对象。</el-text>
          <el-image :src="photo2" style="width: 500px; height: 350px; margin-bottom: 30px; margin-left: 130px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            基于选定的一个或多个字段，计算该字段下样本数量、不同取值个数、众数、众数的频数、均值、标准差、最小值、上四分位数、中位数、下四分位数、最大值等信息，帮助更好地对数据集字段进行初步诊断。
          </el-text>
          <el-text class="original_text">部分统计指标介绍如下：</el-text>
          <el-text class="right_text">● 样本数：非空值的数量</el-text>
          <el-text class="right_text">● 众数：出现次数最多的取值</el-text>
          <el-text class="right_text">● 众数的频数：众数的出现次数</el-text>
          <el-text class="right_text">● 下四分位数：将全部数据从小到大排列，正好排列在25%位置上的数</el-text>
          <el-text class="right_text_bottom">● 上四分位数：将全部数据从小到大排列，正好排列在75%位置上的数</el-text>
          <el-text class="original_text">对于不同类型的变量，我们会采用不同统计指标：</el-text>
          <el-text class="right_text">●
            对于连续型变量，通常会统计样本数、均值、标准差、最小值、上四分位数、中位数、下四分位数、最小值和最大值等指标。
          </el-text>
          <el-text class="right_text">● 对于离散型变量，通常会统计样本数、不同取值个数、众数、众数的频数等指标。</el-text>
        </el-space>
        <el-space v-if="pageId == 3" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">查看某些数据字段的唯一取值，以及这些取值在该字段中出现的次数。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 统计列：选择一个指定的数据字段查看其唯一取值及数量。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回指定的数据字段的唯一值及数量的信息，保存在表格中。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回指定的数据字段的唯一值及数量的信息。</el-text>
          <el-image :src="photo3" class="images" style="width: 500px; height: 200px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            可以查看一个指定字段中有多少个不同的数据值，并计算不同值出现的频数。查看唯一值对了解数据的分布、是否存在异常值和错误值，都有着重要意义。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 4" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">计算数据集中数值型特征之间的相关性。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 选择列：选择指定的多个关心的数值型字段，考察这些数值型字段的相关性。</el-text>
          <el-text class="right_text_bottom">●
            相关性指标：相关性计算指标，分别为Pearson相关系数、Spearman相关系数和Kendall相关系数，默认为Pearson相关系数。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回指定数据字段的相关性矩阵，保存在表格中。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回指定数据字段的相关性矩阵以及相关性热力图。</el-text>
          <el-image :src="photo4" class="images" style="width: 500px; height: 450px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            相关性可以衡量变量间的关联程度。本组件基于选定的若干个字段，考察这些字段两两之间的相关性，并返回字段相关性矩阵。
          </el-text>
          <el-text class="original_text">计算指标包括Pearson相关系数、Spearman相关系数和Kendall相关系数。</el-text>
          <el-text class="right_text">●
            Pearson相关系数描述的是连续变量的线性相关关系。相关系数计算结果通常介于-1和1之间。若相关系数为0，则表示两个变量间无线性关系；大于0表示正相关；小于0表示负相关。计算公式如下：
          </el-text>
          <el-image :src="photo4_2" class="images" style="width: 270px; height: 70px"/>
          <el-text class="right_text">●
            Spearman相关系数是无参数的等级相关系数，即其值与两个相关变量的具体值无关，而仅仅与其值之间的大小关系有关。计算公式如下。其中，di表示两个变量分别排序后成对的变量位置差，N表示样本数量：
          </el-text>
          <el-image :src="photo4_3" class="images" style="width: 170px; height: 55px"/>
          <el-text class="right_text">● Kendall相关系数描述的是有序分类变量的相关关系，属于等级相关系数。相关系数计算结果通常介于-1和1之间。变量排序一致，则为1，
            排序完全相反则为-1。计算公式如下：
          </el-text>
          <el-image :src="photo4_4" class="images" style="width: 400px; height: 70px"/>

        </el-space>
        <el-space v-if="pageId == 5" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">检测数据中是否存在缺失值，并可选是否直接过滤缺失值。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 过滤缺失值：控制是否直接过滤检测到的缺失值所在的行，默认不勾选。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">●
            输出桩：1个，返回过滤缺失值后的数据对象，若不存在缺失值或不勾选过滤缺失值，返回原数据对象。
          </el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">
            返回数据的每个字段名称与这些字段中的缺失值数量组成的表格，然后返回本次过滤的缺失值行数。下面是对一份鸢尾花数据集进行缺失值检测后的报告：
          </el-text>
          <el-text class="original_text">数据缺失值情况：</el-text>
          <el-image :src="photo5" class="images" style="width: 500px; height: 270px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            缺失值检测是数据质量诊断的重要手段，可以查看字段的缺失值数量，如存在缺失值，则计算缺失值数量或占比。过滤缺失值可以过滤掉缺失值所在行，过滤后可以得到一个完整的数据子集，便于后续数据处理。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 6" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">检测数据中的数值型字段是否存在异常值。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 检测列：选择一个或多个数值型数据字段，检测每一列的异常值。</el-text>
          <el-text class="right_text">●
            检测方式：检测异常值所采用的策略，包括两种，四分位距和拉伊达准侧，默认为四分位距策略。
          </el-text>
          <el-text class="right_text_bottom">●
            是否过滤异常值：是否直接过滤检测到的异常值所在的行，默认为是，将每个列检测出的异常值取并集后一起过滤。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">●
            输出桩：1个，返回过滤异常值后的数据对象，若不存在异常值或不勾选过滤异常值，返回原数据对象。
          </el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">
            返回检测到的异常值行数，然后返回这些异常值行数据，以及过滤这些异常值行所得到的数据。
          </el-text>
          <el-image :src="photo6" class="images" style="width: 500px; height: 500px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">检测策略共有四分位距和拉伊达准则两种。</el-text>
          <el-text class="original_text">
            四分位距策略首先找到该数据字段的下四分位数，中位数和上四分位数，分别标记为Q1,Q2,Q3。上四分位数和下四分位数的差标记为IQR。在该策略下，数据字段的最大值估计为Q3
            + 1.5*IQR，最小值估计为Q1 - 1.5*IQR。则低于最小值估计，或高于最大值估计的数据均被标记为异常值。
          </el-text>
          <el-text class="original_text">
            拉伊达准则又被称为3σ策略，一般要求数据服从或近似服从正态分布。假设数据的均值为mean，标准差为std，该策略假定数据服从均值为mean，标准差为std的正态分布，并将大于mean
            + 3*std或小于mean - 3*std的数据标记为异常值。在标准正态分布中，数据落在这两个值之间的概率为99.74%。
          </el-text>

        </el-space>
        <el-space v-if="pageId == 7" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">检测数据中是否存在完全重复的行。</el-text>
          <el-text class="sub_head" style="margin-bottom: 20px">面板参数说明</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回所检测到的数据中完全重复的行。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回所检测到的重复行数量，然后返回所检测到的完全重复的行数据信息。</el-text>
          <el-image :src="photo7" class="images" style="width: 500px; height: 270px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            检测数据中是否存在完全重复的行，若存在则返回重复行数量及完全重复的行数据信息；不存在则返回原数据。删除重复值可以有效提高数据质量。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 8" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">可用于计算样本间的相似度计算，返回相关性矩阵，从而确定相关性。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 计算列：选择每个样本中需要参与计算的列。</el-text>
          <el-text class="right_text_bottom">● 相似度：计算相似度的方式，包括余弦距离、欧式距离、绝对值距离。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回指定样本的相似度矩阵，保存在表格中。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">
            返回距离最近（相似度高）的10对样本，如下图，第一行表示索引为149的样本和索引为150的样本距离为1，选取的距离计算方式是余弦距离。
          </el-text>
          <el-image :src="photo8_1" class="images" style="width: 500px; height: 350px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            通过计算样本间距离，确定在给定特征下样本的相似性。常用的计算方法包括余弦距离、欧式距离、绝对值距离等。现在假设有两个d维样本x和y。
          </el-text>
          <el-text class="right_text">● 余弦距离又被称作余弦相似度，是用向量空间中两个向量夹角的余弦值作为衡量两个个体间差异的大小的度量。取值范围是[-1,1],
            取值越大，表明两个向量距离越近。计算公式如下：
          </el-text>
          <el-image :src="photo8_2" class="images" style="width: 200px; height: 50px"/>
          <el-text class="right_text">●
            欧式距离又被称为欧几里得距离，是欧几里得空间中两点间的即直线距离，取值非负。计算公式如下：
          </el-text>
          <el-image :src="photo8_3" class="images" style="width: 200px; height: 70px"/>
          <el-text class="right_text">●
            绝对值距离又被称作曼哈顿距离，是两个点在标准坐标系上分量绝对值之差的和，取值非负。计算公式如下：
          </el-text>
          <el-image :src="photo8_4" class="images" style="width: 200px; height: 68px"/>
        </el-space>
        <el-space v-if="pageId == 9" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">删除数据表格中的某列或某几列。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 需要删除的列：选择一个或多个希望删除的数据列对应的数据字段。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出删除数据列后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回删除数据列后的数据表，例如下面的例子：</el-text>
          <el-text class="original_text">原始数据：</el-text>
          <el-image :src="photo1_2" class="images" style="width: 500px; height: 350px"/>
          <el-text class="original_text">返回删除前三列后的结果：</el-text>
          <el-image :src="photo9_2" class="images" style="width: 500px; height: 350px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">对于数据集中存在的冗余数据，可以通过删除的方式去掉这些冗余信息。</el-text>
        </el-space>
        <el-space v-if="pageId == 10" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">将数据集样本划分为训练集和测试集两部分。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 标签列：选取有监督数据集样本中的标签列，单选。</el-text>
          <el-text class="right_text">●
            测试集大小：输入测试集占数据样本总体的比例，范围为(0,1)，例如输入值为0.2，则表示测试集占数据样本总体的20%，训练集占80%，训练集与测试集的比例为4:1。
          </el-text>
          <el-text class="right_text">● 采样随机数：输入大于等于0的整数，相同的值可以保证每次划分的结果一致。</el-text>
          <el-text class="right_text">● 是否分层抽样：选择是否进行分层抽样，默认为否。</el-text>
          <el-text class="right_text_bottom">●
            分层列：是否分层抽样选择是时弹出，选择按照哪一列进行分层抽样，一般选择标签列，在分类任务中，可以保证训练集和测试集中各类样本的比例一致。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：2个，左输出桩返回训练集数据对象，右输出桩返回测试集数据对象。
          </el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">输出划分后的训练集和测试集样本数量分布饼状图，如下图所示。</el-text>
          <el-image :src="photo10" class="images" style="width: 500px; height: 350px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            在使用数据集训练模型之前，我们需要先将整个数据集分为训练集和测试集。训练集用来训练模型，通过尝试不同的方法和思路使用训练集来训练不同的模型，再利用评价指标通过测试集来评估模型的效果。
          </el-text>
          <el-text class="original_text">
            一般情况下，训练集和测试集的比例为7:3。若数据量充足，则应该尽量加大测试集的占比，最好保证训练集和测试集的比例为1:1，以便更加充分地评估模型的效果。由于程序每次划分的结果都是随机的，通过设置相同的随机种子数，可以保证每次划分的结果都一样，以便在相同数据下比较不同模型的效果。
          </el-text>
          <el-text class="original_text">
            在分类任务中，划分训练集和测试集一般采取分层抽样的方式，目的是尽量保证训练集、测试集与总体数据样本分布的一致性，减少因数据划分过程引入额外的偏差而对模型的性能产生影响。例如二分类任务中，总体样本中正负类样本数量比为1:3，则划分后训练集和测试集中正负样本数量比都为1:3。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 11" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对离散型变量进行数字编码，例如性别（男，女）编码为（0，1）。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 编码列：选取需要进行数字编码的列，单选。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出进行数字编码后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回所选列进行数字编码后的结果以及所选列中的值对应的编码值。</el-text>
          <el-image :src="photo11" class="images" style="width: 500px; height: 500px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            在实际问题中，获取的原始数据会包含非数值型特征，因此需要对其进行数字编码，使用数字对离散型的取值进行表示。
          </el-text>
          <el-text class="original_text">数字编码方法是从0开始赋予特征的每一个取值一个整数。对于等级型特征，按照特征取值从小到大进行整数编码可以保证编码后的数据保留原有次序关系。例如对于特征
            “收入水平”={贫困，低收入，小康，中等收入，富有}，可以将其数字编码后转换成”收入水平“= {0, 1, 2, 3, 4}。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 13" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对数据集中某一列的类型进行转换。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 需要转换的列：选取要进行类型转换的列，单选</el-text>
          <el-text class="right_text_bottom">●
            转换为：选取需要转换成的数据类型，包括整型（int32，int64）,浮点型（float32，float64），字符型（object），布尔型（bool）和datetime时间类型（datetime64）。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出将选择列进行转换后的数据对象，转换后的列名为原列名_trans。
          </el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">节点报告显示转换后的数据集的数据预览。</el-text>
          <el-image :src="photo13" class="images" style="width: 500px; height: 400px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            当我们处理数据的时候，经常会遇到数据类型不匹配的问题。所以，在我们进行处理数据之前，首先要进行确定的便是数据的类型是正确的，如果不正确，就需要进行数据类型的转化。
          </el-text>
          <el-text class="original_text">
            数据能转化的类型是Python数据处理包Pandas所能处理的数据类型来确定的，整数数据类型有int32和int64，浮点型数据有float32和float64，object类型代表字符串类型，bool为布尔值类型，datetime64为日期时间类型。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 14" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对某些数据字段进行重命名操作。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 需要重命名的列：选择对哪些数据列进行重命名，单选。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回数据字段重命名后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回数据字段重命名后的数据对象。</el-text>
          <el-image :src="photo14" class="images" style="width: 700px; height: 340px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            某些时候，原有的数据集的数据字段标签所代表的含义并不直观，或者在我们进行字符串分割等操作后衍生出了新的数据字段，为了便于我们识别这些字段，可以利用数据字段重命名组件把字段更改成我们想要的名字。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 15" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对数据中某列进行加、减、乘、除、乘方、开方运算。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 计算列：选取需要进行计算的列，单选。</el-text>
          <el-text class="right_text">● 计算类型：从加、减、乘、除、乘方、开方中选择一种计算方式。</el-text>
          <el-text class="right_text_bottom">● 计算值：输入数值，可根据所选的计算类型进行相应的运算。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回添加计算结果列的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">
            返回数据集并添加计算结果一列，如下图将SepalLength一列加5，结果自动添加为SepalLength_cal列。
          </el-text>
          <el-image :src="photo15" class="images" style="width: 500px; height: 370px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">在部分数据分析的场景中，需要对数据列执行加减乘除等计算操作，辅助后续的分析工作。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 16" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">指定一个或多个字段，批量替换数据中的某些值为指定值。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 替换列：选择一个数据字段，以对其中的值进行批量替换。</el-text>
          <el-text class="right_text">● 替换方式：可选择替换值的输入方式。可选单值替换或列表替换。</el-text>
          <el-text class="right_text">● 被替换值：输入原数据中的一个或一组数据。</el-text>
          <el-text class="right_text_bottom">● 替换值：输入相应的一个或一组替换后的数据。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回值替换后得到的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回值替换后得到的数据对象。</el-text>
          <el-image :src="photo16" class="images" style="width: 700px; height: 340px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            单值替换会将被替换值中的值替换为替换值。列表替换要求输入两个等长的列表，依次将被替换值中输入的列表中的值，替换为替换值中输入的列表中的值。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 17" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">
            对数据中某列的缺失值进行填补，可以对均值、中位数、众数进行填补或指定值进行填补。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 填补列：选择需要进行缺失值填补的数据列。</el-text>
          <el-text class="right_text">● 缺失值：填写缺失值的形式，不填写则为空，系统自动处理为NaN。</el-text>
          <el-text class="right_text">●
            填补策略：可选择均值、中位数、众数或指定值对缺失值进行填补，请根据填补列的数据类型选择合适的填补策略。
          </el-text>
          <el-text class="right_text_bottom">●
            填补值：填补策略选择指定值时弹出，输入指定值进行填补，注意保证输入值的数据类型和填补列的数据类型保持一致。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回填补后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text_bottom">返回填补后的数据表格，直接在填补列的缺失值处进行填补，不创建新的数据列。
          </el-text>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="right_text">●
            数据缺失是指在数据收集、传输和处理等过程中，由于某些原因导致数据不完整的情况。缺失值的存在会给数据的统计带来问题。面对数据缺失的情况，有两类处理办法：删除法和填补法。
          </el-text>
          <el-text class="right_text">●
            删除法通过删除包括缺失值的数据，来得到一个完整的数据子集，适用于缺失值占比较小的情况。填补法的思想是采用某种方法对缺失值进行填补。例如对于连续型特征，使用均值进行填补，对于离散型特征，使用众数进行填补。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 18" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">将数据集依照某列取值进行排序。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 排序列：选取按照哪一列对数据集进行排序，可扩展选择多列。</el-text>
          <el-text class="right_text_bottom">● 是否降序排列：默认为否，按照升序排序，选择是，按照升序排序。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回排序后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回排序后的数据对象。</el-text>
          <el-text class="original_text">原数据，排序列为SepalLength：</el-text>
          <el-image :src="photo18_1" class="images" style="width: 500px; height: 400px"/>
          <el-text class="original_text">降序排列结果：</el-text>
          <el-image :src="photo18_2" class="images" style="width: 500px; height: 350px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            数据排序是数据分析的一种常用方法，排序将一个“无序”的数据集调整为“有序”的数据集，得到最符合分析要求的结果，从排序后的数据集中也更易发现数据间的规律。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 19" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">OneHot编码将包含k个取值的离散型特征转换为k个二元特征。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 编码列：选择需要进行One-Hot编码的数据列。</el-text>
          <el-text class="right_text_bottom">●
            删除首个取值：是否删除转换后的第一个二元特征，默认为否；若选择是，假设原数据列有k个不同取值，OneHot编码后转换为k−1个二元特征列，也称为哑编码（dummy
            encoding）。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回转换后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">
            对编码后的数据进行预览，编码后的列位于最后。假设编码列为class，有3种取值分别为“Iris-setosa”，“Iris-versicolor”和"Iris-virginica"。原数据如下图所示：
          </el-text>
          <el-image :src="photo19_1" class="images" style="width: 500px; height: 120px; margin-bottom: 10px"/>
          <el-text class="original_text">则不同情况下的节点报告如下所示：</el-text>
          <el-text class="original_text" style="font-weight: bold;">（1）不删除首个取值：</el-text>
          <el-image :src="photo19_2" class="images" style="width: 500px; height: 350px; margin-bottom: 10px"/>
          <el-text class="original_text" style="font-weight: bold;">（2）删除首个取值：</el-text>
          <el-image :src="photo19_3" class="images" style="width: 500px; height: 350px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            OneHot编码是将无序离散型特征转换为机器学习算法易于利用的一种形式的过程。将包含k个取值的无序离散型特征转换成k个二元特征（取值为0或1）。经过OneHot编码之后，不同的原始特征取值之间拥有相同的距离。
          </el-text>
          <el-text class="original_text">
            但随着特征显著增多，会增加特征之间的相关性。哑编码将包含k个取值的离散型特征转换成k-1个二元特征（取值为0或1），解决了OneHot编码特征之间存在线性关系的问题，避免特征编码对线性回归等模型的影响。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 20" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">将原始数据进行Z-Score标准化变换，使变换后数据的均值为0，标准差为1。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 处理列：选择希望进行转换的数据列，可选多个。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出进行标准化之后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">节点报告展示两部分内容：一是标准化后的数据预览；二是原数据中各特征的均值和标准差。假设我们选择鸢尾花数据集
            ，原数据预览如下图：
          </el-text>
          <el-image :src="photo20_1" class="images" style="width: 500px; height: 200px"/>
          <el-text class="original_text">对四个数值特征进行Z-Score标准化，得到的节点报告如下：</el-text>
          <el-image :src="photo20_2" class="images" style="width: 500px; height: 500px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">Z-Score标准化是最常用的标准化方法。
            该方法通过对数据集中的每一个样本进行处理，使得处理后的数据具有固定均值和标准差。
          </el-text>
          <el-text class="original_text">
            经过Z-score标准化后的特征能够直观反应每一个取值距离平均值的标准差距离，从而理解特征的整体分布情况。特征的均值落在0附近，而每一个样本离0的距离可解释为其值远离均值的标准差距离。
          </el-text>
          <el-text class="original_text">Z-Score标准化适用于特征的最大值或最小值未知和样本分布非常分散的情况。</el-text>
        </el-space>
        <el-space v-if="pageId == 21" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">Min-Max标准化通过对特征作线性变换，使得转换后特征的取值分布在
            [0,1]区间内。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 处理列：选取想要标准化的数据列，可选多个。</el-text>
          <el-text class="right_text">● 最小值：输入进行Min-Max标准化的下限，默认为0。</el-text>
          <el-text class="right_text_bottom">● 最大值：输入进行Min-Max标准化的上限，默认为1。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出进行标准化之后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">
            返回进行标准化之后的数据表，如下图，对SepalLength，SepalWidth，PetalLength和PetalWidth四列进行Min-Max标准化，将取值缩放到
            [0,1] 之间。
          </el-text>
          <el-image :src="photo21" class="images" style="width: 500px; height: 370px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">Min-Max标准化通过对特征作线性变换，使得转换后特征的取值分布在[0,1]区间内。
          </el-text>
          <el-text class="original_text">Min-Max标准化适用于需要将特征取值简单地线性映射到某一区间中的情形。
            其不足之处在于当数据集中有新数据加入时，特征的最大值或最小值会发生变化。 此时需要计算新的最小值和最大值，并将之前的数据重新进行标准化操作。
            Min-Max标准化由于需要计算特征取值的最小值和最大值，因此当数据存在离群值时，标准化后的效果较差。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 22" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">Logistic标准化利用Logistic函数的特性，将特征取值映射到 (0,1) 区间内。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 处理列：选取想要标准化的数据列，可选多个。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出进行标准化之后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">节点报告展示标准化后的数据预览。假设我们选择 鸢尾花数据集 ，原数据预览如下图：
          </el-text>
          <el-image :src="photo22_1" class="images" style="width: 500px; height: 200px"/>
          <el-text class="original_text">对四个数值特征进行Logistic标准化，得到的节点报告如下：</el-text>
          <el-image :src="photo22_2" class="images" style="width: 500px; height: 370px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">Logistic函数是皮埃尔·弗朗索瓦·韦吕勒(Pierre François
            Verhulst)在研究人口增长时发明的。Logistic函数图像如下：
          </el-text>
          <el-image :src="photo22_3" class="images" style="width: 500px; height: 250px"/>
          <el-text class="original_text">Logistic标准化方法适用于数据列取值分布相对比较集中的情况。如果数据列取值分散且均远离
            0，那么标准化后的数据列取值会聚集于 0 或 1 附近, 造成原始数据列的分布及取值间关系被改变。因此在应用Logistic标准化方法之前，需要首先分析原始数据列取值的分布状况。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 23" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">使用最大绝对值方法对特征进行标准化变换。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 处理列：选取想要标准化的数据列，可选多个。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出进行标准化之后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回进行标准化之后的数据对象，并分析所选标签列的数据分布。假设我们选择 鸢尾花数据集
            ，原数据预览如下图：
          </el-text>
          <el-image :src="photo23_1" class="images" style="width: 500px; height: 200px"/>
          <el-text class="original_text">对四个数值特征进行最大绝对值标准化，得到的节点报告如下：</el-text>
          <el-image :src="photo23_2" class="images" style="width: 500px; height: 370px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            最大绝对值标准化通过除以特征f每个取值最大绝对值从而把特征变换到闭区间[−1,1]中，不会平移整个分布，也不会破坏原来每一个特征向量的稀疏性。
          </el-text>
          <el-text class="original_text">
            例如有特征取值为[−1000,100,10]，最大绝对值为1000，转换为[−1000/1000,100/1000,10/1000]=[−1,0.1,0.01]。如果最大绝对值是一个离群点，显然这种处理方式是很不合理的。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 24" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">根据连续型数据的取值，将其均匀地划分为若干区间，每个区间的宽度相等。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 处理列：可选参数，选择需要进行等距离散化的数据列。</el-text>
          <el-text class="right_text_bottom">● 分段数：输入参数，将数据列分为几组。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出离散化后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">
            直接在处理列上进行离散化，不创建新的数据列，每一组分配一个标签，属于这组的数据直接由标签进行替换，返回离散化后的数据表格对象以及每组分配标签的对照表。
          </el-text>
          <el-image :src="photo24" class="images" style="width: 500px; height: 500px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            等距离散化是最早的数据离散化方法之一，它根据连续型数据的取值，将其均匀地划分为k个区间，每个区间的宽度均相等，然后将数据的取值划入对应的区间从而完成数据离散化。用f表示需要进行离散化的连续型数据，通过数据的最大值和最小值计算出区间段的宽度。
          </el-text>
          <el-text class="original_text">
            根据区间宽度，以及数据的最大值、最小值，可以找到k−1个切分点，从而完成数据离散化的过程。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 25" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">将原始数据进行等频离散化处理。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text_bottom">● 处理列：可选参数，选取想要转化的数据列。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出离散化后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回进行离散化之后的数据对象以及分组区间与标签的对照表。</el-text>
          <el-image :src="photo25" class="images" style="width: 500px; height: 500px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            在数据清洗和预处理过程中，有时我们需要适当地对数据集进行离散化处理。等频离散化是将相同数量的记录放在每个区间，保证每个区间的数量基本一致。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 26" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">
            应用KMeans聚类方法对数据列的取值进行聚类，根据聚类结果对数据列进行离散化。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 处理列：可选参数，选取想要转化的数据列。</el-text>
          <el-text class="right_text_bottom">● 分段数：输入参数，输入需要划分的区间段的数量。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出离散化后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回离散化后的数据对象及所选列划分的区间段和对应的区间取值。</el-text>
          <el-image :src="photo26" class="images" style="width: 500px; height: 500px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            KMeans离散化是基于聚类的离散化，属于无监督离散化方法。在离散化连续型数据的时候，如果相似的样本都能落在相同的区间段内，那么这样的划分可以更好地代表原始数据的信息。
            而聚类正是将样本划分到不同的类或者簇的一个过程。聚类的结果是同一个簇中的样本有很大的相似性，不同簇间的样本则有很大的差异性。如何选定簇的个数也会影响聚类算法的效果，从而影响数据的离散化。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 27" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">
            卡方离散化是一种有监督的离散化方法，递归式地将卡方值最小的相邻区间进行合并。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 处理列：可选参数，选取想要转化的数据列。</el-text>
          <el-text class="right_text">● 标签列：用于计算卡方值的标签（为离散型变量），单选。</el-text>
          <el-text class="right_text_bottom">● 最大分箱数：默认为10。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出离散化后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">
            第一个表格为已进行卡方离散化的数据对象，第二个表格为分箱时的区间及对应的区间取值。
          </el-text>
          <el-image :src="photo27" class="images" style="width: 500px; height: 500px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="right_text">● 基于卡方独立性检验，计算处理列和标签列的频数列联表。</el-text>
          <el-text class="right_text">●
            初始时，将处理列的取值作为分箱边界，计算所有相邻分箱的卡方值，卡方值小说明两分箱内的数据分布相似。
          </el-text>
          <el-text class="right_text">●
            递归地合并卡方值最小的一对相邻区间，直到区间数小于最大分箱数或卡方值小于给定阈值（置信度为95%对应的卡方拟合优度临界值）。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 28" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">本组件基于决策树模型进行离散化，是一种有监督的离散化方法。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 处理列：可选参数，选取想要转化的数据列。</el-text>
          <el-text class="right_text">● 标签列：用于计算卡方值的标签（为离散型变量），单选。</el-text>
          <el-text class="right_text">● 最大分箱数：默认为10。</el-text>
          <el-text class="right_text_bottom">●
            模型类型：若标签列为定类变量，应选择“分类”，调用分类决策树；若标签列为连续变量，应选择“回归”，调用回归决策树。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出离散化后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">
            第一个表格为已进行决策树离散化的数据对象，第二个表格为分箱时的区间及对应的区间取值。
          </el-text>
          <el-image :src="photo28" class="images" style="width: 500px; height: 500px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            决策树离散化通过特征的分裂来创建箱或区间，是一种有监督离散化方法。基本思想是使用决策树来确定箱子或连续间隔的最佳分裂点。
          </el-text>
          <el-text class="original_text">
            首先根据需要离散化的列训练一个有限深度的决策树来预测标签列。随后将原始变量值替换为树返回的概率。每个箱内的所有观测值的概率相同，因此用概率替换相当于将决策树决定的截止值内的观测值分组。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 29" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">利用主成分分析法对数据进行降维。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：选取要进行降维处理的特征，至少选择2个。</el-text>
          <el-text class="right_text_bottom">●
            维数：降维之后的保留主成分的个数，注意，保留主成分的个数需要小于等于选择的特征列的数量。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回主成分分析降维之后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回降维处理后的结果、主成分得分矩阵以及解释方差比的柱形图。</el-text>
          <el-image :src="photo29_1_1" class="images" style="width: 500px; height: 500px; margin-bottom: 0px"/>
          <el-image :src="photo29_1_2" class="images" style="width: 500px; height: 350px; margin-top: 0px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">主成分分析(Principal Component Analysis，PCA)是由著名统计学家卡尔·皮尔逊(Karl
            Pearson)于1901年提出的线性降维方法。 它在人脸识别、图像压缩等领域得到了广泛的应用。 在主成分分析中，信息的重要性是通过方差来表示的。
            因而它的基本思想是：构造原始特征的一系列线性组合形成低维的特征，以去除数据的相关性，并使降维后的数据最大程度地保持原始高维数据的方差信息。
          </el-text>
          <el-text class="original_text">我们首先通过一个简单的例子来理解PCA的思想。
            假设原始数据集包含两个特征x1和x2，原始数据集的散点图如图所示。
          </el-text>
          <el-image :src="photo29_2" class="images" style="width: 500px; height: 400px; margin-bottom: 10px"/>
          <el-text class="original_text">现在，我们需要将数据降低到一维，即找到一个方向，使得在该方向上原始数据经过投影后的方差最大。
            直观来看，图中直线的方向就是我们需要的方向。 这是PCA的第一种表达方式，即降维后数据的方差最大。
          </el-text>
          <el-image :src="photo29_3" style="width: 800px; height: 600px; margin-left: 30px"/>
        </el-space>
        <el-space v-if="pageId == 30" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">线性判别分析（Linear Discriminant Analysis,
            LDA）是一种经典的有监督线性降维方法。基本思想是利用样本的类别信息，找到数据的线性低维表示，使得低维数据表示更有利于对数据进行分类。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：选取要进行降维处理的特征。</el-text>
          <el-text class="right_text">● 目标列：可选参数，选择表示样本类别信息的标签列。</el-text>
          <el-text class="right_text_bottom">● 维数：输入参数，指定希望降维后的特征维度数目。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，输出降维后的数据对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回降维后的数据对象，及降维后主成分的方差贡献率图。</el-text>
          <el-image :src="photo30_1" class="images" style="width: 500px; height: 380px; margin-bottom: 0px"/>
          <el-image :src="photo30_2" class="images" style="width: 500px; height: 320px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="right_text">●
            LDA利用样本的类别信息，找到数据的线性低维表示，使得低维表示最有利于数据进行分类。这个目标可以从两个角度来量化。第一个角度是使得降维后相同类样本尽可能近。这可以使用类内样本的方差来定量表示，也称为类内离散度。第二个角度是使得降维后不同类样本尽可能远，这可以使用不同类样本的均值的方差定量表示，也称为类间离散度。
          </el-text>
          <el-text class="right_text">●
            线性判别分析是一种有监督的线性降维方法。它既能作为一种降维方法，也能作为一种分类算法。LDA能够找到最有利于对数据分类的特征，因此也可以作为分类问题的特征选择方法。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 31" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对数据进行线性回归建模。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取有监督数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取有监督数据集样本中的标签列。</el-text>
          <el-text class="right_text">●
            训练截距项：可选参数，默认为是，是否计算此模型的截距。如果设置为否，则在计算中不使用任何截距（即数据已经中心化）。
          </el-text>
          <el-text class="right_text_bottom">●
            数据归一化：可选参数，默认为否，是否将选取的特征列进行归一化。当训练截距项设置为否时，该参数将被忽略。如果为是，则回归因子X将在回归之前归一化。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回建模后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回线性回归建模后的模型的参数。</el-text>
          <el-image :src="photo31_1" class="images" style="width: 500px; height: 220px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-image :src="photo31_2" style="width: 800px; height: 360px; margin-left: 30px"/>
        </el-space>
        <el-space v-if="pageId == 32" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">
            L1正则化的线性回归模型，能得到稀疏的回归系数。它在某些情况下很有用，因为它倾向于选择非零系数较少的解，有效地减少了给定解所依赖的特征数。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取有监督数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取有监督数据集样本中的标签列。</el-text>
          <el-text class="right_text">● 正则系数：输入参数，初始值为1，数值越大则对复杂模型的惩罚力度越大。</el-text>
          <el-text class="right_text">●
            训练截距项：可选参数，默认为是，是否计算此模型的截距。如果设置为否，则在计算中不使用任何截距（即数据已经中心化）。
          </el-text>
          <el-text class="right_text_bottom">●
            数据归一化：可选参数，默认为否，是否将选取的特征列进行归一化。当训练截距项设置为否时，该参数将被忽略。如果为是，则回归因子X将在回归之前归一化。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回建模后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回各特征的系数，及模型学习到的截距。</el-text>
          <el-image :src="photo32_1" class="images" style="width: 500px; height: 220px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">LASSO (Least Absolute Shrinkage and Selection
            Operator)是一种线性回归正则化方法。正则化是一种通过在模型中添加一些惩罚项或约束条件来控制模型复杂度，来减轻过度拟合的方法。LASSO
            的解没有解析表达式，但能得到稀疏的回归系数，即很多分量非常接近 0。因此，LASSO模型得到的结果可以帮助我们做特征选择。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 33" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对数据进行岭回归建模。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取有监督数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取有监督数据集样本中的标签列。</el-text>
          <el-text class="right_text">● 正则系数：输入参数，初始值为1，数值越大则对复杂模型的惩罚力度越大。</el-text>
          <el-text class="right_text">●
            训练截距项：可选参数，默认为是，是否计算此模型的截距。如果设置为否，则在计算中不使用任何截距（即数据已经中心化）。
          </el-text>
          <el-text class="right_text_bottom">●
            数据归一化：可选参数，默认为否，是否将选取的特征列进行归一化。当训练截距项设置为否时，该参数将被忽略。如果为是，则回归因子X将在回归之前归一化。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回建模后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回各特征的系数，及模型学习到的截距。</el-text>
          <el-image :src="photo33_1" class="images" style="width: 500px; height: 220px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-image :src="photo33_2" style="width: 800px; height: 300px; margin-left: 30px"/>
        </el-space>
        <el-space v-if="pageId == 34" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">
            同时使用l1正则化和l2正则化的线性回归模型。既有Lasso的稀疏性，也保留了岭回归的稳定性。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取有监督数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取有监督数据集样本中的标签列。</el-text>
          <el-text class="right_text">● l1正则系数：输入l1正则化系数，初始值为0.5，数值越大则对模型的正则化力度越大。
          </el-text>
          <el-text class="right_text">● l2正则系数：输入l2正则化系数，初始值为0.5，数值越大则对模型的正则化力度越大。
          </el-text>
          <el-text class="right_text">●
            训练截距项：可选参数，默认为是，是否计算此模型的截距。如果设置为否，则在计算中不使用任何截距（即数据已经中心化）
          </el-text>
          <el-text class="right_text_bottom">●
            数据归一化：可选参数，默认为否，是否将选取的特征列进行归一化。当训练截距项设置为否时，该参数将被忽略。如果为是，则回归因子X将在回归之前归一化。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回建模后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回各特征的系数，及模型学习到的截距。</el-text>
          <el-image :src="photo34_1" class="images" style="width: 500px; height: 220px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">弹性网络（Elastic Net）综合了岭回归和LASSO的正则化方式，呈现出一个特征分组的效果。即高度相关的特征对应的回归系数倾向于相等
            (对于负相关的特征，系数有符号差别)。它克服了LASSO在这方面的缺点，在微阵列分类和基因选择中得到了成功的应用。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 35" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对数据进行K近邻回归建模。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取有监督数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取有监督数据集样本中的标签列。</el-text>
          <el-text class="right_text">● 邻居个数：输入参数，默认为1，为正则化项前的系数，需大于零。</el-text>
          <el-text class="right_text">●
            权重计算方式：可选参数，默认为uniform，指定权重计算的方式。uniform为统一权重，每个邻域中的所有点的权重相等；distance依据点间距离的倒数计算权重，点的较近邻居将比较远的邻居具有更大的影响。
          </el-text>
          <el-text class="right_text">● 距离计算方式：距离度量的计算方法，默认为 euclidean 距离（欧氏距离）。可选的计算方式还有
            manhattan 距离、minkowski 距离和 chebyshev 距离，并且选择 minkowski 距离时可选择幂的大小。
          </el-text>
          <el-text class="right_text_bottom">● 幂（p）：minkowski 度量的幂参数，默认为2。当 p = 1 时，等价于使用 manhattan
            距离，p = 2 时使用 euclidean 距离。对于任意 p，使用 minkowski 距离的p次幂。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回建模后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回K近邻回归建模后的模型的参数。</el-text>
          <el-image :src="photo35_1" class="images" style="width: 500px; height: 220px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">K近邻（K-Nearest Neighbor,
            KNN）算法是一种简单且有效的有监督学习方法，当对数据的分布只有很少或者没有任何先验知识时，K近邻算法是一个不错的选择。
          </el-text>
          <el-text class="original_text">
            K近邻算法的基本原理为：当对测试样本进行回归时，首先扫描训练集，找到与该测试样本最相似的k个训练样本，根据这k个样本的类别进行计算确定测试样本的回归值。
          </el-text>
          <el-text class="original_text">K近邻回归算法的具体步骤如下：</el-text>
          <el-text class="right_text">1. 确定K的大小和距离计算的方法；</el-text>
          <el-text class="right_text">2. 从训练样本中得到K个与测试样本最相似的样本；</el-text>
          <el-text class="right_text">3.
            根据K个最相似训练样本的目标值，通过计算这些样本的平均目标值确定测试样本的目标值。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 36" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">使用CART算法，训练回归决策树模型。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取有监督数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取有监督数据集样本中的标签列。</el-text>
          <el-text class="right_text">● 最大树深度：输入参数，设定决策树的最大深度。</el-text>
          <el-text class="right_text">●
            节点分裂最小样本数：输入参数，一个节点在分枝后的每个子节点都必须包含的最小样本数量。
          </el-text>
          <el-text class="right_text_bottom">● 叶节点最小样本数：输入参数，一个节点必须包含的最小样本数量。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回建模后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回各个特征对模型重要性的条形图。</el-text>
          <el-image :src="photo36_1" class="images" style="width: 500px; height: 350px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            决策树是通过一系列问题的诊断结果来进行决策的。决策树的生成一般是从根节点开始，选择对应特征；然后选择该节点特征的分裂点，根据分裂点分裂节点。对于离散型特征，节点根据特征取值进行分裂；如根节点特征为“收入”，则根据其取值“高“、”中等“和”低“根节点分裂成三个子节点。对于连续型特征，则需要根据具体特征值(分裂点)来分裂子节点。一般而言，当某一个节点中数据只属于某类别(分类问题)
            或者方差较小(回归问题) 时，节点则不再分裂。
          </el-text>
          <el-text class="original_text">
            决策树生成的核心问题为：如何选择节点特征和特征分裂点。决策树分裂节点的目标是使得节点分裂前后，样本的类别分布更加不均衡，也就是不纯度需要降低。因此我们选择使得节点分裂前后，不纯度下降最大的特征和分裂点。不纯度用来表示落在当前节点的样本的类别分布的均衡程度。
          </el-text>
          <el-text class="original_text">
            决策树算法有可能会产生过于复杂的树(例如树的层数太多、树的节点数过多等)，从而使得学习到的决策树模型在测试集上的效果不理想，即容易产生过拟合问题。如果我们学习到了过于复杂的树，可以通过剪枝(pruning)
            策略来对树的复杂性进行控制。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 37" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对数据进行朴素贝叶斯分类建模。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 贝叶斯分类器：选择要使用的贝叶斯分类模型，默认为BernoulliNB。</el-text>
          <el-text class="right_text">●
            平滑参数：输入参数，设置平滑项，默认为1.0。当贝叶斯分类器选择BernoulliNB、MultinomialNB和CategoricalNB时可进行设置。附加平滑参数，设置为0时不平滑，为1时为拉普拉斯平滑。
          </el-text>
          <el-text class="right_text">●
            学习先验概率：选择是否进行先验概率的学习，默认为是。当贝叶斯分类器选择BernoulliNB、MultinomialNB和CategoricalNB时可进行设置。
            如果选择否，将使用统一先验概率。
          </el-text>
          <el-text class="right_text">●
            二值化阈值：输入参数，设置样本特征二值化（映射到布尔值）的阈值，默认为1.0。当贝叶斯分类器选择BernoulliNB时可进行设置。如果没有，则假定输入已经由二进制向量组成。
          </el-text>
          <el-text class="right_text_bottom">● 最小类别数：输入参数，设置每个特征的最小类别数，默认为1。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回朴素贝叶斯建模之后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回朴素贝叶斯建模后的模型的参数。</el-text>
          <el-image :src="photo36_1" class="images" style="width: 500px; height: 350px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-image :src="photo37_2" style="width: 800px; height: 400px; margin-left: 30px"/>
        </el-space>
        <el-space v-if="pageId == 38" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">使用数据集训练线性SVC模型。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取数据集样本中的标签列。</el-text>
          <el-text class="right_text">● 正则化系数：输入参数，默认为1，为正则化项前的系数，需大于零。</el-text>
          <el-text class="right_text">● 最小收敛数：输入参数，默认为0.0001，指定终止迭代的阈值。</el-text>
          <el-text class="right_text">● 最大迭代数：输入参数，默认为1000，指定要运行的最大迭代次数。</el-text>
          <el-text class="right_text_bottom">●
            训练截距项：可选参数，默认为是，是否计算此模型的截距。如果设置为否，则在计算中不使用任何截距（即数据已经中心化）。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回建模后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回线性SVC建模所得到的模型的参数。</el-text>
          <el-image :src="photo38_1" class="images" style="width: 500px; height: 300px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-image :src="photo38_2" style="width: 800px; height: 450px; margin-left: 30px"/>
        </el-space>
        <el-space v-if="pageId == 39" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">
            SVM学习的基本想法是求解能够正确划分训练数据集并且几何间隔最大的分离超平面。
          </el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：输入支持向量机的特征（自变量X），多选。</el-text>
          <el-text class="right_text">● 标签列：支持向量机需要学习的标签，因变量y。</el-text>
          <el-text class="right_text">● 训练错误率上限：为0-1之前的浮点数，默认值为0.5。</el-text>
          <el-text class="right_text">● 核函数：支持向量机所使用的核函数类型，分为poly、sigmoid、rbf三种。</el-text>
          <el-text class="right_text">● gamma：核函数的系数。若为scale，取值为1/(特征树✖X的方差)，若为auto，取值为1/特征数
          </el-text>
          <el-text class="right_text">● degree（仅适用于poly核函数）：多项式度数，默认为3。</el-text>
          <el-text class="right_text">● coef0（适用于sigmoid和poly核函数）：核函数中的独立项，默认为0。</el-text>
          <el-text class="right_text_bottom">● 类别权重：若为None，对所有类别的权重相同；若为Balanced,
            按照类别样本个数进行加权。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回支持向量机模型。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回各类别的支持向量个数和截距。</el-text>
          <el-image :src="photo39_1" class="images" style="width: 500px; height: 250px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-image :src="photo39_2" style="width: 770px; height: 170px; margin-left: 60px"/>
        </el-space>
        <el-space v-if="pageId == 40" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">使用CART算法，训练分类决策树模型。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取有监督数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取有监督数据集样本中的标签列。</el-text>
          <el-text class="right_text">● 最大树深度：输入参数，设定决策树的最大深度。</el-text>
          <el-text class="right_text">●
            节点分裂最小样本数：输入参数，一个节点在分枝后的每个子节点都必须包含的最小样本数量。
          </el-text>
          <el-text class="right_text_bottom">● 叶节点最小样本数：输入参数，一个节点必须包含的最小样本数量。</el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回建模后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回各个特征对模型重要性的条形图。</el-text>
          <el-image :src="photo40_1" class="images" style="width: 500px; height: 350px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">
            决策树是通过一系列问题的诊断结果来进行决策的。决策树的生成一般是从根节点开始，选择对应特征；然后选择该节点特征的分裂点，根据分裂点分裂节点。对于离散型特征，节点根据特征取值进行分裂；如根节点特征为“收入”，则根据其取值“高“、”中等“和”低“根节点分裂成三个子节点。对于连续型特征，则需要根据具体特征值(分裂点)来分裂子节点。一般而言，当某一个节点中数据只属于某类别(分类问题)
            或者方差较小(回归问题) 时，节点则不再分裂。
          </el-text>
          <el-text class="original_text">
            决策树生成的核心问题为：如何选择节点特征和特征分裂点。决策树分裂节点的目标是使得节点分裂前后，样本的类别分布更加不均衡，也就是不纯度需要降低。因此我们选择使得节点分裂前后，不纯度下降最大的特征和分裂点。不纯度用来表示落在当前节点的样本的类别分布的均衡程度。
          </el-text>
          <el-text class="original_text">
            决策树算法有可能会产生过于复杂的树(例如树的层数太多、树的节点数过多等)，从而使得学习到的决策树模型在测试集上的效果不理想，即容易产生过拟合问题。如果我们学习到了过于复杂的树，可以通过剪枝(pruning)
            策略来对树的复杂性进行控制。
          </el-text>
        </el-space>
        <el-space v-if="pageId == 41" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对数据进行逻辑回归建模。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取有监督数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取有监督数据集样本中的标签列。</el-text>
          <el-text class="right_text">● C系数：输入参数，默认为1.0，为正则化系数λ的倒数，C越小，正则化能力越强。</el-text>
          <el-text class="right_text">● 收敛系数：输入参数，默认为0.0001，指定终止迭代的阈值。</el-text>
          <el-text class="right_text">●
            随机种子：输入参数，默认为10，产生随机数的种子，即该组随机数的编号，在重复试验时保证随机数一致。
          </el-text>
          <el-text class="right_text_bottom">●
            类别权重：可选参数，用于标示分类模型中各种类型的权重，通常用于在误分类代价很高或类别不平衡的情况下。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回逻辑回归建模之后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回逻辑回归建模后的模型的参数。</el-text>
          <el-image :src="photo41_1" class="images" style="width: 500px; height: 220px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-image :src="photo41_2" style="width: 800px; height: 300px; margin-left: 30px"/>
        </el-space>
        <el-space v-if="pageId == 42" direction="vertical" style="float: left; align-items: flex-start">
          <el-text class="sub_head">概述</el-text>
          <el-text class="original_text_bottom">对数据进行K近邻分类建模。</el-text>
          <el-text class="sub_head">面板参数说明</el-text>
          <el-text class="right_text">● 特征列：可选参数，选取有监督数据集样本中的特征列，可选多个。</el-text>
          <el-text class="right_text">● 标签列：可选参数，选取有监督数据集样本中的标签列。</el-text>
          <el-text class="right_text">● 邻居个数：输入参数，默认为1，为正则化项前的系数，需大于零。</el-text>
          <el-text class="right_text">●
            权重计算方式：可选参数，默认为uniform，指定权重计算的方式。uniform为统一权重，每个邻域中的所有点的权重相等；distance依据点间距离的倒数计算权重，点的较近邻居将比较远的邻居具有更大的影响。
          </el-text>
          <el-text class="right_text">● 距离计算方式：距离度量的计算方法，默认为 euclidean 距离（欧氏距离）。可选的计算方式还有
            manhattan 距离、minkowski 距离和 chebyshev 距离，并且选择 minkowski 距离时可选择幂的大小。
          </el-text>
          <el-text class="right_text_bottom">● 幂（p）：minkowski 度量的幂参数，默认为2。当 p = 1 时，等价于使用 manhattan
            距离，p = 2 时使用 euclidean 距离。对于任意 p，使用 minkowski 距离的p次幂。
          </el-text>
          <el-text class="sub_head">输入输出桩说明</el-text>
          <el-text class="right_text">● 输入桩：1个，连接数据对象。</el-text>
          <el-text class="right_text_bottom">● 输出桩：1个，返回K近邻分类建模之后的模型对象。</el-text>
          <el-text class="sub_head">节点报告说明</el-text>
          <el-text class="original_text">返回K近邻分类建模后的模型的参数。</el-text>
          <el-image :src="photo42_1" class="images" style="width: 500px; height: 220px"/>
          <el-text class="sub_head">原理说明</el-text>
          <el-text class="original_text">K近邻（K-Nearest Neighbor,
            KNN）算法是一种简单且有效的有监督学习方法，当对数据的分布只有很少或者没有任何先验知识时，K近邻算法是一个不错的选择。
          </el-text>
          <el-text class="original_text">
            K近邻算法的基本原理为：当对测试样本进行分类时，首先扫描训练集，找到与该测试样本最相似的k个训练样本，根据这k个样本的类别进行投票确定测试样本的类别。
          </el-text>
          <el-text class="original_text">K近邻分类算法的具体步骤如下：</el-text>
          <el-text class="right_text">1. 确定K的大小和距离计算的方法；</el-text>
          <el-text class="right_text">2. 从训练样本中得到K个与测试样本最相似的样本；</el-text>
          <el-text class="right_text">3. 根据K个最相似训练样本的类别，通过投票的方式来确定测试样本的类别。</el-text>
        </el-space>
      </a-layout-content>
    </a-layout>
    </a-col>
  </a-row>
</template>

<script>
import {UserOutlined, LaptopOutlined, NotificationOutlined} from '@ant-design/icons-vue';
import photo1_1 from "../assets/1_1.png"
import photo1_2 from "../assets/1_2.png"
import photo2 from "../assets/2.png"
import photo3 from "../assets/3.png"
import photo4 from "../assets/4.png"
import photo4_2 from "../assets/4_2.png"
import photo4_3 from "../assets/4_3.png"
import photo4_4 from "../assets/4_4.png"
import photo5 from "../assets/5.png"
import photo6 from "../assets/6.png"
import photo7 from "../assets/7.png"
import photo8_1 from "../assets/8_1.png"
import photo8_2 from "../assets/8_2.png"
import photo8_3 from "../assets/8_3.png"
import photo8_4 from "../assets/8_4.png"
import photo9_2 from "../assets/9_2.png"
import photo10 from "../assets/10.png"
import photo11 from "../assets/11.png"
import photo13 from "../assets/13.png"
import photo14 from "../assets/14.png"
import photo15 from "../assets/15.png"
import photo16 from "../assets/16.png"
import photo18_1 from "../assets/18_1.png"
import photo18_2 from "../assets/18_2.png"
import photo19_1 from "../assets/19_1.png"
import photo19_2 from "../assets/19_2.png"
import photo19_3 from "../assets/19_3.png"
import photo20_1 from "../assets/20_1.png"
import photo20_2 from "../assets/20_2.png"
import photo21 from "../assets/21.png"
import photo22_1 from "../assets/22_1.png"
import photo22_2 from "../assets/22_2.png"
import photo22_3 from "../assets/22_3.png"
import photo23_1 from "../assets/23_1.png"
import photo23_2 from "../assets/23_2.png"
import photo24 from "../assets/24.png"
import photo25 from "../assets/25.png"
import photo26 from "../assets/26.png"
import photo27 from "../assets/27.png"
import photo28 from "../assets/28.png"
import photo29_1_1 from "../assets/29_1_1.png"
import photo29_1_2 from "../assets/29_1_2.png"
import photo29_2 from "../assets/29_2.png"
import photo29_3 from "../assets/29_3.png"
import photo30_1 from "../assets/30_1.png"
import photo30_2 from "../assets/30_2.png"
import photo31_1 from "../assets/31_1.png"
import photo31_2 from "../assets/31_2.png"
import photo32_1 from "../assets/32_1.png"
import photo33_1 from "../assets/33_1.png"
import photo33_2 from "../assets/33_2.png"
import photo34_1 from "../assets/34_1.png"
import photo35_1 from "../assets/35_1.png"
import photo36_1 from "../assets/36_1.png"
import photo37_1 from "../assets/37_1.png"
import photo37_2 from "../assets/37_2.png"
import photo38_1 from "../assets/38_1.png"
import photo38_2 from "../assets/38_2.png"
import photo39_1 from "../assets/39_1.png"
import photo39_2 from "../assets/39_2.png"
import photo40_1 from "../assets/40_1.png"
import photo41_1 from "../assets/41_1.png"
import photo41_2 from "../assets/41_2.png"
import photo42_1 from "../assets/42_1.png"

export default {
  name: "Introduction",
  components: {
    UserOutlined,
    LaptopOutlined,
    NotificationOutlined,
  },
  setup() {
    console.log(window.innerWidth)
  },
  data() {
    return {
      pageId: 0,
      menuWidth: window.innerWidth / 6 + 'px',
      id_to_name: {
        1: '读数据表',
        2: '字段基本统计信息',
        3: '查看唯一值及数量',
        4: '数据相关性',
        5: '缺失值检测',
        6: '单变量异常值检测',
        7: '重复值检测',
        8: '样本相似度计算',
        9: '列删除',
        10: '训练/测试集划分',
        11: '数字编码',
        12: '人工数字编码',
        13: '类型转换',
        14: '列重命名',
        15: '数据列计算',
        16: '数据值替换',
        17: '缺失值填补',
        18: '数据按列值排序',
        19: 'OneHot编码',
        20: 'Z-Score标准化',
        21: 'Min-Max标准化',
        22: 'Logistic标准化',
        23: '最大绝对值标准化',
        24: '等距离散化',
        25: '等频离散化',
        26: 'Kmeans离散化',
        27: '卡方离散化',
        28: '决策树离散化',
        29: '主成分分析',
        30: '线性判别分析',
        31: '线性回归',
        32: 'LASSO',
        33: '岭回归',
        34: '弹性网络',
        35: 'K近邻回归',
        36: '回归决策树',
        37: '朴素贝叶斯',
        38: '线性SVC',
        39: '支持向量机',
        40: '分类决策树',
        41: '逻辑回归',
        42: 'K近邻',
      },
      photo1_1,
      photo1_2,
      photo2,
      photo3,
      photo4,
      photo4_2,
      photo4_3,
      photo4_4,
      photo5,
      photo6,
      photo7,
      photo8_1,
      photo8_2,
      photo8_3,
      photo8_4,
      photo9_2,
      photo10,
      photo11,
      photo13,
      photo14,
      photo15,
      photo16,
      photo18_1,
      photo18_2,
      photo19_1,
      photo19_2,
      photo19_3,
      photo20_1,
      photo20_2,
      photo21,
      photo22_1,
      photo22_2,
      photo22_3,
      photo23_1,
      photo23_2,
      photo24,
      photo25,
      photo26,
      photo27,
      photo28,
      photo29_1_1,
      photo29_1_2,
      photo29_2,
      photo29_3,
      photo30_1,
      photo30_2,
      photo31_1,
      photo31_2,
      photo32_1,
      photo33_1,
      photo33_2,
      photo34_1,
      photo35_1,
      photo36_1,
      photo37_1,
      photo37_2,
      photo38_1,
      photo38_2,
      photo39_1,
      photo39_2,
      photo40_1,
      photo41_1,
      photo41_2,
      photo42_1
    }
  },
  methods: {
    changePage(key) {
      this.pageId = key
    }
  },
}
</script>

<style scoped>
.sub_head {
  margin-left: 30px;
  color: black;
  font-size: 20px
}

.original_text {
  margin-left: 30px;
  width: 800px;
  text-align: justify;
}

.original_text_bottom {
  margin-left: 30px;
  text-align: justify;
  width: 800px;
  margin-bottom: 30px
}

.right_text {
  text-align: justify;
  width: 770px;
  margin-left: 60px;
}

.right_text_bottom {
  text-align: justify;
  width: 770px;
  margin-left: 60px;
  margin-bottom: 30px;
}

.images {
  margin-bottom: 30px;
  margin-left: 130px
}
</style>