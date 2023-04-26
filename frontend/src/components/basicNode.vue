<template>
  <div class="node" :class="status" @click.stop v-if="['success', 'failed'].includes(status)" @contextmenu="rightClickFinish">
    <img :src="image.logo" />
    <span class="label">{{ label }}</span>
    <span class="status" v-if="status === 'success'">
        <img :src="image.success"/>
    </span>
    <span class="status" v-else-if="status === 'failed'">
        <img :src="image.failed" />
    </span>
  </div>
  <div class="node" :class="status" @click.stop v-else-if="['running', 'default'].includes(status)" @contextmenu="rightClick">
    <img :src="image.logo" />
    <span class="label">{{ label }}</span>
    <span class="status" v-if="status === 'running'">
        <img :src="image.running" />
    </span>
  </div>

</template>

<script lang="ts">
import { menusEvent } from 'vue3-menus'
import {reactive, ref} from "vue"
import axios from "axios";
import {Cell, Graph} from "@antv/x6";
import {SelectProps} from "ant-design-vue";


interface NodeStatus {
  id: string
  status: 'default' | 'success' | 'failed' | 'running'
  label?: string
}

let optionsCharacterColumns = ref<SelectProps['options']>([]);
let optionsCharacterColumns1 = ref<SelectProps['options']>([]);

