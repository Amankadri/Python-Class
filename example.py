from random import random



import instaloader

L = instaloader.Instaloader()

name=input("Enter profilename:")
pic = L.download_profile(name,profile_pic_only = True)