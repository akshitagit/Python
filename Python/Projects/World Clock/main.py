import datetime  

while (True):
  city = input("Enter city: ")
  city = city.lower()
  current_time = datetime.datetime.now()
  hour = current_time.hour
  minute = current_time.minute
  second = current_time.second
  
  if city == "boston":
    hour = hour - 4 

  elif city == "tokyo":
    hour = hour + 9

  elif city == "chicago":
    hour = hour - 5 

  elif city == "seattle":
    hour = hour - 7

  ## add more cities here

  elif city == "mumbai":
    hour = hour + 5.5

  elif city == "beijing":
    hour = hour + 8

  elif city == "karachi":
    hour = hour + 5

  elif city == "now":
    hour = hour

  elif city == "exit":
    break
    
  else:
    print(city, "is not added")
    city = "GMT" 

  print(city[0].upper() + city[1:].lower(), str(hour) + ":" + str(minute) + ":" + str(second))

# The error is of GMT time setting. As GMT time setting outputs time as of now.
# The error is of GMT time setting. As GMT time setting outputs time as of now.
