# program to calculate the speed ?
# // speed=distance/time 


distance=float(input("enter your distance in km \n"))

time=float(input("enter your time hour \n"))

distance=distance*100

time=time*60

speed=distance/time

print(f"distance = {distance} meter\ntime = {time} minute \nspeed = {speed} per minute")
