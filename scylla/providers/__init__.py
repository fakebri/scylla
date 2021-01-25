from scylla.providers.proxy_list_provider import ProxyListProvider
from scylla.providers.proxy_scraper_provider import ProxyScraperProvider
from scylla.providers.proxylists_provider import ProxylistsProvider
from scylla.providers.proxynova_provider import ProxyNovaProvider
from scylla.providers.pubproxy_provider import PubproxyProvider
from scylla.providers.rmccurdy_provider import RmccurdyProvider
from scylla.providers.rudnkh_provider import RudnkhProvider
from scylla.providers.the_speedX_provider import TheSpeedXProvider
from .a2u_provider import A2uProvider
from .base_provider import BaseProvider
from .cool_proxy_provider import CoolProxyProvider
from .data5u_provider import Data5uProvider
from .free_proxy_list_provider import FreeProxyListProvider
from .http_proxy_provider import HttpProxyProvider
from .ipaddress_provider import IpaddressProvider
from .kuaidaili_provider import KuaidailiProvider
from .spys_me_provider import SpyMeProvider
from .spys_one_provider import SpysOneProvider
from .xici_provider import XiciProvider
# fakebri edit
from .fate0_proxy_list_provider import Fate0ProxyListProvider
from .smallseotools_provider import SmallseotoolsProvider
from .proxy_daily_provider import ProxyDailyProvider
from .i_86ip_and_66ip_provider import i89ipAnd66ipProvider
from .xiladaili_provider import XiladailiProvider
from .proxy_scraper_com_provider import ProxyScrapeComProvider
from .iphai_provider import IphaiProvider


all_providers = [
    A2uProvider,
    CoolProxyProvider,
    Data5uProvider,
    FreeProxyListProvider,
    HttpProxyProvider,
    # KuaidailiProvider,
    SpyMeProvider,
    SpysOneProvider,
    # XiciProvider
    IpaddressProvider,
    ProxyListProvider,
    ProxyScraperProvider,
    ProxylistsProvider,
    ProxyNovaProvider,
    PubproxyProvider,
    RmccurdyProvider,
    RudnkhProvider,
    TheSpeedXProvider,
    Fate0ProxyListProvider,
    SmallseotoolsProvider,
    ProxyDailyProvider,
    i89ipAnd66ipProvider,
    XiladailiProvider,
    ProxyScrapeComProvider,
    IphaiProvider
]

# Provider references:
# https://github.com/franklingu/proxypool/issues/2
