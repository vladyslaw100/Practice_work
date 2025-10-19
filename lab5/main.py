import time
import random
import os
import json
import requests
import math
import numpy as np
import pandas as pd
import numbers
import decimal

#time
def lib_time():
    try:
        time.sleep(3)
        print("Time")
    except Exception as e:
        print(f"Neuspishno: {e}")
def lib_random():
    try:
        print("Random: ", random.random())
    except Exception as e:
        print(f"Neuspishno: {e}")
def lib_math():
    try:
        a = 15
        print("math:", math.sqrt(a))
    except Exception as e:
        print(f"Neuspishno: {e}")

def lib_numpy():
    try:
        print("numpy: ", np.zeros(4))
    except Exception as e:
        print(f"Neuspishno: {e}")

def lib_numbers():
    try:
        x = 5.3

        if isinstance(x, numbers.Number):
            print(f"numbers: {x} — tse chyslo")
        else:
            print(f"numbers: {x} — ne chyslo")

    except Exception as e:
        print(f"Neuspishno: {e}")

def main():
    lib_time()
    lib_random()
    lib_math()
    lib_numbers()
    lib_numpy()

if __name__ == '__main__':
    main()