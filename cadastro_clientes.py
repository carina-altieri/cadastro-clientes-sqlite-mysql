import sqlite3
from sqlalchemy import create_engine
import pandas as pd
import tkinter as tk
import tkinter.messagebox as messagebox

def cadastrar_clientes():
    #capturando informações do cliente
    id_cliente = entry_id.get()
    nome = entry_nome.get()
    email = entry_email.get()
    celular = entry_celular.get()
    cpf = entry_cpf.get()
    
    #realizando conexão com banco de dados SQLite
    con = sqlite3.connect("cadastro_clientes.db")
    cur = con.cursor()
    #cur.execute("CREATE TABLE clientes(id_cliente, nome, email, celular, cpf)")
    cur.execute("""INSERT INTO clientes VALUES (?,?,?,?,?)""",
                (id_cliente, nome, email, celular, cpf))
    con.commit()
    con.close()

    #limpando as entradas das caixas de texto
    entry_id.delete(0, "end")
    entry_nome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_celular.delete(0, "end")
    entry_cpf.delete(0, "end")

    #sinalizar quando o cadastro tiver sido concluído
    messagebox.showinfo("Parabéns", "Cadastro concluído com sucesso!")

    #chamando a função para migrar os dados automaticamente
    sqlite_to_mysql()

def salvar_csv():
    con = sqlite3.connect("cadastro_clientes.db")
    query = """ select * from clientes """
    df = pd.read_sql(query, con)
    con.close()
    df.to_csv("clientes.csv", index=False)
    messagebox.showinfo("Parabéns", "Arquivo CSV exportado com sucesso!")
 
def salvar_excel():
    con = sqlite3.connect("cadastro_clientes.db")
    query = """ select * from clientes """
    df = pd.read_sql(query, con)
    con.close()
    df.to_excel("clientes.xlsx", index=False)
    messagebox.showinfo("Parabéns", "Arquivo Excel exportado com sucesso!")

#migrando dados do SQLite para o MySQL
def sqlite_to_mysql():
    #conectando ao db no SQLite e pegando os dados
    con_sqlite = sqlite3.connect("cadastro_clientes.db")
    query = """ select * from clientes """
    df = pd.read_sql(query, con_sqlite)
    con_sqlite.close()

    #conectando com MySQL usando SQLAlchemy
    eng_mysql = create_engine("mysql+mysqlconnector://{usuário}:{senha}@{localhost}/{database}")

    #inserindo os dados do DF no MySQL
    df.to_sql('clientes', con=eng_mysql, if_exists='replace', index=False)    

janela_cadastro = tk.Tk()
janela_cadastro.title("Cadastro de clientes")

label_id = tk.Label(janela_cadastro, text="ID:").grid(row=0, column=0, padx=10, pady=10)

entry_id = tk.Entry(janela_cadastro, width=30)
entry_id.grid(row=0, column=1, padx=10, pady=10)

label_nome = tk.Label(janela_cadastro, text="Nome:").grid(row=1, column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela_cadastro, width=30)
entry_nome.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(janela_cadastro, text="E-mail:").grid(row=2, column=0, padx=10, pady=10)

entry_email = tk.Entry(janela_cadastro, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

label_celular = tk.Label(janela_cadastro, text="Celular:").grid(row=3, column=0, padx=10, pady=10)

entry_celular = tk.Entry(janela_cadastro, width=30)
entry_celular.grid(row=3, column=1, padx=10, pady=10)

label_cpf = tk.Label(janela_cadastro, text="CPF:").grid(row=4, column=0, padx=10, pady=10)

entry_cpf = tk.Entry(janela_cadastro, width=30)
entry_cpf.grid(row=4, column=1, padx=10, pady=10)

#botão para fazer cadastro
#executar a função que captura os dados dos clientes ao clicar no botão
bt_cadastro = tk.Button(janela_cadastro, text="Cadastrar cliente", width=15, command=cadastrar_clientes).grid(row=5, column=0, padx=10, pady=10)

#botão para gerar arquivo CSV
bt_csv = tk.Button(janela_cadastro, text="Gerar CSV", width=15, command=salvar_csv).grid(row=5, column=1, padx=10, pady=10)

#botão para gerar Excel
bt_excel = tk.Button(janela_cadastro, text="Gerar Excel", width=15, command=salvar_excel).grid(row=5, column=2, padx=10, pady=10)

janela_cadastro.mainloop()