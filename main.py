from scraper import buscar_eventos

eventos = buscar_eventos()

print("Quantidade de eventos:", len(eventos))
print(eventos)