from random import randint
import pytest
from hashtable import HashTable
class TestClass:
    def test_adder(self):
        st = set()
        hasht = HashTable()
        for i in range(1000):
          num = randint(1, 1000000000)
          hasht.add(num)
          st.add(num)
        s = set()
        for j in hasht:
          s.add(j)
        assert s == st


    def test_remover(self):
      st = set()
      hasht = HashTable()
      for i in range(100000):
        num = randint(1, 1000)
        hasht.add(num)
        st.add(num)

      for i in range(10):
        num = randint(1, 1000)
        hasht.remove(num)
        st.remove(num)
      s = set()
      for j in hasht:
        s.add(j)
      assert s == st

    def test_checker(self):
      st = set()
      hasht = HashTable()
      for i in range(10000):
        num = randint(1, 1000000)
        hasht.add(num)
        st.add(num)
      s = set()
      ss = set()
      for i in range(10):
        num = randint(1, 1000000)
        if (num in hasht):
          s.add(num)
        if (num in st):
          ss.add(num)
      
      assert s == ss
    
    def test_len(self):
      st = set()
      hasht = HashTable()
      for i in range(100000):
        num = randint(1, 1000)
        hasht.add(num)
        st.add(num)
      s = set()
      ss = set()
      for i in range(10):
        num = randint(1, 1000)
        hasht.remove(num)
        st.remove(num)
        s.add(len(hasht))
        ss.add(len(st))

      assert s == ss

