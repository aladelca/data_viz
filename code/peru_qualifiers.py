import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from matplotlib.pyplot import figure
import numpy as np


data = pd.read_csv('https://raw.githubusercontent.com/calarcond/data_viz/main/data/conmebol_qualifiers.csv')
paises = list(data['Pais'])
columnas = list(data.columns)
columnas_consideradas = columnas[1:]
data.set_axis(data['Pais'], inplace = True)
#filtro = data.Pais.isin(['Peru','Chile'])
#data = data[data['Pais'].isin['Peru','Chile']]
#data = data[filtro]
data_final = data.iloc[:,1:]
data_final = data_final.rename_axis(None)
data_final_transpuesta = data_final.transpose()
data_final_transpuesta
fig, ax = plt.subplots(figsize = (15,8))

for i in range(1,19):
    data_grafico = data_final_transpuesta.iloc[:i,:]
    plt.ylim(11,0)
    plt.pause(0.2)
    ruta = ['C:/Users/Adrián Alarcón/Downloads/peru_flag.png','C:/Users/Adrián Alarcón/Downloads/brasil_flag.png']
    
    peru = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/peru_flag.png')
    brasil = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/brasil_flag.png')
    argentina = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/argentina_flag.png')
    ecuador = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/ecuador_flag.png')
    uruguay = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/uruguay_flag.png')
    colombia = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/colombia_flag.png')
    chile = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/chile_flag.png')
    paraguay = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/paraguay_flag.png')
    bolivia = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/bolivia_flag.png')
    venezuela = mpimg.imread('C:/Users/Adrián Alarcón/Downloads/venezuela_flag.png')


    #imagen = mpimg.imread(peru)
    imagebox_pe = OffsetImage(peru, zoom = 0.025)
    imagebox_br = OffsetImage(brasil, zoom = 0.015)
    imagebox_ec = OffsetImage(ecuador, zoom = 0.015)
    imagebox_ur = OffsetImage(uruguay, zoom = 0.015)
    imagebox_co = OffsetImage(colombia, zoom = 0.015)
    imagebox_cl = OffsetImage(chile, zoom = 0.015)
    imagebox_pa = OffsetImage(paraguay, zoom = 0.015)
    imagebox_bo = OffsetImage(bolivia, zoom = 0.015)
    imagebox_ve = OffsetImage(venezuela, zoom = 0.015)
    imagebox_ar = OffsetImage(argentina, zoom = 0.025)
    #xy = [i-1,data_grafico['Peru'].iloc[-1]]
    xy_pe = [i-1,data_grafico['Peru'].iloc[-1]]
    xy_br = [i-1,data_grafico['Brasil'].iloc[-1]]
    xy_ec = [i-1,data_grafico['Ecuador'].iloc[-1]]
    xy_ur = [i-1,data_grafico['Uruguay'].iloc[-1]]
    xy_co = [i-1,data_grafico['Colombia'].iloc[-1]]
    xy_cl = [i-1,data_grafico['Chile'].iloc[-1]]
    xy_pa = [i-1,data_grafico['Paraguay'].iloc[-1]]
    xy_bo = [i-1,data_grafico['Bolivia'].iloc[-1]]
    xy_ve = [i-1,data_grafico['Venezuela'].iloc[-1]]
    xy_ar = [i-1,data_grafico['Argentina'].iloc[-1]]
    ab_pe = AnnotationBbox(imagebox_pe, xy_pe)
    ab_br = AnnotationBbox(imagebox_br, xy_br)
    ab_ec = AnnotationBbox(imagebox_ec, xy_ec)
    ab_ur = AnnotationBbox(imagebox_ur, xy_ur)
    ab_co = AnnotationBbox(imagebox_co, xy_co)
    ab_cl = AnnotationBbox(imagebox_cl, xy_cl)
    ab_pa = AnnotationBbox(imagebox_pa, xy_pa)
    ab_bo = AnnotationBbox(imagebox_bo, xy_bo)
    ab_ve = AnnotationBbox(imagebox_ve, xy_ve)
    ab_ar = AnnotationBbox(imagebox_ar, xy_ar)

    ax.add_artist(ab_pe)
    ax.add_artist(ab_br)
    ax.add_artist(ab_ec)
    ax.add_artist(ab_ur)
    ax.add_artist(ab_co)
    ax.add_artist(ab_cl)
    ax.add_artist(ab_pa)
    ax.add_artist(ab_bo)
    ax.add_artist(ab_ve)
    ax.add_artist(ab_ar)
    x = np.arange(1,11,1)
    plt.plot( data_grafico.index,  data_grafico['Brasil'], color = 'gray', linewidth = 0.3)
    plt.plot( data_grafico.index,  data_grafico['Argentina'], color = 'gray', linewidth = 0.3)
    plt.plot( data_grafico.index,  data_grafico['Uruguay'], color = 'gray', linewidth = 0.3)
    plt.plot( data_grafico.index,  data_grafico['Ecuador'], color = 'gray', linewidth = 0.3)
    plt.plot( data_grafico.index,  data_grafico['Peru'], color = 'red', linewidth = 1.5)
    plt.plot( data_grafico.index,  data_grafico['Colombia'], color = 'gray', linewidth = 0.3)
    plt.plot( data_grafico.index,  data_grafico['Chile'], color = 'gray', linewidth = 0.3)
    plt.plot( data_grafico.index,  data_grafico['Paraguay'], color = 'gray', linewidth = 0.3)
    plt.plot( data_grafico.index,  data_grafico['Bolivia'], color = 'gray', linewidth = 0.3)
    plt.plot( data_grafico.index,  data_grafico['Venezuela'], color = 'gray', linewidth = 0.3)
    plt.title('Peru Standing Evolution - Qatar 2022 FIFA World Cup Qualifiers', fontsize = 20, fontweight = 'bold')
    plt.xlabel('Matchday')
    plt.ylabel('Standing')
    plt.yticks(x)
    #plt.legend(labels = paises,prop={'size': 6}, loc =  'upper left')
    

plt.show()




