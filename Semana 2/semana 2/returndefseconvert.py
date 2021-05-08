def sec(seconds):
    hours = seconds // 3600 #The double slash indicates is a mod divition
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, seconds, minutes = sec(5000)
print(hours, minutes, seconds)
