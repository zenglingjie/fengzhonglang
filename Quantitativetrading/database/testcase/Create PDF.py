# -*- coding: utf-8 -*-
from reportlab.rl_config import defaultPageSize  # 默认页面大小
from reportlab.pdfbase import pdfmetrics  #
from reportlab.pdfbase.cidfonts import UnicodeCIDFont  # 设置CID字体（另一种是TTF字体）


pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))  # 设置宋体字体

from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer  # 段落、模板、空白行
from reportlab.lib.units import inch  # 导入画布的单位
from reportlab.lib.enums import TA_CENTER  # 样式对其方式
from reportlab.lib.styles import ParagraphStyle  # 导入段落样式

# from reportlab.pdfbase.ttfonts import TTFont          #TTFont字体
# pdfmetrics.registerFont(TTFont('msyh', 'msyh.ttf'))
PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]

# 标题样式
style1 = ParagraphStyle(
    name='Title',
    fontName='STSong-Light',  # 设置字体宋体
    fontSize=24,  # 设置字体大小
    alignment=TA_CENTER,  # 设置标题居中引入reportlab.lib.enums（TA_CENTER,TA_JUSTIFY,TA_LEFT,TA_RIGHT）
    leftIndent=40,  # 设置左边距
    rightIndent=40,  # 设置右边距
    leading=20)  # 设置行距

# 正文样式
style2 = ParagraphStyle(
    name='content',
    fontName='STSong-Light',
    fontSize=10,
    leading=20,
    firstLineIndent=20)


class pdfFunction(object):
    """
    该类用以写PDF文件
    """

    def __init__(self, news_Title, news_source, news_time, news_content):  # 初始化变量
        self.news_Title = news_Title  # 新闻标题
        self.news_source = news_source  # 新闻来源
        self.news_time = news_time  # 发布时间
        self.news_content = news_content # 新闻内容

    # 设置第一页，当第一页不够写时写入第二页
    def myFirstPage(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('STSong-Light', 10)  # 设置来源字体及大小
        canvas.drawRightString(PAGE_WIDTH - 350, PAGE_HEIGHT - 170, self.news_source)  # 以画字符串的方式在规定位置画入来源信息
        canvas.drawRightString(PAGE_WIDTH - 200, PAGE_HEIGHT - 170, self.news_time)  # 以画字符串的方式在规定位置画入时间信息
        canvas.setFont('STSong-Light', 8)  # 设置页码大小
        canvas.drawCentredString(PAGE_WIDTH / 2, 0.75 * inch, "Page %d" % doc.page)  # 以画字符串的方式在规定位置获取文档页码信息

    def mySecondPage(self, canvas, doc):
        canvas.saveState()  # 保存当前页
        canvas.setFont('STSong-Light', 8)  # 画布的字体
        canvas.drawCentredString(PAGE_WIDTH / 2, 0.75 * inch, "Page %d" % doc.page)  # 画页码

    def run(self, file_path):
        Story = []  # 定义一个列表
        head = Paragraph(self.news_Title, style1)  # 以段落格式写入标题，当长度达到一定是自动换行
        Story.append(head)  # 往列表里加入标题文字
        Story.append(Spacer(1, 1.5 * inch))  # 往列表里加入空白行
        pa = Paragraph(self.news_content, style2)  # 以段落形式写正文内容
        Story.append(pa)  # 往列表里加入正文内容
        doc = SimpleDocTemplate(file_path)  # 创建一个简单的pdf文件文档
        # 往文档中插入列表数据，当第一页不够写时开始第二页
        doc.build(Story, onFirstPage=self.myFirstPage, onLaterPages=self.mySecondPage)


if __name__ == "__main__":
    news_Title = 'xxxxxxxx'#标题
    news_source = '11111'
    news_time = '2017-6-25'
    news_content = ''
    createPDF = pdfFunction(news_Title, news_source,news_time, news_content)
    createPDF.run("E:/Quantitativetrading/jide_code/testcase/db/"+'caca.PDF')
