import requests

def consulta_ddd(ddd):
    url = f'https://brasilapi.com.br/api/ddd/v1/{ddd}'

    r = requests.get(url)
    if(r.status_code == 200):
        dados = r.json()
        print(
            f'\n'
            f'Estado: {dados["state"]} \n'
            f'Cidades'
        )
        for i in dados["cities"]:
            print(
                f'- {i}'
            )
            
    else:
        if(r.status_code >= 400) and (r.status_code <= 499):
            print(f'{r.status_code} - Error related with client error responses')
        elif(r.status_code >= 500) and (r.status_code <= 599):
            print(f'{r.status_code} - Error related with server error responses')
        else:
            print(f'Error: {r.status_code}')

#########################################################################################

condition = False

print("########## CONSULTAR DDD ##########")
while(condition == False):
    input_ddd = input("Digite o DDD:")
    if(len(input_ddd) == 2):
        condition = True
        consulta_ddd(input_ddd)
    elif(len(input_ddd) == 3):
        new_input = input_ddd.replace("0","")
        condition = True
        consulta_ddd(new_input)
    else:
        print(
            f'\n'
            f'Something was wrong with DDD input "{input_ddd}". \n'
            f'Try again...'
            )
