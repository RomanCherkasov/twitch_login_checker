import requests
endpoint = 'https://id.twitch.tv/oauth2/validate'

def token_input(tokens_file: str) -> list:
    tokens = []
    with open(tokens_file) as proxy_list:
        for line in proxy_list:
            tokens.append(line[:-1])
    return(tokens)

def token_output(token_list: list):
    for token in token_list:
        a = str(token)
        headers = {'Authorization': f'Bearer {a}'}
        res = requests.get(endpoint, headers=headers)
        login = res.json().get('login')
        with open('output.txt', 'a') as output_file:
            output_file.write(f'{token} : {login}\n')

tokens = token_input('tokens.txt')
token_output(tokens)