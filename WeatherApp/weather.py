# Program to make a weather displaying app

# Importing all the necessasry libraries 
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import requests
from time import strftime
from PIL import ImageTk, Image
from urllib.request import urlopen
from io import BytesIO

# A function to get data from the api and add it  to the labels and frames
def getWeather(canvas):
    # Input box to enter the city name
    city=textfileld.get()
    # Requesting the api to send data about the entered place
    api= "http://api.weatherapi.com/v1/current.json?key=f8aa8f58913041549b362154222303&q="+city+"&aqi=no"
    json_data=requests.get(api).json()
    # Getting the data about the place from the api 
    condition=json_data["current"]["condition"]["text"]
    temp=float(json_data["current"]["temp_c"])
    pressure=float(json_data["current"]["pressure_in"])
    humidity=float(json_data["current"]["humidity"])
    location=json_data["location"]["name"]
    lat=json_data["location"]["lat"]
    lon=json_data["location"]["lon"]
    tm=json_data["location"]["localtime"]
    feels_like=json_data["current"]["feelslike_c"]
    # Importing the imagelink from the api and convorting the image link to image
    URL=json_data["current"]["condition"]["icon"]
    URL="https:"+URL
    u=urlopen(URL)
    raw_data=u.read()
    u.close()
    i=Image.open(BytesIO(raw_data))
    img=ImageTk.PhotoImage(i)

    # Finalizing all the data and adding it to the lables
    final_info=condition+"\n"+str(temp)
    final_data="\nPressure : "+str(pressure)+"\nHumidity : "+str(humidity)
    local_data=location+"\nLatitude: "+str(lat)+"\nLongitude: "+str(lon)+"\nLocal Date and Time: "+str(tm)+"\nFeels Like: "+str(feels_like)
    label3.config(text=local_data)
    label1.config(text=final_info)
    label2.config(text=final_data)
    ilable.config(image=img)
    ilable.image=img



# A method for the clock in the app
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Creating and setting up the  the canvas environment
canvas=tk.Tk()
canvas.geometry("700x600")
canvas.title("Weather App")
canvas.configure(bg="grey")
# Importing some fonts and customizing them for the application
f=("poppins",15,"bold")
t=("poppins",35,"bold")

# Customizing the canvas and calling the function to get data
textfileld = tk.Entry(canvas,font =t,bg="black",fg="white")
textfileld.pack(pady= 20)
textfileld.focus()
textfileld.bind('<Return>',getWeather)


# Creating frames to keep the time and weather widget
frame=Frame(canvas)
frame.pack(side=TOP)
wframe=Frame(canvas)
wframe.pack(side=TOP)

# Creating labels to keep all the data and pack them in the canvas
label=Label(frame,font=("ds-digital",20),background="grey",foreground="red")
label.pack(anchor='center')
time()
ilable=tk.Label(wframe,bg="grey")
ilable.pack()
label1=tk.Label(canvas,font=t,bg="grey")
label1.pack()
label2=tk.Label(canvas,font=f,bg="grey")
label2.pack()
label3=Label(canvas,anchor="w",font=f,bg="grey")
label3.pack()

# Telling python to run the tkinter canvas loop
canvas.mainloop()