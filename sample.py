import __pycache__/instaloader.cpython-310.pyc

mydata = instaloader.Instaloader()

name = input("ENter profilename")
pic = mydata.download_profile(name,profile_pic_only = True)