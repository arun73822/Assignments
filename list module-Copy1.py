#!/usr/bin/env python
# coding: utf-8

# In[104]:


import logging
import copy

logging.basicConfig(filename='list.log', level=logging.DEBUG, format='%(asctime)s,%(levelname)s,%(message)s')

class list_1:
    """ The list_1 class contains all operations of list like 
    append,copy,count,extend,index,insert,pop,remove,reverse,sort,clear """
    def __init__(self,x):
        """ x is must be in form of list """
        self.x=x
        logging.info('list is {}'.format(self.x))
    def append(self,*a):
        """ The append method takes only one argument. the argument is any data type """
        if type(self.x)==list:
            self.x=self.x+[a]
            logging.info('the value append is {}'.format(a))
            logging.info('After append list is {}'.format(self.x))
            return ('After append list is {}'.format(self.x))
    def copy(self):
        """ The copy method gives the shallow copy """
        x=input('Give the new list name ')
        old_list=self.x
        new_list=copy.copy(old_list)
        logging.info('The new list name is {}'.format(x))
        logging.info('old list is {}, {} is {}'.format(old_list,x,new_list))
        logging.info('old list id is {}, {} id is {}'.format(id(old_list),x,id(new_list)))
        return ('old list is {}, {} is {}'.format(old_list,x,new_list))
    def count(self,r):
        """ Return number of occurrences of value """
        a=r
        count=0
        for i in (self.x):
            if type(i)==tuple or type(i)==list or type(i)==set:
                for j in i:
                    self.x.append(j)
            elif type(i)==dict:
                for l in i.values():
                    self.x.append(l)
            elif a==i:
                count=count+1
        logging.info('Number of occurences of {} is {} times pesent in the list'.format(a,count))
        return count
    def extend(self,y): 
        if type(y)==int or type(y)==float or type(y)==complex:
            logging.exception('Please give valid input given to y')
            raise TypeError('Please give valid input',y)
        elif type(y)==list or type(y)==tuple or type(y)==str or type(y)==set:
            for i in y:
                (self.x).append(i)
            logging.info('Extend total list is {}'.format(self.x))
            return self.x
    def index(self):
        """ This function may help to find index of primitie data types """
        for i in range(len(self.x)):
            if type(self.x[i])==int or type(self.x[i])==float or type(self.x[i])==str or type(self.x[i])==bool or type(self.x[i])==list or type(self.x[i])==tuple or type(self.x[i])==dict:
                logging.info('element is {} , index is {} , type of element is {}'.format(self.x[i],i,type(self.x[i])))
            if type(self.x[i])==list:
                for j in range(len(self.x[i])):
                    logging.info('element is {} , index is {} , type of element is {}'.format(self.x[i][j],j,type(self.x[i][j])))
            if type(self.x[i])==tuple:
                for k in range(len(self.x[i])):
                    logging.info('element is {} , index is {} , type of element is {}'.format(self.x[i][k],k,type(self.x[i][k])))
            if type(self.x[i])==dict:
                for l in range(len(self.x[i])):
                    for m in self.x[i].keys():
                        for n in self.x[i].values():
                            logging.info('key is {} , value is {} , type of value is {}'.format(m,n,type(n)))
    def insert(self,ind,value):
        """ Insert object before index."""
        s=len(self.x)
        if len(self.x)<=ind:
            self.x.append(value)
            logging.info('The after insertion list is {}'.format(self.x))
            return ('The after insertion list is {}'.format(self.x))
        else:
            self.x[ind]=value
            logging.info('The afetr insertion list is {}'.format(self.x))
            return ('The afetr insertion list is {}'.format(self.x))
    def pop(self,index):
        """ Remove and return item at index """
        logging.info('The poping element is {}'.format(self.x[index]))
        l1=[]
        for i in range(len(self.x)):
            if self.x[index]!=self.x[i]:
                l1.append(self.x[i])
        self.x=l1
        logging.info('After poping list is {}'.format(self.x))
        return ('After poping list is {}'.format(self.x))
    def remove(self,value):
        """ Remove first occurrence of value."""
        l2=[]
        for i in range(len(self.x)):
            if value!=self.x[i]:
                l2.append(self.x[i])
            if value not in self.x:
                logging.info('removing element is {}'.format(value))
                logging.exception('element not in list {}'.format(value))
                raise ValueError('element not in list',value)
                break
        self.x=l2
        logging.info('After call removing method list is {}'.format(self.x))
        return self.x
    def reverse(self):
        """ Reverse *IN PLACE*."""
        self.x=self.x[ : : -1]
        logging.info('The After reversing list is {}'.format(self.x))
        return self.x
    def sort(self):
        """ Sort the list in ascending order """
        for i in range(len(self.x)):
            for j in range(i+1,len(self.x)):
                try:
                    if self.x[i]>self.x[j]:
                        self.x[i],self.x[j]=self.x[j],self.x[i]
                except Exception as e:
                    logging.exception(e)
                break    
        return self.x        
        logging.info('Sorted list is {}'.format(self.x))
    def clear(self):
        """ Remove all items from list."""
        l3=[]
        self.x=l3
        logging.info('After clear method executed list is {}'.format(self.x))
        return self.x


# In[ ]:





# In[105]:


b=list_1([1,2,3,4,5,7,90])


# In[91]:


b.append([90,20,19],(60,45,78),{'k1':1,'k2':2})


# In[80]:


b.copy()


# In[92]:


b.count(1)


# In[93]:


b.extend([100,2.3])


# In[83]:


b.index()


# In[94]:


b.insert(3,7000)


# In[95]:


b.pop(6)


# In[96]:


b.remove(1)


# In[97]:


b.reverse()


# In[98]:


b.sort()


# In[ ]:


b.clear()


# In[ ]:


logging.shutdown()


# In[ ]:




