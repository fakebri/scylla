#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-01-24 03:20:55
# @Author  : BriBri (null)
# @Link    : https://github.com/iBriBri
# @Version : $Id$
import re

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider


class IphaiProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []
        data = html.raw_html.decode('gb2312')
        proxy_list = re.findall(
            "\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\:\\d{1,5}", str(data))
        for proxy in proxy_list:
            ip_address = proxy[0]
            port = proxy[1]
            if ip_address and port:
                p = ProxyIP(ip=ip_address, port=port)
                ip_list.append(p)

    def urls(self) -> [str]:
        return [
            'http://www.ip3366.net/free/?stype=1',
            'http://www.ip3366.net/free/?stype=2',
        ]
