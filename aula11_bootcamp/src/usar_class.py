from interface.classes.csv_class import CsvProcessor

arquivo_csv = '../exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(['estado', 'preco'], ['SP', '10,50']))

