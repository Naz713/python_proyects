#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:43:40 2018

@author: naz
"""
import random as r
import numpy as np

def create_json(l=12):
    return robject(l)
    
def robject(l):
    if l<= 0:
        return ""
    ret = "{"
    for i in np.arange(r.randint(1,l)):
        if i>0 :
            ret += ","+rstring(l-1)+":"+rvalue(l-1)
        else:
            ret += rstring(l-1)+":"+rvalue(l-1)
    return ret+"}"

def rvalue(l):
    if l<= 0:
        return ""
    for i in np.arange(r.randint(1,l)):
        op = r.randint(1,7)
        if op == 1:
            return rstring(l-1)
        elif op == 2 :
            return rnumber(l-1)
        elif op == 3:
            return robject(l-1)
        elif op == 4:
            return rarray(l-1)
        elif op == 5:
            return "true"
        elif op == 6:
            return "false"
        elif op == 7:
            return "null"
        else:
            return ""

def rarray(l):
    if l<= 0:
        return ""
        ret = "["
    for i in np.arange(r.randint(1,l)):
        if i>0 :
            ret += ","+rvalue(l-1)
        else:
            ret += rvalue(l-1)
    return ret+"]"