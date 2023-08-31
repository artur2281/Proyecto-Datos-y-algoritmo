#Incio de sesion
from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox
from tkinter import PhotoImage

c_negro = '#010101'
c_morado = "#7f5af0"
c_verde = "#2cb67d"


root = CTk()
root.geometry('500*600+350+20')
root.minsize(480, 500)
root.config(bg = c_negro)
root.title('Inicio de sesion')

logo = PhotoImage(file = 'images/logo.png')

frame = CTkFrame(root, fg_color= c_negro)
frame.grid(column = 0, row = 0, sticky = 'nsew', padx = 50, pady = 50)

frame.columnconfigure([0,1], weight = 1)
frame.rowconfigure([0,1,2,3,4,5], weight = 1)

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

# usamos CTkLabel
CTkLabel(frame, image = logo).grid(columnspan = 2, row = 0)

#Para lass ventanas de usuario y constraseña
usuario = CTkEntry(frame, font = ('sans rerif', 12), placeholder_text ='Usuario',
    border_color = c_verde, fg_color = c_negro, width = 220, height = 40)
usuario.grid(columnspan = 2, row=1, padx =4, pady = 4)

password = CTkEntry(frame, font = ('sans rerif', 12 ), placeholder_text ='Contraseña',
    border_color = c_verde, fg_color = c_negro, width = 220, height = 40)
password.grid(columnspan = 2, row=2, padx =4, pady = 4)

#Crear para guardar
checkBox = CTkCheckBox(frame, text='Recordarme', hover_color=c_morado, 
        border_color=c_verde, fg_color=c_verde)
checkBox.grid(columnspan=2, row=3, padx=4, pady=4)

bt_iniciar = CTkButton(frame, font = ('sans serif', 12), border_color = c_verde, fg_color = c_negro,
        hover_color = c_verde, corner_radius = 12, border_width = 2, text = 'INICIAR SESION', height = 40)
bt_iniciar.grid(columnspan = 2, row = 4, pady=4, padx = 4)

root.call('wm','iconphoto', root._w, logo)
root.mainloop()