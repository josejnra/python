# Importando o módulo Bokeh

# Usando output_file para gravar as visualizações
from bokeh.plotting import figure, output_file, show

# Arquivo gerado pela visualização
output_file("/home/jose/Bokeh-Grafico-Interativo.html")

p = figure()

p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

show(p)
