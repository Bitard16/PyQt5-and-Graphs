import App
import sys
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.Qt import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import networkx as nx
from networkx import *
import easygui 
from heapq import heapify,heappop,heappush
import numpy as np
from PIL import Image



class MainApp(QtWidgets.QMainWindow,App.Ui_MainWindow):
    def __init__(self): # Конструктор
        super().__init__() 
        self.setupUi(self)
        self.pushButton.clicked.connect(self.DrawWithHand) # Нажатие на кнопки
        self.pushButton_2.clicked.connect(self.DrawwithText)
        self.win = QWidget()
        self.scene = QGraphicsScene() # Взаимодействие с библиотекой
        self.view = QGraphicsView()
        self.text_Edit = QTextEdit()
        
# Функции для рисования на и обраотки Дейкстры      
    def DrawWithHand(self):
        graph = nx.Graph()
        data = self.textEdit_4.toPlainText()
        dataforpos = self.textEdit_6.toPlainText()
        dataforkol = self.textEdit_5.toPlainText()
        if dataforpos == str(1):
            for i in range(int(dataforkol)):
                o = data.split()
                m=int(o[0])
                n=int(o[1])
                mytext = self.textEdit_2.toPlainText() # Считываем матрицу
                data2 = np.matrix(mytext)
                graph = nx.from_numpy_matrix(data2)
                pos = nx.spring_layout(graph)
                labels = nx.get_edge_attributes(graph, 'weight')
                G = nx.draw_networkx(graph,pos=pos,title="Граф для Дейкстры", with_labels=True)
                G = nx.draw_networkx_edge_labels(G,pos, edge_labels=labels)
                length,path=bidirectional_dijkstra(graph,m,n)
                length = str(length)
                path = str(path)
                self.textEdit_3.append('Длина пути - ' + length)
                self.textEdit_3.append('Путь -' + path)
                savepic = str(i) + '.png'
                plt.savefig(savepic) # Сохраняем картинку
                img = Image.open(savepic) # С помощью PIL
                img.show()
        else:
            for i in range(dataforkol):
                o = data.split()
                m=int(o[0])
                n=int(o[1])
                mytext = self.textEdit_2.toPlainText()
                data2 = np.matrix(mytext)
                graph = nx.from_numpy_matrix(data2)
                pos = dataforpos.dict()
                labels = nx.get_edge_attributes(graph, 'weight')
                G = nx.draw_networkx(graph,pos=pos,title="Граф для Дейкстры", with_labels=True)
                G = nx.draw_networkx_edge_labels(G,pos, edge_labels=labels)
                
                length,path=bidirectional_dijkstra(graph,m,n)
                length = str(length)
                path = str(path)
                self.textEdit_3.append('Длина пути - ' + length)
                self.textEdit_3.append('Путь -' + path)
                G = nx.draw_networkx(graph,pos=pos,title="Граф для Дейкстры", with_labels=True)
                G = nx.draw_networkx_edge_labels(G,pos, edge_labels=labels)
                savepic = str(i) + '.png'
                plt.savefig(savepic) # Сохраняем картинку
                img = Image.open(savepic) # С помощью PIL
                img.show()

    def DrawwithText(self):
        import numpy as np
        import networkx as nx
        # Считываем количество графов
        path = easygui.fileopenbox(filetypes=["*.txt"])
        f = open(path,'r')
        datakol = f.readline()
        kolgraph = int(datakol)
        f.close() 
        # для загрузки данных между какими граф
        for i in range(kolgraph):
            # Загрузка вершин
            path = easygui.fileopenbox(filetypes=["*.txt"])
            f = open(path,'r')
            data = f.readline()
            o=data.split()
            m=int(o[0])
            n=int(o[1])
            f.close()
            
            # для загрузки данных матрицы
            path = easygui.fileopenbox(filetypes=["*.txt"])
            f2 = open(path,'r')
            data = f2.readline()
            data2 = np.matrix(data)
            graph = nx.from_numpy_matrix(data2)
            pos = nx.spring_layout(graph)  # Построение графа по окружности
            labels = nx.get_edge_attributes(graph, 'weight') # Дает атрибуты
            G = nx.draw_networkx(graph,pos=pos,title="Граф для Дейкстры", with_labels=True)
            G = nx.draw_networkx_edge_labels(G,pos, edge_labels=labels)
            
            savepic = str(i) + '.png'
            plt.savefig(savepic) # Сохраняем картинку
            img = Image.open(savepic) # С помощью PIL
            img.show()
            # Визуализация
           
            # Сам алгоритм
            length,path=bidirectional_dijkstra(graph,m,n)
            length = str(length)
            path = str(path)
            self.textEdit_3.append('Длина пути - ' + length)
            self.textEdit_3.append('Путь -' + path)
            #self.textEdit_3.append(mytext)
        
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec()
    
if __name__ == '__main__':
    main()
    
