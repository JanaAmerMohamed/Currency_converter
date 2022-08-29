import tkinter as tk
import pip._vendor.requests as requests
import json 

windos=tk.Tk()
windos.title("Currency converter")
windos.geometry("420x420")
windos.config(background="#00688B")
windos.resizable(height=False, width=False)

#label at the top of the page 
lab1=tk.Label(text="Entre the value here", font="Times", bg="#00688B",fg="yellow")
lab1.pack()

# text input
text1=tk.Canvas( width=160, height=40, bg="#00688B" )
text1.pack()
a=tk.Entry()
text1.create_window(81.5,22, window=a,width=160,height=39)


# label2 of the ( from)
lab2=tk.Label(text="From:", font="Times", bg="#00688B",fg="yellow",width=12, height=1,padx=0,pady=0 )
lab2.place(x=10,y=100)


#label3 of the(to)
lab3=tk.Label(text="To:", font="Times", bg="#00688B",fg="yellow",width=12, height=1,padx=0,pady=0 )
lab3.place(x=240,y=100)

#text2  for the (from)
text2=tk.Canvas( width=60, height=30, bg="#00688B" )
b=tk.Entry()
text2.create_window(31.5,16.5,window=b,width=60,height=30)
text2.place(x=50,y=135)

#text3 from the (to) 
text3=tk.Canvas( width=60, height=30, bg="#00688B" )
c=tk.Entry()
text3.create_window(31.5,16.5,window=c,width=60,height=30)
text3.place(x=290,y=135)


# text 4 output
text4=tk.Label(text=" ", width=15,height=2, bg="#D6D6D6",fg="black",font="Times")
text4.place(x=120,y=230)

#==========================================
# function 
def converter():
    amount_1=a.get()
    from_currency=b.get()
    to_currency=c.get()
    

    url = f"https://api.fastforex.io/convert?from={from_currency}&to={to_currency}&amount={amount_1}&api_key=cd3e787ddd-dcdc70dba8-rhawrm"

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)
    data=json.loads(response.text)
    converted_amount=data['result'][to_currency]
    text4['text']=converted_amount
    print(converted_amount)

#========================================

# button
button=tk.Button(text="Convert", width=10, padx=5,height=1,bg="yellow",fg="black",font="Times",command=converter)
button.place(x=260,y=340)


windos.mainloop()
