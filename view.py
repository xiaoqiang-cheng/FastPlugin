import netron
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QSplitter, QTreeWidgetItem, QCheckBox, QVBoxLayout, QHBoxLayout
from PySide2.QtCore import QTimer, Qt, QModelIndex, QUrl
from PySide2.QtWebEngineWidgets import QWebEnginePage
from PySide2.QtWebEngineWidgets import QWebEngineView

class View():
    '''
        mvc模式中的视图部分，本身不包含任何逻辑，仅作界面显示使用
    '''
    def __init__(self):
        self.spliter_dict = {}
        self.ui = QUiLoader().load('config/main.ui')

        self.webview_plugin = QWebEngineView()
        self.ui.groupBox_2.layout().addWidget(self.webview_plugin)

        self.set_qspilter("main_form",
                        Qt.Horizontal,
                        [self.ui.groupBox, self.ui.groupBox_2],
                        [2, 5],
                        self.ui.central_widget.layout())
        # self.show_plugin_in_netron("/home/cxq/Develop/lab_code/FastPlugin/plugin.onnx")

    def set_qspilter(self, spliter_name,
                            spliter_dir,
                            widget_list,
                            factor_list,
                            layout_set):
        # Qt.Horizontal or v
        self.spliter_dict[spliter_name] = QSplitter(spliter_dir)

        for w in widget_list:
            self.spliter_dict[spliter_name].addWidget(w)

        for i, f in enumerate(factor_list):
            self.spliter_dict[spliter_name].setStretchFactor(i, f)
        layout_set.addWidget(self.spliter_dict[spliter_name])

    def show_plugin_in_netron(self, plugin_path):
        netron.stop()
        ret = netron.start(plugin_path, browse=False)
        url = "http://%s:%s"%(ret[0], ret[1])
        self.webview_plugin.load(QUrl(url))
        self.webview_plugin.show()

    def set_onnx_path(self, pathname):
        self.ui.linetext_onnx_path.setText(pathname)


    def get_plugin_name(self):
        return self.ui.linetext_op_name.text()

    def get_plugin_input(self):
        return self.ui.text_input_shape.toPlainText()

    def get_plugin_output(self):
        return self.ui.text_output_shape.toPlainText()

    def get_plugin_param(self):
        return self.ui.text_param.toPlainText()

    def show(self):
        self.ui.show()

if __name__=="__main__":
    from qt_material import apply_stylesheet

    app = QApplication([])
    apply_stylesheet(app, theme='light_blue.xml')
    obj = View()
    obj.show()
    app.exec_()