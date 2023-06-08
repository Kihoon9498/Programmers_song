import numpy as np

def solution(arr1, arr2):
    dots = np.dot(arr1, arr2)
    return dots.tolist()