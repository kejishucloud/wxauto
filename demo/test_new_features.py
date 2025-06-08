import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wxauto import WeChat


def test_stubs():
    wx = WeChat()
    tests = [
        lambda: wx.SendCustomEmoji('path/to/emoji.png', '文件传输助手'),
        lambda: wx.MergeForward(['msg1', 'msg2'], ['张三']),
        lambda: wx.QuoteAt('msg_id', ['张三']),
        lambda: wx.AddFriendFromMessage('msg_id'),
        lambda: wx.GetDetailFromMessage('msg_id'),
        lambda: wx.GetCardMessageLink('msg_id'),
        lambda: wx.EditRemark('张三', '测试备注'),
        lambda: wx.AddTags('张三', ['测试']),
        lambda: wx.InviteToGroup('张三', '测试群'),
        lambda: wx.SetGroupName('测试群', '新群名'),
        lambda: wx.SetGroupRemark('测试群', '群备注'),
        lambda: wx.SetGroupAnnouncement('测试群', '公告内容'),
        lambda: wx.SetSelfNickInGroup('测试群', '我的昵称'),
        lambda: wx.MuteSession('张三', True),
        lambda: wx.GetGroupList(),
        lambda: wx.Moments(),
        lambda: wx.BackgroundMode(True),
    ]
    for func in tests:
        try:
            func()
        except NotImplementedError as e:
            print(e)


if __name__ == '__main__':
    test_stubs()
