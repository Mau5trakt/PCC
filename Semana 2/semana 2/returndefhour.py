def getsec(hours, minutes, seconds):
    return hours*3600 + minutes*60 + seconds

sec1= getsec(2,30,0)
sec2= getsec(0,45,15)
total= sec1 +sec2

print(total)