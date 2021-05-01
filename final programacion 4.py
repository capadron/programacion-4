from tkinter import *

def send_data():
  nombre_info = nombre.get()
  apellido_info = apellido.get()
  dia_info = dia.get()
  hora_info = str(hora.get())
  print(nombre_info,"\t", apellido_info,"\t", dia_info,"\t", hora_info)
 
  file = open("user.txt", "a")
  file.write(nombre_info)
  file.write("\t")
  file.write(apellido_info)
  file.write("\t")
  file.write(dia_info)
  file.write("\t")
  file.write(hora_info)
  file.write("\t\n")
  file.close()
  print(" Nuevo paciente registrado. Nombre: {} | Apellido: {}   ".format(nombre_info, apellido_info))
 
  nombre_entry.delete(0, END)
  apellido_entry.delete(0, END)
  dia_entry.delete(0, END)
  hora_entry.delete(0, END)

mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Registro de Pacientes", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

nombre_label = Label(text = "Nombre", bg = "#FFEEDD")
nombre_label.place(x = 22, y = 70)
apellido_label = Label(text = "Apellido", bg = "#FFEEDD")
apellido_label.place(x = 22, y = 130)
dia_label = Label(text = "Día", bg = "#FFEEDD")
dia_label.place(x = 22, y = 190)
hora_label = Label(text = "Hora", bg = "#FFEEDD")
hora_label.place(x = 22, y = 250)
 
nombre = StringVar()
apellido = StringVar()
dia = StringVar()
hora = StringVar()
 
nombre_entry = Entry(textvariable = nombre, width = "40")
apellido_entry = Entry(textvariable = apellido, width = "40")
dia_entry = Entry(textvariable = dia, width = "40")
hora_entry = Entry(textvariable = hora, width = "40")
 
nombre_entry.place(x = 22, y = 100)
apellido_entry.place(x = 22, y = 160)
dia_entry.place(x = 22, y = 220)
hora_entry.place(x = 22, y = 280)

submit_btn = Button(mywindow,text = "Submit Info", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 320)

mywindow.mainloop()