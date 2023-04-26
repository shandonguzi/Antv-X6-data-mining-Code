<template>
  <a-row>
    <!--  gutter表示水平（col和col之间）和垂直（row和row之间）间隔，span表示每个col在水平方向所占大小（总共24）  -->
    <a-col :span="4">
      <div id="stencil"></div>
    </a-col>
    <a-col :span="15">
      <div id="container"></div>
    </a-col>

    <el-dialog v-model="dialogTableVisible" :title="dialogContent.label"
               v-if="(dialogContent.id != 4) || (dialogContent.id != 10) || (dialogContent.id != 29) || (dialogContent.id != 30) || (dialogContent.id != 36)">

      <!-- 1 -->
      <el-table :data="dialogContent.dataBase.slice(0, 20)" v-if="dialogContent.id == 1" max-height="400px"
                :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 5 -->
      <el-text v-if="dialogContent.id == 5" size="default" style="float: left; margin-bottom: 5px">
        过滤的缺失值行数：{{ dialogContent.hasLossRows }}
      </el-text>

      <!-- 6 -->
      <el-space v-if="dialogContent.id == 6" direction="vertical" style="float: left; align-items: flex-start">
        <el-text>检测到的异常值行数为：{{ dialogContent.queer_data_num }}</el-text>
        <el-text>异常值行预览：</el-text>
      </el-space>
      <el-table :data="dialogContent.result" v-if="dialogContent.id == 6" max-height="400px" style="margin-bottom: 20px"
                :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns" :key="i" :property="item" :label="item"/>
      </el-table>
      <el-text v-if="dialogContent.id == 6" size="default" style="float: left; margin-bottom: 5px">得到数据输出预览：
      </el-text>
      <el-table :data="dialogContent.output.slice(0, 20)" v-if="dialogContent.id == 6" max-height="400px"
                :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns1" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 7 -->
      <el-space v-if="dialogContent.id == 7" direction="vertical" style="float: left; align-items: flex-start">
        <el-text>检测到的重复值行数为：{{ dialogContent.repeat_data_num }}</el-text>
        <el-text>重复行预览：</el-text>
      </el-space>

      <!-- 11 -->
      <el-table :data="dialogContent.output.slice(0, 20)" v-if="dialogContent.id == 11" max-height="400px"
                style="margin-bottom: 20px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns1" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 20 -->
      <el-table :data="dialogContent.output.slice(0, 20)" v-if="dialogContent.id == 20" max-height="400px"
                style="margin-bottom: 20px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns1" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 24 -->
      <el-table :data="dialogContent.output.slice(0, 20)" v-if="dialogContent.id == 24" max-height="400px"
                style="margin-bottom: 20px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns1" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 25 -->
      <el-table :data="dialogContent.output.slice(0, 20)" v-if="dialogContent.id == 25" max-height="400px"
                style="margin-bottom: 20px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns1" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 26 -->
      <el-table :data="dialogContent.output.slice(0, 20)" v-if="dialogContent.id == 26" max-height="400px"
                style="margin-bottom: 20px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns1" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 27 -->
      <el-table :data="dialogContent.output.slice(0, 20)" v-if="dialogContent.id == 27" max-height="400px"
                style="margin-bottom: 20px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns1" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 28 -->
      <el-table :data="dialogContent.output.slice(0, 20)" v-if="dialogContent.id == 28" max-height="400px"
                style="margin-bottom: 20px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns1" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 30 -->
      <el-text v-if="dialogContent.id == 30" size="default" style="float: left; margin-bottom: 5px">降维数据：</el-text>

      <!-- 31、32、33 -->
      <el-space v-if="[31, 32, 33, 34].includes(dialogContent.id)" direction="vertical"
                style="float: left; align-items: flex-start">
        <el-text size="default">截距：</el-text>
        <el-text size="default">{{ dialogContent.intercept }}</el-text>
        <el-text size="default" style="margin-top: 20px">系数：</el-text>
      </el-space>
      <el-table :data="dialogContent.result" v-if="[31, 32, 33, 34].includes(dialogContent.id)" max-height="400px"
                :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 35、37、42 -->
      <el-text v-if="[35, 37, 42].includes(dialogContent.id)" size="default" style="float: left; margin-bottom: 5px">
        参数列表：
      </el-text>

      <!-- 38 -->
      <el-text v-if="dialogContent.id == 38" size="default" style="float: left; margin-bottom: 5px">系数：</el-text>
      <el-table :data="dialogContent.coef" v-if="dialogContent.id == 38" max-height="400px"
                :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.coefDataColumns" :key="i" :property="item" :label="item"/>
      </el-table>
      <el-text v-if="dialogContent.id == 38" size="default" style="float: left; margin-top: 20px; margin-bottom: 5px">
        截距：
      </el-text>

      <!-- 39 -->
      <el-text v-if="dialogContent.id == 39" size="default" style="float: left; margin-bottom: 5px">支持向量个数：
      </el-text>
      <el-table :data="dialogContent.n_support" v-if="dialogContent.id == 39" max-height="400px"
                :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.n_supportDataColumns" :key="i" :property="item"
                         :label="item"/>
      </el-table>
      <el-text v-if="dialogContent.id == 39" size="default" style="float: left; margin-top: 20px; margin-bottom: 5px">
        截距：
      </el-text>

      <!-- 41 -->
      <el-text v-if="dialogContent.id == 41" size="default" style="float: left; margin-bottom: 5px">系数：</el-text>

      <!-- 需要限制前20行的输出 -->
      <el-table :data="dialogContent.result.slice(0, 20)"
                v-if="[3, 7, 9, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23].includes(dialogContent.id)"
                max-height="400px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns" :key="i" :property="item" :label="item"/>
      </el-table>

      <!-- 无限制输出 -->
      <el-table :data="dialogContent.result"
                v-if="[2, 5, 8, 11, 20, 24, 25, 26, 27, 28, 35, 37, 38, 39, 41, 42].includes(dialogContent.id)"
                max-height="400px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns" :key="i" :property="item" :label="item"/>
      </el-table>

    </el-dialog>


    <el-dialog v-model="dialogTableVisible"
               :visible.sync="dialogTableVisible"
               :title="dialogContent.label"
               v-if="dialogContent.id == 4"
               @opened="openId4">
      <el-table :data="dialogContent.result" style="margin-bottom: 20px"
                max-height="400px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns" :key="i" :property="item" :label="item"/>
      </el-table>
      <el-text size="default" style="float: left; font-weight: bold">热力图：</el-text>
      <div id="relation_heatmap" style="width: 100%; height: 300px; margin-top: 50px"></div>
    </el-dialog>

    <el-dialog v-model="dialogTableVisible"
               :visible.sync="dialogTableVisible"
               :title="dialogContent.label"
               v-if="dialogContent.id == 10"
               @opened="openId10">
      <div id="pie_10" style="width: 600px; height: 400px; margin: auto"></div>
    </el-dialog>

    <el-dialog v-model="dialogTableVisible"
               :visible.sync="dialogTableVisible"
               :title="dialogContent.label"
               v-if="dialogContent.id == 29"
               @opened="openId29">
      <el-text size="default" style="float: left; margin-bottom: 5px">降维数据：</el-text>
      <el-table :data="dialogContent.output.slice(0, 20)" max-height="400px"
                style="margin-bottom: 20px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns1" :key="i" :property="item" :label="item"/>
      </el-table>
      <el-text size="default" style="float: left; margin-bottom: 5px">PCA主成分：</el-text>
      <el-table :data="dialogContent.result"
                max-height="400px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns" :key="i" :property="item" :label="item"/>
      </el-table>
      <div id="histogram_29" style="width: 600px; height: 400px; margin: auto"></div>
    </el-dialog>

    <el-dialog v-model="dialogTableVisible"
               :visible.sync="dialogTableVisible"
               :title="dialogContent.label"
               v-if="dialogContent.id == 30"
               @opened="openId30">
      <el-text size="default" style="float: left; margin-bottom: 5px">降维数据：</el-text>
      <el-table :data="dialogContent.result"
                max-height="400px" :header-cell-style="{background: '#edf6ff', color: '#606266'}">
        <el-table-column v-for="(item ,i) in dialogContent.dataColumns" :key="i" :property="item" :label="item"/>
      </el-table>
      <div id="histogram_30" style="width: 600px; height: 400px; margin: auto"></div>
    </el-dialog>

    <el-dialog v-model="dialogTableVisible"
               :visible.sync="dialogTableVisible"
               :title="dialogContent.label"
               v-if="dialogContent.id == 36"
               @opened="openId36">
      <div id="histogram_36" style="width: 600px; height: 400px; margin: auto"></div>
    </el-dialog>

    <el-dialog v-model="dialogTableVisible"
               :visible.sync="dialogTableVisible"
               :title="dialogContent.label"
               v-if="dialogContent.id == 40"
               @opened="openId36">
      <div id="histogram_36" style="width: 600px; height: 400px; margin: auto"></div>
    </el-dialog>


    <a-col :span="5">
      <div style="padding: 20px 10px">
        <a-form :model="formData">
        <a-form-item label="组件名称" v-show="formData.title !== null">
          <el-text style="color: #000000">{{ formData.title }}</el-text>
        </a-form-item>

        <a-form-item label="节点名称" v-show="formData.name !== null">
          <a-input v-model:value="formData.name" @change="onNameChange" :style="{ width: selectWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="选取数据集" v-if="formData.id == 1">
          <!--          <a-select-->
          <!--              v-model:value="formData.content.dataSource"-->
          <!--              show-search-->
          <!--              placeholder="Please select"-->
          <!--              :options="options_1"-->
          <!--              style="width: 190px; float: right; margin-right: 10px"-->
          <!--              :filter-option="filterOption"-->
          <!--              @change="onDataChange"-->
          <!--          ></a-select>-->
          <a-input id="dataInput" :style="{ width: selectWidth, float: 'right' }"
                   v-model:value="formData.content.dataSource" @change="onDataChange">
            <template #addonAfter>
              <edit-outlined @click="showModal"/>
            </template>
          </a-input>
          <a-modal v-model:visible="visible" width="1000px" title="选取数据集" @ok="handleOk">
            <div style="display: flex">
              <div style="width: 300px">
                <a-table
                    :columns="columns"
                    :dataSource="tableData"
                    :pagination="false"
                    :row-selection="{
                      selectedRowKeys: selectedRowKeys,
                      onChange: onSelectChange,
                      type: 'radio',
                    }"
                    :show-header="false"
                >
                </a-table>
              </div>
              <div v-if="showData" style="width: 650px">
                <el-text style="font-size: larger; font-weight: bold; margin-left: 20px">{{
                    selectedRowName
                  }}
                </el-text>
                <el-table :data="data.dataBase.slice(0, 10)" style="margin-left: 20px; margin-top: 30px"
                          max-height="600px"
                          :header-cell-style="{background: '#edf6ff', color: '#606266'}" empty-text="暂无数据">
                  <el-table-column v-for="(item ,i) in data.dataColumns" :key="i" :property="item" :label="item"/>
                </el-table>
              </div>
            </div>
          </a-modal>
        </a-form-item>

        <a-form-item label="统计列" v-if="formData.id == 2">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              :style="{ width: selectWidth, float: 'right' }"
              placeholder="Please select"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="统计列" v-if="formData.id == 3">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="选择列" v-if="formData.id == 4">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="相关性指标" v-if="formData.id == 4">
          <a-select
              v-model:value="formData.content.indicator"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              :options="options_4"
              @change="onIndicatorChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="过滤缺失值" v-if="formData.id == 5">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="检测列" v-if="formData.id == 6">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="检测策略" v-if="formData.id == 6">
          <a-select
              v-model:value="formData.content.method"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              :options="options_6"
              @change="onMethodChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="是否过滤异常值" v-if="formData.id == 6">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="是否过滤重复值" v-if="formData.id == 7">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="计算列" v-if="formData.id == 8">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="相似度" v-if="formData.id == 8">
          <a-select
              v-model:value="formData.content.similarity"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              :options="options_8"
              @change="onSimilarityChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="删除列" v-if="formData.id == 9">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 10">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="测试集大小" v-if="formData.id == 10">
          <a-input-number v-model:value="formData.content.testSize"
                          :min="0" :max="1" :step="0.1" @change="onTestSizeChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="采样随机数" v-if="formData.id == 10">
          <a-input-number v-model:value="formData.content.randomState"
                          :min="0" :max="100" @change="onRandomStateChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="分层抽样" v-if="formData.id == 10">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '24px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="分层列" v-if="formData.id == 10 & formData.content.checked == true">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="编码列" v-if="formData.id == 11">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="编码列" v-if="formData.id == 12">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="转换列" v-if="formData.id == 13">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="转换为" v-if="formData.id == 13">
          <a-select
              v-model:value="formData.content.type"
              :options="options_13"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onTypeChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="选择列" v-if="formData.id == 14">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="重命名为" v-if="formData.id == 14">
          <a-input v-model:value="formData.content.newName" @change="onNewNameChange"
                   :style="{ width: selectWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="计算列" v-if="formData.id == 15">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="计算类型" v-if="formData.id == 15">
          <a-select
              v-model:value="formData.content.computeType"
              :options="options_15"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onComputeTypeChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="计算值" v-if="formData.id == 15">
          <a-input v-model:value="formData.content.computeNum" @change="onComputeNumChange"
                   :style="{ width: selectWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="替换列" v-if="formData.id == 16">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="替换方式" v-if="formData.id == 16">
          <a-select
              v-model:value="formData.content.substituteMethod"
              :options="options_16"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onSubstituteMethodChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="被替换值" v-if="formData.id == 16">
          <a-input v-model:value="formData.content.bySub" @change="onBySubChange"
                   :style="{ width: selectWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="替换值" v-if="formData.id == 16">
          <a-input v-model:value="formData.content.sub" @change="onSubChange"
                   :style="{ width: selectWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="填补列" v-if="formData.id == 17">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="填补策略" v-if="formData.id == 17">
          <a-select
              v-model:value="formData.content.fillMethod"
              :options="options_17"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onFillMethodChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="填补值" v-if="formData.id == 17 & formData.content.fillMethod == 'specific'">
          <a-input v-model:value="formData.content.specificNum" @change="onSpecificNumChange"
                   :style="{ width: selectWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="排序列" v-if="formData.id == 18">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="降序排列" v-if="formData.id == 18">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '24px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="编码列" v-if="formData.id == 19">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="删除首个取值" v-if="formData.id == 19">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '24px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 20">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              :style="{ width: selectWidth, float: 'right' }"
              placeholder="Please select"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 21">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="最小值" v-if="formData.id == 21">
          <a-input v-model:value="formData.content.minNum" @change="onMinNumChange"
                   :style="{ width: selectWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="最大值" v-if="formData.id == 21">
          <a-input v-model:value="formData.content.maxNum" @change="onMaxNumChange"
                   :style="{ width: selectWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 22">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 23">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 24">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="分段数" v-if="formData.id == 24">
          <a-input-number v-model:value="formData.content.numOfDuan"
                          :min="1" :max="100" @change="onNumOfDuanChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 25">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="分段数" v-if="formData.id == 25">
          <a-input-number v-model:value="formData.content.numOfDuan"
                          :min="1" :max="100" @change="onNumOfDuanChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 26">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="分段数" v-if="formData.id == 26">
          <a-input-number v-model:value="formData.content.numOfDuan"
                          :min="1" :max="100" @change="onNumOfDuanChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 27">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 27">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="最大分箱数" v-if="formData.id == 27">
          <a-input-number v-model:value="formData.content.numOfBox"
                          :min="1" :max="100" @change="onNumOfBoxChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 28">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 28">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="模型类型" v-if="formData.id == 28">
          <a-select
              v-model:value="formData.content.modelType"
              :options="options_28"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onModelTypeChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="最大分箱数" v-if="formData.id == 28">
          <a-input-number v-model:value="formData.content.numOfBox"
                          :min="1" :max="100" @change="onNumOfBoxChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 29">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="维数" v-if="formData.id == 29">
          <a-input-number v-model:value="formData.content.numOfDim"
                          :min="1" :max="100" @change="onNumOfDimChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="处理列" v-if="formData.id == 30">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 30">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="维数" v-if="formData.id == 30">
          <a-input-number v-model:value="formData.content.numOfDim"
                          :min="1" :max="100" @change="onNumOfDimChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 31">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 31">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="训练截距项" v-if="formData.id == 31">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="数据归一化" v-if="formData.id == 31">
          <a-switch v-model:checked="formData.content.checked1" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange1" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 32">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 32">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="正则系数" v-if="formData.id == 32">
          <a-input-number v-model:value="formData.content.normalNum"
                          :min="1" :max="100" @change="onNormalNumChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="训练截距项" v-if="formData.id == 32">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="数据归一化" v-if="formData.id == 32">
          <a-switch v-model:checked="formData.content.checked1" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange1" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 33">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 33">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="正则系数" v-if="formData.id == 33">
          <a-input-number v-model:value="formData.content.normalNum"
                          :min="1" :max="100" @change="onNormalNumChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="训练截距项" v-if="formData.id == 33">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="数据归一化" v-if="formData.id == 33">
          <a-switch v-model:checked="formData.content.checked1" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange1" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 34">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 34">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="阿尔法值" v-if="formData.id == 34">
          <a-input-number v-model:value="formData.content.normalNum"
                          :min="0" :max="100" :step="0.1" @change="onNormalNumChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="贝塔值" v-if="formData.id == 34">
          <a-input-number v-model:value="formData.content.normalNum1"
                          :min="0" :max="100" :step="0.1" @change="onNormalNumChange1"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="训练截距项" v-if="formData.id == 34">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="数据归一化" v-if="formData.id == 34">
          <a-switch v-model:checked="formData.content.checked1" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange1" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 35">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 35">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="邻居个数" v-if="formData.id == 35">
          <a-input-number v-model:value="formData.content.numberOfNeighbor"
                          :min="1" :max="100" @change="onNumberOfNeighborChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="权重计算方式" v-if="formData.id == 35">
          <a-select
              v-model:value="formData.content.weightType"
              :options="options_35_1"
              size="middle"
              placeholder="Please select"
              :style="{ width: numberWidth, float: 'right' }"
              @change="onWeightTypeChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="距离计算方式" v-if="formData.id == 35">
          <a-select
              v-model:value="formData.content.distanceType"
              :options="options_35_2"
              size="middle"
              placeholder="Please select"
              :style="{ width: numberWidth, float: 'right' }"
              @change="onDistanceTypeChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 36">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 36">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="最大树深度" v-if="formData.id == 36">
          <a-input-number v-model:value="formData.content.maxDepth"
                          :min="1" :max="100" @change="onMaxDepthChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="分裂最少样本" v-if="formData.id == 36">
          <a-input-number v-model:value="formData.content.minSplit"
                          :min="1" :max="100" @change="onMinSplitChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="叶节点最少样本" v-if="formData.id == 36">
          <a-input-number v-model:value="formData.content.minLeaf"
                          :min="1" :max="100" @change="onMinLeafChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 37">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 37">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="贝叶斯分类器" v-if="formData.id == 37">
          <a-select
              v-model:value="formData.content.bayesType"
              :options="options_37"
              size="middle"
              placeholder="Please select"
              :style="{ width: numberWidth, float: 'right' }"
              @change="onBayesTypeChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="平滑系数" v-if="formData.id == 37 & formData.content.bayesType != 'GaussianNB'">
          <a-input-number v-model:value="formData.content.smooth"
                          :min="0" :max="100" :step="0.1" @change="onSmoothChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="学习先验概率" v-if="formData.id == 37 & formData.content.bayesType != 'GaussianNB'">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '24px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="二值化阈值" v-if="formData.id == 37 & formData.content.bayesType == 'BernoulliNB'">
          <a-input-number v-model:value="formData.content.binarization"
                          :min="0" :max="100" :step="0.1" @change="onBinarizationChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 38">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 38">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="正则化系数" v-if="formData.id == 38">
          <a-input-number v-model:value="formData.content.normalNum"
                          :min="0" :max="100" :step="1" @change="onNormalNumChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="最小收敛数" v-if="formData.id == 38">
          <a-input-number v-model:value="formData.content.minConverge"
                          :min="0" :max="100" :step="1" @change="onMinConvergeChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="最大迭代数" v-if="formData.id == 38">
          <a-input-number v-model:value="formData.content.maxIter"
                          :min="0" :max="10000" :step="1" @change="onMaxIterChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="训练截距项" v-if="formData.id == 38">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange" :style="{ 'margin-left': '10px', float: 'left' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 39">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 39">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="训练错误率上限" v-if="formData.id == 39">
          <a-input-number v-model:value="formData.content.trainMaxError"
                          :min="0" :max="1" :step="0.01" @change="onTrainMaxErrorChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="核函数" v-if="formData.id == 39">
          <a-select
              v-model:value="formData.content.coreFunction"
              :options="options_39_1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCoreFunctionChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="gamma" v-if="formData.id == 39">
          <a-select
              v-model:value="formData.content.gamma"
              :options="options_39_2"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onGammaChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="coef0" v-if="formData.id == 39 & formData.content.coreFunction != 'rbf'">
          <a-input-number v-model:value="formData.content.coef0"
                          :min="0" :max="1" :step="0.01" @change="onCoef0Change"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="degree" v-if="formData.id == 39 & formData.content.coreFunction == 'poly'">
          <a-input-number v-model:value="formData.content.degree"
                          :min="0" :max="100" @change="onDegreeChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="类别权重" v-if="formData.id == 39">
          <a-select
              v-model:value="formData.content.classWeight"
              :options="options_39_3"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onClassWeightChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 40">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 40">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="最大树深度" v-if="formData.id == 40">
          <a-input-number v-model:value="formData.content.maxDepth"
                          :min="1" :max="100" @change="onMaxDepthChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="分裂最少样本" v-if="formData.id == 40">
          <a-input-number v-model:value="formData.content.minSplit"
                          :min="1" :max="100" @change="onMinSplitChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="叶节点最少样本" v-if="formData.id == 40">
          <a-input-number v-model:value="formData.content.minLeaf"
                          :min="1" :max="100" @change="onMinLeafChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 41">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 41">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="正则化项" v-if="formData.id == 41">
          <a-select
              v-model:value="formData.content.normalItem"
              :options="options_41"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onNormalItemChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="正则化系数" v-if="formData.id == 41">
          <a-input-number v-model:value="formData.content.normalNum"
                          :min="0" :max="100" :step="1" @change="onNormalNumChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="收敛系数" v-if="formData.id == 41">
          <a-input-number v-model:value="formData.content.minConverge"
                          :min="0" :max="100" :step="1" @change="onMinConvergeChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="随机种子" v-if="formData.id == 41">
          <a-input-number v-model:value="formData.content.randomState"
                          :min="0" :max="100" @change="onRandomStateChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="类别权重" v-if="formData.id == 41">
          <a-select
              v-model:value="formData.content.classWeight"
              :options="options_39_3"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onClassWeightChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 42">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 42">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="邻居个数" v-if="formData.id == 42">
          <a-input-number v-model:value="formData.content.numberOfNeighbor"
                          :min="1" :max="100" @change="onNumberOfNeighborChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="权重计算方式" v-if="formData.id == 42">
          <a-select
              v-model:value="formData.content.weightType"
              :options="options_35_1"
              size="middle"
              placeholder="Please select"
              :style="{ width: numberWidth, float: 'right' }"
              @change="onWeightTypeChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="距离计算方式" v-if="formData.id == 42">
          <a-select
              v-model:value="formData.content.distanceType"
              :options="options_35_2"
              size="middle"
              placeholder="Please select"
              :style="{ width: numberWidth, float: 'right' }"
              @change="onDistanceTypeChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="特征列" v-if="formData.id == 43">
          <a-select
              v-model:value="formData.content.characterColumn"
              :options="optionsCharacterColumns"
              mode="multiple"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCharacterChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="聚类数" v-if="formData.id == 43">
          <a-input-number v-model:value="formData.content.numOfCluster"
                          :min="0" :max="100" @change="onNumOfClusterChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="质心初始化" v-if="formData.id == 43">
          <a-select
              v-model:value="formData.content.centerInitial"
              :options="options_43"
              size="middle"
              placeholder="Please select"
              :style="{ width: selectWidth, float: 'right' }"
              @change="onCenterInitialChange"
          ></a-select>
        </a-form-item>

        <a-form-item label="初始化次数" v-if="formData.id == 43">
          <a-input-number v-model:value="formData.content.initialTimes"
                          :min="0" :max="100" @change="onInitialTimesChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="最大迭代数" v-if="formData.id == 43">
          <a-input-number v-model:value="formData.content.maxIter"
                          :min="0" :max="1000" @change="onMaxIterChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="最小收敛值" v-if="formData.id == 43">
          <a-input-number v-model:value="formData.content.minConverge"
                          :min="0" :max="100" @change="onMinConvergeChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="随机种子" v-if="formData.id == 43">
          <a-input-number v-model:value="formData.content.randomState"
                          :min="0" :max="100" @change="onRandomStateChange"
                          :style="{ width: numberWidth, float: 'right' }"/>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 49">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"

              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="均方误差(MSE)" v-if="formData.id == 49">
          <a-switch v-model:checked="formData.content.checked" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange"/>
        </a-form-item>

        <a-form-item label="平均绝对误差(MAE)" v-if="formData.id == 49">
          <a-switch v-model:checked="formData.content.checked1" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange"/>
        </a-form-item>

        <a-form-item label="决定系数(R2)" v-if="formData.id == 49">
          <a-switch v-model:checked="formData.content.checked2" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange"/>
        </a-form-item>

        <a-form-item label="中位绝对误差" v-if="formData.id == 49">
          <a-switch v-model:checked="formData.content.checked3" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange"/>
        </a-form-item>

        <a-form-item label="解释方差" v-if="formData.id == 49">
          <a-switch v-model:checked="formData.content.checked4" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange"/>
        </a-form-item>

        <a-form-item label="最大误差" v-if="formData.id == 49">
          <a-switch v-model:checked="formData.content.checked5" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange"/>
        </a-form-item>

        <a-form-item label="平均泊松偏差" v-if="formData.id == 49">
          <a-switch v-model:checked="formData.content.checked6" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange"/>
        </a-form-item>

        <a-form-item label="平均伽马偏差" v-if="formData.id == 49">
          <a-switch v-model:checked="formData.content.checked7" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange"/>
        </a-form-item>

        <a-form-item label="平均Tweedie偏差" v-if="formData.id == 49">
          <a-switch v-model:checked="formData.content.checked8" checked-children="yes" un-checked-children="no"
                    @change="onCheckedChange"/>
        </a-form-item>

        <a-form-item label="标签列" v-if="formData.id == 50">
          <a-select
              v-model:value="formData.content.characterColumn1"
              :options="optionsCharacterColumns1"
              size="middle"
              placeholder="Please select"

              @change="onCharacterChange1"
          ></a-select>
        </a-form-item>

        <a-form-item label="正类标签" v-if="formData.id == 50">
          <a-input v-model:value="formData.content.positiveTag" @change="onPositiveTagChange"/>
        </a-form-item>
      </a-form>
      </div>
    </a-col>
  </a-row>
