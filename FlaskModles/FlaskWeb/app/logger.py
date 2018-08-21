# -*- coding:utf-8 -*-
'''
日志记录文件,logging模块
'''

import logging
from flask import current_app
# from app import app

class WrLog(object):
    '''
    日志写入
    '''
    def __init__(self):
        
        self.hander = logging.FileHandler('flask.log', mode='a+')
        self.hander.setLevel(logging.INFO)
        self.logging_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
        )
        self.hander.setFormatter(self.logging_format)
        
    def wlog_debug(self, loginfo):
        'debug信息'
        self.app = current_app._get_current_object()
        self.app.logger.addHandler(self.hander)
        self.app.logger.debug(loginfo)

    def wlog_info(self, loginfo):
        'info信息'
        self.app = current_app._get_current_object()
        self.app.logger.addHandler(self.hander)
        self.app.logger.info(loginfo)

    def wlog_warning(self, loginfo):
        'warning信息'
        self.app = current_app._get_current_object()
        self.app.logger.addHandler(self.hander)
        self.app.logger.warning(loginfo)
    
    def wlog_error(self, loginfo):
        'error信息'
        self.app = current_app._get_current_object()
        self.app.logger.addHandler(self.hander)
        self.app.logger.error(loginfo)
