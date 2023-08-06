//处理自定义方法字段和对话框

Vue.component('HtmlRender', {
    props: ['html'],
    mounted() {
        //调用vue来渲染
        try {
            let res = Vue.compile(`<div>${this.html}</div>`);
            new Vue({
                el: this.$el,
                render: res.render,
                staticRenderFns: res.staticRenderFns
            });
        } catch (e) {
            console.warn(`Data can only be displayed as text`);
        }
    },
    template: `<div ref="el" v-html="html"></div>`
});

Vue.component('ModalDialog', {
    props: ['data'],
    data() {
        return {
            visible: false,
        }
    },
    watch: {
        visible(val) {
            if (val) {
                window.currentModal = this;
            }
        }
    },
    methods: {
        showDialog() {
            this.visible = true;
        },
        close() {
            this.visible = false;
        }
    },
    template: `
      <div>
        <div @click="showDialog()">
            <HtmlRender :html="data.cell"/>
        </div>
        <el-dialog
          :title="data.title"
          :visible.sync="visible"
          :width="data.width">
          <div :style="{height:data.height,overflow:'auto'}" >
            
            <iframe v-if="visible&&data.url" :src="data.url" frameborder="0" width="100%" height="100%"></iframe>
            <el-alert v-else type="error" title="请设置ModalDialog的url"></el-alert>
          </div>
          <span slot="footer" class="dialog-footer">
            <el-button v-if="data.show_cancel" size="small" @click="visible = false">取 消</el-button>
          </span>
        </el-dialog>
      </div>
    `
});

Vue.component('func', {
    props: ['value'],
    computed: {
        isDialog() {
            return typeof this.value == 'object';
        }
    },
    template: `
    <ModalDialog v-if="isDialog&&value._type=='ModalDialog'" :data="value"></ModalDialog>
    <HtmlRender v-else :html="value"/>
    `
});