# import tkinter as tk
# from  tkinter import ttk
# win=tk.Tk()
# win.title("LOOP")

# # labels

# labels=['What is your name','What is your age','What is your gender','City','State','Country','Address']
# for i in range(len(labels)):
#     cur_label ='label'+ str(i)
#     cur_label=ttk.Label(win, text =labels[i])
#     cur_label.grid(row=i,column=0,sticky=tk.W,padx=40,pady=4)

# # entry box
# name_bar=tk.StringVar()
# user_info ={

#     'name':tk.StringVar(),
#     'age':tk.StringVar(),
#     'gender':tk.StringVar(),
#     'City':tk.StringVar(),
#     'State':tk.StringVar(),
#     'Country':tk.StringVar(),
#     'Address':tk.StringVar(),
# }
# counter = 0
# for i in user_info:
#     curr_entrybox='entry' +i
#     curr_entrybox=ttk.Entry(win,width=16,textvariable=user_info[i])
#     curr_entrybox.grid(column=1,row =counter,padx=40,pady=4)
#     counter+=1

# # name_bar=tk.StringVar()
# # name_entry =ttk.Entry(win, width=16, textvariable=name_bar)
# # name_entry.grid(row=0,column=1)

# def submit():
#     print(user_info['name'].get())
#     print(user_info['age'].get())
#     print(user_info['gender'].get())
#     print(user_info['City'].get())
#     print(user_info['State'].get())
#     print(user_info['Country'].get())
#     print(user_info['Address'].get())
# submit_button=ttk.Button(win,text='Submit',command=submit)
# submit_button.grid(row=7,column=1)
# win.mainloop()

import tkinter as tk 
from tkinter import ttk
win = tk.Tk()
win.title('LOOP')

labels = ['What is your name : ' , 'What is your age ', 'What is your gender : ', 'Country : ', 'State : ', 'City : ', 'address']

for i in range(len(labels)):
    cur_label = 'label' + str(i) # label0, label1
    cur_label = ttk.Label(win, text = labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W, padx = 2, pady=2)

# entry box
name_var = tk.StringVar() 
user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'country': tk.StringVar(),
    'state': tk.StringVar(),
    'city': tk.StringVar(),
    'address' : tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox = 'entry' + i # entryname # entryage
    cur_entrybox = ttk.Entry(win, width=16, textvariable=user_info[i])
    cur_entrybox.grid(column=1, row=counter, padx = 2, pady=2)
    counter += 1 

def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())

submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=7, columnspan=2)


win.mainloop()
