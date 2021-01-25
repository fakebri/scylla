#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-01-23 05:22:06
# @Author  : fakebri (null)
# @Link    : https://github.com/fakebri
# @Version : 0.1

from requests_html import HTML
import demjson

from scylla.database import ProxyIP
from .base_provider import BaseProvider


class Fate0ProxyListProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []

        lines = html.text.split("\n")
        for line in lines:
            try:
                data = demjson.decode(line)
            except Exception as e:
                pass
            ip_address = str(data['host'])
            port = str(data['port'])
            if ip_address and port:
                p = ProxyIP(ip=ip_address, port=port)
                ip_list.append(p)

        return ip_list

    def urls(self) -> [str]:
        return [
            'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
        ]
