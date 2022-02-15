
from tkinter import *
from tkinter import ttk
from calc import Calculo

root = Tk()

class Application_Combust(Calculo):
    
    def __init__(self):
       self.root = root
       self.principal()
       self.componentes()

       root.mainloop()

    def principal(self):
        root.title('Calc')
        root.geometry('400x400+300+100')

    def componentes(self):
        self.primeiro_label = Label(self.root,text = 'Calculadora de Combustível',font=('Helvetica-bold',14),fg='gray')
        self.primeiro_label.place(relx=0.05,rely=0.1)

        self.label_selecione = Label(self.root,text='Selecionar Combustível',font=('Helvetica-bold',12),fg='gray')
        self.label_selecione.place(relx=0.1,rely=0.25)
        self.lista_combustiveis = ['Alcool','Diesel','Gás Natural','Gasolina']
        self.selecionar_combustivel = ttk.Combobox(self.root,values=self.lista_combustiveis,font=('helvetica-bold',10))
        self.selecionar_combustivel.place(relx=0.1,rely=0.35)
        
        self.consumo_veiculo = Label(self.root, text='Consumo KM/litro',font=('Helvetica-bold',12),fg='gray')
        self.consumo_veiculo.place(relx=0.1,rely=0.45)
        self.enrty_consumo = ttk.Entry(self.root,font=('Helvetica-bold',12))
        self.enrty_consumo.place(relx=0.1,rely=0.55,relheight=0.06,relwidth=0.41)

        self.label_distancia = Label(self.root, text='Distância em KM',font=('Helvetica-bold',12),fg='gray')
        self.label_distancia.place(relx=0.1,rely=0.65)
        self.enrty_distancia = ttk.Entry(self.root,font=('Helvetica-bold',12))
        self.enrty_distancia.place(relx=0.1,rely=0.75,relheight=0.06,relwidth=0.41)

        self.btn_calcular = Button(self.root,text='Calcular',font=('Helvetica-bold',12),fg='black',command=self.calcular_gasto)
        self.btn_calcular.place(relx=0.4,rely=0.85)
        self.btn_fechar = Button(self.root,text='Fechar',font=('Helvetica-bold',12),fg='black',command=self.root.destroy)
        self.btn_fechar.place(relx=0.6,rely=0.85)

    def janela_resultado(self):
        self.jan_res = Toplevel()
        self.jan_res.title('Resultado')
        self.jan_res.geometry('400x400+600+100')
        self.jan_res.grab_set()
        self.jan_res.focus_force()

        self.lbl_res = Label(self.jan_res,text='Resultado',font=('Helvetica-bold',16))
        self.lbl_res.place(relx=0.3,rely=0.1)

        self.lbl_res_combust = Label(self.jan_res,text=f'O valor do combustível custa R$ {self.selecionar_combust}.',font=('Helvetica-bold',13))
        self.lbl_res_combust.place(relx=0.2,rely=0.2)
        self.lbl_res_total = Label(self.jan_res,text= f'O gasto será de R$ {self.total},',font=('Helvetica-bold',13))
        self.lbl_res_total.place(relx=0.2,rely=0.27)
        self.lbl_res_dist = Label(self.jan_res,text=f'para percorrer {self.valor_distancia} km.',font=('Helvetica-bold',13))
        self.lbl_res_dist.place(relx=0.2,rely=0.34)

        self.btn_voltar = Button(self.jan_res,text='Voltar',font=('Helvetica-bold',12),fg='black',command=self.limpa_dados)
        self.btn_voltar.place(relx=0.4,rely=0.85)



Application_Combust()