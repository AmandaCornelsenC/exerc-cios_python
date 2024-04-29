login = 'AntonioBC97'
senha = 1479

login_usuario = input('Informe o seu login de usuário: ')
login_senha = int(input('Informe a sua senha de login: '))

if login_usuario == login:
    print('Login Correto!')
else:
    print('Usuário incorreto!')

if login_senha == senha:
    print('Acesso liberado!')
else:
    print('Senha incorreta, tente novamente!')
