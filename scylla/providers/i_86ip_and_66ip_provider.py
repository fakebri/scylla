#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-01-24 02:44:50
# @Author  : BriBri (null)
# @Link    : https://github.com/iBriBri
# @Version : $Id$

import re

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider


class i89ipAnd66ipProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []
        data = html.text
        proxy_list = re.findall(
            "\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\:\\d{1,5}", str(data))
        for proxy in proxy_list:
            proxy = proxy.split(':')
            ip_address = proxy[0]
            port = proxy[1]
            if ip_address and port:
                p = ProxyIP(ip=ip_address, port=port)
                ip_list.append(p)

    def urls(self) -> [str]:
        return [
            'https://www.89ip.cn/tqdl.html?api=1&num=9999&port=&address=&isp=',
            'http://www.66ip.cn/mo.php?sxb=&tqsl=9999&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=',
        ]
