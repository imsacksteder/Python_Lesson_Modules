'''
Code worked on by: Izze Sacksteder,
Last worked on: 3 Nov, 2020
'''

# In[1]:

import tkinter as tk

# In[6]:
#initialize the tk interface
# m = master
    
m = tk.Tk()
m.title('Key Exchange')
m.resizable(True, True) 


# In[6]:
tk.Label(m, text='Alice', fg="blue").grid(column=0)
tk.Label(m, text='~Public~', fg='green3').grid(row=0,column=1)
tk.Label(m, text='Bob', fg="red").grid(row=0, column=2)
tk.Label(m, text='').grid(row=3, column=2)
input1 = tk.Entry(m, textvariable = 'in1', fg='blue')
input2 = tk.Entry(m, textvariable = 'in2', fg='red')
inputPublic = tk.Entry(m, textvariable = 'inPub', fg='green3')
prime = tk.Entry(m, textvariable = 'pr', fg='green3')

tk.Label(m, text='Input Private Integer:').grid(row=1, column=0)
tk.Label(m, text='Input Public Key:', fg='green3').grid(row=1,column=1)
tk.Label(m, text='Input Prime Modulus:', fg='green3').grid(row=3, column=1)
tk.Label(m, text='Input Private Integer:').grid(row=1, column=2)

tk.Label(m, text='').grid(row=5)
tk.Label(m, text='').grid(row=6)
tk.Label(m, text='').grid(row=7)
tk.Label(m, text='').grid(row=8)
tk.Label(m, text='').grid(row=9)

#buttons
tk.Label(m, text='Click to compute private keys \u2192').grid(row=10, column=0)
tk.Label(m, text='\u2190 Click to compute private keys').grid(row=10, column=2)

#buttons
tk.Label(m, text='Click to compute shared code \u2192').grid(row=11, column=0)
tk.Label(m, text='\u2190 Click to compute chared code').grid(row=11, column=2)

input1.grid(row=2, column=0)
input2.grid(row = 2, column = 2)
inputPublic.grid(row = 2, column = 1)
prime.grid(row = 4, column = 1)
# In[7]:

#part 1 of Diffie-Hellman
def check():   
    
    aliceIn = int(input1.get())
    bobIn = int(input2.get())
    
    g = int(inputPublic.get())
    p = int(prime.get())

    alicePrivate = (g**aliceIn)%p
    bobPrivate = (g**bobIn)%p
    
    tk.Label(m, text=f'Alice computes ({g}^{aliceIn} mod {p})').grid(row=4, column=0)
    tk.Label(m, text=f'Bob computes ({g}^{bobIn} mod {p})').grid(row=4, column=2)

    tk.Label(m, text=f'private Key = {alicePrivate}', fg="blue").grid(row=5, column=0)
    tk.Label(m, text=f'private Key = {bobPrivate}', fg="red").grid(row=5, column=2)
    
    tk.Label(m, text=f'from Alice to Bob: {alicePrivate} \u2192', fg="green3").grid(row=6, column=1)
    tk.Label(m, text=f'\u2190 from Bob to Alice: {bobPrivate}', fg="green3").grid(row=7, column=1)
    
    
#part 2 of diffie Hellman   
def code():   
    
    aliceIn = int(input1.get())
    bobIn = int(input2.get())
    
    g = int(inputPublic.get())
    p = int(prime.get())

    alicePrivate = (g**aliceIn)%p
    bobPrivate = (g**bobIn)%p
    
    
    aliceShared = (bobPrivate**aliceIn)%p
    bobShared = (bobPrivate**aliceIn)%p
    
       
    tk.Label(m, text=f'secret code = {aliceShared}', fg="blue").grid(row=8, column=0)
    tk.Label(m, text=f'secret code = {bobShared}', fg="red").grid(row=8, column=2)
    
    tk.Label(m, text=f'Alice computes ({bobPrivate}^{aliceIn} mod {p})').grid(row=7, column=0)
    tk.Label(m, text=f'Bob computes ({alicePrivate}^{bobIn} mod {p})').grid(row=7, column=2)
    
    tk.Label(m,text='').grid(row=9)
    
# In[11]:
    
b = tk.Button(m, text="keys",
        command=check)
b.grid(row=10, column=1)

b0 = tk.Button(m, text="code",
        command=code)
b0.grid(row=11, column=1)

# In[6]:
m.mainloop()