# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:20:59 2021

@author: QI
"""


"""
包子铺售卖情况模拟

"""
import random
import setup
import simpy

ini = int(input('请输入初始条件下，包子铺的顾客人数：'))        
Waiter =int(input('请输入包子铺的服务员：'))  
Costtime = 0   
Simtime = int(input('请输入本次模拟的时间：'))  

class Service(object):

    def __init__(self, env, Waiter, Costtime):
             
        self.env = env
        self.tool = simpy.Resource(env, Waiter)
        self.Costtime = Costtime

    def degree_of_satisfaction(self, human):
        
        yield self.env.timeout(Costtime)
        
        satis = ("%s 本次的满意程度%d%%" %(human, random.randint(65, 99)))
        print(satis)
def human(env, name, ens):
    
    
    Costtime = random.uniform(0.5,3)
    
    arrive = ('%s 在%.f分到达包子铺（1A%s）' % (name, env.now, name))
    print(arrive)
    with ens.tool.request() as request:
        
        yield request
        sev = ('%s 在%.f分开始被服务(2S%s)' % (name, env.now, name))
        print(sev)
        yield env.process(ens.degree_of_satisfaction(name))
        lev = ('%s 在%.f分离开包子铺(3L%s)' % (name, env.now, name))
        print(lev)
        
        with open ('testing.txt','a') as f:
            
            f.write('%s/n' %(arrive))
            f.write('%s/n' %(sev))
            f.write('%s/n' %(lev))
            f.write('%s/n' %(satis))


print('模拟开始')
env = simpy.Environment()
env.run(until=Simtime)
