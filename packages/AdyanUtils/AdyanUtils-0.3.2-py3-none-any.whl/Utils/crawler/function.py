#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/2 15:22
# @Author  : Adyan
# @File    : function.py


import json
import re
import time
from datetime import datetime

import pytz

cntz = pytz.timezone("Asia/Shanghai")


class Fun:

    @classmethod
    def find(
            cls, target: str,
            dictData: dict,
    ) -> list:
        queue = [dictData]
        result = []
        while len(queue) > 0:
            data = queue.pop()
            for key, value in data.items():
                if key == target:
                    result.append(value)
                elif isinstance(value, dict):
                    queue.append(value)
        if result:
            return result[0]

    @classmethod
    def finds(
            cls, target: str,
            dictData: dict,
    ) -> list:
        queue = [dictData]
        result = []
        while len(queue) > 0:
            data = queue.pop()
            if isinstance(data, str):
                continue
            if isinstance(data, dict):
                for key, value in data.items():
                    if key == target:
                        if value not in result:
                            result.insert(0, value)
                    queue.append(value)
            if isinstance(data, list):
                for dic in data:
                    queue.append(dic)
        if result:
            return result

    @classmethod
    def timeconvert(cls, times, timestamp=None, int_time=None):
        if int_time:
            return int(time.mktime(time.strptime(times, "%Y-%m-%d")))
        if type(times) is str:
            times = int(time.mktime(time.strptime(times, "%Y-%m-%d %H:%M:%S")))
        if timestamp:
            times = times + timestamp
        return str(datetime.fromtimestamp(times, tz=cntz))

    @classmethod
    def is_None(
            cls, dic: dict,
    ) -> dict:
        """
        :param dic: dict
        :return: 返回字典中值是None的键值对
        """
        return {
            k: v
            for k, v in dic.items()
            if not v
        }


class ReDict:

    @classmethod
    def string(
            cls,
            re_pattern: dict,
            string_: str,
    ):
        if string_:
            return {
                key: cls.compute_res(
                    re_pattern=re.compile(scale),
                    string_=string_.translate(
                        {
                            ord('\t'): '', ord('\f'): '',
                            ord('\r'): '', ord('\n'): '',
                            ord(' '): '',
                        })
                )
                for key, scale in re_pattern.items()
            }

    @classmethod
    def compute_res(
            cls,
            re_pattern: re,
            string_=None
    ):
        data = [
            result.groups()[0]
            for result in re_pattern.finditer(string_)
        ]
        if data:
            try:
                return json.loads(data[0])
            except:
                return data[0]
        else:
            return None
