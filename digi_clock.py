def digi_clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    date = time.strftime("%x")
    
    my_clock.config(text= hour + ":" + minute + ":" + second + " " + am_pm)
    my_clock.after (1000, digi_clock)
    my_clock2.config(text = day + " " + date)
    
    
def update():
    my_clock.config(text = "New Text")