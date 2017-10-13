#by nikoong
#for develop train.txt test.txt query.txt gallery.txt

#-*-coding:utf-8-*- 
import os
import numpy as np

#file to list
def Makefilelist(data_path):
    fullnamefiles=[]
    files= os.listdir(data_path)
    for filename in files:
        fullfilename = os.path.join(data_path,filename)
        fullnamefiles.append(fullfilename)
    return fullnamefiles,files

#txt to list
def txt2list(txt_path):
    txt_list = []
    with open(txt_path) as f :
        for line in f:
            txt_list.append(line.split('\n')[0])
    return txt_list

#list to txt
def list2txt(txt_list,txt_path):
    with open(txt_path,'w') as f :
        for line in txt_list:
            f.write(line+'\n')

def genlable(txt_path,new_txt_path):

    new_txt = []
    with open(txt_path) as f:
        for line in f:
            id = str(int(line.split('/')[-1].split('_')[0]))
            newline = line.split('\n')[0] + ' ' + id 
            new_txt.append(newline)
    list2txt(new_txt,new_txt_path)

#generate label from imagename
def genlable(datalist):
    newlist = []
    for element in newlist:
        label = str(int(element.split('/')[-1].split('_')[0]))
        newelement = element + ' ' + label 
        new_list.append(newelement)
    return newlist

#sort list by label
def sort_list(txt_list):
    value_list = []
    for line in txt_list:
        value = int(line.split(' ')[1])
        value_list.append(value)
    value_list = np.array(value_list) 
    txt_list = np.array(txt_list)     
    index_list = np.argsort(value_list)
    txt_list =txt_list[index_list]
    return txt_list

def parselist(datalist):
    file_list=[]
    label_list=[]
    for element in datalist:
        file_list.append(element.split(' ')[0])
        label_list.append(int(element.split(' ')[1]))
    return file_list, label_list 

#map label into (0-n)
def normalize_label(datalist):
    datalist = sort_list(datalist)
    file_list,label_list = parselist(datalist)
    newlist = []
    newlist.append(0);
    for i in range(len(label_list) - 1):
         newlabel = newlist[i]+1 if label_list[i+1]>label_list[i] else newlist[i]
         newlist.append(newlabel)
    newdatalist=[]
    for i in range(len(newlist)):
        element = file_list[i] +' '+ str(newlist[i])
        newdatalist.append(element)
    return newdatalist




txtlist = txt2list (txt)
list2 = normalize_label(txtlist)





datasets = ['Market1501','DukeMTMC-reid']

for dataset in datasets:
    if (dataset == 'DukeMTMC-reid'):

        fullnamefiles,files = Makefilelist('/home/nikoong/dataset/attribute/DukeMTMC-reID/bounding_box_test')
        txt = '/home/nikoong/dataset/attribute/DukeMTMC-reID/test.txt'
        list2txt(fullnamefiles , txt)
        genlable(txt , txt)

        fullnamefiles,files = Makefilelist('/home/nikoong/dataset/attribute/DukeMTMC-reID/bounding_box_train')
        txt = '/home/nikoong/dataset/attribute/DukeMTMC-reID/train.txt'
        list2txt(fullnamefiles , txt)
        genlable(txt , txt)

        fullnamefiles,files = Makefilelist('/home/nikoong/dataset/attribute/DukeMTMC-reID/query')
        txt = '/home/nikoong/dataset/attribute/DukeMTMC-reID/query.txt'
        list2txt(fullnamefiles , txt)
        genlable(txt , txt)



    if (dataset == 'Market1501'):
        fullnamefiles,files = Makefilelist('/home/nikoong/dataset/attribute/Market-1501/bounding_box_test')
        txt = '/home/nikoong/dataset/attribute/Market-1501/test.txt'
        list2txt(fullnamefiles , txt)
        genlable(txt , txt)

        fullnamefiles,files = Makefilelist('/home/nikoong/dataset/attribute/Market-1501/bounding_box_train')
        txt = '/home/nikoong/dataset/attribute/Market-1501/train.txt'
        list2txt(fullnamefiles , txt)
        genlable(txt , txt)

        fullnamefiles,files = Makefilelist('/home/nikoong/dataset/attribute/Market-1501/gt_bbox')
        txt = '/home/nikoong/dataset/attribute/Market-1501/gt_bbox.txt'
        list2txt(fullnamefiles , txt)
        genlable(txt , txt)

        fullnamefiles,files = Makefilelist('/home/nikoong/dataset/attribute/Market-1501/gt_query')
        txt = '/home/nikoong/dataset/attribute/Market-1501/gt_query.txt'
        list2txt(fullnamefiles , txt)
        genlable(txt , txt)

        fullnamefiles,files = Makefilelist('/home/nikoong/dataset/attribute/Market-1501/query')
        txt = '/home/nikoong/dataset/attribute/Market-1501/query.txt'
        list2txt(fullnamefiles , txt)
        genlable(txt , txt)










