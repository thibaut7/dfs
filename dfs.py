# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 09:15:14 2021

@author: thibaut
"""
from collections import defaultdict
class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
        
    def addEdge(self, u, v):
        
         
        
    def dfs(self, s):
        
        visited = []
        visited.append(s)
        
        for i in self.graph[s]:
            if i not in vistied:
                dfs(self, i)