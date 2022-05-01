from ast import Try
from logging import exception
from tkinter import *
from tkinter import *
from tkinter import font
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
from view import *
from tkinter import messagebox 
#AUTHOR-------------------------- @FireXtz----------------------------- 

#Tabela de Cores

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue


window= Tk()
window.title("MyProjectPython")
window.geometry("1080x443")
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

#Frames definidos cima,baixo e direita

frame_top = Frame(window,width=310,height=50,bg=co2,relief='flat' )
frame_top.grid(row=0,column=0)

frame_down = Frame(window,width=350,height=403,bg=co1,relief='flat' )
frame_down.grid(row=1,column=0, sticky=NSEW,padx=0,pady=1)

frame_right = Frame(window,width=588,height=403,bg=co1,relief='flat' )
frame_right.grid(row=0,column=1,rowspan=2,padx=1,pady=0,sticky=NSEW)

#Labels l_name = label nome>>>>>>>>> nome da label 
# FRAME,LABEL E ENTRY NOME
app_nome = Label(frame_top,text='FORMULARIO DE CADASTRO',anchor=NW, font=('Ivy 13 bold'),bg=co2,fg=co1,relief='flat') 
app_nome.place(x=10,y=20)

l_nome = Label(frame_down,text='Nome *',anchor=NW, font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_nome.place(x=10,y=20)
	 
e_nome= Entry(frame_down,width=55, justify='left',relief='solid')
e_nome.place(x=15,y=40)
	       
l_email = Label(frame_down,text='Email',anchor=NW, font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_email.place(x=10,y=70)

e_email= Entry(frame_down,width=55, justify='left',relief='solid')
e_email.place(x=15,y=100)

l_tel = Label(frame_down,text='Telefone *',anchor=NW, font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_tel.place(x=10,y=130)

e_tel= Entry(frame_down,width=55, justify='left',relief='solid')
e_tel.place(x=15,y=160)

	#DATA CONSULTA

l_cal = Label(frame_down,text='Data de consulta *',anchor=NW, font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_cal.place(x=10,y=190)

e_cal= DateEntry(frame_down,width=12, justify='left',relief='solid',year=2022)
e_cal.place(x=15,y=220)


	#ESTADO DA CONSULTA
l_estado = Label(frame_down,text='Estado da consulta *',anchor=NW, font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_estado.place(x=160,y=190)

e_estado= Entry(frame_down,width=31, justify='left',relief='solid')
e_estado.place(x=160,y=220)


	#Consulta os cadastros

l_pesquisa = Label(frame_down,text='INFORMAÇÕES ADCIONAIS',anchor=NW, font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_pesquisa.place(x=15,y=260)

e_pesquisa= Entry(frame_down,width=55, justify='left',relief='solid')
e_pesquisa.place(x=15,y=290)


	





#VARIAVEL GLOBAL DO TREE
global tree


#FUNCAO DO BOTAO INSERIR


def inserir():
    
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    dia = e_cal.get()
    estado = e_estado.get()
    pesquisa = e_pesquisa.get()
    lista = [nome,email,tel,dia,estado,pesquisa]
    if nome == '':
        messagebox.showerror('ERRO','O CAMPO ESTA VAZIO COMPLETE OS CAMPO')
    else:
     inserir_info(lista)
    messagebox.showinfo('SUCESSO','OS DADOS FORAM INSERIDOS COM EXITO')

    e_nome.delete(0,'end')
    e_email.delete(0,'end')
    e_tel.delete(0,'end')
    e_cal.delete(0,'end')
    e_estado.delete(0,'end')
    e_pesquisa.delete(0,'end')
    
    for widget in frame_right.winfo_children():
        widget.destroy()
        mostrar()


    
def deletar():
   
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    tree_lista = treev_dicionario['values']
       

    valor_id= [tree_lista[0]]
    deletar_info (valor_id)
    messagebox.showinfo('SUCESSO','OS DADOS FORAM APAGADOS')

    for widget in frame_right.winfo_children():
        widget.destroy()
                
        mostrar()
    
        
        
    
    
    

    
    

    
#FUNCAO PARA ATUALIZAR DADOS

def atualizar():
    try:
      
       treev_dados = tree.focus()
       treev_dicionario = tree.item(treev_dados)
       tree_lista = treev_dicionario['values']
       
       valor_id = tree_lista[0]
       
       e_nome.delete(0,'end')
       e_email.delete(0,'end')
       e_tel.delete(0,'end')
       e_cal.delete(0,'end')
       e_estado.delete(0,'end')
       e_pesquisa.delete(0,'end')
       
       
       e_nome.insert(0,tree_lista[1])
       e_email.insert(0,tree_lista[2])
       e_tel.insert(0,tree_lista[3])
       e_cal.insert(0,tree_lista[4])
       e_estado.insert(0,tree_lista[5])
       e_pesquisa.insert(0,tree_lista[6])

       
       if e_nome == '':
          messagebox.showerror('ERRO','O CAMPO ESTA VAZIO COMPLETE OS CAMPO')
       else:
           atualizar_info(tree_lista)
           messagebox.showinfo('SUCESSO','OS DADOS FORAM INSERIDOS COM EXITO')
 
           e_nome.delete(0,'end')
           e_email.delete(0,'end')
           e_tel.delete(0,'end')
           e_cal.delete(0,'end')
           e_estado.delete(0,'end')
           e_pesquisa.delete(0,'end')
    
       for widget in frame_right.winfo_children():
           widget.destroy()
           mostrar()
    except IndexError:
        messagebox.showerror ('ERRO','SELECIONE UM DADO DA TABELA')
        



        






def update():
        
        
        
           
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    tree_lista = treev_dicionario['values']
            
    valor_id = tree_lista[0]
            
            
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    dia = e_cal.get()
    estado = e_estado.get()
    pesquisa = e_pesquisa.get()
  
            
        
        
            
    lista = [nome,email,tel,dia,estado,pesquisa,valor_id]
    if nome == '':
       messagebox.showerror('ERRO','AO ATUALIZAR OS DADOS','CAMPO NOME NÃO FOI PREENCHIDO')
    else:
        atualizar_info(lista)
        messagebox.showinfo('SUCESSO','DADOS ATUALIZADOS COM SUCESSO')

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_tel.delete(0,'end')
        e_cal.delete(0,'end')
        e_estado.delete(0,'end')
        e_pesquisa.delete(0,'end')
                
            
    for widget in frame_right.winfo_children():
        widget.destroy()

        mostrar()
               
                
                
                




       
b_deletar = Button(frame_down,command=deletar,text='DELETAR',anchor=NW, font=('Ivy 9 bold'),bg=co7,fg=co4,relief='raised',width=10)
b_deletar.place(x=200,y=340)

b_atualizar = Button(frame_down,command=update,text='ATUALIZAR',anchor=NW, font=('Ivy 9 bold'),bg=co6,fg=co4,relief='raised',width=10)
b_atualizar.place(x=110,y=340)

b_inserir = Button(frame_down,command=inserir,text='INSERIR',anchor=NW, font=('Ivy 9 bold'),bg=co2,fg=co4,relief='raised',width=10)
b_inserir.place(x=15,y=340)

#b_confirmar = Button(frame_down,command=atualizar,text='CONFIRMAR',anchor=NW, font=('Ivy 9 bold'),bg=co2,fg=co4,relief='raised',width=10)
#b_confirmar.place(x=100,y=360)
    

def mostrar():
    
    global tree
    
    lista= mostrar_info()

    tabela_head = ['ID','Nome','Email','Telefone','Data','Estado','Sobre']
    tree = ttk.Treeview(frame_right,selectmode="extended",columns=tabela_head, show="headings")
    vsb = ttk.Scrollbar(frame_right,orient="vertical",command=tree.yview)

    hsb = ttk.Scrollbar(frame_right,orient="horizontal",command=tree.xview)

    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)




    tree.grid(column=0,row=0,sticky='nsew')
    vsb.grid(column=1,row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')


    frame_right.grid_rowconfigure(0, weight=12)
    hd = ["nw","nw","nw","nw","nw","center","center"] 
    h = [30,170,140,100,120,50,100]
    n = 0


    for col in tabela_head:
        tree.heading(col,text=col.title(),anchor=CENTER)
        tree.column(col,width=h[n],anchor=hd[n])
        n+=1

    for item in lista:
        tree.insert('','end',values=item)



mostrar()


        







window.mainloop()


