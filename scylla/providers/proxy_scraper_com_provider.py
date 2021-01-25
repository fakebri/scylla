#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-01-24 02:53:16
# @Author  : fakebri (null)
# @Link    : https://github.com/fakebri
# @Version : $Id$

from scylla.providers.plain_text_provider import PlainTextProvider


class ProxyScrapeComProvider(PlainTextProvider):

    def urls(self) -> [str]:
        return [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=all&simplified=true',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=yes&anonymity=all&simplified=true',
        ]
