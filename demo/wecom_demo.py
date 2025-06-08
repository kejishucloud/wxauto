from wxauto import WeCom


def main():
    wx = WeCom()
    who = '文件传输助手'
    for i in range(3):
        wx.SendMsg(f'wecom test {i+1}', who)


if __name__ == '__main__':
    main()