export default {
  name: "basicNode",
  inject: ['getNode'],
  props: {
    graph: Graph
  },
  data() {
    //console.log(this)
    return {
      status: 'default',
      label: '基础节点',
      image: {
        logo: 'https://gw.alipayobjects.com/mdn/rms_43231b/afts/img/A*evDjT5vjkX0AAAAAAAAAAAAAARQnAQ',
        success:
            'https://gw.alipayobjects.com/mdn/rms_43231b/afts/img/A*6l60T6h8TTQAAAAAAAAAAAAAARQnAQ',
        failed:
            'https://gw.alipayobjects.com/mdn/rms_43231b/afts/img/A*SEISQ6My-HoAAAAAAAAAAAAAARQnAQ',
        running:
            'https://gw.alipayobjects.com/mdn/rms_43231b/afts/img/A*t8fURKfgSOgAAAAAAAAAAAAAARQnAQ',
      },
      menus: [
        {
          label: "运行",
          click: () => {
            // console.log(this)
            if(this.getNode().getData().id == 1){
                // 先设置为running状态
                this.getNode().setData({
                  ...(this.getNode().getData() as NodeStatus),
                  status: 'running',
                })
                // 模拟请求数据库
                console.log('正在请求数据库')
                let dataNameToSource = {
                  '鸢尾花数据集': 'show_yuanweihua',
                  '大学毕业生收入数据集': 'show_graduateIncome'
                }
                axios.get('http://127.0.0.1:8000/api/' + dataNameToSource[this.getNode().getData().dataSource]).then(res => {
                  console.log(res)
                  // 请求成功则将数据中的fields字段拿出来赋值给dataBase字段，并改变状态为success
                  if(res.statusText === 'OK'){
                    // const data = []
                    // res.data.list.forEach((item)=>{
                    //   data.push(item.fields)
                    // })
                    const data = res.data.list

                    // 同时设置供选择的特征列
                    let columnValuesLabels = []
                    Object.keys(data[0]).forEach((item)=>{
                      columnValuesLabels.push({value:item, label:item})
                    })
                    optionsCharacterColumns.value = columnValuesLabels;
                    // 向父组件传递数据
                    this.$emit('columns', optionsCharacterColumns.value)
                    // 向父组件传递数据
                    optionsCharacterColumns1.value = columnValuesLabels;
                    this.$emit('columns1', optionsCharacterColumns1.value)

                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'success',
                      dataBase: data,
                      dataId: res.data.dataId,
                      dataColumns: Object.keys(data[0]),
                    }, {overwrite: true})
                    // console.log(this.getNode().getData())
                  }
                }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
              } else {
                // 先将状态设置为running
                this.getNode().setData({
                  ...(this.getNode().getData() as NodeStatus),
                  status: 'running',
                })
                // 获取前cell的数据
                // const frontCell: Cell = this.graph.getIncomingEdges(this.getNode())[0].getSourceCell()
                // // 如果上个cell有输出，则直接拿过来
                // if(frontCell.getData().hasOwnProperty('output')){
                //   this.getNode().setData({
                //       ...(this.getNode().getData() as NodeStatus),
                //       lastOutput: frontCell.getData().output,
                //   })
                // // 上个cell没有输出，取他的dataId，去数据库中取数据
                // } else {
                //   const dataId = frontCell.getData().dataId
                //   this.getNode().setData({
                //       ...(this.getNode().getData() as NodeStatus),
                //       dataId: dataId,
                //   })
                // }
                // 将获取到的数据和模型参数传回后端进行运算
                console.log('正在请求后端服务')

                if(this.getNode().getData().id == 2){
                  axios.post('http://127.0.0.1:8000/api/summary', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 3.查看唯一值及数量
                else if(this.getNode().getData().id == 3){
                  axios.post('http://127.0.0.1:8000/api/unique_amount', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0])
                      })
                      console.log(this.getNode().getData().result)
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 4.数据相关性
                else if(this.getNode().getData().id == 4){
                  axios.post('http://127.0.0.1:8000/api/relation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0])
                      })
                      console.log(this.getNode().getData().result)
                    }
                    ///////// 绘制热力图

                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 5.过滤缺失值
                else if(this.getNode().getData().id == 5){
                  axios.post('http://127.0.0.1:8000/api/filter_loss', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        hasLossRows: res.data.has_loss_rows
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 6.单变量异常值检测
                else if(this.getNode().getData().id == 6){
                  axios.post('http://127.0.0.1:8000/api/filter_queer', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        queer_data_num: res.data.queer_data_num,
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 7.重复值检测
                else if(this.getNode().getData().id == 7){
                  axios.post('http://127.0.0.1:8000/api/filter_repeat', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        repeat_data_num: res.data.repeat_data_num,
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 8.样本相似度计算
                else if(this.getNode().getData().id == 8){
                  axios.post('http://127.0.0.1:8000/api/sample_similarity', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0])
                      })
                      console.log(this.getNode().getData().result)
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 9.删除列
                else if(this.getNode().getData().id == 9){
                  axios.post('http://127.0.0.1:8000/api/delete_columns', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData().result)
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 10.训练/测试集划分
                else if(this.getNode().getData().id == 10){
                  axios.post('http://127.0.0.1:8000/api/preprocess_train_test_split', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        train_df: res.data.train_table,
                        test_df: res.data.test_table,
                      })

                      ///////////////////画饼状图
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 11.数字编码
                else if(this.getNode().getData().id == 11){
                  axios.post('http://127.0.0.1:8000/api/digital_coding', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 13.类型转换
                else if(this.getNode().getData().id == 13){
                  axios.post('http://127.0.0.1:8000/api/type_change', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 14.列重命名
                else if(this.getNode().getData().id == 14){
                  axios.post('http://127.0.0.1:8000/api/name_change', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 15.数据列计算
                else if(this.getNode().getData().id == 15){
                  axios.post('http://127.0.0.1:8000/api/compute_column', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 16.数据值替换
                else if (this.getNode().getData().id == 16){
                  axios.post('http://127.0.0.1:8000/api/preprocess_replace_value', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 17.缺失值填补
                else if (this.getNode().getData().id == 17){
                  axios.post('http://127.0.0.1:8000/api/preprocess_fillna', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 18.数据按列值排序
                else if (this.getNode().getData().id == 18){
                  axios.post('http://127.0.0.1:8000/api/preprocess_sort_by_value', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 19.Onehot编码
                else if (this.getNode().getData().id == 19){
                  axios.post('http://127.0.0.1:8000/api/onehot', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData().result)
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 20.Z-Score标准化
                else if (this.getNode().getData().id == 20){
                  axios.post('http://127.0.0.1:8000/api/z_score_regulation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 21.Min-Max标准化
                else if (this.getNode().getData().id == 21){
                  axios.post('http://127.0.0.1:8000/api/min_max_regulation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 22.Logistic标准化
                else if (this.getNode().getData().id == 22){
                  axios.post('http://127.0.0.1:8000/api/logistic_regulation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 23.最大绝对值标准化
                else if (this.getNode().getData().id == 23){
                  axios.post('http://127.0.0.1:8000/api/max_abs_regulation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 24.等距离散化
                else if (this.getNode().getData().id == 24){
                  axios.post('http://127.0.0.1:8000/api/isometric_dispersion', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 25.等频离散化
                else if (this.getNode().getData().id == 25){
                  axios.post('http://127.0.0.1:8000/api/equal_freq_discretization', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 26.Kmeans离散化
                else if (this.getNode().getData().id == 26){
                  axios.post('http://127.0.0.1:8000/api/kmeans_discretization', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 27.卡方离散化
                else if (this.getNode().getData().id == 27){
                  axios.post('http://127.0.0.1:8000/api/kafang_discretization', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 28.决策树离散化
                else if (this.getNode().getData().id == 28){
                  axios.post('http://127.0.0.1:8000/api/decision_tree_discretization', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 29.主成分分析
                else if (this.getNode().getData().id == 29){
                  axios.post('http://127.0.0.1:8000/api/PCA_reduce_dim', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                        ratios: res.data.ratios
                      })
                      /////////////////// 画柱状图
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 30.线性判别分析
                else if (this.getNode().getData().id == 30){
                  axios.post('http://127.0.0.1:8000/api/linear_reduce_dim', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                        ratios: res.data.ratios
                      })
                      /////////////////// 画柱状图
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 31.线性回归
                else if (this.getNode().getData().id == 31){
                  axios.post('http://127.0.0.1:8000/api/linear_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        intercept: res.data.intercept,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 32.LASSO回归
                else if (this.getNode().getData().id == 32){
                  axios.post('http://127.0.0.1:8000/api/lasso_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        intercept: res.data.intercept,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 33.岭回归
                else if (this.getNode().getData().id == 33){
                  axios.post('http://127.0.0.1:8000/api/ridge_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        intercept: res.data.intercept,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 34.弹性网络
                else if (this.getNode().getData().id == 34){
                  axios.post('http://127.0.0.1:8000/api/elastic_net', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        intercept: res.data.intercept,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 35.K近邻回归
                else if (this.getNode().getData().id == 35){
                  axios.post('http://127.0.0.1:8000/api/knn_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 36.决策树回归
                else if (this.getNode().getData().id == 36){
                  axios.post('http://127.0.0.1:8000/api/decision_tree_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        tree: res.data.tree,
                        model: res.data.model
                      })
                      ////////////////// 画柱状图和树
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 37.朴素贝叶斯
                else if (this.getNode().getData().id == 37){
                  axios.post('http://127.0.0.1:8000/api/naive_bayes', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 38.线性SVC
                else if (this.getNode().getData().id == 38){
                  axios.post('http://127.0.0.1:8000/api/linear_SVC', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        coef: res.data.coef,
                        coefDataColumns: Object.keys(res.data.coef[0]),
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 39.支持向量机
                else if (this.getNode().getData().id == 39){
                  axios.post('http://127.0.0.1:8000/api/SVM_classification', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        n_support: res.data.n_support,
                        n_supportDataColumns: Object.keys(res.data.n_support[0]),
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 40.分类决策树
                else if (this.getNode().getData().id == 40){
                  axios.post('http://127.0.0.1:8000/api/decision_tree_classification', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        tree: res.data.tree,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 41.逻辑回归
                else if (this.getNode().getData().id == 41){
                  axios.post('http://127.0.0.1:8000/api/logistic_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 42.K近邻
                else if (this.getNode().getData().id == 42){
                  axios.post('http://127.0.0.1:8000/api/knn_classification', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
              }
          }
        },
        {
          label: "删除",
          click: () => {
            this.getNode().remove()
          }
        }
      ],
      menus_finish: [
        {
          label: "运行",
          click: () => {
            // console.log(this)
            if(this.getNode().getData().id == 1){
                // 先设置为running状态
                this.getNode().setData({
                  ...(this.getNode().getData() as NodeStatus),
                  status: 'running',
                })
                // 模拟请求数据库
                console.log('正在请求数据库')
                let dataNameToSource = {
                  '鸢尾花数据集': 'show_yuanweihua',
                  '大学毕业生收入数据集': 'show_graduateIncome'
                }
                axios.get('http://127.0.0.1:8000/api/' + dataNameToSource[this.getNode().getData().dataSource]).then(res => {
                  console.log(res)
                  // 请求成功则将数据中的fields字段拿出来赋值给dataBase字段，并改变状态为success
                  if(res.statusText === 'OK'){
                    // const data = []
                    // res.data.list.forEach((item)=>{
                    //   data.push(item.fields)
                    // })
                    const data = res.data.list

                    // 同时设置供选择的特征列
                    let columnValuesLabels = []
                    Object.keys(data[0]).forEach((item)=>{
                      columnValuesLabels.push({value:item, label:item})
                    })
                    optionsCharacterColumns.value = columnValuesLabels;
                    // 向父组件传递数据
                    this.$emit('columns', optionsCharacterColumns.value)
                    // 向父组件传递数据
                    optionsCharacterColumns1.value = columnValuesLabels;
                    this.$emit('columns1', optionsCharacterColumns1.value)

                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'success',
                      dataBase: data,
                      dataId: res.data.dataId,
                      dataColumns: Object.keys(data[0]),
                    }, {overwrite: true})
                    // console.log(this.getNode().getData())
                  }
                }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
              } else {
                // 先将状态设置为running
                this.getNode().setData({
                  ...(this.getNode().getData() as NodeStatus),
                  status: 'running',
                })
                // 获取前cell的数据
                // const frontCell: Cell = this.graph.getIncomingEdges(this.getNode())[0].getSourceCell()
                // // 如果上个cell有输出，则直接拿过来
                // if(frontCell.getData().hasOwnProperty('output')){
                //   this.getNode().setData({
                //       ...(this.getNode().getData() as NodeStatus),
                //       lastOutput: frontCell.getData().output,
                //   })
                // // 上个cell没有输出，取他的dataId，去数据库中取数据
                // } else {
                //   const dataId = frontCell.getData().dataId
                //   this.getNode().setData({
                //       ...(this.getNode().getData() as NodeStatus),
                //       dataId: dataId,
                //   })
                // }
                // 将获取到的数据和模型参数传回后端进行运算
                console.log('正在请求后端服务')

                if(this.getNode().getData().id == 2){
                  axios.post('http://127.0.0.1:8000/api/summary', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 3.查看唯一值及数量
                else if(this.getNode().getData().id == 3){
                  axios.post('http://127.0.0.1:8000/api/unique_amount', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0])
                      })
                      console.log(this.getNode().getData().result)
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 4.数据相关性
                else if(this.getNode().getData().id == 4){
                  axios.post('http://127.0.0.1:8000/api/relation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0])
                      })
                      console.log(this.getNode().getData().result)
                    }
                    ///////// 绘制热力图

                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 5.过滤缺失值
                else if(this.getNode().getData().id == 5){
                  axios.post('http://127.0.0.1:8000/api/filter_loss', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        hasLossRows: res.data.has_loss_rows
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 6.单变量异常值检测
                else if(this.getNode().getData().id == 6){
                  axios.post('http://127.0.0.1:8000/api/filter_queer', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        queer_data_num: res.data.queer_data_num,
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 7.重复值检测
                else if(this.getNode().getData().id == 7){
                  axios.post('http://127.0.0.1:8000/api/filter_repeat', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        repeat_data_num: res.data.repeat_data_num,
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 8.样本相似度计算
                else if(this.getNode().getData().id == 8){
                  axios.post('http://127.0.0.1:8000/api/sample_similarity', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0])
                      })
                      console.log(this.getNode().getData().result)
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 9.删除列
                else if(this.getNode().getData().id == 9){
                  axios.post('http://127.0.0.1:8000/api/delete_columns', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData().result)
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 10.训练/测试集划分
                else if(this.getNode().getData().id == 10){
                  axios.post('http://127.0.0.1:8000/api/preprocess_train_test_split', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        train_df: res.data.train_table,
                        test_df: res.data.test_table,
                      })

                      ///////////////////画饼状图
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 11.数字编码
                else if(this.getNode().getData().id == 11){
                  axios.post('http://127.0.0.1:8000/api/digital_coding', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 13.类型转换
                else if(this.getNode().getData().id == 13){
                  axios.post('http://127.0.0.1:8000/api/type_change', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 14.列重命名
                else if(this.getNode().getData().id == 14){
                  axios.post('http://127.0.0.1:8000/api/name_change', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 15.数据列计算
                else if(this.getNode().getData().id == 15){
                  axios.post('http://127.0.0.1:8000/api/compute_column', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 16.数据值替换
                else if (this.getNode().getData().id == 16){
                  axios.post('http://127.0.0.1:8000/api/preprocess_replace_value', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 17.缺失值填补
                else if (this.getNode().getData().id == 17){
                  axios.post('http://127.0.0.1:8000/api/preprocess_fillna', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 18.数据按列值排序
                else if (this.getNode().getData().id == 18){
                  axios.post('http://127.0.0.1:8000/api/preprocess_sort_by_value', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 19.Onehot编码
                else if (this.getNode().getData().id == 19){
                  axios.post('http://127.0.0.1:8000/api/onehot', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData().result)
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 20.Z-Score标准化
                else if (this.getNode().getData().id == 20){
                  axios.post('http://127.0.0.1:8000/api/z_score_regulation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 21.Min-Max标准化
                else if (this.getNode().getData().id == 21){
                  axios.post('http://127.0.0.1:8000/api/min_max_regulation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 22.Logistic标准化
                else if (this.getNode().getData().id == 22){
                  axios.post('http://127.0.0.1:8000/api/logistic_regulation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 23.最大绝对值标准化
                else if (this.getNode().getData().id == 23){
                  axios.post('http://127.0.0.1:8000/api/max_abs_regulation', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 24.等距离散化
                else if (this.getNode().getData().id == 24){
                  axios.post('http://127.0.0.1:8000/api/isometric_dispersion', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 25.等频离散化
                else if (this.getNode().getData().id == 25){
                  axios.post('http://127.0.0.1:8000/api/equal_freq_discretization', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 26.Kmeans离散化
                else if (this.getNode().getData().id == 26){
                  axios.post('http://127.0.0.1:8000/api/kmeans_discretization', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 27.卡方离散化
                else if (this.getNode().getData().id == 27){
                  axios.post('http://127.0.0.1:8000/api/kafang_discretization', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 28.决策树离散化
                else if (this.getNode().getData().id == 28){
                  axios.post('http://127.0.0.1:8000/api/decision_tree_discretization', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 29.主成分分析
                else if (this.getNode().getData().id == 29){
                  axios.post('http://127.0.0.1:8000/api/PCA_reduce_dim', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                        ratios: res.data.ratios
                      })
                      /////////////////// 画柱状图
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 30.线性判别分析
                else if (this.getNode().getData().id == 30){
                  axios.post('http://127.0.0.1:8000/api/linear_reduce_dim', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        output: res.data.output,
                        dataColumns1: Object.keys(res.data.output[0]),
                        ratios: res.data.ratios
                      })
                      /////////////////// 画柱状图
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 31.线性回归
                else if (this.getNode().getData().id == 31){
                  axios.post('http://127.0.0.1:8000/api/linear_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        intercept: res.data.intercept,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 32.LASSO回归
                else if (this.getNode().getData().id == 32){
                  axios.post('http://127.0.0.1:8000/api/lasso_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        intercept: res.data.intercept,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 33.岭回归
                else if (this.getNode().getData().id == 33){
                  axios.post('http://127.0.0.1:8000/api/ridge_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        intercept: res.data.intercept,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 34.弹性网络
                else if (this.getNode().getData().id == 34){
                  axios.post('http://127.0.0.1:8000/api/elastic_net', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        intercept: res.data.intercept,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 35.K近邻回归
                else if (this.getNode().getData().id == 35){
                  axios.post('http://127.0.0.1:8000/api/knn_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 36.决策树回归
                else if (this.getNode().getData().id == 36){
                  axios.post('http://127.0.0.1:8000/api/decision_tree_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        tree: res.data.tree,
                        model: res.data.model
                      })
                      ////////////////// 画柱状图和树
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 37.朴素贝叶斯
                else if (this.getNode().getData().id == 37){
                  axios.post('http://127.0.0.1:8000/api/naive_bayes', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 38.线性SVC
                else if (this.getNode().getData().id == 38){
                  axios.post('http://127.0.0.1:8000/api/linear_SVC', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        coef: res.data.coef,
                        coefDataColumns: Object.keys(res.data.coef[0]),
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 39.支持向量机
                else if (this.getNode().getData().id == 39){
                  axios.post('http://127.0.0.1:8000/api/SVM_classification', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        n_support: res.data.n_support,
                        n_supportDataColumns: Object.keys(res.data.n_support[0]),
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 40.分类决策树
                else if (this.getNode().getData().id == 40){
                  axios.post('http://127.0.0.1:8000/api/decision_tree_classification', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        tree: res.data.tree,
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 41.逻辑回归
                else if (this.getNode().getData().id == 41){
                  axios.post('http://127.0.0.1:8000/api/logistic_regression', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
                // 42.K近邻
                else if (this.getNode().getData().id == 42){
                  axios.post('http://127.0.0.1:8000/api/knn_classification', this.getNode().getData()).then(res => {
                    console.log(res)
                    if(res.statusText === 'OK'){
                      this.getNode().setData({
                        ...(this.getNode().getData() as NodeStatus),
                        status: 'success',
                        result: res.data.result,
                        dataColumns: Object.keys(res.data.result[0]),
                        model: res.data.model
                      })
                      console.log(this.getNode().getData())
                    }
                  }).catch(error => {
                    this.getNode().setData({
                      ...(this.getNode().getData() as NodeStatus),
                      status: 'failed',
                    })
                    console.log(this.getNode())
                    console.log(error)
                  })
                }
              }
          }
        },
          {
          label: "查看运行结果",
          click: () => {
            this.$emit('showInfo', {showBasicInfo: true, info: this.getNode().getData()})
          }
        },
        {
          label: "删除",
          click: () => {
            this.getNode().remove()
          }
        }
      ]
    }
  },
  mounted() {
    const node = this.getNode()
    const data = node?.getData() as NodeStatus
    const { label, status = 'default' } = data
    this.label = label
    this.status = status

    // 必须有，监听数据变化
    node.on("change:data", ({ current }) => {
      this.label = current.label
      this.status = current.status
    });
  },
  methods: {
    rightClick(event) {
      menusEvent(event, this.menus);
      event.preventDefault();
    },
    rightClickFinish(event) {
      menusEvent(event, this.menus_finish);
      event.preventDefault();
    }
  },
}
</script>

<style scoped>
.node {
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: #fff;
  border: 1px solid #c2c8d5;
  border-left: 4px solid #5F95FF;
  border-radius: 4px;
  box-shadow: 0 2px 5px 1px rgba(0, 0, 0, 0.06);
}
.node img {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  margin-left: 8px;
}
.node .label {
  display: inline-block;
  flex-shrink: 0;
  width: 104px;
  margin-left: 8px;
  color: #666;
  font-size: 12px;
}
.node .status {
  flex-shrink: 0;
}
.node.success {
  border-left: 4px solid #52c41a;
}
.node.failed {
  border-left: 4px solid #ff4d4f;
}
.node.running .status img {
  animation: spin 1s linear infinite;
}
.x6-node-selected .node {
  border-color: #1890ff;
  border-radius: 2px;
  box-shadow: 0 0 0 4px #d4e8fe;
}
.x6-node-selected .node.success {
  border-color: #52c41a;
  border-radius: 2px;
  box-shadow: 0 0 0 4px #ccecc0;
}
.x6-node-selected .node.failed {
  border-color: #ff4d4f;
  border-radius: 2px;
  box-shadow: 0 0 0 4px #fedcdc;
}
.x6-edge:hover path:nth-child(2){
  stroke: #1890ff;
  stroke-width: 1px;
}

.x6-edge-selected path:nth-child(2){
  stroke: #1890ff;
  stroke-width: 1.5px !important;
}

@keyframes running-line {
  to {
    stroke-dashoffset: -1000;
  }
}
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>