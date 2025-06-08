"""Simple Enterprise WeChat demo.

This script sends a few test messages via :class:`WeCom`.  In environments
without the Enterprise WeChat client, initialisation may fail.  The example now
handles such errors and prints a helpful message instead of raising an
exception.
"""

from wxauto import WeCom


def main():
    try:
        wx = WeCom()
    except Exception as exc:  # pragma: no cover - platform specific
        print(f"Failed to initialise WeCom: {exc}")
        print("Ensure the Enterprise WeChat client is running and accessible.")
        return

    who = '文件传输助手'
    for i in range(3):
        wx.SendMsg(f'wecom test {i + 1}', who)


if __name__ == '__main__':
    main()
