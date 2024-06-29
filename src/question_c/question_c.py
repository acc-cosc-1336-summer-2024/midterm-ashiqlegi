#write functions here, don't add input('') statements here
def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0:
        return "Invalid Argument"
    if minutes < 0:
        return "Invalid Argument"
    conversion = 0.621371
    miles = kilometers * conversion
    hours = minutes/60
    return miles/hours
    
    
