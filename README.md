# Python项目说明文档
## 项目故事介绍
全球气候的变化一直是现在世界人们热切关注的话题，希望通过分析城市建设发展和年度降雨和年度气温等变化，分析人类的发展和气候变化之间的联系
## 项目目标
使用pyecharts及plotly完成两份交互可视化交互图形界面（至少包涵一份地图）
## 项目地址
* Github代码URL：[点此查看代码](https://github.com/Yaolingxin/Python_data)
* Pythonanywhere：[点此进入](http://yaolingxin959.pythonanywhere.com/)  
                 [其他的URL](http://yaolingxin959.pythonanywhere.com/qw)
## 一共有5份数据5份图表。
* [1933-2018年温度变化差值]
* [中国经济发展与温室气体排放]
* [2012全球oc气体排放量分布]
* [2012全球排放的温室气体占比]
* [2012各行业占生产发展的CO2排放比]
## 说明
### 技术文档书写
* HTML档：   * 实现了下拉框对于不同表格的选择 * 使用者点击地图某处会浮现相应数值，地图拥有的放大缩小的功能 * 用户鼠标浮动到对应的地点时可以显示数值并高亮。 * 使用者点击相应按钮呈现对应图表
* python档：运用了列表循环的方法提取data中的数据，有合理的if语句运用
* 函数运用：自定义制作可视化图的函数fu.py，引用了plotly、cufflinks、pyechart模块，
* 数据交互：实现了数据的python与前端HTML页面交互，并且前端能够正确接收到同样的数据传递结果
* HTML界面：在result2.html处使用了基本模板，进行了基本布局

