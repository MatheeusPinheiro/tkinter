from tkinter import *
from tkinter import ttk
from tkinter import messagebox

janela = Tk()

janela.geometry('950x350')
janela.title('TreeView')

# ---------------------------------------------------------------
"""Campos para digitar na tela"""

id =  Label(text = 'ID', font= 'Arial 12')
id.grid(row=1, column= 0, sticky='W')

campo_digitavel_id = Entry(font="Arial 12")
campo_digitavel_id.grid(row=1, column= 1, sticky='W')

nome =  Label(text = 'Nome', font= 'Arial 12')
nome.grid(row=1, column= 2, sticky='W')

campo_digitavel_nome = Entry(font="Arial 12")
campo_digitavel_nome.grid(row=1, column= 3, sticky='W')

idade =  Label(text = 'Idade', font= 'Arial 12')
idade.grid(row=1, column= 4, sticky='W')

campo_digitavel_idade = Entry(font="Arial 12")
campo_digitavel_idade.grid(row=1, column= 5, sticky='W')

sexo =  Label(text = 'sexo', font= 'Arial 12')
sexo.grid(row=1, column= 6, sticky='W')

campo_digitavel_sexo = Entry(font="Arial 12")
campo_digitavel_sexo.grid(row=1, column= 7, sticky='W')

# ------------------------------------------------------------------

def limpar_campos():
    #Limpando os campos
    campo_digitavel_id.delete(0, 'end')
    campo_digitavel_nome.delete(0, 'end')
    campo_digitavel_idade.delete(0, 'end')
    campo_digitavel_sexo.delete(0, 'end')


def add_item_tree_view():

    campos_faltando = []

    if not campo_digitavel_id.get():
        campos_faltando.append("ID")
    
    if not campo_digitavel_nome.get():
        campos_faltando.append("Nome")

    if not campo_digitavel_idade.get():
        campos_faltando.append("Idade")

    if not campo_digitavel_sexo.get():
        campos_faltando.append("Sexo")

    if campos_faltando:
        messagebox.showerror('Erro', f'Por favor, preencha os campos: {", ".join(campos_faltando)}')
        return

    tree_view_dados.insert("", "end", 
                        values=(str(campo_digitavel_id.get()), 
                                str(campo_digitavel_nome.get()), 
                                str(campo_digitavel_idade.get()), 
                                str(campo_digitavel_sexo.get()))
                                )

    limpar_campos()
    messagebox.showinfo('Sucesso', 'Cadastro realizado com sucesso')
  
    


def deletar_item_treeview():
    #pega o item selecionado
    itens_selecionado = tree_view_dados.selection()

    for item in itens_selecionado:
        tree_view_dados.delete(item)


def alterar_item_treeview():

    campos_faltando = []

    if not campo_digitavel_id.get():
        campos_faltando.append("ID")
    
    if not campo_digitavel_nome.get():
        campos_faltando.append("Nome")

    if not campo_digitavel_idade.get():
        campos_faltando.append("Idade")

    if not campo_digitavel_sexo.get():
        campos_faltando.append("Sexo")

    if campos_faltando:
        messagebox.showerror('Erro', f'Por favor, preencha os campos: {", ".join(campos_faltando)}')
        return
    
    #pega a posição do item selecionado
    item_selecionado = tree_view_dados.selection()[0]

    #Substituir o item selecionado
    tree_view_dados.item(item_selecionado,
                            values=(str(campo_digitavel_id.get()), 
                                   str(campo_digitavel_nome.get()), 
                                   str(campo_digitavel_idade.get()), 
                                   str(campo_digitavel_sexo.get())) 
                           )
    
    limpar_campos()
    messagebox.showinfo('Sucesso', 'Dados alterados com sucesso')



botao_adicionar = Button(text="Cadastrar", font="Arial 12", command=add_item_tree_view)
botao_adicionar.grid(row=2, column=0, columnspan=2, sticky='NSEW')

botao_deletar = Button(text="Deletar", font="Arial 12", command=deletar_item_treeview)
botao_deletar.grid(row=2, column=2, columnspan=2, sticky='NSEW')


botao_alterar = Button(text="Aterar", font="Arial 12", command=alterar_item_treeview)
botao_alterar.grid(row=2, column=4, columnspan=2, sticky='NSEW')



#theme_use - alt, classic default
#Configurando o titulo e o stilo
estilo_da_treeview =  ttk.Style()
estilo_da_treeview.theme_use('alt')
estilo_da_treeview.configure('.', font="Arial 14")

#Column - Criando 4 colunas
tree_view_dados = ttk.Treeview(janela, column=(1, 2, 3 , 4), show = 'headings' )

#Centralizando a coluna
tree_view_dados.column('1', anchor=CENTER)
#Coloco o titulo da coluna
tree_view_dados.heading('1', text="ID")

#Centralizando a coluna
tree_view_dados.column('2', anchor=CENTER)
#Coloco o titulo da coluna
tree_view_dados.heading('2', text="Nome")

#Centralizando a coluna
tree_view_dados.column('3', anchor=CENTER)
#Coloco o titulo da coluna
tree_view_dados.heading('3', text="Idade")

#Centralizando a coluna
tree_view_dados.column('4', anchor=CENTER)
#Coloco o titulo da coluna
tree_view_dados.heading('4', text="Sexo")

#Inserindo dados na treeview
tree_view_dados.insert("", "end", text="1", values=("1", "Matheus", 27, "Masculino"))
tree_view_dados.insert("", "end", text="2", values=("2", "Bruna", 24, "Feminino"))
tree_view_dados.insert("", "end", text="3", values=("3", "Ceramar", 63, "Masculino"))
tree_view_dados.insert("", "end", text="4", values=("4", "Mariana", 61, "Feminino"))
tree_view_dados.insert("", "end", text="5", values=("5", "Douglas", 16, "Masculino"))

#Adicionando o tree view na tela
tree_view_dados.grid(row=3, column=0, columnspan=8, sticky='NSEW')

janela.mainloop()