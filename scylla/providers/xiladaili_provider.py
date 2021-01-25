#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-01-24 03:11:42
# @Author  : BriBri (null)
# @Link    : https://github.com/iBriBri
# @Version : $Id$
import re

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider


class XiladailiProvider(BaseProvider):

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
            'http://www.xiladaili.com/putong/',
            'http://www.xiladaili.com/gaoni/',
            'http://www.xiladaili.com/http/',
            'http://www.xiladaili.com/https/',
        ]
