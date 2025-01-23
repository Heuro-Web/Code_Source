
# Veillez installer requests allez dans le terminal et tapez pip install requests
import tkinter
from tkinter import scrolledtext, messagebox  
import requests


def accueil():
    print("Bienvenue !!!")

dark = False
def theme_():
    global dark
    dark = not dark
    if dark:
        app_scrapping.config(bg='black')
        Menu_Principal.config(bg='darkgray', fg='white')
        Window_Menu.entryconfig(0, label='Light Mode')

    else:
        app_scrapping.config(bg='white')
        Menu_Principal.config(bg='lightgray', fg='black')
        Window_Menu.entryconfig(0, label='Dark Mode')


def effacer():
    Champ_code.delete(0, tkinter.END)

def code_source():  
    url = Champ_code.get()  
    if not url:  
        messagebox.showwarning("Input Error", "Please enter a valid URL.")  
        return  
    try:  
        response = requests.get(url)  
        response.raise_for_status()  # Vérifie si la requête a échoué  
        txt_output.delete(1.0, tkinter.END)  # Efface le texte précédent  
        txt_output.insert(tkinter.END, response.text)  # Affiche le code source  
    except requests.RequestException as e:  
        messagebox.showerror("U3ne Erreur s'est produite", str(e))  


Banque_des_Couleurs = {
    "Black" : "#000000",
    "Red" : "#FF0000",
    "Maron" : "#800000",
    "Jaune" : "#FFFF00",
    "Bleu_Ciel" : "#33FF33",
    "Orange" : "#996600",
    "Orange_f" : "#333300"
}


app_scrapping = tkinter.Tk()
app_scrapping.title("App_scrapping")
app_scrapping.geometry("1920x800")
# app_scrapping.geometry("500x300")


label_message = tkinter.Label(app_scrapping,text="Web Scrapping App ", height=2, width=100,fg=Banque_des_Couleurs['Bleu_Ciel'], bg="green").pack()
label_message_2 = tkinter.Label(app_scrapping,text="Ici", height=2, width=100).pack()


Champ_code = tkinter.Entry(app_scrapping, width=70)
Champ_code.pack(pady=20)
Champ_code.insert(0, "Veuillez entrer le lien Ici")

button_effacer = tkinter.Button(app_scrapping, text='DELETE ALL', height=3, width=16,bg='#CC9933', command=effacer).place(x=580, y=500)
Button_gen = tkinter.Button(app_scrapping, text='GENERATEUR DU CODE SOURCE', height=3, width=30,bg='#7121ac', command=code_source).place(x=530, y=600)

txt_output = scrolledtext.ScrolledText(app_scrapping, wrap=tkinter.WORD, width=150, height=20, background="#CCCC99")  
txt_output.pack(pady=30)  





# Widget Principal
Menu_Principal = tkinter.Menu(app_scrapping)

# Sous Menu Entree
Sous_Menu_input = tkinter.Menu(Menu_Principal, tearoff=0)  # Enleve les petits trains dans la fenetre
Sous_Menu_input.add_command(label="Accueil",command=accueil)

Window_Menu = tkinter.Menu(Menu_Principal, tearoff=0)  # Enleve les petits trains dans la fenetre 
Window_Menu.add_command(label="Dark Mode", command=theme_)
Window_Menu.add_separator()
Window_Menu.add_command(label="Quitter", command=app_scrapping.quit)



# Menu Principal pour Entree
Menu_Principal.add_cascade(label="HOME", menu=Sous_Menu_input)
Menu_Principal.add_cascade(label="WINDOW", menu=Window_Menu)

# Boucle Principale
app_scrapping.config(menu=Menu_Principal)
app_scrapping.mainloop()

# Contactez moi Ici, copiez le lien dans  chrome
# https://www.facebook.com/profile.php?id=100053586395756