</template>

<script lang="ts">
import {defineComponent, onMounted, createVNode, reactive, ref, watch, nextTick} from "vue";
import {Graph, Cell, Path} from '@antv/x6'
import {Selection} from "@antv/x6-plugin-selection";
import {register} from "@antv/x6-vue-shape";
import {Stencil} from "@antv/x6-plugin-stencil";
import basicNode from "./basicNode.vue";
import type {SelectProps} from 'ant-design-vue';
import {EditOutlined} from '@ant-design/icons-vue'
import axios from "axios";
import * as echarts from "echarts";
import dagNodeData from '../assets/dagNode.json'

// 选取数据集
interface User {
  key: number
  dataName: string
  dataId: number
  backendName: string
}

interface NodeStatus {
  id: number
  status: 'default' | 'success' | 'failed' | 'running'
  label?: string
}

interface form {
  id: number
  title: string
  name: string
  content?: { [propName: string]: any }
}

// 表单数据
let formData: form = reactive({
  id: null,
  title: null,
  name: null,
  content: {}
})

// console.log('register node!')

Graph.registerEdge(
    'dagEdge',
    {
      inherit: 'edge',
      attrs: {
        line: {
          stroke: '#C2C8D5',
          strokeWidth: 1,
          targetMarker: null,
        },
      },
    },
    true,
)
// console.log('register edge!')

