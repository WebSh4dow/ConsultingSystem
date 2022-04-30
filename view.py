import sqlite3 as lite


con= lite.connect('dados.db')

#CRUD


#CREATE (INSERINDO AS INFORMACOES)



def inserir_info(i):
    with con:
         cur = con.cursor()
         query = "INSERT INTO formulario (nome,email,telefone,dia_em,estado,assunto) VALUES(?,?,?,?,?,?)"
         cur.execute(query,i)

# UPDATE
def mostrar_info():
    lista=[]
    with con:
         cur = con.cursor()
         query = "SELECT * FROM formulario"
         cur.execute(query)
         info = cur.fetchall()

         for i in info:
             lista.append(i)
    return lista
  





#UPDATING INFORMATIONS
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?,email=?,dia_em=?,telefone=?,estado=?,assunto=? WHERE id=?"
        cur.execute(query,i)
     
     

#DELETAR AS INFORMACOES
def deletar_info(i):

    

    with con:
     cur = con.cursor()
     query = "DELETE FROM formulario WHERE id=?"
     cur.execute(query,i)




