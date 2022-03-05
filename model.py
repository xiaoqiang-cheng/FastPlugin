from tkinter.messagebox import NO
import torch
import torch.nn as nn


class FakePlugin(torch.autograd.Function):
    @staticmethod
    def symbolic(g, input0, input1):
        return g.op("scatter_max", input0, input1)

    @staticmethod
    def forward(ctx, input0, input1):
        return (input0 + input1)

class PluginLayer(nn.Module):
    def __init__(self):
        super(PluginLayer, self).__init__()
        pass

    def forward(self, *input):
        return FakePlugin.apply(*input)

class TorchModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.plugin = PluginLayer()

    def forward(self, *input):
        ret = self.plugin(*input)
        return ret




class ModelCenter(object):
    def __init__(self) -> None:
        pass

    def run_model(self):


if __name__=="__main__":
    obj = ModelCenter()
