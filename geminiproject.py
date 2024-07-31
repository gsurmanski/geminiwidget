#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:30:44 2024

@author: geffi
"""

import google.generativeai as genai
import os
#import tkinter for window management
from tkinter import *
from tkinter import ttk

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

def save_text():
    pass

def send_prompt():
    user_input = text_input.get("1.0", "end-1c")  # Get all text from the text area
    response = model.generate_content(user_input)
    text_input.delete("1.0", "end")  # Clear the text area

    # Update the output Text widget with the model's response

    text_output.delete("1.0", "end")  # Clear previous content
    text_output.insert("1.0", response.text)  # Insert new content


def clear_text(event):
    text_input.delete("1.0", "end")  # Clear the text area
    text_input.unbind("<FocusIn>")  # Unbind this event after the first click

#create initial frame
root = Tk()
root.title("Can I Assist?")
root.winfo_rgb('#3FF')
frm = ttk.Frame(root, padding=40)
frm.grid()
#create label
ttk.Label(frm, text="Ask Me Anything").grid(column=0, row=0)

#textarea. contaibs tag to designate text color
text_input = Text(frm, width=40, height=10, wrap="word")
text_input.tag_configure("colored", foreground="grey50")
text_input.insert('1.0', 'type something here', 'colored')
text_input.grid(column=0, row=2, columnspan=3, pady=(20, 0))
# Bind the clear_text function to the FocusIn event
text_input.bind("<FocusIn>", clear_text)

# Create an output area for Gemini output
text_output = Text(frm, width=40, height=10, wrap="word")
text_output.grid(column=0, row=5, columnspan=3, pady=(20, 0))

# Create a Scrollbar widget for the output Text widget
scrollbar_output = Scrollbar(frm, orient="vertical", command=text_output.yview)
text_output.config(yscrollcommand=scrollbar_output.set)
scrollbar_output.grid(column=3, row=5, columnspan=3, sticky="ns", padx=(10))

#send button
ttk.Button(frm, text="Send", command=send_prompt).grid(column=2, row=0)

#quit button
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


root.mainloop()