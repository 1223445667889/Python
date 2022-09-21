#导入的模块
import wx

# 自定义窗口
class MyFrame(wx.Frame):
    def __init__(self):
        #窗口的大小和位置
        super().__init__(None,title="事件处理",size=(300,180))
        #添加窗口中的控件

        #创建面板对象，参数parent传递的是self，即设置面板的父容器为当前窗口对象
        panel = wx.Panel(parent = self)

        #创建静态文本(StaticTxte)对象，将静态文本对象放到panel面板中，所以parent参数传递的是panel，参数label是在静态文本对象
        #上显示的文字，参数pos用于设置静态文本对象的位置。
        #statictext = wx.StaticText(parent=panel,label="Hello World!",pos=(10,10))
        self.statictext = wx.StaticText(parent=panel, label="OK", pos=(110, 50))

        #创建按钮
        b = wx.Button(parent = panel, label = 'OK',pos=(100,20))

        #绑定事件，wx.EVT_BUTTON是事件类型，即按钮单击事件，self.on_click是事件处理程序，b是事件源，即按钮对象
        self.Bind(wx.EVT_BUTTON, self.on_click,b)

        #事件处理程序
    def on_click(self, event):
            self.statictext.SetLabelText('Hello,World. ')


#创建应用程序对象
app = wx.App()

#创建窗口对象
frm = MyFrame()

#窗口默认隐藏，需调用Show()方法才能显示
frm.Show()

#让应用进入主事件循环中
app.MainLoop()
