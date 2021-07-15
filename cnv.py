#coding=utf-8
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
import shutil
from tkinter import messagebox as mb
from chardet.universaldetector import UniversalDetector
from inspect import getsourcefile

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.grid()
        self.com_ex = "pyinstaller --onefile "
        self.name_icon = ""
        self.rasp_pict = ""
        self.short_rasp_pict = ""
        self.use_cmd = ""
        
        self.begin_tk()
    
    def begin_tk(self):
        self.ask_prog_l = tk.Label(text="Выбрать программу для преобразования в exe:")
        self.ask_prog_l.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.ask_prog_but = tk.Button(text="Обзор", command=self.ask_prog)
        self.ask_prog_but.grid(row=0, column=1, padx=5, pady=5, sticky='e')
        
        self.ask_icon_var = tk.BooleanVar()
        self.ask_icon_var.set(0)
        self.ask_icon_ch_but = tk.Checkbutton(text="Добавить иконку к готовой программе?",
                    variable=self.ask_icon_var, onvalue = 1, offvalue = 0,
                    command=self.ask_icon_check)
        self.ask_icon_ch_but.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.ask_icon_ch_but.grid_remove()
        
        self.icon_l = tk.Label(text="Выберите нужную иконку:")
        self.icon_l.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.icon_but = tk.Button(text="Обзор", command=self.ask_icon)
        self.icon_but.grid(row=2, column=1, padx=5, pady=5, sticky='e')
        self.icon_l.grid_remove()
        self.icon_but.grid_remove()
        
        self.ask_pict_var = tk.BooleanVar()
        self.ask_pict_var.set(0)
        self.ask_pict_ch_but = tk.Checkbutton(text="Использует ли программа картинки?",
                    variable=self.ask_pict_var, onvalue = 1, offvalue = 0,
                    command=self.ask_pict_check)
        self.ask_pict_ch_but.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.ask_pict_ch_but.grid_remove()
        
        self.pict_l = tk.Label(text=
                    """Поместите все используемые программой картинки\nв отдельную папку и укажите ее расположение:\n(не забудьте сменить расположение картинок\nв своей программе)""")
        self.pict_l.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.pict_but = tk.Button(text="Обзор", command=self.ask_pict)
        self.pict_but.grid(row=4, column=1, padx=5, pady=5, sticky='e')
        self.pict_l.grid_remove()
        self.pict_but.grid_remove()
        
        self.ask_cmd_var = tk.BooleanVar()
        self.ask_cmd_var.set(0)
        self.ask_cmd_ch_but = tk.Checkbutton(text=
                    """Нужно ли скрыть консоль? (для программ, разработанных\nс использованием Tkinter и других библиотек, которые\nработают в отдельном окне)""",
                    variable=self.ask_cmd_var, onvalue = 1, offvalue = 0,
                    command=self.ask_cmd_check)
        self.ask_cmd_ch_but.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.ask_cmd_ch_but.grid_remove()
        
        self.start_but = tk.Button(text="Старт", command=self.start)
        self.start_but.grid(row=10, column=0, padx=5, pady=5, sticky='w')
        self.start_but.grid_remove()
        
        self.end_but = tk.Button(text="Выход", command=self.master.destroy)
        self.end_but.grid(row=10, column=1, padx=5, pady=5, sticky='e')
    
    def ask_prog(self):
        self.name_prog = askopenfilename()
        if self.name_prog == "":
            mb.showerror("Ошибка!", "Выберите файл для преобразования")
            return 0
        if self.name_prog[-2:] != "py":
            mb.showerror("Ошибка!", "Файл должен иметь расширение .py")
            return 0
        if len(self.name_prog.split()) != 1:
            mb.showerror("Ошибка!", "Имя файла не может содержать пробелов")
            return 0
        
        self.directory = os.path.abspath(getsourcefile(lambda:0))
        self.directory = self.directory[:self.directory.rfind("/")+1]
        self.prog_directory = self.name_prog[:self.name_prog.rfind("/")+1]
        
        self.name_prog = self.name_prog[self.name_prog.rfind("/")+1:]
        self.old_name_prog = self.name_prog
        self.name_prog = self.name_prog.replace(".py", "_copy.py")
        
        self.spec_file_name = self.name_prog[:-2] + "spec"
        self.exe_file_name = self.name_prog[:-2] + "exe"
        self.old_exe_file_name = self.old_name_prog[:-2] + "exe"
        
        shutil.copy(os.path.join(self.prog_directory, self.old_name_prog), os.path.join(self.directory, self.name_prog))
        
        self.ask_icon_ch_but.grid()
        self.ask_pict_ch_but.grid()
        self.ask_cmd_ch_but.grid()
        self.start_but.grid()
    
    def ask_icon(self):
        self.name_icon = askopenfilename()
        if self.name_icon == "":
            mb.showerror("Ошибка!", "Выберите иконку")
            return 0
        if self.name_icon[-3:] != "ico":
            mb.showerror("Ошибка!", "Иконка должна быть в формате .ico")
            return 0
        self.name_icon = "--icon=" + self.name_icon + " "
    
    def ask_pict(self):
        self.rasp_pict = askdirectory()
        if self.rasp_pict == "":
            mb.showerror("Ошибка!", "Выберите папку со всеми используемыми картинками")
            return 0
        self.short_rasp_pict = self.rasp_pict[self.rasp_pict.rfind("/")+1:]
        
        shutil.copytree(self.rasp_pict, os.path.join(self.directory, self.short_rasp_pict))
    
    def ask_icon_check(self):
        if self.ask_icon_var.get() == 1:
            self.icon_l.grid()
            self.icon_but.grid()
        else:
            self.icon_l.grid_remove()
            self.icon_but.grid_remove()
    
    def ask_pict_check(self):
        if self.ask_pict_var.get() == 1:
            self.pict_l.grid()
            self.pict_but.grid()
        else:
            self.pict_l.grid_remove()
            self.pict_but.grid_remove()
    
    def ask_cmd_check(self):
        if self.ask_cmd_var.get() == 1:
            self.use_cmd = "--noconsole "
        else:
            self.use_cmd = ""
    
    def start(self):        
        self.check()
        
        self.flag = 0
        self.err = "Для начала процесса не хватает:" #31
        if self.ask_icon_var.get() == 1 and self.name_icon == "":
            self.err += "\n• иконки                     " # 10 + 21
            self.flag = 1
        if self.ask_pict_var.get() == 1 and self.rasp_pict == "":
            self.err += "\n• папки с картинками         " # 22 + 9
            self.flag = 1
        
        if self.flag:
            mb.showerror("Ошибка!", self.err)
            return 0
        
        self.do_prog()
        
        self.master.destroy()

    def check(self):
        if self.ask_icon_var.get() == 0 and self.name_icon != "":
            self.ans_icon = mb.askyesno("Ошибка!", "Вы отменили использование иконки, но выбрали ее расположение.\nВключить ли иконку в Вашу программу?")
        else:
            self.ans_icon = self.ask_icon_var.get()
        
        if self.ask_pict_var.get() == 0 and self.rasp_pict != "":
            self.ans_pict = mb.askyesno("Ошибка!", "Вы отменили использование картинок, но выбрали используемую папку.\nВключить ли эту папку в Вашу программу?")
        else:
            self.ans_pict = self.ask_pict_var.get()
    
    def do_prog(self):
        #проверка установки pyinstaller
        if os.system("pyinstaller") != 2:
            os.system("pip install pyinstaller")
        
        #смена директории
        os.system("cd " + self.directory)
        os.system(self.directory[:2])
        
        #изменение программы
        self.change_prog()

        #запуск pyinstaller с установленными пользователем настройками
        os.system(self.com_ex + self.name_icon + self.use_cmd + self.name_prog)
       
        #изменение .spec, если используются картинки
        if self.ans_pict:
            self.change_spec()
            shutil.rmtree(os.path.join(self.directory, "__pycache__"), ignore_errors=True)
            os.system("pyinstaller " + self.spec_file_name)        
        
        #удаление файлов
        self.delete_files()
    
    def change_prog(self):
        self.cod = "#coding=utf-8\n\n"
        self.input_prog = """\n\ninput('''\nНажмите любую клавишу для выхода из программы: ''')"""
        self.input_pict_cod = """
import os
import sys
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
"""
        
        with open(os.path.join(self.directory, self.name_prog), "rb") as self.file_prog:
            self.old_data = self.file_prog.read()
        
        self.old_data = self.old_data.replace(b"/", b"\\")
        
        self.detector = UniversalDetector()
        self.detector.feed(self.old_data)
        self.detector.close()
        
        self.pict_rasp_in_prog = self.rasp_pict.replace(self.prog_directory, "")
        
        if self.ask_cmd_var.get() == 0:
            if self.ans_pict == 1:
                for self.x in [self.e for self.e in os.listdir(self.rasp_pict) if self.e.endswith((".jpg", ".jpeg", ".png", ".gif", ".svg"))]:
                    if self.old_data.decode(self.detector.result["encoding"]).find(os.path.join(self.rasp_pict, self.x)) != -1:
                        self.old_data = self.old_data.decode(self.detector.result["encoding"]).replace('"' + os.path.join(self.rasp_pict, self.x) + '"', 'resource_path("' + os.path.join(self.rasp_pict, self.x) + '")').encode(self.detector.result["encoding"])
                    elif self.old_data.decode(self.detector.result["encoding"]).find(os.path.join(self.pict_rasp_in_prog, self.x)) != -1:
                        self.old_data = self.old_data.decode(self.detector.result["encoding"]).replace('"' + os.path.join(self.pict_rasp_in_prog, self.x) + '"', 'resource_path("' + os.path.join(self.pict_rasp_in_prog, self.x) + '")').encode(self.detector.result["encoding"])
                    elif self.old_data.decode(self.detector.result["encoding"]).find(os.path.join(self.short_rasp_pict, self.x)) != -1:
                        self.old_data = self.old_data.decode(self.detector.result["encoding"]).replace('"' + os.path.join(self.short_rasp_pict, self.x) + '"', 'resource_path("' + os.path.join(self.short_rasp_pict, self.x) + '")').encode(self.detector.result["encoding"])
                
                with open(os.path.join(self.directory, self.name_prog), "w", encoding="utf-8") as self.file_prog:
                    self.file_prog.write(self.cod +
                                self.input_pict_cod +
                                self.old_data.decode(self.detector.result["encoding"]) +
                                self.input_prog)
            else:
                with open(os.path.join(self.directory, self.name_prog), "w", encoding="utf-8") as self.file_prog:
                    self.file_prog.write(self.cod +
                                self.old_data.decode(self.detector.result["encoding"]) +
                                self.input_prog)
        else:
            if self.ans_pict == 1:
                for self.x in [self.e for self.e in os.listdir(self.rasp_pict) if self.e.endswith((".jpg", ".jpeg", ".png", ".gif", ".svg"))]:
                    if self.old_data.decode(self.detector.result["encoding"]).find(os.path.join(self.rasp_pict, self.x)) != -1:
                        self.old_data = self.old_data.decode(self.detector.result["encoding"]).replace('"' + os.path.join(self.rasp_pict, self.x) + '"', 'resource_path("' + os.path.join(self.rasp_pict, self.x) + '")').encode(self.detector.result["encoding"])
                    elif self.old_data.decode(self.detector.result["encoding"]).find(os.path.join(self.pict_rasp_in_prog, self.x)) != -1:
                        self.old_data = self.old_data.decode(self.detector.result["encoding"]).replace('"' + os.path.join(self.pict_rasp_in_prog, self.x) + '"', 'resource_path("' + os.path.join(self.pict_rasp_in_prog, self.x) + '")').encode(self.detector.result["encoding"])                    
                    elif self.old_data.decode(self.detector.result["encoding"]).find(os.path.join(self.short_rasp_pict, self.x)) != -1:
                        self.old_data = self.old_data.decode(self.detector.result["encoding"]).replace('"' + os.path.join(self.short_rasp_pict, self.x) + '"', 'resource_path("' + os.path.join(self.short_rasp_pict, self.x) + '")').encode(self.detector.result["encoding"])

                with open(os.path.join(self.directory, self.name_prog), "w", encoding="utf-8") as self.file_prog:
                    self.file_prog.write(self.cod +
                                self.input_pict_cod +
                                self.old_data.decode(self.detector.result["encoding"]))
            else:
                with open(os.path.join(self.directory, self.name_prog), "w", encoding="utf-8") as self.file_prog:
                    self.file_prog.write(self.cod +
                                self.old_data.decode(self.detector.result["encoding"]))
        
        #shutil.copyfile(os.path.join(self.directory, self.name_prog), os.path.join(self.directory, "измененная программа.txt"))
    
    def change_spec(self):
        with open(os.path.join(self.directory, self.spec_file_name), "r") as self.spec:
            self.spec_data = self.spec.read()
        
        self.spec_data = self.spec_data.replace("datas=[]", "datas=[('{}/*', '{}')]".format(self.short_rasp_pict, self.short_rasp_pict))
        
        with open(os.path.join(self.directory, self.spec_file_name), "w") as self.spec:
            self.spec.write(self.spec_data)
    
    def delete_files(self):
        shutil.move(os.path.join(self.directory, "dist", self.exe_file_name), self.prog_directory)
        os.rename(os.path.join(self.prog_directory, self.exe_file_name), os.path.join(self.prog_directory, self.old_exe_file_name))

        shutil.rmtree(os.path.join(self.directory, self.short_rasp_pict), ignore_errors=True)
        shutil.rmtree(os.path.join(self.directory, "dist"), ignore_errors=True)
        shutil.rmtree(os.path.join(self.directory, "build"), ignore_errors=True)
        shutil.rmtree(os.path.join(self.directory, "__pycache__"), ignore_errors=True)
        os.remove(os.path.join(self.directory, self.spec_file_name))
        os.remove(os.path.join(self.directory, self.name_prog))

if __name__ == "__main__":
    root = tk.Tk()
    root.title(".py to .exe")
    root.geometry("+300+300")
    app = Application(master=root)
    root.resizable(width=False, height=False)
    app.mainloop()