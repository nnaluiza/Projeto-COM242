import requests


def crawler_hoteis(city, people, nights):
    url_airports = "https://travel-advisor.p.rapidapi.com/airports/search"
    querystring_airports = {"query": city, "locale": "pt_BR"}
    headers_airports = {
        "X-RapidAPI-Key": "078970b91fmsh164399a8cea7b86p1b5929jsnd4eff745e74a",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
    }

    response_airports = requests.get(
        url_airports, headers=headers_airports, params=querystring_airports
    )

    # Verifica se a resposta da primeira API é bem-sucedida
    if response_airports.status_code == 200:
        airports_data = response_airports.json()

        if airports_data:
            # Pega o valor de location_id da primeira posição
            location_id = airports_data[0]["location_id"]

            # Segunda API com location_id da primeira posição
            url_hotels = "https://travel-advisor.p.rapidapi.com/hotels/list"
            querystring_hotels = {
                "location_id": location_id,
                "adults": people,
                "rooms": "1",
                "nights": nights,
                "offset": "0",
                "currency": "BRL",
                "order": "asc",
                "limit": "10",
                "sort": "recommended",
                "lang": "pt_BR",
            }

            headers_hotels = {
                "X-RapidAPI-Key": "078970b91fmsh164399a8cea7b86p1b5929jsnd4eff745e74a",
                "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
            }

            response_hotels = requests.get(
                url_hotels, headers=headers_hotels, params=querystring_hotels
            )

            # Verifica se a resposta da segunda API é bem-sucedida
            if response_hotels.status_code == 200:
                result_data = response_hotels.json()

                # Mostra os campos desejados da API
                hotels_data = result_data.get("data", [])
                print(hotels_data)
                # Definição de coleção de hoteis
                hoteis = []

                # Imprime os campos desejados
                for hotel in hotels_data:
                    hoteis.append(
                        {
                            "Nome": hotel.get("name", "Não disponível"),
                            "Classificação": hotel.get("rating", "Não disponível"),
                            "Nível de Preço": hotel.get(
                                "price_level", "Não disponível"
                            ),
                            "Preço": hotel.get("price", "Não disponível"),
                            "Classificação no Ranking": hotel.get(
                                "ranking", "Não disponível"
                            ),
                        }
                    )
                return hoteis
            else:
                print("Erro na segunda API:", response_hotels.status_code)
        else:
            print(f"Nenhum aeroporto encontrado para '{city}'")
    else:
        print("Erro na primeira API:", response_airports.status_code)
