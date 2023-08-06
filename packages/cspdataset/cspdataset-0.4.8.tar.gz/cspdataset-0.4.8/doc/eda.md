# edatools工具说明

# 1 工具简介

数据集分析工具，包含在 cspdataset 库中，可通过 pip 安装后以命令行形式调用  

工具可对图像目标检测任务中 VOC 格式数据集下的标注文件(即xml文件)进行数据探查分析，分析结果将保存  
为若干张 xxx.png 图片和一份 xxx.json 文件，并自动统一保存于源标注文件夹同级文件夹下，名为data_report

# 2 安装 cspdataset 包

```python
! pip install cspdataset
```

# 3 VOC数据集示例

VOC  
|------JPEGImages  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----------1.jpg  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----------2.jpg  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----------xxx.jpg  
|------Annotations  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----------1.xml  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----------2.xml  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----------xxx.xml  
       
JPEGImages：图片文件夹  
Annotations：标注文件夹

# 4 命令调用

## 4.1 命令行帮助说明

```python
! edatools -h
```

## 4.2 调用示例

```python
! edatools -f your_voc_dataset_path/Annotations
```

## 4.3参数说明

-h 查看命令说明  
-f xml文件所在的文件夹路径(注意：路径结尾不加'/')  

