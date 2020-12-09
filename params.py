from thop import profile
from thop import clever_format
import torch
from model import *

input = torch.randn(1, 3, 512, 512)
model_def = "config/yolov3-spp-1cls.cfg"
model = Darknet(model_def, img_size=512)
flops, params = profile(model, inputs=(input, ))
print(flops, params) # 1819066368.0 11689512.0
flops, params = clever_format([flops, params], "%.3f")
print(flops, params) # 1.819G 11.690M