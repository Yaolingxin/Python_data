#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randrange
from flask import Flask, render_template, request
import pandas as pd
import csv, os
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Map,Pie, Page, Grid,Bar,Tab,Line,Timeline,Scatter
from plotly.graph_objs import Scatter,Layout,Figure,Bar,Pie
from pyecharts.globals import ChartType, SymbolType
from fu import jup,jns,co,oc,zh
# 模块读进来, 组合拳  组合拳  组合拳

app = Flask(__name__)

d2 = pd.read_csv('data\World.csv') #世界CO2排放-年总-2012-2014，所有国家
d4 = pd.read_csv('data\China2.csv') #中国温室气体排放1999-2014
d5 = pd.read_csv('data\GDP2.csv')#分省GDP-中国1999-2014
d6 = pd.read_csv('data\WQT.csv')#全球各行业燃料燃烧产CO2占比2014
d7 = pd.read_csv('data\QT.csv')#世界温室气体排放2011-2014
d8 = pd.read_csv('data\WDJP.csv')#温度距平


dict = {"1933-2018年温度变化差值" : d8, "中国经济发展与温室气体排放" : d4, "2012全球CO2气体排放量分布" : d2 , "2012全球排放的温室气体占比" : d7,"2012各行业占生产发展的CO2排放比":d6}#选择字典

regions_available_loaded = ['1933-2018年温度变化差值','中国经济发展与温室气体排放','2012全球CO2气体排放量分布','2012全球排放的温室气体占比','2012各行业占生产发展的CO2排放比']#选框内容

# 基本cufflinks 及ploty設置, 查文檔看書貼上而已
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()


@app.route('/',methods=['GET'])
def run_2():
    
    data_str = d8.to_html()         #数据框
    
    regions_available = regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                           the_res = data_str,# 表
                           the_select_region=regions_available)   

@app.route('/qw',methods=['POST'])
def run_select():
    
    the_region = request.form["the_region_selected"]  ## 取得用户交互输入
    print(the_region)
    
    data_str = dict[the_region].to_html()#数据表

    #制作图表切换效果
    if the_region =="1933-2018年温度变化差值":
        G=jup()
        with open(G, encoding="utf8", mode="r") as f:                  
            plot_all = "".join(f.readlines())  
            
    elif the_region=="中国经济发展与温室气体排放":
        J=jns()
        with open(J, encoding="utf8", mode="r") as f:                  
            plot_all = "".join(f.readlines())
            
    elif the_region=="2012全球CO2气体排放量分布":
        H=zh()
        with open(H, encoding="utf8", mode="r") as f:                  
            plot_all = "".join(f.readlines())
     
    elif the_region=="2012全球排放的温室气体占比":
        C=co()
        with open(C, encoding="utf8", mode="r") as f:                  
            plot_all = "".join(f.readlines())
        
    elif the_region=="2012各行业占生产发展的CO2排放比":
        O=oc()
        with open(oc(), encoding="utf8", mode="r") as f:                  
            plot_all = "".join(f.readlines())
        
   
        
    
    regions_available =  regions_available_loaded  #下拉选单有内容
    return render_template('results2.html',
                            the_plot_all = plot_all,
                            the_res = data_str,
                            the_select_region=regions_available,
                           )

if __name__ == '__main__':
    app.run(port = 8030,debug=True)   # debug=True, 在py使用, 在ipynb不使用

