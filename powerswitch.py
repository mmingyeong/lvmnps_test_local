# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Mingyeong Yang (mingyeong@khu.ac.kr)
# @Date: 2021-07-05

#host: 163.180.145.123
#userid: admin
#passward: irlab
#scheme = 'http'
#base_url = '%s://%s' % (scheme, host)

from __future__ import annotations
import asyncio
import httpx


class PowerSwitch(object):

    def __init__(self, host=None, userid=None, password=None):
        """
        Class initialization
        """

        self.host = host
        self.userid = userid
        self.password = password

        self.scheme = 'http'
        self.base_url = '%s://%s' % (self.scheme, self.host)
        self.clients = {}

    async def add_client(self):
        """Access the url object"""
        
        auth = httpx.DigestAuth(self.userid, self.password)
        self.clients[self.host] = httpx.AsyncClient(
            auth=auth,
            base_url=self.base_url,
            headers={},
        )

    async def geturl(self, url='index.htm'):
        """Get a URL"""
        full_url = "%s/%s" % (self.base_url, url)

        if self.host not in self.clients:
            raise ValueError(f"Client for host {self.host} not defined.")
        
        r = await self.clients[self.host].get(url=full_url)
        
        if r.status_code != 200:
            raise RuntimeError(f"GET returned code {r.status_code}.")
        else:
            result = r.text
            
        await self.clients[self.host].aclose()
        print(result)
        return result

    async def puturl(self, url='index.htm'):
        """Get a URL"""
        full_url = "%s/%s" % (self.base_url, url)

        if self.host not in self.clients:
            raise ValueError(f"Client for host {self.host} not defined.")
        
        r = await self.clients[self.host].put(url=full_url)
        
        if r.status_code != 200:
            raise RuntimeError(f"GET returned code {r.status_code}.")
        else:
            result = r.content
            
        await self.clients[self.host].aclose()
        print(r)
        return result

    async def on(self, outlet_number:int):
        """Turn on power to an outlet
           False = Success
           True = Fail
        """
        await self.geturl(url='outlet?%d=ON' % outlet_number)


    async def off(self, outlet_number:int):
        """Turn on power to an outlet
           False = Success
           True = Fail
        """
        await self.geturl(url='outlet?%d=OFF' % outlet_number)


    async def cycle(self, outlet_number:int):
        if await self.off(outlet_number):
            return True
        await self.on(outlet_number)
        #await self.geturl(url='outlet?%d=CCL' % outlet_number)
        return False

    

class PowerException(Exception):
    """
    An error occurred taking the DLI Power Switch
    """
    pass