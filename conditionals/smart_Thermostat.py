device_status = "active"

tempreature = 38

if device_status == "active":
    if tempreature> 35 :
        print("High Tempreature Alert -- ")
    else:
        print("Tempreature is Normal")
else:
    print("Device is Offline")