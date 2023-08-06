#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

import os
import sys
import platform

from loguru import logger

def get_logger(
    logger_name: str = '',
    work_path: str = '',
    debug: bool = False,
    level: str = 'INFO',
    dist_num: int = 0
) -> logger:
    """设置日志模块

    Args:
        logger_name (str, optional): 日志名称. Defaults to 'root'.
        work_path (str, optional): 工作路径用于设置日志路径logs. Defaults to None.
        debug (bool, optional): 是否调试模式. Defaults to False.
        level (str, optional): 日志记录级别. Defaults to 'DEBUG'.

    Returns:
        object: logger
    """
    if not logger_name:
        logger_name = os.path.basename(sys.argv[0]).split('.')[0]
    if not work_path:
        work_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    log_path = os.path.join(work_path, 'log')
    if not os.path.isdir(log_path):
        os.makedirs(log_path)

    if debug:
        level = 'DEBUG'

    log_file = os.path.join(log_path, f'{logger_name}.log')

    logger.add(
        log_file,
        filter="",
        level=level,
        rotation="00:00",
        retention="10 days",
        backtrace=True,
        diagnose=True
    )

    logger.info(f'SYSTEM:{platform.platform()}')
    logger.info(f'PYTHON:{sys.version}')
    logger.info(f'LOG: {log_path} [{level}]')
    return logger
