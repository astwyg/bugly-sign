## 注意

这是一个Flask+React试验项目, 请勿用于某些公司自动打卡.

## 如何实现自动打卡

在crontab中, 增加定时任务, 运行signOnce.py <iccid> <phone> <password>

## 如何启动web服务

1. `pip install -r requiments.txt`
2. `python server.py`