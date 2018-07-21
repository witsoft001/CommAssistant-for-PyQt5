# CommAssistant-for-PyQt5
1. 这是一个用PyQt库写的上位机，能实现基本的串口收发。

2. 界面库的版本是PyQt5.11.2，dist文件夹下的.exe文件，可直接再windows系统上执行。

3. 如果要在MACOS上执行，可能需要下载源代码和pycharm IDE再编译一次，理论上是可行的，因为QT是一个跨平台的GUI。

4. 关于src->stytle文件夹下的qwindowsvistastyle.dll文件说明：该文件主要是为了解决Pyqt5在win10环境下，界面Style会变成win98的情况，
在用pyinstaller 打包时需要把样式一并打包进去。请查阅CommAssistant.spec文件说明。

界面如下：

![Image text](https://github.com/zengjiawei/CommAssistant-for-PyQt5/blob/master/Example/interface.jpg)
