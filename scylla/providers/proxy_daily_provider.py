#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-01-24 02:09:18
# @Author  : fakebri (null)
# @Link    : https://github.com/fakebri
# @Version : $Id$

import re

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider


class ProxyDailyProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []
        # text = html.raw_html.decode('utf-8')
        content = r.html.find(
            'div .centeredProxyList.freeProxyStyle', first=True)
        proxy_list = re.findall(
            "\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\:\\d{1,5}", str(content.text))
        for proxy in proxy_list:
            proxy = proxy.split(':')
            ip_address = proxy[0]
            port = proxy[1]
            if ip_address and port:
                p = ProxyIP(ip=ip_address, port=port)
                ip_list.append(p)

    def urls(self) -> [str]:
        return [
            'https://proxy-daily.com/'
        ]
