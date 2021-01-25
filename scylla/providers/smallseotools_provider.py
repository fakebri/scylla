#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-01-24 00:52:09
# @Author  : fakebri (null)
# @Link    : https://github.com/fakebri
# @Version : $Id$
import re

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider


class SmallseotoolsProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []

        content = html.find('div#page-url-list', first=True)

        proxy_list = re.findall(
            "\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\:\\d{1,5}", str(content.html))

        for proxy in proxy_list:

            proxy = proxy.split(':')

            ip_address = proxy[0]
            port = proxy[1]

            if ip_address and port:
                p = ProxyIP(ip=ip_address, port=port)
                ip_list.append(p)

        return ip_list

    def urls(self) -> [str]:
        return [
            'https://smallseotools.com/free-proxy-list/'
        ]
