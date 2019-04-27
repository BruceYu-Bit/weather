# coding:utf-8
import tkinter  # 导入TKinter模块
import csv
import requests
from requests import RequestException
import re
import webbrowser
def getuser():
    user = user_text.get()  # 获取文本框内容
    print(user)
    with open("data.csv", 'r', encoding='utf-8') as f:
        rawinfos = dict(csv.reader(f));
    try:
        address=rawinfos.get(user)
        url='http://www.weather.com.cn/weather1d/'+address+'.shtml'
        get_info(url)
    except:
        var.set("无该城市")
        print("无该城市")
ytm = tkinter.Tk()  # 创建Tk对象
ytm.title("天气查询")  # 设置窗口标题
ytm.geometry("500x300")  # 设置窗口尺寸
l1 = tkinter.Label(ytm, text="天气查询")  # 标签
l1.pack()  # 指定包管理器放置组件
user_text = tkinter.Entry()  # 创建文本框
user_text.pack()
var = tkinter.StringVar()  # 文字变量储存器
tkinter.Button(ytm, text="查询", command=getuser).pack()  # command绑定获取文本框内容方法
# 设置标签
l = tkinter.Label(textvar=var, bg='yellow', width=60, height=10)  # 参数textvar不同于text,bg是backgroud
l.pack()  # 放置标签

def get_info(url):
    info=""
    try:
        response=requests.get(url);
        if response.status_code==200:
            response.encoding='utf-8'
            html = response.text
            #查看天气数据
            ADDRESS = re.findall('<title>(.*?)</title>', html)
            aim = re.findall(
                '<input type="hidden" id="hidden_title" value="(.*?)月(.*?)日(.*?)时(.*?) (.*?)  (.*?)  (.*?)"', html,
                re.S)
            airdata = re.findall(
                '<li class="li6 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>', html, re.S)
            print(ADDRESS[0][1:5])
            print("当前日期：%s月%s日,%s" % (aim[0][0], aim[0][1], aim[0][4]))
            print("更新时间：%s:00" % aim[0][2])
            print("当前天气：%s" % aim[0][5])
            print("今日温度：%s" % aim[0][6])
            print("空气质量：" + airdata[0][0] + "," + airdata[0][2])
            info="当前日期："+aim[0][0]+"月"+aim[0][1]+"日,"+aim[0][4]+'\n'+"" \
                  "更新时间："+aim[0][2]+":00"+'\n'\
                 +"当前天气："+aim[0][5]+"\n"\
                 +"今日温度："+aim[0][6]+"\n"\
                 +"空气质量："+ airdata[0][0] + "," + airdata[0][2]
            var.set(info)
            # #详细查看数据
            # ask_ok = input("是否深入查看（Y/N）：")
            # if ask_ok == 'Y' or ask_ok == 'y':
            #     lightdata = re.findall(
            #         '<li class="li1 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>', html,
            #         re.S)
            #     colddata = re.findall('<li class="li2 hot">\n(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>', html, re.S)
            #     weardata = re.findall(
            #         '<li class="li3 hot" id="chuanyi">\n(.*?)<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>', html,
            #         re.S)
            #     washdata = re.findall(
            #         '<li class="li4 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>', html,
            #         re.S)
            #     bloodata = re.findall(
            #         '<li class="li5 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>', html,
            #         re.S)
            #     detail = re.findall('hour3data={"1d":(.*?),"23d"', html, re.S)
            #     detail = re.findall('"(.*?)"', detail[0], re.S)
            #     print("--" * 40)
            #     print('详细数据：')
            #     print("%-10s\t%-10s\t%-10s\t%-10s\t%-10s" % ("时间", "状态", "温度", "风向", "风力"))
            #     for each in detail:
            #         each = each.split(',')
            #         print("%-10s\t%-10s\t%-10s\t%-10s\t%-10s" % (each[0], each[2], each[3], each[4], each[5]))
            #     print("--" * 40)
            #     print("%s:\t%s\t%s" % (lightdata[0][1], lightdata[0][0], lightdata[0][2]))
            #     print("%s:\t%s" % (colddata[0][1], colddata[0][2]))
            #     print("%s:\t%s\t%s" % (washdata[0][1], washdata[0][0], washdata[0][2]))
            #     print("血糖指数:\t%s,%s" % (bloodata[0][0], bloodata[0][2]))
            #     print("%s:\t%s\t%s" % (weardata[0][2], weardata[0][1], weardata[0][3]))
            #     print("--" * 40)
            #     flag = input("是否查看详细穿衣建议（Y/N）：")
            #     if flag == 'Y' or flag == 'y':
            #         webbrowser.open("http://www.weather.com.cn/forecast/ct.shtml?areaid=" + url)
        return None
    except RequestException:
        print('无法获取网站内容')
        return None

ytm.mainloop()  # 进入主循环