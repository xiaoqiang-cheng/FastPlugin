import torch
import torch.nn as nn
from config import *

class FakePlugin(torch.autograd.Function):
    @staticmethod
    def symbolic(g, *inputs):
        return g.op(global_setting["plugin"]["name"],
                        *inputs,
                        **global_setting["plugin"]["params"])

    @staticmethod
    def forward(ctx, *inputs):
        out_list = []
        for key, result in global_setting["outputs"].items():
            out_list.append(torch.ones(result))
        return out_list[0]

class PluginLayer(nn.Module):
    def __init__(self):
        super(PluginLayer, self).__init__()
        pass

    def forward(self, *inputs):
        return FakePlugin.apply(*inputs)

class TorchModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.plugin = PluginLayer()

    def forward(self, *inputs):
        ret = self.plugin(*inputs)
        return ret


class ModelCenter(object):
    def __init__(self) -> None:
        self.torch_model = TorchModel()
        self.torch_model.eval()

    def run_model(self, inputs):
        ret = self.torch_model(*inputs)
        return ret

    def export_onnx(self, inputs, in_name, out_name):
        print(tuple(inputs))
        torch.onnx.export(
            self.torch_model,
            tuple(inputs),
            "plugin.onnx",
            input_names = in_name,
            output_names = out_name,
            verbose = True,
            opset_version = 9,
            enable_onnx_checker = False
        )

if __name__=="__main__":
    obj = ModelCenter()

    inputs_list = []
    inputs_name = []

    for key, result in global_setting["inputs"].items():
        inputs_name.append(key)
        inputs_list.append(torch.ones(result))

    out_list = []
    outs_name = []
    for key, result in global_setting["outputs"].items():
        outs_name.append(key)
        out_list.append(torch.ones(result))

    print(inputs_list)
    ret = obj.run_model(inputs_list)
    print(ret)
    obj.export_onnx(inputs_list, inputs_name, outs_name)

