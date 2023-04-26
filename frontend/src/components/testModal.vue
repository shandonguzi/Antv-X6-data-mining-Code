<template>
  <a-button @click="showModal">aaaaaa</a-button>
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
        <el-table :data="data.dataBase.slice(0, 20)" style="margin-left: 20px; margin-top: 30px" max-height="600px"
                  :header-cell-style="{background: '#edf6ff', color: '#606266'}" empty-text="暂无数据">
          <el-table-column v-for="(item ,i) in data.dataColumns" :key="i" :property="item" :label="item" />
        </el-table>
      </div>
    </div>
  </a-modal>
</template>

<script lang="ts">
import {ref, defineComponent, Ref, reactive} from "vue";
import axios from "axios";

interface User {
  key: number
  dataName: string
  dataId: number
}


export default defineComponent({
  name: "testModal",
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
    let visible = ref(false)
    const showModal = () => {
      visible.value = true
    }
    const handleOk = () => {
      visible.value = false
    }

    const tableData: User[] = [
      {
        key: 1,
        dataName: '鸢尾花数据集',
        dataId: 2
      },
      {
        key: 2,
        dataName: '信贷数据集',
        dataId: 3,
      },
    ]
    const columns = [
      {
        title: 'dataName',
        dataIndex: 'dataName',
      }
    ];

    return {
      visible,
      showModal,
      handleOk,
      tableData,
      columns
    }
  },
  methods: {
    onSelectChange(selectedRowKeys, selectionRows) {
      this.selectedRowKeys = selectedRowKeys
      this.selectedRows = selectionRows
      this.selectedRowName = selectionRows[0].dataName
      axios.get('http://127.0.0.1:8000/api/' + 'show_yuanweihua').then(res => {
        console.log(res)
        if (res.statusText === 'OK') {
          const data = []
          res.data.list.forEach((item) => {
            data.push(item.fields)
          })
          this.data.dataBase = data
          this.data.dataColumns = Object.keys(data[0])
          this.showData = true
        }
      })
    },
  }
})
</script>

<style scoped>

</style>