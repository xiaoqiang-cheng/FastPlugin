import netron
import os

ret = netron.start("/home/cxq/Develop/lab_code/FastPlugin/plugin.onnx", browse=False)
print(ret)