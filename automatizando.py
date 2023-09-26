import matplotlib.pyplot as plt

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas = [85, 90, 78, 92, 88, 96, 94, 98, 100, 102, 150, 108]

plt.plot(meses, vendas, marker='1')

# Adicionando um vspan para destacar o intervalo de meses com vendas a partir de julho
plt.axvspan(meses.index('Jul'), meses.index('Dez'), color='lightgreen', alpha=0.15)

# Adicionando texto para destacar o intervalo dos meses com vendas a partir de julho
plt.text(6, 80, 'Recuperação de crescimento', fontsize=9, color='green', weight='bold')

plt.ylabel('Vendas (em milhares)')
plt.title('Crescimento das vendas ao longo do Ano')

for posicao in range(len(meses)):
    plt.annotate(vendas[posicao], xy=(meses[posicao], vendas[posicao]),
                 xytext=(-5, 5), textcoords='offset points', ha='center', va='bottom',
                 color='green', weight='bold')
plt.yticks([])
plt.tick_params(axis='x', length=0)
plt.box(False)

plt.show()

