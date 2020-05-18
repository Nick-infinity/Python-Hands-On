# NIKHIL GUPTA
# 18 May 2020
# This program contains string foramtting techniques
#
name = "nIkhiL GupTa"
title_name = name.title()
print(title_name)
#
print(name.upper())
print(name.lower())
#
first_name = "nIkhil"
last_name = "gUpTa"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
#
#for python version 3.5 or lower use format method
#FORMAT
#
full_name = "{} {}".format(first_name,last_name)
print("Hello, {}!".format(full_name).title())
#
print("My Friends:\n\tParas\n\tAbhinav\n\tIsha")
#
#Stripping White Spaces
#
sweetdish = " Maal Pua "
print(sweetdish.rstrip())
print(sweetdish.lstrip())
print(sweetdish.strip())
#
name = "\tNikhil \n"
print(name.lstrip())
print(name.rstrip())
print(name.strip())
#
apostrophe_message = "Nikhil's tissot is dying"
print(apostrophe_message)
#
#RAW
print(r"C:/n/t/Documents")
#