Graph.registerConnector(
    'dagConnector',
    (s, e) => {
      const offset = 4
      const deltaY = Math.abs(e.y - s.y)
      const control = Math.floor((deltaY / 3) * 2)

      const v1 = {x: s.x, y: s.y + offset + control}
      const v2 = {x: e.x, y: e.y - offset - control}

      return Path.normalize(
          `M ${s.x} ${s.y}
       L ${s.x} ${s.y + offset}
       C ${v1.x} ${v1.y} ${v2.x} ${v2.y} ${e.x} ${e.y - offset}
       L ${e.x} ${e.y}
      `,
      )
    },
    true,
)
// console.log('register connector!')

export default defineComponent({
  name: "homeView",
  data() {
    return {
      selectedRows: [],
      selectedRowKeys: [],
      selectedRowName: null,
      data: reactive({
        dataBase: [],
        dataColumns: []
      }),
      showData: false,
    }
  },
  setup() {
    let background = reactive({graph: null});
    let stencil: Stencil;
    let curCell: Cell;
    let cells: Cell[] = []

    // 控制下拉框内容
    let optionsCharacterColumns = ref<SelectProps['options']>([]);
    let optionsCharacterColumns1 = ref<SelectProps['options']>([]);

    // 控制弹出结果框
    let dialogTableVisible = ref(false)

    // 控制结果框中的内容
    let dialogContent = ref({
      label: null,
      result: null,
      dataColumns: null,
      ratios: null
    })

    // 数据输入框内容
    let dataBaseInput = ref(null)

    const basic_columns_to_home = (columns) => {
      // console.log("接收数据触发的回调函数")
      optionsCharacterColumns.value = columns
    }

    const basic_columns_to_home1 = (columns) => {
      // console.log("接收数据触发的回调函数")
      optionsCharacterColumns1.value = columns
    }

    const basic_info_to_home = (message) => {
      console.log("弹出结果框")
      dialogContent.value = null
      dialogContent.value = message.info
      console.log(dialogContent.value)
      dialogTableVisible.value = message.showBasicInfo
    }

    function openId4() {
      nextTick(() => {
        let heatmap = echarts.getInstanceByDom(document.getElementById('relation_heatmap'));
        if (heatmap == null) {
          heatmap = echarts.init(document.getElementById('relation_heatmap'))
        }
        let heatmap_data = []
        dialogContent.value.result.forEach((item, index) => {
          let array = Object.keys(item)
          for (let i = 1; i < array.length; i++) {
            heatmap_data.push([i - 1, index, item[array[i]]])
          }
        })
        console.log(heatmap_data)
        heatmap_data = heatmap_data.map(function (item) {
          return [item[1], item[0], item[2]];
        });
        let option = {
          tooltip: {
            position: 'top'
          },
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          animation: false,
          grid: {
            height: '50%',
            left: '13%',
            top: '20',
          },
          xAxis: {
            type: 'category',
            data: dialogContent.value.dataColumns.slice(1),
            splitArea: {
              show: true
            }
          },
          yAxis: {
            type: 'category',
            data: dialogContent.value.dataColumns.slice(1),
            splitArea: {
              show: true
            }
          },
          visualMap: {
            min: -1,
            max: 1,
            align: 'top',
            calculable: true,
            left: 'center',
            orient: 'horizontal',
            inRange: {
              color: ['white', 'rgb(191,68,76)']
            }
          },
          series: [{
            name: 'data_col',
            type: 'heatmap',
            data: heatmap_data,
            // label: {
            //   show: true,
            //   color: 'white'
            // },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: 'white'
              },
            }
          }]
        }
        heatmap.setOption(option)

      })
    }

    function openId10() {
      nextTick(() => {
        let pie_10 = echarts.getInstanceByDom(document.getElementById('pie_10'));
        if (pie_10 == null) {
          pie_10 = echarts.init(document.getElementById('pie_10'))
        }
        let pie_data = dialogContent.value.result
        const option = {
          tooltip: {
            position: 'top'
          },
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          legend: {
            // 图例
            data: ["训练集", "测试集"],
            left: "right",
            top: "30%",
            orient: "vertical"
          },
          series: [
            {
              type: "pie",
              data: [
                {
                  value: pie_data.index_counts[0],
                  name: pie_data.index_cols[0]
                },
                {
                  value: pie_data.index_counts[1],
                  name: pie_data.index_cols[1]
                }
              ]
            }
          ]
        };
        pie_10.setOption(option)

      })
    }

    function openId29() {
      nextTick(() => {
        let histogram_29 = echarts.getInstanceByDom(document.getElementById('histogram_29'));
        if (histogram_29 == null) {
          histogram_29 = echarts.init(document.getElementById('histogram_29'))
        }
        let histogram_x = []
        let histogram_item = []
        dialogContent.value.ratios.forEach((item) => {
          histogram_x.push(item['主成分'])
          histogram_item.push(item['ratios'])
        })
        const option = {
          tooltip: {
            position: 'top'
          },
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          title: {
            text: 'PCA主成分方差比例',
            left: 'center',
            top: 'bottom'
          },
          xAxis: {
            data: histogram_x,
            name: '成分',
            nameLocation: 'center',
          },
          yAxis: {
            name: '方差比例',
            nameRotate: '90',
            nameLocation: 'center',
            nameGap: 40,
          },
          series: [
            {
              type: "bar",
              data: histogram_item
            }
          ]
        };
        histogram_29.setOption(option)

      })
    }

    function openId30() {
      nextTick(() => {
        let histogram_30 = echarts.getInstanceByDom(document.getElementById('histogram_30'));
        if (histogram_30 == null) {
          histogram_30 = echarts.init(document.getElementById('histogram_30'))
        }
        let histogram_x = []
        let histogram_item = []
        dialogContent.value.ratios.forEach((item) => {
          histogram_x.push(item['主成分'])
          histogram_item.push(item['ratios'])
        })
        const option = {
          tooltip: {
            position: 'top'
          },
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          title: {
            text: 'LDA主成分方差比例',
            left: 'center',
            top: 'bottom'
          },
          xAxis: {
            data: histogram_x,
            name: '成分',
            nameLocation: 'center',
          },
          yAxis: {
            name: '方差比例',
            nameRotate: '90',
            nameLocation: 'center',
            nameGap: 40,
          },
          series: [
            {
              type: "bar",
              data: histogram_item
            }
          ]
        };
        histogram_30.setOption(option)
      })
    }

    function openId36() {
      nextTick(() => {
        let histogram_36 = echarts.getInstanceByDom(document.getElementById('histogram_36'));
        if (histogram_36 == null) {
          histogram_36 = echarts.init(document.getElementById('histogram_36'))
        }
        let histogram_x = Object.keys(dialogContent.value.result[0])
        let histogram_item = Object.values(dialogContent.value.result[0])
        const option = {
          tooltip: {
            position: 'top'
          },
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          title: {
            text: '决策树特征重要度',
            left: 'center',
            top: 'bottom'
          },
          xAxis: {
            data: histogram_x,
          },
          yAxis: {
            name: '特征重要度',
            nameRotate: '90',
            nameLocation: 'center',
            nameGap: 40,
          },
          series: [
            {
              type: "bar",
              data: histogram_item
            }
          ]
        };
        histogram_36.setOption(option)
      })
    }


    watch(
        () => formData.content.dataSource,
        (val, preVal) => {
          //val为修改后的值,preVal为修改前的值
          onDataChange()
        },
        {
          //如果加了这个参数，值为true的话，就消除了惰性，watch会在创建后立即执行一次
          //那么首次执行，val为默认值,preVal为undefined
          immediate: false,
          //这个参数代表监听对象时，可以监听深度嵌套的对象属性
          //比如message是一个对象的话，可以监听到message.a.b.c，也就是message下的所有属性
          deep: true,
        }
    )

    onMounted(() => {
      background.graph = new Graph({
        container: document.getElementById('container') as HTMLElement,
        height: window.innerHeight,
        background: {
          // color: '#fffbe6',
          color: 'white'
        },
        grid: {
          size: 10,
          visible: true,
        },
        // 画布平移
        panning: {
          enabled: true,
          // 鼠标左击、滑轮
          eventTypes: ['leftMouseDown', 'mouseWheel'],
        },
        // 按住ctrl+滑轮实现缩放
        mousewheel: {
          enabled: true,
          modifiers: 'ctrl',
          factor: 1.1,
          maxScale: 1.5,
          minScale: 0.5,
        },
        // 当某些事件发生时，触发高亮
        highlighting: {
          // 连线过程中，自动吸附到连接桩时被使用
          magnetAdsorbed: {
            name: 'stroke',
            args: {
              attrs: {
                fill: '#fff',
                stroke: '#31d0c6',
                strokeWidth: 4,
              },
            },
          },
        },
        // 全局连线规则
        connecting: {
          // 当 snap 设置为 true 时连线的过程中距离节点或者连接桩 50px 时会触发自动吸附
          snap: true,
          // 不允许连接到画布空白位置的点
          allowBlank: false,
          // 不允许创建循环连线
          allowLoop: false,
          // 拖动边时，高亮显示所有可用的连接桩或节点
          highlight: true,
          connector: 'dagConnector',
          connectionPoint: 'anchor',
          anchor: 'center',
          // 点击 magnet 时 根据 validateMagnet 返回值来判断是否新增边，触发时机是 magnet 被按下，如果返回 false ，则没有任何反应，如果返回 true ，会在当前 magnet 创建一条新的边
          validateMagnet({magnet}) {
            // top连接桩不会伸出连接线
            return magnet.getAttribute('port-group') !== 'top'
          },
          // 创建新边的类型
          createEdge() {
            return background.graph.createEdge({
              shape: 'dagEdge',
              attrs: {
                line: {
                  strokeDasharray: '5 5',
                },
              },
              zIndex: -1,
            })
          },
        },
      })

      register({
            shape: 'dagNode',
            width: 180,
            height: 36,
            // component: {
            //   template: `<AlgoNode/>`,
            //   component: AlgoNode,
            // },
            // 仅以下方法可以使用
            component: {
              render: () => {
                return createVNode(basicNode,
                    {
                      graph: background.graph,
                      // 在子组件触发的事件名前加on，这样就能接收子组件的信息，并触发回调
                      onColumns: basic_columns_to_home,
                      onColumns1: basic_columns_to_home1,
                      onShowInfo: basic_info_to_home,
                    })
              }
            },
            ports: {
              groups: {
                top: {
                  position: 'top',
                  attrs: {
                    circle: {
                      r: 4,
                      magnet: true,
                      stroke: '#C2C8D5',
                      strokeWidth: 1,
                      fill: '#fff',
                    },
                  },
                },
                bottom: {
                  position: 'bottom',
                  attrs: {
                    circle: {
                      r: 4,
                      magnet: true,
                      stroke: '#C2C8D5',
                      strokeWidth: 1,
                      fill: '#fff',
                    },
                  },
                },
              },
            },
          },
      )

      // 设置框选，按住shift+鼠标左键实现多node框选
      background.graph.use(new Selection({
        enabled: true,
        multiple: true,
        rubberEdge: true,
        rubberNode: true,
        modifiers: 'shift',
        rubberband: true,
      }))

      // 边连接时，连接的边
      background.graph.on('edge:connected', ({edge}) => {
        edge.attr({
          line: {
            // 虚线设置，不设置参数表示为实线，可以设置为20（实线20，间距20，以此类推）/ 20 40（实线20，间距40，实线20...）
            strokeDasharray: '',  // strokeDasharray： '20' / strokeDasharray： '20 40'
          },
        })
        const frontCell: Cell = edge.getSourceCell()
        // 如果上个cell有输出，则直接拿过来
        if (frontCell.getData().hasOwnProperty('output')) {
          edge.getTargetCell().setData({
            ...(edge.getTargetCell().getData() as NodeStatus),
            lastOutput: frontCell.getData().output,
          })
          // 上个cell没有输出，取他的dataId，去数据库中取数据
        } else {
          const dataId = frontCell.getData().dataId
          edge.getTargetCell().setData({
            ...(edge.getTargetCell().getData() as NodeStatus),
            dataId: dataId,
          })
        }
      })

      // 节点数据改变时
      background.graph.on('node:change:data', ({node}) => {
        // 获取连接到节点的输入边
        const edges = background.graph.getIncomingEdges(node)
        // 拿到数据，设置为NodeStatus类型
        const {status} = node.getData() as NodeStatus
        edges?.forEach((edge) => {
          // 节点是running状态，所有输入边设置为虚线，动画为
          if (status === 'running') {
            edge.attr('line/strokeDasharray', 5)
            edge.attr('line/style/animation', 'running-line 30s infinite linear')
          } else {
            edge.attr('line/strokeDasharray', '')
            edge.attr('line/style/animation', '')
          }
        })
      })

      // 按钮
      // graph.on('node:mouseenter', ({node}) => {
      //   node.addTools({
      //     name: 'button-remove',
      //     args: {
      //       x: '100%',
      //       y: 0,
      //       offset: {x: -10, y: 10},
      //     },
      //   })
      //   node.addTools({
      //     name: 'button',
      //     args: {
      //       markup: [
      //         {
      //           tagName: 'circle',
      //           selector: 'button',
      //           attrs: {
      //             r: 8,
      //             stroke: '#4fb4f6',
      //             strokeWidth: 2,
      //             fill: 'white',
      //             cursor: 'pointer',
      //           },
      //         },
      //         {
      //           tagName: 'text',
      //           textContent: '▶',
      //           selector: 'icon',
      //           attrs: {
      //             fill: '#4fb4f6',
      //             fontSize: 8,
      //             textAnchor: 'middle',
      //             pointerEvents: 'none',
      //             y: '0.3em',
      //           },
      //         },
      //       ],
      //       x: "100%",
      //       y: "100%",
      //       offset: {x: -10, y: -10},
      //       onClick({cell}: { cell: Cell }) {
      //         // 获取当前节点的入边
      //         const edges = graph.getIncomingEdges(cell)
      //         // 初始读数据节点，从后端读取数据库数据，并将结果保存在data中
      //         if (edges === null) {
      //           // 先设置为running状态
      //           cell.setData({
      //             ...(cell.getData() as NodeStatus),
      //             status: 'running',
      //           })
      //           // 模拟请求数据库
      //           console.log('正在请求数据库')
      //           axios.get('http://127.0.0.1:8000/api/' + cell.getData().dataSource).then(res => {
      //             // console.log(res)
      //             // 请求成功则将数据中的fields字段拿出来赋值给dataBase字段，并改变状态为success
      //             if (res.statusText === 'OK') {
      //               const data = []
      //               res.data.list.forEach((item) => {
      //                 data.push(item.fields)
      //               })
      //               console.log(data)
      //
      //               // 同时设置供选择的特征列
      //               let columnValuesLabels = []
      //               Object.keys(data[0]).forEach((item) => {
      //                 columnValuesLabels.push({value: item, label: item})
      //               })
      //               optionsCharacterColumns.value = columnValuesLabels;
      //               optionsCharacterColumns1.value = columnValuesLabels;
      //
      //
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'success',
      //                 dataBase: data,
      //                 dataId: res.data.dataId,
      //               })
      //             }
      //             // console.log(cell)
      //           }).catch(error => {
      //             cell.setData({
      //               ...(cell.getData() as NodeStatus),
      //               status: 'failed',
      //             })
      //             console.log(cell)
      //             console.log(error)
      //           })
      //         } else {
      //           // 先将状态设置为running
      //           cell.setData({
      //             ...(cell.getData() as NodeStatus),
      //             status: 'running',
      //           })
      //           // 获取前cell的数据
      //           const frontCell: Cell = edges[0].getSourceCell()
      //           const dataId = frontCell.getData().dataId
      //           cell.setData({
      //             ...(cell.getData() as NodeStatus),
      //             dataId: dataId,
      //           })
      //
      //           // 将获取到的数据和模型参数传回后端进行运算
      //           console.log('正在请求后端服务')
      //
      //           if (cell.getData().id == 2) {
      //             axios.post('http://127.0.0.1:8000/api/summary', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 3.查看唯一值及数量
      //           else if (cell.getData().id == 3) {
      //             axios.post('http://127.0.0.1:8000/api/unique_amount', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 4.数据相关性
      //           else if (cell.getData().id == 4) {
      //             axios.post('http://127.0.0.1:8000/api/relation', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //               ///////// 绘制热力图
      //
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 5.过滤缺失值
      //           else if (cell.getData().id == 5) {
      //             axios.post('http://127.0.0.1:8000/api/filter_loss', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 6.单变量异常值检测
      //           else if (cell.getData().id == 6) {
      //             axios.post('http://127.0.0.1:8000/api/filter_queer', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 7.重复值检测
      //           else if (cell.getData().id == 7) {
      //             axios.post('http://127.0.0.1:8000/api/filter_repeat', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 8.样本相似度计算
      //           else if (cell.getData().id == 8) {
      //             axios.post('http://127.0.0.1:8000/api/sample_similarity', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 9.删除列
      //           else if (cell.getData().id == 9) {
      //             axios.post('http://127.0.0.1:8000/api/delete_columns', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 10.训练/测试集划分
      //           else if (cell.getData().id == 10) {
      //             axios.post('http://127.0.0.1:8000/api/preprocess_train_test_split', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 11.数字编码
      //           else if (cell.getData().id == 11) {
      //             axios.post('http://127.0.0.1:8000/api/digital_coding', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 13.类型转换
      //           else if (cell.getData().id == 13) {
      //             axios.post('http://127.0.0.1:8000/api/type_change', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 14.列重命名
      //           else if (cell.getData().id == 14) {
      //             axios.post('http://127.0.0.1:8000/api/name_change', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 15.数据列计算
      //           else if (cell.getData().id == 15) {
      //             axios.post('http://127.0.0.1:8000/api/compute_column', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 16.数据值替换
      //           else if (cell.getData().id == 16) {
      //             axios.post('http://127.0.0.1:8000/api/preprocess_replace_value', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 17.缺失值填补
      //           else if (cell.getData().id == 17) {
      //             axios.post('http://127.0.0.1:8000/api/preprocess_fillna', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 18.数据按列值排序
      //           else if (cell.getData().id == 18) {
      //             axios.post('http://127.0.0.1:8000/api/preprocess_sort_by_value', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 19.Onehot编码
      //           else if (cell.getData().id == 19) {
      //             axios.post('http://127.0.0.1:8000/api/onehot', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 20.Z-Score标准化
      //           else if (cell.getData().id == 20) {
      //             axios.post('http://127.0.0.1:8000/api/z_score_regulation', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 21.Min-Max标准化
      //           else if (cell.getData().id == 21) {
      //             axios.post('http://127.0.0.1:8000/api/min_max_regulation', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 22.Logistic标准化
      //           else if (cell.getData().id == 22) {
      //             axios.post('http://127.0.0.1:8000/api/logistic_regulation', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 23.最大绝对值标准化
      //           else if (cell.getData().id == 23) {
      //             axios.post('http://127.0.0.1:8000/api/max_abs_regulation', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 24.等距离散化
      //           else if (cell.getData().id == 24) {
      //             axios.post('http://127.0.0.1:8000/api/isometric_dispersion', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 25.等频离散化
      //           else if (cell.getData().id == 25) {
      //             axios.post('http://127.0.0.1:8000/api/equal_freq_discretization', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 26.Kmeans离散化
      //           else if (cell.getData().id == 26) {
      //             axios.post('http://127.0.0.1:8000/api/kmeans_discretization', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 27.卡方离散化
      //           else if (cell.getData().id == 27) {
      //             axios.post('http://127.0.0.1:8000/api/kafang_discretization', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 28.决策树离散化
      //           else if (cell.getData().id == 28) {
      //             axios.post('http://127.0.0.1:8000/api/decision_tree_discretization', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 29.主成分分析
      //           else if (cell.getData().id == 29) {
      //             axios.post('http://127.0.0.1:8000/api/PCA_reduce_dim', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 30.线性判别分析
      //           else if (cell.getData().id == 30) {
      //             axios.post('http://127.0.0.1:8000/api/linear_reduce_dim', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 31.线性回归
      //           else if (cell.getData().id == 31) {
      //             axios.post('http://127.0.0.1:8000/api/linear_regression', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 32.LASSO回归
      //           else if (cell.getData().id == 32) {
      //             axios.post('http://127.0.0.1:8000/api/lasso_regression', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 33.岭回归
      //           else if (cell.getData().id == 33) {
      //             axios.post('http://127.0.0.1:8000/api/ridge_regression', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 34.弹性网络
      //           else if (cell.getData().id == 34) {
      //             axios.post('http://127.0.0.1:8000/api/elastic_net', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 35.K近邻回归
      //           else if (cell.getData().id == 35) {
      //             axios.post('http://127.0.0.1:8000/api/knn_regression', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 36.决策树回归
      //           else if (cell.getData().id == 36) {
      //             axios.post('http://127.0.0.1:8000/api/decision_tree_regression', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 37.朴素贝叶斯
      //           else if (cell.getData().id == 37) {
      //             axios.post('http://127.0.0.1:8000/api/naive_bayes', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 38.线性SVC
      //           else if (cell.getData().id == 38) {
      //             axios.post('http://127.0.0.1:8000/api/linear_SVC', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 39.支持向量机
      //           else if (cell.getData().id == 39) {
      //             axios.post('http://127.0.0.1:8000/api/SVM_classification', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 40.分类决策树
      //           else if (cell.getData().id == 40) {
      //             axios.post('http://127.0.0.1:8000/api/decision_tree_classification', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 41.逻辑回归
      //           else if (cell.getData().id == 41) {
      //             axios.post('http://127.0.0.1:8000/api/logistic_regression', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //           // 42.K近邻
      //           else if (cell.getData().id == 42) {
      //             axios.post('http://127.0.0.1:8000/api/knn_classification', cell.getData()).then(res => {
      //               console.log(res)
      //               if (res.statusText === 'OK') {
      //                 cell.setData({
      //                   ...(cell.getData() as NodeStatus),
      //                   status: 'success',
      //                   result: res.data,
      //                 })
      //                 console.log(cell.getData().result)
      //               }
      //             }).catch(error => {
      //               cell.setData({
      //                 ...(cell.getData() as NodeStatus),
      //                 status: 'failed',
      //               })
      //               console.log(cell)
      //               console.log(error)
      //             })
      //           }
      //         }
      //       },
      //     },
      //   })
      // })

      // 按钮消失
      // graph.on('node:mouseleave', ({node}) => {
      //   node.removeTools()
      // })

      // 创建左侧菜单栏
      stencil = new Stencil({
        title: '搜索',
        target: background.graph,
        search(cell, keyword) {
          return cell.getData().label.indexOf(keyword) !== -1
        },
        placeholder: '请输入节点名称',
        notFoundText: '没有找到',
        stencilGraphWidth: (window.innerWidth)/6,
        collapsable: true,
        groups: [
          {
            name: 'source',
            collapsable: true,
            collapsed: true,
            title: '数据源',
            graphHeight: 100,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'explore',
            collapsable: true,
            collapsed: true,
            title: '数据探索',
            graphHeight: 570,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'sift',
            collapsable: true,
            collapsed: true,
            title: '数据筛选',
            graphHeight: 180,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'transform',
            collapsable: true,
            collapsed: true,
            title: '数据转换',
            graphHeight: 660,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'extraction',
            collapsable: true,
            collapsed: true,
            title: '特征抽取',
            graphHeight: 100,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'normalization',
            collapsable: true,
            collapsed: true,
            title: '标准化',
            graphHeight: 330,
            layoutOptions: {
              columns: 1,
              dx: 33,
              marginX: ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'discretion',
            collapsable: true,
            collapsed: true,
            title: '离散化',
            graphHeight: 410,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'dimensional',
            collapsable: true,
            collapsed: true,
            title: '降维',
            graphHeight: 175,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'regression',
            collapsable: true,
            collapsed: true,
            title: '回归',
            graphHeight: 500,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'classification',
            collapsable: true,
            collapsed: true,
            title: '分类',
            graphHeight: 500,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          //   {
          //   name: 'cluster',
          //   collapsable: true,
          //   collapsed: true,
          //   title: '聚类',
          //   graphHeight: 420,
          //   layoutOptions: {
          //     columns: 1,
          //     marginX: 65,
          //   }
          // },
          {
            name: 'predication',
            collapsable: true,
            collapsed: true,
            title: '预测',
            graphHeight: 100,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
          {
            name: 'evaluate',
            collapsable: true,
            collapsed: true,
            title: '评估',
            graphHeight: 175,
            layoutOptions: {
              columns: 1,
              dx: 32 + ((window.innerWidth)/6 - 180)/2
            }
          },
        ]
      })
      document.querySelector('#stencil').appendChild(stencil.container)

      // fetch("/dagNode.json")
      //     .then((response) => response.json())
      //     .then((data: Cell.Metadata[]) => {
      //       data.forEach((item) => {
      //         cells.push(background.graph.createNode(item))
      //         // 加载几种节点
      //         if (cells.length == 1) {
      //           stencil.load(cells, 'source')
      //         } else if (cells.length == 8) {
      //           stencil.load(cells.slice(1), 'explore')
      //         } else if (cells.length == 10) {
      //           stencil.load(cells.slice(8), 'sift')
      //         } else if (cells.length == 18) {
      //           stencil.load(cells.slice(10), 'transform')
      //         } else if (cells.length == 19) {
      //           stencil.load(cells.slice(18), 'extraction')
      //         } else if (cells.length == 23) {
      //           stencil.load(cells.slice(19), 'normalization')
      //         } else if (cells.length == 28) {
      //           stencil.load(cells.slice(23), 'discretion')
      //         } else if (cells.length == 30) {
      //           stencil.load(cells.slice(28), 'dimensional')
      //         } else if (cells.length == 36) {
      //           stencil.load(cells.slice(30), 'regression')
      //         } else if (cells.length == 42) {
      //           stencil.load(cells.slice(36), 'classification')
      //         }
      //             // else if (cells.length == 47){
      //             //   stencil.load(cells.slice(42), 'cluster')
      //         // }
      //         else if (cells.length == 48) {
      //           stencil.load(cells.slice(47), 'predication')
      //         } else if (cells.length == 50) {
      //           stencil.load(cells.slice(48), 'evaluate')
      //         }
      //       })
      //     })
      dagNodeData.forEach((item) => {
        cells.push(background.graph.createNode(item))
        // 加载几种节点
        if (cells.length == 1) {
          stencil.load(cells, 'source')
        } else if (cells.length == 8) {
          stencil.load(cells.slice(1), 'explore')
        } else if (cells.length == 10) {
          stencil.load(cells.slice(8), 'sift')
        } else if (cells.length == 18) {
          stencil.load(cells.slice(10), 'transform')
        } else if (cells.length == 19) {
          stencil.load(cells.slice(18), 'extraction')
        } else if (cells.length == 23) {
          stencil.load(cells.slice(19), 'normalization')
        } else if (cells.length == 28) {
          stencil.load(cells.slice(23), 'discretion')
        } else if (cells.length == 30) {
          stencil.load(cells.slice(28), 'dimensional')
        } else if (cells.length == 36) {
          stencil.load(cells.slice(30), 'regression')
        } else if (cells.length == 42) {
          stencil.load(cells.slice(36), 'classification')
        }
            // else if (cells.length == 47){
            //   stencil.load(cells.slice(42), 'cluster')
        // }
        else if (cells.length == 48) {
          stencil.load(cells.slice(47), 'predication')
        } else if (cells.length == 50) {
          stencil.load(cells.slice(48), 'evaluate')
        }
      })

      initEvent();
    })

    // 节点点击事件
    function initEvent() {
      background.graph.on('cell:click', ({cell}) => {
        curCell = cell
        formData.id = cell.getData()?.id
        formData.title = cell.getData().label
        formData.name = cell.getData().name
        // 1.读数据表
        if (formData.id == 1) {
          formData.content = {}
          formData.content['dataSource'] = cell.getData().dataSource
          // 2.字段基本统计信息
        } else if (formData.id == 2) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
        } else if (formData.id == 3) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
        } else if (formData.id == 4) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['indicator'] = cell.getData().indicator
        } else if (formData.id == 5) {
          formData.content = {}
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          formData.content['checked'] = cell.getData().checked
        } else if (formData.id == 6) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['method'] = cell.getData().method
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          formData.content['checked'] = cell.getData().checked
        } else if (formData.id == 7) {
          formData.content = {}
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          formData.content['checked'] = cell.getData().checked
        } else if (formData.id == 8) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['similarity'] = cell.getData().similarity
        } else if (formData.id == 9) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
        } else if (formData.id == 10) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().testSize == undefined) {
            cell.getData().testSize = 0.2
          }
          formData.content['testSize'] = cell.getData().testSize
          if (cell.getData().randomState == undefined) {
            cell.getData().randomState = 0
          }
          formData.content['randomState'] = cell.getData().randomState
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          formData.content['checked'] = cell.getData().checked
        } else if (formData.id == 11) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
        } else if (formData.id == 12) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
        } else if (formData.id == 13) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          if (cell.getData().type == undefined) {
            cell.getData().type = 'int32'
          }
          formData.content['type'] = cell.getData().type
        } else if (formData.id == 14) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['newName'] = cell.getData().newName
        } else if (formData.id == 15) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['computeType'] = cell.getData().computeType
          formData.content['computeNum'] = cell.getData().computeNum
        } else if (formData.id == 16) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['substituteMethod'] = cell.getData().substituteMethod
          formData.content['bySub'] = cell.getData().bySub
          formData.content['sub'] = cell.getData().sub
        } else if (formData.id == 17) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          if (cell.getData().fillMethod == undefined) {
            cell.getData().fillMethod = '均值'
          }
          formData.content['fillMethod'] = cell.getData().fillMethod
          formData.content['specificNum'] = cell.getData().specificNum
        } else if (formData.id == 18) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          formData.content['checked'] = cell.getData().checked
        } else if (formData.id == 19) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          formData.content['checked'] = cell.getData().checked
        } else if (formData.id == 20) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
        } else if (formData.id == 21) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['minNum'] = cell.getData().minNum
          formData.content['maxNum'] = cell.getData().maxNum
        } else if (formData.id == 22) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
        } else if (formData.id == 23) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
        } else if (formData.id == 24) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          if (cell.getData().numOfDuan == undefined) {
            cell.getData().numOfDuan = 5
          }
          formData.content['numOfDuan'] = cell.getData().numOfDuan
        } else if (formData.id == 25) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          if (cell.getData().numOfDuan == undefined) {
            cell.getData().numOfDuan = 5
          }
          formData.content['numOfDuan'] = cell.getData().numOfDuan
        } else if (formData.id == 26) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          if (cell.getData().numOfDuan == undefined) {
            cell.getData().numOfDuan = 5
          }
          formData.content['numOfDuan'] = cell.getData().numOfDuan
        } else if (formData.id == 27) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().numOfBox == undefined) {
            cell.getData().numOfBox = 10
          }
          formData.content['numOfBox'] = cell.getData().numOfBox
        } else if (formData.id == 28) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          formData.content['modelType'] = cell.getData().modelType
          if (cell.getData().numOfBox == undefined) {
            cell.getData().numOfBox = 10
          }
          formData.content['numOfBox'] = cell.getData().numOfBox
        } else if (formData.id == 29) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          if (cell.getData().numOfDim == undefined) {
            cell.getData().numOfDim = 2
          }
          formData.content['numOfDim'] = cell.getData().numOfDim
        } else if (formData.id == 30) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().numOfDim == undefined) {
            cell.getData().numOfDim = 2
          }
          formData.content['numOfDim'] = cell.getData().numOfDim
        } else if (formData.id == 31) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          if (cell.getData().checked1 == undefined) {
            cell.getData().checked1 = false
          }
          formData.content['checked'] = cell.getData().checked
          formData.content['checked1'] = cell.getData().checked1
        } else if (formData.id == 32) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().normalNum == undefined) {
            cell.getData().normalNum = 1
          }
          formData.content['normalNum'] = cell.getData().normalNum
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          if (cell.getData().checked1 == undefined) {
            cell.getData().checked1 = false
          }
          formData.content['checked'] = cell.getData().checked
          formData.content['checked1'] = cell.getData().checked1
        } else if (formData.id == 33) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().normalNum == undefined) {
            cell.getData().normalNum = 1
          }
          formData.content['normalNum'] = cell.getData().normalNum
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          if (cell.getData().checked1 == undefined) {
            cell.getData().checked1 = false
          }
          formData.content['checked'] = cell.getData().checked
          formData.content['checked1'] = cell.getData().checked1
        } else if (formData.id == 34) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().normalNum == undefined) {
            cell.getData().normalNum = 0.5
          }
          if (cell.getData().normalNum1 == undefined) {
            cell.getData().normalNum1 = 0.5
          }
          formData.content['normalNum'] = cell.getData().normalNum
          formData.content['normalNum1'] = cell.getData().normalNum1
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          if (cell.getData().checked1 == undefined) {
            cell.getData().checked1 = false
          }
          formData.content['checked'] = cell.getData().checked
          formData.content['checked1'] = cell.getData().checked1
        } else if (formData.id == 35) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().numberOfNeighbor == undefined) {
            cell.getData().numberOfNeighbor = 5
          }
          formData.content['numberOfNeighbor'] = cell.getData().numberOfNeighbor
          formData.content['weightType'] = cell.getData().weightType
          formData.content['distanceType'] = cell.getData().distanceType
        } else if (formData.id == 36) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().maxDepth == undefined) {
            cell.getData().maxDepth = 3
          }
          if (cell.getData().minSplit == undefined) {
            cell.getData().minSplit = 5
          }
          if (cell.getData().minLeaf == undefined) {
            cell.getData().minLeaf = 5
          }
          formData.content['maxDepth'] = cell.getData().maxDepth
          formData.content['minSplit'] = cell.getData().minSplit
          formData.content['minLeaf'] = cell.getData().minLeaf
        } else if (formData.id == 37) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          formData.content['bayesType'] = cell.getData().bayesType
          if (cell.getData().smooth == undefined) {
            cell.getData().smooth = 1.0
          }
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          if (cell.getData().binarization == undefined) {
            cell.getData().binarization = 1.0
          }
          formData.content['smooth'] = cell.getData().smooth
          formData.content['checked'] = cell.getData().checked
          formData.content['binarization'] = cell.getData().binarization
        } else if (formData.id == 38) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().normalNum == undefined) {
            cell.getData().normalNum = 1
          }
          if (cell.getData().checked == undefined) {
            cell.getData().checked = false
          }
          if (cell.getData().minConverge == undefined) {
            cell.getData().minConverge = 0.0001
          }
          if (cell.getData().maxIter == undefined) {
            cell.getData().maxIter = 1000
          }
          formData.content['normalNum'] = cell.getData().normalNum
          formData.content['minConverge'] = cell.getData().minConverge
          formData.content['maxIter'] = cell.getData().maxIter
          formData.content['checked'] = cell.getData().checked
        } else if (formData.id == 39) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().trainMaxError == undefined) {
            cell.getData().trainMaxError = 0.50
          }
          if (cell.getData().coef0 == undefined) {
            cell.getData().coef0 = 0.0
          }
          if (cell.getData().degree == undefined) {
            cell.getData().degree = 3
          }
          formData.content['trainMaxError'] = cell.getData().trainMaxError
          formData.content['coreFunction'] = cell.getData().coreFunction
          formData.content['gamma'] = cell.getData().gamma
          formData.content['coef0'] = cell.getData().coef0
          formData.content['degree'] = cell.getData().degree
          formData.content['classWeight'] = cell.getData().classWeight
        } else if (formData.id == 40) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().maxDepth == undefined) {
            cell.getData().maxDepth = 3
          }
          if (cell.getData().minSplit == undefined) {
            cell.getData().minSplit = 5
          }
          if (cell.getData().minLeaf == undefined) {
            cell.getData().minLeaf = 5
          }
          formData.content['maxDepth'] = cell.getData().maxDepth
          formData.content['minSplit'] = cell.getData().minSplit
          formData.content['minLeaf'] = cell.getData().minLeaf
        } else if (formData.id == 41) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          formData.content['normalItem'] = cell.getData().normalItem
          if (cell.getData().normalNum == undefined) {
            cell.getData().normalNum = 1
          }
          if (cell.getData().minConverge == undefined) {
            cell.getData().minConverge = 0.0001
          }
          if (cell.getData().randomState == undefined) {
            cell.getData().randomState = 10
          }
          formData.content['normalNum'] = cell.getData().normalNum
          formData.content['minConverge'] = cell.getData().minConverge
          formData.content['randomState'] = cell.getData().randomState
          formData.content['classWeight'] = cell.getData().classWeight
        } else if (formData.id == 42) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          if (cell.getData().numberOfNeighbor == undefined) {
            cell.getData().numberOfNeighbor = 5
          }
          formData.content['numberOfNeighbor'] = cell.getData().numberOfNeighbor
          formData.content['weightType'] = cell.getData().weightType
          formData.content['distanceType'] = cell.getData().distanceType
        } else if (formData.id == 43) {
          formData.content = {}
          formData.content['characterColumn'] = cell.getData().characterColumn
          formData.content['numOfCluster'] = cell.getData().numOfCluster ? cell.getData().numOfCluster : 8
          formData.content['centerInitial'] = cell.getData().centerInitial
          formData.content['initialTimes'] = cell.getData().initialTimes ? cell.getData().initialTimes : 10
          formData.content['maxIter'] = cell.getData().maxIter ? cell.getData().maxIter : 300
          formData.content['minConverge'] = cell.getData().minConverge ? cell.getData().minConverge : 0.0001
          formData.content['randomState'] = cell.getData().randomState ? cell.getData().randomState : 10
        } else if (formData.id == 49) {
          formData.content = {}
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          formData.content['checked'] = cell.getData().checked
          formData.content['checked1'] = cell.getData().checked1
          formData.content['checked2'] = cell.getData().checked2
          formData.content['checked3'] = cell.getData().checked3
          formData.content['checked4'] = cell.getData().checked4
          formData.content['checked5'] = cell.getData().checked5
          formData.content['checked6'] = cell.getData().checked6
          formData.content['checked7'] = cell.getData().checked7
          formData.content['checked8'] = cell.getData().checked8
        } else if (formData.id == 50) {
          formData.content = {}
          formData.content['characterColumn1'] = cell.getData().characterColumn1
          formData.content['positiveTag'] = cell.getData().positiveTag
        }
        // 实现列选择动态变化，根据上一个的表头显示
        if (cell.getData().lastOutput != undefined) {
          let columnValuesLabels = []
          Object.keys(cell.getData().lastOutput[0]).forEach((item) => {
            columnValuesLabels.push({value: item, label: item})
          })
          optionsCharacterColumns.value = columnValuesLabels
          optionsCharacterColumns1.value = columnValuesLabels
        }
      })
    }

    // 所有节点——name改变时
    function onNameChange() {
      curCell.getData().name = formData.name
      // console.log(curCell.getData())
    }

    // 1.读数据表
    const options_1 = ref<SelectProps['options']>([
      {value: 'show_yuanweihua', label: '鸢尾花数据集'},
      {value: 'show_graduateIncome', label: '大学毕业生收入数据集'},
    ]);

    // 1.读数据——搜索功能
    const filterOption = (input: string, option: any) => {
      return option.indexOf(input) >= 0;
    };

    // 1.读数据——数据集
    function onDataChange() {
      curCell.getData().dataSource = formData.content.dataSource
    }

    // 2.字段基本统计信息——统计列
    // 3.查看唯一值及数量——统计列
    // 4.数据相关性——选择列
    // 6.单变量异常值检测——检测列
    // 8.样本相似度计算——计算列
    // 9.列删除——删除列
    // 10.训练/测试集划分——标签列
    // 11.数字编码——编码列
    // 12.人工数字编码——编码列
    // 13.类型转换——转换列
    // 14.列重命名——选择列
    // 15.数据列计算——计算列
    // 16.数据值替换——替换列
    // 17.缺失值填补——填补列
    // 18.数据按列值排序——排序列
    // 19.OneHot编码——编码列
    // 20.Z-Score标准化——处理列
    // 21.Min-Max标准化——处理列
    // 22.Logistic标准化——处理列
    // 23.最大绝对值标准化——处理列
    // 24.等距离散化——处理列
    // 25.等频离散化——处理列
    // 26.Kmeans离散化——处理列
    // 27.卡方离散化——处理列
    // 28.决策树离散化——处理列
    // 29.主成分分析——特征列
    // 30.线性判别分析——特征列
    // 31.线性回归——特征列
    // 32.LASSO——特征列
    // 33.岭回归——特征列
    // 34.弹性网络——特征列
    // 35.K近邻回归——特征列
    // 36.回归决策树——特征列
    // 37.朴素贝叶斯——特征列
    // 38.线性SVC——特征列
    // 39.支持向量机——特征列
    // 40.分类决策树——特征列
    // 41.逻辑回归——特征列
    // 42.K近邻——特征列
    // 43.K-Means聚类——特征列
    function onCharacterChange() {
      curCell.getData().characterColumn = formData.content.characterColumn
    }

    // 10.训练/测试集划分——分层列
    // 27.卡方离散化——标签列
    // 28.决策树离散化——处理列
    // 30.线性判别分析——目标列
    // 31.线性回归——标签列
    // 32.LASSO——标签列
    // 33.岭回归——标签列
    // 34.弹性网络——标签列
    // 35.K近邻回归——标签列
    // 36.回归决策树——标签列
    // 37.朴素贝叶斯——标签列
    // 38.线性SVC——标签列
    // 39.支持向量机——标签列
    // 40.分类决策树——标签列
    // 41.逻辑回归——标签列
    // 42.K近邻——标签列
    // 49.回归模型评估——标签列
    // 50.分类模型评估——标签列
    function onCharacterChange1() {
      curCell.getData().characterColumn1 = formData.content.characterColumn1
    }

    // 4.数据相关性——相关性指标
    const options_4 = ref<SelectProps['options']>([
      {value: 'pearson', label: 'Pearson相关系数'},
      {value: 'kendall', label: 'Kendall相关系数'},
      {value: 'spearman', label: 'Spearman相关系数'},
    ]);

    // 4.数据相关性——相关性指标
    function onIndicatorChange() {
      curCell.getData().indicator = formData.content.indicator
    }

    // 5.缺失值检测——过滤缺失值
    // 6.单变量异常值检测——是否过滤异常值
    // 10.训练/测试集划分
    // 18.数据按列值排序——降序排列
    // 19.OneHot编码——删除首个取值
    // 31.线性回归——训练截距项
    // 32.LASSO——训练截距项
    // 33.岭回归——训练截距项
    // 34.弹性网络——训练截距项
    // 37.朴素贝叶斯——学习先验概率
    // 38.线性SVC——训练截距项
    // 49.回归模型评估——均方误差(MSE)
    function onCheckedChange() {
      curCell.getData().checked = formData.content.checked
    }

    // 31.线性回归——数据归一化
    // 32.LASSO——数据归一化
    // 33.岭回归——数据归一化
    // 34.弹性网络——数据归一化
    // 49.回归模型评估——平均绝对误差(MAE)
    function onCheckedChange1() {
      curCell.getData().checked1 = formData.content.checked1
    }

    // 6.单变量异常值检测——检测策略
    const options_6 = ref<SelectProps['options']>([
      {value: 'four', label: '四分位距'},
      {value: 'la', label: '拉伊达准则'},
    ]);

    // 6.单变量异常值检测——检测策略
    function onMethodChange() {
      curCell.getData().method = formData.content.method
    }

    // 8.样本相似度计算——相似度
    const options_8 = ref<SelectProps['options']>([
      {value: 'cos', label: '余弦距离'},
      {value: 'ou', label: '欧式距离'},
      {value: 'abs', label: '绝对值距离'},
    ]);

    // 8.样本相似度计算——相似度
    function onSimilarityChange() {
      curCell.getData().similarity = formData.content.similarity
    }

    // 10.训练/测试集划分——测试集大小
    function onTestSizeChange() {
      curCell.getData().testSize = formData.content.testSize
    }

    // 10.训练/测试集划分——采样随机数
    // 41.逻辑回归——随机种子
    // 43.K-Means聚类——随机种子
    function onRandomStateChange() {
      curCell.getData().randomState = formData.content.randomState
    }

    // 13.类型转换——转换为
    const options_13 = ref<SelectProps['options']>([
      {value: 'int32', label: 'int32'},
      {value: 'int64', label: 'int64'},
      {value: 'float32', label: 'float32'},
      {value: 'float64', label: 'float64'},
      {value: 'object', label: 'object'},
      {value: 'bool', label: 'bool'},
      {value: 'datetime64', label: 'datetime64'},
    ]);

    // 13.类型转换——转换列
    function onTypeChange() {
      curCell.getData().type = formData.content.type
    }

    // 14.列重命名——重命名为
    function onNewNameChange() {
      curCell.getData().newName = formData.content.newName
    }

    // 15.数据列计算——计算类型
    const options_15 = ref<SelectProps['options']>([
      {value: 'plus', label: '加'},
      {value: 'minus', label: '减'},
      {value: 'multiply', label: '乘'},
      {value: 'divide', label: '除'},
      {value: 'involution', label: '乘方'},
      {value: 'disinvolution', label: '开方'},
    ]);

    // 15.数据列计算——计算类型
    function onComputeTypeChange() {
      curCell.getData().computeType = formData.content.computeType
    }

    // 15.数据列计算——计算值
    function onComputeNumChange() {
      curCell.getData().computeNum = formData.content.computeNum
    }

    // 16.数据值替换——替换方式
    const options_16 = ref<SelectProps['options']>([
      {value: 'single', label: '单值替换'},
      {value: 'list', label: '列表替换'},
    ]);

    // 16.数据值替换——替换方式
    function onSubstituteMethodChange() {
      curCell.getData().substituteMethod = formData.content.substituteMethod
    }

    // 16.数据值替换——被替换值
    function onBySubChange() {
      curCell.getData().bySub = formData.content.bySub
    }

    // 16.数据值替换——替换值
    function onSubChange() {
      curCell.getData().sub = formData.content.sub
    }

    // 17.缺失值填补——填补策略
    const options_17 = ref<SelectProps['options']>([
      {value: 'mean', label: '均值'},
      {value: 'mode', label: '众数'},
      {value: 'median', label: '中位数'},
      {value: 'specific', label: '指定值'},
    ]);

    // 8.样本相似度计算——相似度
    function onFillMethodChange() {
      curCell.getData().fillMethod = formData.content.fillMethod
    }

    // 17.缺失值填补——填补值
    function onSpecificNumChange() {
      curCell.getData().specificNum = formData.content.specificNum
    }

    // 21.Min-Max标准化——最小值
    function onMinNumChange() {
      curCell.getData().minNum = formData.content.minNum
    }

    // 21.Min-Max标准化——最大值
    function onMaxNumChange() {
      curCell.getData().maxNum = formData.content.maxNum
    }

    // 24.等距离散化——分段数
    // 25.等距离散化——分段数
    // 26.Kmeans离散化——分段数
    function onNumOfDuanChange() {
      curCell.getData().numOfDuan = formData.content.numOfDuan
    }

    // 27.卡方离散化——最大分箱数
    // 28.决策树离散化——最大分箱数
    function onNumOfBoxChange() {
      curCell.getData().numOfBox = formData.content.numOfBox
    }

    // 28.决策树离散化——模型类型
    const options_28 = ref<SelectProps['options']>([
      {value: 'classification', label: '分类'},
      {value: 'regression', label: '回归'},
    ]);

    // 28.决策树离散化——模型类型
    function onModelTypeChange() {
      curCell.getData().modelType = formData.content.modelType
    }

    // 29.主成分分析——维数
    // 30.线性判别分析——维数
    function onNumOfDimChange() {
      curCell.getData().numOfDim = formData.content.numOfDim
    }

    // 32.LASSO——正则系数
    // 33.岭回归——正则系数
    // 34.弹性网络——正则系数1
    // 38.线性SVC——正则化系数
    // 41.逻辑回归——正则系数
    function onNormalNumChange() {
      curCell.getData().normalNum = formData.content.normalNum
    }

    // 34.弹性网络——正则系数2
    function onNormalNumChange1() {
      curCell.getData().normalNum1 = formData.content.normalNum1
    }

    // 35.K近邻回归——邻居个数
    // 42.K近邻——邻居个数
    function onNumberOfNeighborChange() {
      curCell.getData().numberOfNeighbor = formData.content.numberOfNeighbor
    }

    // 35.K近邻回归——权重计算方式
    // 42.K近邻——权重计算方式
    const options_35_1 = ref<SelectProps['options']>([
      {value: 'uniform', label: 'uniform'},
      {value: 'distance', label: 'distance'},
    ]);

    // 35.K近邻回归——权重计算方式
    // 42.K近邻——权重计算方式
    function onWeightTypeChange() {
      curCell.getData().weightType = formData.content.weightType
    }

    // 35.K近邻回归——距离计算方式
    // 42.K近邻——距离计算方式
    const options_35_2 = ref<SelectProps['options']>([
      {value: 'euclidean', label: 'euclidean'},
      {value: 'manhattan', label: 'manhattan'},
      {value: 'chebyshev', label: 'chebyshev'},
      {value: 'minkowski', label: 'minkowski'},
    ]);

    // 35.K近邻回归——距离计算方式
    // 42.K近邻——距离计算方式
    function onDistanceTypeChange() {
      curCell.getData().distanceType = formData.content.distanceType
    }

    // 36.回归决策树——最大树深度
    // 40.分类决策树——最大树深度
    function onMaxDepthChange() {
      curCell.getData().maxDepth = formData.content.maxDepth
    }

    // 36.回归决策树——分裂最少样本
    // 40.分类决策树——分裂最少样本
    function onMinSplitChange() {
      curCell.getData().minSplit = formData.content.minSplit
    }

    // 36.回归决策树——叶节点最少样本
    // 40.分类决策树——叶节点最少样本
    function onMinLeafChange() {
      curCell.getData().minLeaf = formData.content.minLeaf
    }

    // 37.朴素贝叶斯——贝叶斯分类器
    const options_37 = ref<SelectProps['options']>([
      {value: 'BernoulliNB', label: 'BernoulliNB'},
      {value: 'GaussianNB', label: 'GaussianNB'},
      {value: 'MultinomialNB', label: 'MultinomialNB'},
    ]);

    // 37.朴素贝叶斯——贝叶斯分类器
    function onBayesTypeChange() {
      curCell.getData().bayesType = formData.content.bayesType
    }

    // 37.朴素贝叶斯——平滑系数
    function onSmoothChange() {
      curCell.getData().smooth = formData.content.smooth
    }

    // 37.朴素贝叶斯——二值化阈值
    function onBinarizationChange() {
      curCell.getData().binarization = formData.content.binarization
    }

    // 38.线性SVC——最小收敛数
    // 41.逻辑回归——收敛系数
    // 43.K-Means聚类——最小收敛值
    function onMinConvergeChange() {
      curCell.getData().minConverge = formData.content.minConverge
    }

    // 38.线性SVC——最大迭代数
    // 43.K-Means聚类——最大迭代数
    function onMaxIterChange() {
      curCell.getData().maxIter = formData.content.maxIter
    }

    // 39.支持向量机——训练错误率上限
    function onTrainMaxErrorChange() {
      curCell.getData().trainMaxError = formData.content.trainMaxError
    }

    // 39.支持向量机——核函数
    const options_39_1 = ref<SelectProps['options']>([
      {value: 'rbf', label: 'rbf'},
      {value: 'poly', label: 'poly'},
      {value: 'sigmoid', label: 'sigmoid'},
    ]);

    // 39.支持向量机——核函数
    function onCoreFunctionChange() {
      curCell.getData().coreFunction = formData.content.coreFunction
    }

    // 39.支持向量机——gamma
    const options_39_2 = ref<SelectProps['options']>([
      {value: 'scale', label: 'scale'},
      {value: 'auto', label: 'auto'},
    ]);

    // 39.支持向量机——gamma
    function onGammaChange() {
      curCell.getData().gamma = formData.content.gamma
    }

    // 39.支持向量机——coef0
    function onCoef0Change() {
      curCell.getData().coef0 = formData.content.coef0
    }

    // 39.支持向量机——degree
    function onDegreeChange() {
      curCell.getData().degree = formData.content.degree
    }

    // 39.支持向量机——类别权重
    // 41.逻辑回归——类别权重
    const options_39_3 = ref<SelectProps['options']>([
      {value: 'None', label: 'None'},
      {value: 'balanced', label: 'Balanced'},
    ]);

    // 39.支持向量机——类别权重
    // 41.逻辑回归——类别权重
    function onClassWeightChange() {
      curCell.getData().classWeight = formData.content.classWeight
    }

    // 41.逻辑回归——正则化项
    const options_41 = ref<SelectProps['options']>([
      {value: 'l1', label: 'L1'},
      {value: 'l2', label: 'L2'},
      {value: 'elasticNet', label: 'ElasticNet'},
      {value: 'None', label: 'None'},
    ]);

    // 41.逻辑回归——正则化项
    function onNormalItemChange() {
      curCell.getData().normalItem = formData.content.normalItem
    }

    // 43.K-Means聚类——聚类数
    function onNumOfClusterChange() {
      curCell.getData().numOfCluster = formData.content.numOfCluster
    }

    // 43.K-Means聚类——质心初始化
    const options_43 = ref<SelectProps['options']>([
      {value: 'kmeans', label: 'k-means++'},
      {value: 'random', label: 'random'},
    ]);

    // 43.K-Means聚类——质心初始化
    function onCenterInitialChange() {
      curCell.getData().centerInitial = formData.content.centerInitial
    }

    // 43.K-Means聚类——初始化次数
    function onInitialTimesChange() {
      curCell.getData().initialTimes = formData.content.initialTimes
    }

    // 49.回归模型评估——决定系数(R2)
    function onCheckedChange2() {
      curCell.getData().checked2 = formData.content.checked2
    }

    // 49.回归模型评估——中位绝对误差
    function onCheckedChange3() {
      curCell.getData().checked3 = formData.content.checked3
    }

    // 49.回归模型评估——解释方差
    function onCheckedChange4() {
      curCell.getData().checked4 = formData.content.checked4
    }

    // 49.回归模型评估——最大误差
    function onCheckedChange5() {
      curCell.getData().checked5 = formData.content.checked5
    }

    // 49.回归模型评估——平均泊松偏差
    function onCheckedChange6() {
      curCell.getData().checked6 = formData.content.checked6
    }

    // 49.回归模型评估——平均伽马偏差
    function onCheckedChange7() {
      curCell.getData().checked7 = formData.content.checked7
    }

    // 49.回归模型评估——平均Tweedie偏差
    function onCheckedChange8() {
      curCell.getData().checked8 = formData.content.checked8
    }

    // 50.分类模型评估——正类标签
    function onPositiveTagChange8() {
      curCell.getData().positiveTag = formData.content.positiveTag
    }

    // 控制数据选择页面
    const visible = ref<boolean>(false)

    function showModal() {
      visible.value = true
    }

    const handleOk = (e: MouseEvent) => {
      visible.value = false;
    };

    const tableData: User[] = [
      {
        key: 1,
        dataName: '鸢尾花数据集',
        dataId: 1,
        backendName: 'yuanweihua'
      },
      {
        key: 2,
        dataName: '大学毕业生收入数据集',
        dataId: 2,
        backendName: 'graduateIncome'
      },
    ]
    const columns = [
      {
        title: 'dataName',
        dataIndex: 'dataName',
      }
    ];

    return {
      tableData,
      columns,
      visible,
      showModal,
      handleOk,
      formData,
      filterOption,
      options_1,
      options_4,
      options_6,
      options_8,
      options_13,
      options_15,
      options_16,
      options_17,
      options_28,
      options_35_1,
      options_35_2,
      options_37,
      options_39_1,
      options_39_2,
      options_39_3,
      options_41,
      options_43,
      optionsCharacterColumns,
      optionsCharacterColumns1,
      dialogTableVisible,
      dialogContent,
      onNameChange,
      onDataChange,
      onCharacterChange,
      onIndicatorChange,
      onCheckedChange,
      onCheckedChange1,
      onMethodChange,
      onSimilarityChange,
      onTestSizeChange,
      onRandomStateChange,
      onTypeChange,
      onNewNameChange,
      onComputeTypeChange,
      onComputeNumChange,
      onSubstituteMethodChange,
      onBySubChange,
      onSubChange,
      onFillMethodChange,
      onSpecificNumChange,
      onMinNumChange,
      onMaxNumChange,
      onNumOfDuanChange,
      onCharacterChange1,
      onNumOfBoxChange,
      onModelTypeChange,
      onNumOfDimChange,
      onNormalNumChange,
      onNormalNumChange1,
      onNumberOfNeighborChange,
      onWeightTypeChange,
      onDistanceTypeChange,
      onMaxDepthChange,
      onMinSplitChange,
      onMinLeafChange,
      onBayesTypeChange,
      onSmoothChange,
      onBinarizationChange,
      onMinConvergeChange,
      onMaxIterChange,
      onTrainMaxErrorChange,
      onCoreFunctionChange,
      onGammaChange,
      onCoef0Change,
      onDegreeChange,
      onClassWeightChange,
      onNormalItemChange,
      onNumOfClusterChange,
      onCenterInitialChange,
      onInitialTimesChange,
      onCheckedChange2,
      onCheckedChange3,
      onCheckedChange4,
      onCheckedChange5,
      onCheckedChange6,
      onCheckedChange7,
      onCheckedChange8,
      onPositiveTagChange8,
      openId4,
      openId10,
      openId29,
      openId30,
      openId36,
    }
  },
  methods: {
    onSelectChange(selectedRowKeys, selectionRows) {
      this.data.dataBase = []
      this.data.dataColumns = []
      this.selectedRowKeys = selectedRowKeys
      this.selectedRows = selectionRows
      this.selectedRowName = selectionRows[0].dataName
      formData.content.dataSource = selectionRows[0].dataName

      axios.get('http://127.0.0.1:8000/api/' + 'show_' + selectionRows[0].backendName).then(res => {
        console.log(res)
        if (res.statusText === 'OK') {
          const data = res.data.list
          this.data.dataBase = data
          this.data.dataColumns = Object.keys(data[0])
          this.showData = true
        }
      })
    },
  },
  computed: {
    selectWidth(){
      return (window.innerWidth)*5/24 - 84 - 20 - 10 + 'px'
    },
    numberWidth(){
      return (window.innerWidth)*5/24 - 112 - 20 - 10 + 'px'
    }
  }
})
</script>

<style scoped lang="scss">
</style>