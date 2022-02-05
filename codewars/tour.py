# https://www.codewars.com/kata/5536a85b6ed4ee5a78000035
import math


def tour(friends, friend_towns, home_to_town_distances):
    arr = []
    for a in friends:
        for b in friend_towns:
            if a in b:
                arr.append(home_to_town_distances[b[-1]])
    dist = arr[0] + arr[-1]
    i = 1
    while i < len(arr):
        dist += math.sqrt(arr[i] ** 2 - arr[i - 1] ** 2)
        i += 1
    return int(dist)
