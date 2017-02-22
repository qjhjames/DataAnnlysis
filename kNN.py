from numpy import *
import operator
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
# inX用于输入向量
# dataSet输入的训练样本集
# labels标签向量
# k用于选择最近邻居的数目
# 标签向量的元素数目和矩阵dataSet的行数相同
def classity0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    classCount={ }
    for i in range(k):
        voteIlable=labels[sortedDistIndicies[i]]
        classCount[voteIlable]=classCount.get(voteIlable,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return  sortedClassCount[0][0]
# 从文件到二维数组转换
def file2matrix(filename):
    fr=open(filename)
    numberOfLines=len(fr.readlines())
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]#标记列
    fr=open(filename)
    index=0
    for line in fr.readlines():
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[0:3]
        classLabelVector.append((listFromLine[-1]))
        index+=1
    return  returnMat,classLabelVector
# 归一化特征值
def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)   
    ranges=maxVals-minVals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return  normDataSet,ranges,minVals

#wwfwfffffwwwee 三十岁 qwe