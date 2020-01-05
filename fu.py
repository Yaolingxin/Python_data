#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

d2 = pd.read_csv('data\World.csv') #世界CO2排放-年总-2012-2014，所有国家
d4 = pd.read_csv('data\China2.csv') #中国温室气体排放1999-2014
d5 = pd.read_csv('data\GDP2.csv')#分省GDP-中国1999-2014
d6 = pd.read_csv('data\WQT.csv')#全球各行业燃料燃烧产CO2占比2014
d7 = pd.read_csv('data\QT.csv')#世界温室气体排放2011-2014
d8 = pd.read_csv('data\WDJP.csv')#温度距平


cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()

def jup():
    df=d8.set_index("距平")
    年平均温度距平= go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x),format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc["年平均温度距平",:].values,
        name ="温度距平")
#温度单位摄氏，并报告为相对于1951年1月至1980年12月的异常平均。不确定性表示95％的置信区间统计和空间欠采样效应百分比。
#估计的1951年1月至1980年12月的绝对温度（C）：8.63 +/- 0.08
    平均高温距平=go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x),format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc["年平均高温距平",:].values,
        name ='高温距平')
#温度在摄氏，并报告为相对于1951年1月至1980年12月的异常平均。不确定性表示95％的置信区间统计和空间欠采样效应百分比。
#估计的1951年1月至1980年12月的绝对温度（C）：14.43 +/- 0.13
    平均低温距平=go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x),format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc["年平均低温距平",:].values,
        name ='低温距平')
#估计的1951年1月至1980年12月的绝对温度（C）：2.91 +/- 0.06
    layout=dict(xaxis=dict(rangeselector=dict(buttons=list([dict(count=120,label="10年",stepmode="backward"),
                                                            dict(count=360,label="30年",stepmode="backward"),
                                                            dict(count=600,label="50年",stepmode="backward"),
                                                            dict(step="all")])),
                           rangeslider=dict(bgcolor="#70EC57")),
                yaxis=dict(title='温度差值（摄氏度）'),
                title="1933-2018年温度变化差值"
               )
    fig=dict(data=[年平均温度距平,平均高温距平,平均低温距平],layout=layout)
    G=py.offline.plot(fig, filename="G.html",auto_open=False)
    return G

def jns():
    x = d4.columns.values.tolist()
    x.pop(0)
    k =list(d4.loc[4].values)
    k.pop(0)
    l =list(d5.loc[31].values)
    l.pop(0)
    GDP=go.Bar(
        x=x[::1],
        y=l[::-1],
        name="GDP（万亿）")
    温室气体排放量=go.Scatter(
        x=x,
        y=k,
        name ="温室气体排放量（CO2当量kt）",
        yaxis='y2')
    layout=go.Layout(title="中国经济发展与温室气体排放",
                     yaxis=dict(title="中国历年GDP总值（万亿）"),
                     yaxis2=dict(title="中国历年温室气体排放量（CO2当量kt）",
                                 overlaying="y",
                                 side="right"))
                
                
    fig=go.Figure(data=[GDP,温室气体排放量],layout=layout)
    G=py.offline.plot(fig, filename="G.html",auto_open=False)
    return G
def co():
    values= [35470891,8014066,3153742,7747217]
    labels=['CO2','甲烷','一氧化二氮','其他温室气体HFC和PFC和SF6']
    colors=['#A52A2A','#E9967A','#FFE4E1','#FFFAFA']
    p=[go.Pie(labels=labels,
              values=values,
              marker=dict(colors=colors))]
    layout=go.Layout(title="2012全球排放的温室气体占比(千吨CO2当量)")
    fig=go.Figure(data=p,layout=layout)
    G=py.offline.plot(fig, filename="G.html",auto_open=False)
    return G

def oc():
    q=[go.Pie(labels=['电力和供热生产','制造业和建筑业','运输产生','住宅建筑和商业及公共服务产生','其他行业'],
          values=['0.49','0.2','0.2','0.09','0.02'],
          marker=dict(colors=['#A52A2A','#E9967A','#CD5C5C','#FFE4E1','#FFFAFA']))]
    layout=go.Layout(title="各行业占生产发展的CO2排放总量(占总燃料燃烧的百分比)")
    fig=go.Figure(data=q,layout=layout)
    G=py.offline.plot(fig, filename="G.html",auto_open=False)
    return G
def zh():
    G="ditu.html"
    return G


# In[ ]:




