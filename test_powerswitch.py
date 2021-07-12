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

import asyncio
import powerswitch as ps

async def main():
    
    #set paramters
    host = '163.180.145.123'
    userid = 'admin'
    password = 'irlab'
    #scheme = 'http'
    #base_url = '%s://%s' % (scheme, host)

    dli = ps.PowerSwitch(host=host, userid=userid, password=password)
    await dli.add_client()
    #await dli.geturl()
    #await dli.puturl()
    await dli.on(1)
    #await dli.off(3)
    #await dli.cycle(outlet_number=1)

asyncio.run(main())