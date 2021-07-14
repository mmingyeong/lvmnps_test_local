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
    
    tasks = []
    dli = ps.LVMPowerSwitch(host=host, userid=userid, password=password)
    await dli.add_client()
    #await dli.on(3)
    #await dli.on(4)
    #await dli.off()
    #await dli.cycle()
    get = await dli.getstatus()
    print(get)
    #tasks.append(dli.on())
    #tasks.append(dli.on())
    #await asyncio.gather(*tasks)

asyncio.run(main())