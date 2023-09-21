import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.tasks = []
        self.current_task_index = 0
        self.timer_running = False
        self.minutes = 25
        self.seconds = 0

        self.task_label = tk.Label(root, text="Tarefas:")
        self.task_label.pack()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_task_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_task_button.pack()

        self.remove_task_button = tk.Button(root, text="Remover Tarefa", command=self.remove_task)
        self.remove_task_button.pack()

        self.timer_label = tk.Label(root, text="")
        self.timer_label.pack()

        self.start_button = tk.Button(root, text="Iniciar Pomodoro", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Parar Pomodoro", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        self.update_task_listbox()
        self.update_timer()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_task_listbox()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks.pop(index)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.reset_timer()

    def update_timer(self):
        if self.timer_running:
            if self.minutes == 0 and self.seconds == 0:
                if self.current_task_index < len(self.tasks):
                    messagebox.showinfo("Pomodoro Concluído", f"Tarefa: {self.tasks[self.current_task_index]} concluída!")
                    self.current_task_index += 1
                if self.current_task_index < len(self.tasks):
                    self.minutes = 25
                else:
                    self.minutes = 5
                self.seconds = 0
            elif self.seconds == 0:
                self.minutes -= 1
                self.seconds = 59
            else:
                self.seconds -= 1

        self.timer_label.config(text=f"Tempo: {self.minutes:02d}:{self.seconds:02d}")
        if self.timer_running:
            self.root.after(1000, self.update_timer)

    def reset_timer(self):
        self.current_task_index = 0
        self.minutes = 25
        self.seconds = 0
        self.timer_label.config(text="")
        self.task_entry.delete(0, tk.END)
        self.tasks = []
        self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
