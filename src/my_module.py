def dates_to_indexes(dates: str) -> list:
    """
    Função auxiliar para converter as datas para índices, sendo:
    - 1 para final de semana
    - 0 para dia de semana

    Parâmetros:
        - dates (str): String de datas

    Retorna:
        - dates_to_indexes (list): Lista indexada para dias de semana ou final de semana
    """
    weekend = ['sat', 'sun']

    dates_to_indexes = []

    for date in dates:
        if(weekend[0] in date) or (weekend[1]) in date:
            dates_to_indexes.append(1)
        else:
            dates_to_indexes.append(0)

    return dates_to_indexes


def get_best_hotel_idx(dict, indexed_dates, client_type):
    """
    Calcula os preços e retorna o índice do hotel com o menor preço. 
    Se dois hotéis apresentarem o mesmo preço, é retornado o hotel com maior classificação.

    Parâmetros:
    - dict (dict): dicionário de hotéis
    - indexed_dates (list): Datas indexadas como dia de semana ou final de semana (vide ` dates_to_indexes(dates)`)
    - client_type (str): tipo do cliente ('Regular' ou 'Reward')

    Retorna:
        Retorna o índice do hotel com o menor preço
    """
    price_list = []
    rating_list = []
    dict_vals = list(dict.values())

    for hotel_idx in range(len(dict)):

        price = 0

        for date in indexed_dates:
            price += dict_vals[hotel_idx]['Prices'][client_type][date]

        price_list.append(price)
        rating_list.append(dict_vals[hotel_idx]['Rating'])

    min_prices_ctr = price_list.count(min(price_list))

    # Eu sei que isso aqui ficou maluco mas melhor funcionar certo e maluco do que errado e bonito :/
    # se houver mais de um valor mínimo na lista:
    if min_prices_ctr > 1:
        # constrói uma lista com is índices dos preços mínimos repetidos
        min_prices_idx = [i for i in range(
            len(price_list)) if price_list[i] == min(price_list)]

        # constrói uma lista com as classificações dos menores preços
        min_price_rating_list = [rating_list[i] for i in min_prices_idx]

        # retorna a posição da maior classificação dos menores preços
        return(min_prices_idx[min_price_rating_list.index(
            max(min_price_rating_list))])

    else:
        return(price_list.index(min(price_list)))


# DO NOT change the function's name
def get_cheapest_hotel(func_input: str) -> str or None:
    """
    Imagino que a função deveria ler um JSON ou algum objeto vindo de uma API com
    os dados dinâmicos, dessa forma criei a variável "data_dict" pra simbolizar esses dados

    Retorna:
        cheapest_hotel (str): String com o nome do hotel mais barato

    """

    data_dict = {
        "Lakewood": {
            "Rating": 3,
            "Prices": {
                "Regular": [110, 90],
                "Reward": [80, 80],
            },
        },
        "Bridgewood": {
            "Rating": 4,
            "Prices": {
                "Regular": [160, 60],
                "Reward": [110, 50],
            },
        },
        "Ridgewood": {
            "Rating": 5,
            "Prices": {
                "Regular": [220, 150],
                "Reward": [100, 40],
            },
        }
    }

    # Separa o tipo do cliente do resto da string
    client_type, dates = func_input.split(':')
    # Separa a string de datas em uma lista
    dates = dates.split(',')
    # Datas indexadas por final de semana ou dia de semana
    indexed_dates = dates_to_indexes(dates)

    # Retomando o índice do melhor preço
    best_price_idx = get_best_hotel_idx(
        client_type=client_type,
        dict=data_dict,
        indexed_dates=indexed_dates)

    dict_keys = list(data_dict.keys())

    cheapest_hotel = dict_keys[best_price_idx]
    return(cheapest_hotel)


clients = [
    "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)",
    "Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)",
    "Reward: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"
]

for client in clients:
    print(get_cheapest_hotel(client))
