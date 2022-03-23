from view import View
from model import ModelCenter
import os
from PySide2.QtWidgets import QApplication
from utils import *
import netron
from config import global_setting
class Controller:
    def __init__(self) -> None:
        self.app = QApplication([])
        self.view = View()
        self.model = ModelCenter()
        self.signal_connect()

    def signal_connect(self):
        self.view.ui.button_open_onnx.clicked.connect(self.select_onnx_file)
        self.view.ui.button_gen_plugin.clicked.connect(self.gen_onnx_plugin)

    def gen_onnx_plugin(self):
        plugin_name = self.view.get_plugin_name()
        global_setting['plugin']['name'] = plugin_name
        input_list = self.view.get_plugin_input().split("\n")
        global_setting['inputs'] = {}
        for ele in input_list:
            key, result = ele.split(":")
            key = key.replace(" ", "")
            global_setting['inputs'][key] = eval(result)

        output_list = self.view.get_plugin_output().split("\n")
        global_setting['outputs'] = {}

        for ele in output_list:
            key, result = ele.split(":")
            key = key.replace(" ", "")
            global_setting['outputs'][key] = eval(result)

        output_list = self.view.get_plugin_param().split("\n")
        global_setting['plugin']['params'] = {}
        for ele in output_list:
            key, result = ele.split(":")
            key = key.replace(" ", "")
            try:
                global_setting['plugin']['params'][key] = eval(result)
            except:
                global_setting['plugin']['params'][key] = result

        onnx_out_path = os.path.join(
            os.getcwd(),
            plugin_name + ".onnx"
        )

        self.model.export_onnx_from_dict(onnx_out_path)
        self.view.show_plugin_in_netron(onnx_out_path)

    def select_onnx_file(self):
        onnx_file_path = choose_file(self.view.ui, "选择onnx文件", "ONNX File(*.onnx)", "./")
        self.view.set_onnx_path(onnx_file_path)
        self.view.show_plugin_in_netron(onnx_file_path)

    def run(self):
        self.view.show()
        self.app.exec_()
        netron.stop()



if __name__ == "__main__":
    obj = Controller()
    obj.run()