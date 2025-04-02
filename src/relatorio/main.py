from RelatorioFactory import RelatorioFactory

# SÓ PARA TESTAR

if __name__ == "__main__":
    factory = RelatorioFactory()
    relatorio = factory.generate_relatorio_padrao("csv")
    relatorio.gerar_relatorio()
