from tkinter import *
import time


# --------------------- GUI Setup ---------------------
root = Tk()
root.title("Typing Speed Tester")
root.geometry("600x450")  # Set window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="#f0f0f0")

# --------------------- Functions ---------------------
root.running = False


def update_timer():
    """Update the timer label while typing."""
    if root.running:
        calculate_time = time.time() - root.start_time
        timer_label.config(text=f"Time: {calculate_time:.2f}s")
        root.after(100, update_timer)


def start_timer():
    """Start the typing test."""
    text_box.config(state="normal")
    root.start_time = time.time()
    timer_label.config(text="Time: 0s")
    root.running = True
    result_label.config(text="")
    text_box.delete("1.0", END)
    wpm_label.config(text="Words per Min: 0")
    word_label.config(text="Words: 0")
    update_timer()


def stop_timer():
    """Stop the typing test and calculate final time."""
    text_box.config(state="disabled")
    root.stop_time = time.time()
    calculate_time = root.stop_time - root.start_time
    timer_label.config(text=f"Final time: {calculate_time:.2f}s")
    root.running = False
    words(calculate_time)


def words(calculate_time):
    typed_text = text_box.get("1.0", END)
    counted_words = len(typed_text.split())
    time_in_mins = calculate_time / 60
    wpm = counted_words / time_in_mins if time_in_mins > 0 else 0
    # if time_in_mins > 0:
    #     wpm = counted_words / time_in_mins
    # else:
    #     wpm = 0
    wpm_label.config(text=f"Words per Min: {wpm:.2f}")
    word_label.config(text=f"Words: {counted_words}")


# --------------------- Frames ---------------------
top_frame = Frame(root, bg="#f0f0f0")
top_frame.pack(pady=20)

middle_frame = Frame(root, bg="#f0f0f0")
middle_frame.pack(pady=10)

bottom_frame = Frame(root, bg="#f0f0f0")
bottom_frame.pack(pady=20)

# --------------------- Reference Text ---------------------
reference_text = "This is a simple typing speed test."
ref_label = Label(
    top_frame,
    text=reference_text,
    wraplength=500,
    font=("Helvetica", 16),
    bg="#f0f0f0",
    fg="#333333",
)
ref_label.pack()

# --------------------- Text Box for Typing ---------------------
text_box = Text(
    middle_frame,
    height=5,
    width=50,
    font=("Lato", 14),
    bd=2,
    relief="groove",
    state="disabled",
)
text_box.pack(pady=10)

# --------------------- Buttons ---------------------
start_button = Button(
    bottom_frame,
    text="Start",
    font=("Helvetica", 12),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=5,
    command=start_timer,
)
start_button.pack(side="left", padx=10)

stop_button = Button(
    bottom_frame,
    text="Stop",
    font=("Helvetica", 12),
    bg="#f44336",
    fg="white",
    padx=20,
    pady=5,
    command=stop_timer,
)
stop_button.pack(side="left", padx=10)

# --------------------- Timer Display ---------------------
timer_label = Label(
    root, text="Time: 0s", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#000000"
)
timer_label.pack(pady=10)


# --------------------- WPM Display ---------------------
wpm_label = Label(
    root,
    text="Words per Min: 0",
    font=("Helvetica", 13, "bold"),
    bg="#f0f0f0",
    fg="#000000",
)
wpm_label.pack(pady=8)

# --------------------- Word Count Display ---------------------
word_label = Label(
    root, text="Words: 0", font=("Helvetica", 13, "bold"), bg="#f0f0f0", fg="#000000"
)
word_label.pack(pady=8)

# --------------------- Result Display ---------------------
result_label = Label(
    root, text="", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#555555"
)
result_label.pack(pady=10)


# #################################
root.mainloop()
