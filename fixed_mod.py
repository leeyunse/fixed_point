caffe_root = '/home/socmgr/caffe/'

import sys
import json
sys.path.insert(0, caffe_root + 'python')
import caffe
import numpy as np

prototxt = '/home/socmgr/caffe/models/SqueezeNet/SqueezeNet_v1.1/deploy.prototxt'
caffemodel = '/home/socmgr/caffe/models/SqueezeNet/SqueezeNet_v1.1/squeezenet_v1.1.caffemodel'

dict_params = {}
net = caffe.Net(prototxt,caffemodel,caffe.TEST)
for param in net.params:
    dict_params[param] = {'data': net.params[param][0].data.tolist(),
                          'shape': net.params[param][0].data.shape}
for param in net.params:
    for a in range(0,dict_params[param]['shape'][0],1):
        for b in range(0,dict_params[param]['shape'][1],1):
            for c in range(0,dict_params[param]['shape'][2],1):
                for d in range(0,dict_params[param]['shape'][3],1):
                    v1=int(net.params[param][0].data[a][b][c][d]* 2**8)
                    v2=float(v1)/2**8
                    net.params[param][0].data[a][b][c][d]=v2
net.save("./fixed_mod.caffemodel")
