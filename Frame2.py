#Boa:Frame:Frame1

import wx
import tool

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1PANEL1,
 wxID_FRAME1PANEL2, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2,
 wxID_FRAME1STATICTEXT3, wxID_FRAME1TEXTCTRL1,
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBITMAP11,
 wxID_FRAME1STATICBITMAP12, wxID_FRAME1STATICBITMAP13,
 wxID_FRAME1STATICBITMAP14, wxID_FRAME1STATICBITMAP15,
 wxID_FRAME1STATICBITMAP2, wxID_FRAME1STATICBITMAP3, wxID_FRAME1STATICBITMAP4,
 wxID_FRAME1STATICBITMAP7, wxID_FRAME1STATICBITMAP8, wxID_FRAME1STATICBITMAP9,
 wxID_FRAME1STATUESSTATICTEXT,wxID_FRAME1HISTORY
] = [wx.NewId() for _init_ctrls in range(23)]



class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
                          pos=wx.Point(229, 141), size=wx.Size(893, 469),
                          style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(877, 430))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
                               pos=wx.Point(0, 0), size=wx.Size(877, 430),
                               style=wx.TAB_TRAVERSAL)

        # 请输入关键词
        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
                                         label=u'\u8bf7\u8f93\u5165\u5173\u952e\u8bcd\uff1a',
                                         name='staticText1', parent=self.panel1, pos=wx.Point(48, 40),
                                         size=wx.Size(84, 14), style=0)

        # 输入框
        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
                                     parent=self.panel1, pos=wx.Point(136, 40), size=wx.Size(100, 22),
                                     style=0)

        # 查询按钮
        self.searchButton = wx.Button(id=wxID_FRAME1BUTTON1, label=u'\u67e5\u8be2',
                                      name='button1', parent=self.panel1, pos=wx.Point(48, 80),
                                      size=wx.Size(75, 24), style=0)
        self.searchButton.Bind(wx.EVT_BUTTON, self.OnButton1Button,
                               id=wxID_FRAME1BUTTON1)

        # 显示按钮
        self.showButton = wx.Button(id=wxID_FRAME1BUTTON2, label=u'\u663e\u793a',
                                    name='button2', parent=self.panel1, pos=wx.Point(160, 80),
                                    size=wx.Size(75, 24), style=0)
        self.showButton.Bind(wx.EVT_BUTTON, self.OnButton2Button,
                             id=wxID_FRAME1BUTTON2)
        self.showButton.Disable()  # 显示按钮默认禁用

        # 状态字段
        self.statuesStaticText = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
                                               label=u'\u72b6\u6001', name='staticText2', parent=self.panel1,
                                               pos=wx.Point(48, 120), size=wx.Size(184, 16), style=0)

        # 搜索历史
        self.history = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
                                               label=u'\u641c\u7d22\u5386\u53f2', name='staticText3',
                                               parent=self.panel1, pos=wx.Point(48, 150), size=wx.Size(48, 14),
                                               style=0)

        self.historyStaticText = wx.StaticText(id=wxID_FRAME1HISTORY, label='staticText2',
                                     name=u'history', parent=self.panel1, pos=wx.Point(48, 176),
                                     size=wx.Size(184, 208), style=0)
        self.initHistoryStaticText()

        # 图片列表
        self.staticBitmaps = [wx.StaticBitmap()] * 13
        self.staticBitmaps[1] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                id=wxID_FRAME1STATICBITMAP1, name='staticBitmap1',
                                                parent=self.panel1, pos=wx.Point(304, 32), size=wx.Size(120, 88),
                                                style=0)

        self.staticBitmaps[2] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                id=wxID_FRAME1STATICBITMAP2, name='staticBitmap2',
                                                parent=self.panel1, pos=wx.Point(448, 32), size=wx.Size(120, 88),
                                                style=0)

        self.staticBitmaps[3] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                id=wxID_FRAME1STATICBITMAP3, name='staticBitmap3',
                                                parent=self.panel1, pos=wx.Point(584, 32), size=wx.Size(128, 88),
                                                style=0)

        self.staticBitmaps[4] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                id=wxID_FRAME1STATICBITMAP4, name='staticBitmap4',
                                                parent=self.panel1, pos=wx.Point(728, 32), size=wx.Size(128, 88),
                                                style=0)

        self.staticBitmaps[5] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                id=wxID_FRAME1STATICBITMAP7, name='staticBitmap7',
                                                parent=self.panel1, pos=wx.Point(296, 136), size=wx.Size(128, 88),
                                                style=0)

        self.staticBitmaps[6] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                id=wxID_FRAME1STATICBITMAP8, name='staticBitmap8',
                                                parent=self.panel1, pos=wx.Point(448, 240), size=wx.Size(120, 88),
                                                style=0)

        self.staticBitmaps[7] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                id=wxID_FRAME1STATICBITMAP9, name='staticBitmap9',
                                                parent=self.panel1, pos=wx.Point(728, 248), size=wx.Size(128, 80),
                                                style=0)

        self.staticBitmaps[8] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                id=wxID_FRAME1STATICBITMAP11, name='staticBitmap11',
                                                parent=self.panel1, pos=wx.Point(728, 144), size=wx.Size(128, 80),
                                                style=0)

        self.staticBitmaps[9] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                id=wxID_FRAME1STATICBITMAP12, name='staticBitmap12',
                                                parent=self.panel1, pos=wx.Point(448, 136), size=wx.Size(120, 88),
                                                style=0)

        self.staticBitmaps[10] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                 id=wxID_FRAME1STATICBITMAP13, name='staticBitmap13',
                                                 parent=self.panel1, pos=wx.Point(584, 136), size=wx.Size(128, 88),
                                                 style=0)

        self.staticBitmaps[11] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                 id=wxID_FRAME1STATICBITMAP14, name='staticBitmap14',
                                                 parent=self.panel1, pos=wx.Point(584, 240), size=wx.Size(128, 88),
                                                 style=0)

        self.staticBitmaps[12] = wx.StaticBitmap(bitmap=wx.NullBitmap,
                                                 id=wxID_FRAME1STATICBITMAP15, name='staticBitmap15',
                                                 parent=self.panel1, pos=wx.Point(296, 240), size=wx.Size(128, 88),
                                                 style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        # 图片的长和宽
        self.width = 120
        self.height = 80
        self.initBitmapSize()

    # 查询按钮
    def OnButton1Button(self, event):
        keyword = self.textCtrl1.GetValue()
        print(keyword)
        if (tool.isKeyWordExist(keyword)):
            self.showButton.Enable()
            self.statuesStaticText.SetLabel("关键词已存在，可显示")
        else:
            self.statuesStaticText.SetLabel("正在查询......")
            # self.showButton.Disable()  # 显示按钮禁用
            tool.searchByKeyword(keyword)
            self.statuesStaticText.SetLabel("查询完毕，可显示")
            self.showButton.Enable()
        event.Skip()

    # 显示按钮
    def OnButton2Button(self, event):
        keyword = self.textCtrl1.GetValue()
        paths = tool.getUrls(keyword)
        for i in range( 0, len(paths) ):
            img = wx.Image(paths[i], wx.BITMAP_TYPE_ANY)
            bmp = img.Scale(self.width, self.height).ConvertToBitmap()
            self.staticBitmaps[i+1].SetBitmap( bmp )

    def initHistoryStaticText(self):
        keywords = tool.getHistoryKeyword()
        content = ""
        for k in keywords:
            content += k
            content += "\n"
        self.historyStaticText.SetLabel(content)

    def initBitmapSize(self):
        # 设置大小
        for i in range( 1, 13 ):
            self.staticBitmaps[i].SetSize( self.width, self.height )

        # 设置位置
        self.pointX = [ 0, 300, 450, 600, 750 ]
        self.pointY = [ 0, 30, 130, 230 ]
        for i in range( 1, 4 ):
            for j in range( 1, 5 ):
                self.staticBitmaps[(i-1)*4+j].SetPosition( ( self.pointX[j]-20, self.pointY[i]+10 ) )

