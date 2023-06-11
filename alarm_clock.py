'''
Python Projects:
Advanced Alarm Clock using Python Tkinter
'''

from tkinter import *
import time
from PIL import ImageTk
from tkinter import ttk, messagebox
from playsound import playsound
import multiprocessing
from datetime import datetime
from threading import *

# Hours List.
hours_list = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24']

# Minutes List.
minutes_list = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59']

# Ringtones list.
ringtones_list = ['mom_calling', 'nice_wake_up', 'romantic', 
'twirling_intime', 'wakeup_alarm_tone']

# Ringtone Paths.
ringtones_path = {
    'mom_calling': 'Ringtones/mom_calling.mp3',
    'nice_wake_up': 'Ringtones/nice_wake_up.mp3',
    'romantic': 'Ringtones/romantic.mp3',
    'twirling_intime': 'Ringtones/twirling_intime.mp3',
    'wakeup_alarm_tone': 'Ringtones/wakeup_alarm_tone.mp3'
}

# The Class: Alarm Clock.
class Alarm_Clock:
    def __init__(self, root):
        self.window = root
        self.window.geometry("680x420+0+0")
        self.window.title("PyClock")

        # Background image of the first window.
        self.bg_image = ImageTk.PhotoImage(file="Images/image_1.jpg")
        self.background = Label(self.window, image=self.bg_image)
        self.background.place(x=0,y=0,relwidth=1,relheight=1)

        # Display Label that shows the current time in the
        # first window
        self.display = Label(self.window, font=('Helvetica', 34), 
        bg = 'gray8', fg = 'yellow')
        self.display.place(x=100,y=150)

        # Calling the the function.
        self.show_time()

        # Placing the set alarm button. 
        # Font Type: relief solid font helevetica.
        set_button = Button(self.window, text="Set Alarm", 
        font=('Helvetica',15), bg="green", fg="white", 
        command=self.another_window)
        set_button.place(x=270, y=220)

    # This function shows the current time in the first window.
    def show_time(self):
        current_time = time.strftime('%H:%M:%S %p, %A')
        # Placing the time format level.
        self.display.config(text = current_time)
        self.display.after(100, self.show_time)

    # Another Window: This window will show, when the "Set Alarm"
    # Button will pressed.
    def another_window(self):
        self.window_2 = Tk()
        self.window_2.title("Set Alarm")
        self.window_2.geometry("680x420+200+200")
        
        # Hour Label.
        hours_label = Label(self.window_2, text="Hours", 
        font=("times new roman",20))
        hours_label.place(x=150, y=50)

        #  Minute Label.
        minute_label = Label(self.window_2, text="Minutes", 
        font=("times new roman",20))
        minute_label.place(x=450, y=50)

        # Hour Combobox.
        self.hours = StringVar()
        self.hours_combobox = ttk.Combobox(self.window_2, 
        width=10, height=10, textvariable=self.hours, 
        font=("times new roman",15))
        self.hours_combobox['values'] = hours_list
        self.hours_combobox.current(0)
        self.hours_combobox.place(x=150,y=90)

        # Minute Combobox.
        self.minutes = StringVar()
        self.minutes_combobox = ttk.Combobox(self.window_2, 
        width=10, height=10, textvariable=self.minutes, 
        font=("times new roman",15))
        self.minutes_combobox['values'] = minutes_list
        self.minutes_combobox.current(0)
        self.minutes_combobox.place(x=450,y=90)

        # Ringtone Label.
        ringtone_label = Label(self.window_2, text="Ringtones", 
        font=("times new roman",20))
        ringtone_label.place(x=150, y=130)

        # Ringtone Combobox(Choose the ringtone).
        self.ringtones = StringVar()
        self.ringtones_combobox = ttk.Combobox(self.window_2, 
        width=15, height=10, textvariable=self.ringtones, 
        font=("times new roman",15))
        self.ringtones_combobox['values'] = ringtones_list
        self.ringtones_combobox.current(0)
        self.ringtones_combobox.place(x=150,y=170)

        # Title or Message Label.
        message_label = Label(self.window_2, text="Message", 
        font=("times new roman",20))
        message_label.place(x=150, y=210)

        # Message Entrybox: This Message will show, when
        # the alarm will ringing.
        self.message = StringVar()
        self.message_entry = Entry(self.window_2, 
        textvariable=self.message, font=("times new roman",14), width=30)
        self.message_entry.insert(0, 'Wake Up')
        self.message_entry.place(x=150, y=250)

        # Test Button: For testing the ringtone music.
        test_button = Button(self.window_2, text='Test', 
        font=('Helvetica',15), bg="white", fg="black", command=self.test_window)
        test_button.place(x=150, y=300)

        # The Cancel Button: For cancel the alarm.
        cancel_button = Button(self.window_2, 
        text='Cancel', font=('Helvetica',15), bg="white", 
        fg="black", command=self.window_2.destroy)
        cancel_button.place(x=390, y=300)

        # The Start Button: For set the alarm time
        start_button = Button(self.window_2, text='Start',
        font=('Helvetica',15), bg="green", fg="white", command=self.Threading_1)
        start_button.place(x=490, y=300)


        self.window_2.mainloop()

# In this function, I have used python multiprocessing module
# to play the ringtones while the alarm gets notified.
    def test_window(self):
        process = multiprocessing.Process(target=playsound, 
        args=(ringtones_path[self.ringtones_combobox.get()],))
        process.start()
        messagebox.showinfo('Playing...', 'press ENTER to stop playing')
        process.terminate()

    # Creating a thread
    def Threading_1(self):
        x = Thread(target=self.set_alarm_time)
        x.start()

# This function gets called when the start button pressed 
# in the another window for setting alarm time.
    def set_alarm_time(self):
        alarm_time = f"{self.hours_combobox.get()}:{self.minutes_combobox.get()}"
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        try:
            while True:
                # The current time is in 24 hour format
                current_time = datetime.now()
                # Converting the current time into hour and minute
                current_time_format = current_time.strftime("%H:%M")
                if current_time_format == alarm_time:
                    process = multiprocessing.Process(target=playsound, 
                    args=(ringtones_path[self.ringtones_combobox.get()],))
                    process.start()
                    # Messagebox: This messagebox will show, when the
                    # alarm will ringing.
                    messagebox.showinfo("Alarm",f"{self.message_entry.get()}, It's {alarm_time}")
                    process.terminate()
                    break
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")

# The main function.
if __name__ == "__main__":
    root = Tk()
    # Object of Alarm_Clock class.
    obj = Alarm_Clock(root)
    root.mainloop()
    