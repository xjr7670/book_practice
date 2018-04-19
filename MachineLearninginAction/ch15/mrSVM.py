#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pickle
import numpy as np

from mrjob.job import MRJob

class MRsvm(MRJob):
    DEFAULT_INPUT_PROTOCAL = 'json_value'

    def __init__(self, *args, **kwargs):
        super(MRsvm, self).__init__(*args, **kwargs)
        self.data = pickle.load(open('/home/cavin/Code/BookPractice/Python/MachineLearninginAction/ch15/svmDat27'))
        self.w = 0
        self.eta = 0.69
        self.dataList = []
        self.k = self.options.batchsize
        self.numMappers = 1
        self.t = 1

    def configure_options(self):
        super(MRsvm, self).configure_options()
        self.add_passthrough_option('--iterations', dest='iterations', default=2, type='int', 
                help='T: number of iterations to run')
        self.add_passthrough_option('--batchsize', dest='batchsize', default=100, type='int',
                help='k: number of data points in a batch')
        
        def steps(self):
            return ([self.mr(mapper=self.map, mapper_final=self.map_fin, reducer=self.reduce)] * self.options.iterations)

    def map(self, mapperId, inVals):
        if False:
            yield
        if inVals[0] == 'w':
            self.w = inVals[1]
        elif inVals[0] == 'x':
            self.dataList.append(inVals[1])
        elif inVals[0] == 't':
            slef.t = inVals[1]

    def map_fin(self):
        labels = self.data[:, -1]
        X = self.data[:, 0:-1]
        if self.w == 0:
            self.w = [0.001] * np.shape(X)[1]
        for index in self.dataList:
            p = np.mat(self.w) * X[index, :].T
            if labels[index] * p < 1.0:
                yield (1, ['u', index])
        yield (1, ['w', self.w])
        yield (1, ['t', self.t])

    def reduce(self, _, packedVals):
        for valArr in packedVals:
            if valArr[0] == 'u':
                self.dataList.append(valArr[1])
            elif valArr[0] == 'w':
                self.w = valArr[1]
            elif valArr[0] == 't':
                self.t = valArr[1]
        labels = self.data[:, -1]
        X = self.data[:, 0:-1]
        wMat = np.mat(self.w)
        wDelta = np.mat(np.zeros(len(self.w)))
        for index in self.dataList:
            wDelta += float(labels[index]) * X[index, :]
        eta = 1.0 / (2.0 * self.t)
        wMat = (1.0 - 1.0 / self.t) * wMat + (eta / self.k) * wDelta
        for mapperNum in range(1, self.numMappers+1):
            yield (mapperNum, ['w', wMat.tolist()[0]])
            if self.t < self.options.iterations:
                yield (mapperNum, ['t', self.t + 1])
                for j in range(self.k / self.numMappers):
                    yield (mapperNum, ['x', random.randint(np.shape(self.data)[0])])

if __name__ == '__main__':
    MRsvm.run()
