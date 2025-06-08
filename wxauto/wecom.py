from .wxauto import WeChat

class WeCom(WeChat):
    """企业微信自动化实例"""
    def __init__(self, language: str = 'cn', debug: bool = False) -> None:
        super().__init__(language=language, debug=debug, client='wecom')
