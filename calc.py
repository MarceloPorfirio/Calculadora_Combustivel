from tkinter import END, Button, Label, Toplevel


class Calculo():
    
    def calcular_gasto(self):
        self.selecionar_combust = self.selecionar_combustivel.get()
        self.valor_consumo =  self.enrty_consumo.get()
        self.valor_distancia = self.enrty_distancia.get() 
        if self.selecionar_combust == 'Alcool':
            self.selecionar_combust = 5.19
            self.total = round(float(self.valor_distancia) /float(self.valor_consumo) *float( self.selecionar_combust),2)
            self.janela_resultado()
        elif self.selecionar_combust == 'Diesel':
            self.selecionar_combust = 3.99
            self.total = round(float(self.valor_distancia) /float(self.valor_consumo) *float( self.selecionar_combust),2)
            self.janela_resultado()
        elif self.selecionar_combust == 'Gás Natural':
            self.selecionar_combust = 3.59
            self.total = round(float(self.valor_distancia) /float(self.valor_consumo) *float( self.selecionar_combust),2)
            self.janela_resultado()
        elif self.selecionar_combust == 'Gasolina':
            self.selecionar_combust = 6.19
            self.total = round(float(self.valor_distancia) /float(self.valor_consumo) *float( self.selecionar_combust),2)
            self.janela_resultado()

    def limpa_dados(self):
        self.selecionar_combustivel.delete(0,END)
        self.enrty_consumo.delete(0,END)
        self.enrty_distancia.delete(0,END)
        self.jan_res.destroy()