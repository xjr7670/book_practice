#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 20:06:50 2017

@author: cavin
"""

import math
import random

import matplotlib.pyplot as plt

from chapter4 import vector_mean, squared_distance, distance

class KMeans:
    """performs k-means clustering"""
    
    def __init__(self, k):
        self.k = k
        self.means = None
    
    def classify(self, input):
        """return the index of the cluster closest to the input"""
        return min(range(self.k), \
                   key=lambda i: squared_distance(input, self.means[i]))
        
    def train(self, inputs):
        # 选择k个随机点作为初始的均值
        self.means = random.sample(inputs, self.k)
        assignments = None
        while True:
            # 查找新分配
            new_assignments = map(self.classify, inputs)
            
            # 如果所有数据点都不再被重新分配，那么就停止
            if assignments == new_assignments:
                return
            
            # 否则重新分配
            assignments = new_assignments
            
            # 并基于新的分配计算新的均值
            for i in range(self.k):
                # 查找分配给聚类i的所有的点
                i_points = [p for p, a in zip(inputs, assignments) if a==i]
                
                # 确保i_inputs不是空的，因此除数不会是0
                if i_points:
                    self.means[i] = vector_mean(i_points)


def squared_clustering_errors(inputs, k):
    """finds the total squared error from k-means clustering the inputs"""
    clusterer = KMeans(k)
    clusterer.train(inputs)
    means = clusterer.means
    assignments = list(map(clusterer.classify, inputs))

    return sum(squared_distance(input,means[cluster])
               for input, cluster in zip(inputs, assignments))

def plot_squared_clustering_errors():

    ks = range(1, len(inputs) + 1)
    errors = [squared_clustering_errors(inputs, k) for k in ks]

    plt.plot(ks, errors)
    plt.xticks(ks)
    plt.xlabel("k")
    plt.ylabel("total squared error")
    plt.show() 

def recolor_image():
    path_to_png_file = r"/home/cavin/Pictures/yang.jpg"
    import matplotlib.image as mpimg
    img = mpimg.imread(path_to_png_file)
    top_row = img[0]
    top_left_pixel = top_row[0]
    red, green, blue = top_left_pixel
    pixels = [pixel for row in img for pixel in row]
    clusterer = KMeans(5)
    clusterer.train(pixels)
    
    def recolor(pixel):
        cluster = clusterer.classify(pixel)
        return clusterer.means[cluster]
    
    new_img = [[recolor(pixel) for pixel in row] for row in img]
    
    plt.imshow(new_img)
    plt.axis('off')
    plt.show()


def is_leaf(cluster):
    """ a cluster is a leaf if it has length 1"""
    return len(cluster) == 1

def get_children(cluster):
    """returns the two children of this cluster if  it's a merged cluster;
    raises an exception if this is a leaf cluster"""
    if is_leaf(cluster):
        raise TypeError("a leaf cluster has no children")
    else:
        return cluster[1]

def get_values(cluster):
    """returns the value in this cluster (if it's a leaf cluster)
    or all the values in the leaf cluster below it (if it's not)"""
    if is_leaf(cluster):
        return cluster
    else:
        return [value \
                for child in get_children(cluster) \
                for value in get_values(child)]

def cluster_distance(cluster1, cluster2, distance_agg=min):
    """compute all the pairwise distances between cluster1 and cluster2
    and apply _distance_agg_ tothe resulting list"""
    return distance_agg([distance(input1, input2) \
                         for input1 in get_values(cluster1) \
                         for input2 in get_values(cluster2)])


def get_merge_order(cluster):
    if is_leaf(cluster):
        return float('inf')
    else:
        return cluster[0]


def bottom_up_cluster(inputs, distance_agg=min):
    # 最开始每个输入都是一个叶聚类／一元组
    clusters = [(input, ) for input in inputs]
    
    # 只要剩余一个以上聚类
    while len(clusters) > 1:
        # 就找出最近的两个聚类
        c1, c2 = min([(cluster1, cluster2) \
                      for i, cluster1 in enumerate(clusters) \
                      for cluster2 in clusters[:i]], \
                      key=lambda p: cluster_distance(p[0], p[1], distance_agg))
        
        # 从聚类列表中将它们移除
        clusters = [c for c in clusters if c != c1 and c != c2]
        
        # 使用merge_order = 剩余聚类的数目来合并它们
        merged_cluster = (len(clusters), [c1, c2])
        
        # 将添加它们的合并
        clusters.append(merged_cluster)
    
    # 当只剩一个聚类时，返回它
    return clusters[0]

def generate_clusters(base_cluster, num_clusters):
    # 开始的列表只有基本聚类
    clusters = [base_cluster]
    
    # 只要我们还没有足够的聚类
    while len(clusters) < num_clusters:
        # 选择上一个合并的聚类
        next_cluster = min(clusters, key=get_merge_order)
        # 将它从列表中移除
        clusters = [c for c in clusters if c != next_cluster]
        # 并将它的子聚累加到列表中（即拆分它）
        clusters.extend(get_children(next_cluster))
    
    # 一旦我们有了足够的聚类
    return clusters



if __name__ == "__main__":

    inputs = [[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],[-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],[-41,8],[-11,-6],[-25,-9],[-18,-3]]
#    recolor_image()
    base_cluster = bottom_up_cluster(inputs)