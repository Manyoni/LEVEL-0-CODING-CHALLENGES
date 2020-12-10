def convert_number_into_time (x):
    
    hour = int(x/60)
    minutes =x%60

    if hour <=1 and minutes <=1 :
        return " %d hour, %02d minute" % (hour,minutes)
    elif minutes <=1:
        return " %d hours, %02d minute" % (hour,minutes)
    elif hour <=1:
        return " %d hour, %02d minutes" % (hour,minutes)
    else:
        return "%d hours, %02d minutes" % (hour,minutes)

print (convert_number_into_time(62))