# import netron
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QSplitter, QTreeWidgetItem, QCheckBox
from PySide2.QtCore import QTimer, Qt, QModelIndex

class View():
    '''
        mvc模式中的视图部分，本身不包含任何逻辑，仅作界面显示使用
    '''
    def __init__(self):
        self.ui = QUiLoader().load('config/main.ui')
        # ret = netron.start("/home/cxq/Develop/lab_code/FastPlugin/plugin.onnx", browse=False)
        # print(ret)

    def show(self):
        self.ui.show()

if __name__=="__main__":
    from qt_material import apply_stylesheet

    app = QApplication([])
    apply_stylesheet(app, theme='dark_teal.xml')
    obj = View()
    obj.show()
    app.exec_()