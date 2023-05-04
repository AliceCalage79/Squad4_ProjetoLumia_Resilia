def identificaUsuario(): #Função mostra boas vindas e solicita identificação do usuario
    print ('\nBem-vindo(a) a Minha Faculdade',
           '\nPor favor, me diga como gostaria de ser chamado(a): ')
    
def primeiraPergunta(nomeUsuario):
    print("\033[1;36m"+"|*************************************|"+"\033[0;0m")
    print(f'\nOlá,',(nomeUsuario),',\nEu sou a atendente virtual Lumia. \nIrei esclarecer as principais dúvidas na',
          'hora de escolher uma graduação.\nSelecione um dos nossos cursos disponíveis para que eu possa falar mais sobre ele.')

#FUNÇÃO VARRE A OUTRA FUNÇÃO 'nomeCurso' ONDE ESTÃO AS OPÇÕES DE CURSO DISPONÍVEL E GUARDA UMA 'string'.
def mostraTodoCursos():
    todas = ''      # mostrando ao usuario 4 opcoes 
    for i in range (1,5,1):
        todas = str(todas) + ('\n'+str(i)+'.'+(nomeCurso(i)))
    return todas   

#EXIBINDO AS OPÇÕES DE CURSOS DISPONÍVEIS
def nomeCurso(curso): 
    if curso == 1 :
        return str('Pedagogia')
    elif curso == 2 :
        return str('Direito')
    elif curso == 3 :
        return str('Análise e desenvolvimento de Sistemas')
    elif curso == 4:
        return str('Encerrar')    
    
#REALIZANDO CHECAGEM DO QUE O USUÁRIO INSERIU COMO RESPOSTA
def validarUsuario (nome,contador): 
    print("\033[1;36m"+"|*************************************|"+"\033[0;0m")
    print ('\n'+"\033[1;31m"+'Opção inválida.'+"\033[0;0m"+'\n'+(nome)+','+'\nDigite novamente. Você tem mais '+'\033[1;31m'+str(contador)+'\033[0;0m'+' tentativas' '\nSuas opções são:')

#CABEÇALHO DE INFORMAÇÕES DA SEGUNDA PARTE DE PERGUNTAS CONTIDA EM CADA OPÇÃO CURSO
def segundaPergunta(curso,nome):
    print("\033[1;36m"+"|*************************************|"+"\033[0;0m")
    print ('\n'+(nome)+'\nVocê escolheu a graduação em '+ str(nomeCurso(int(curso)))+'\nVeja abaixo as principais dúvidas',
           '\nPara acessar as informações, digite a opção desejada:\n')

#???
def mostraTodasDuvidas(curso):
        todas = ''
        for i in range (1,5,1):
           todas = str(todas) + ('\n'+str(i)+'.'+str(duvidas(curso,(i)))+'')
        return todas  
 
#FUNÇÃO QUE EXIBE A SEGUNDA PARTE DE PERGUNTAS CONTIDA EM CADA OPÇÃO DE CURSO
def duvidas(curso,duvida): 
    
    if duvida == 1 :
        return print (f'1. Quem é o público alvo da graduação em ' + str(nomeCurso(int(curso)))+'?')
    if duvida == 2 :
        return print (f'2. Em que área posso atuar com a graduação em ' + str(nomeCurso(int(curso)))+'?')
    if duvida == 3 :
        return print (f'3. Qual a média salarial de um profissional na área de ' + str(nomeCurso(int(curso)))+'?')
    elif duvida == 4:
        return print ('4. Voltar')
    
#FUNÇÃO QUE EXIBE AS RESPOSTAS AO USUÁRIO
def mostraResposta(duvida, curso, nome):
    print("\033[1;36m"+"|*************************************|"+"\033[0;0m")
    if duvida== '1':
        if curso =='1':
            print ('\n'+'\033[1m'+'\n[Público alvo]\n'+'\033[0m'+(nome)+','+'\n(1) Em '+str(nomeCurso(int(curso)))+', criatividade, dinâmica e paciência são características \nimportantes para quem deseja seguir a carreira.')
            print('Saiba mais em nosso site:'+'{}|www.minhafaculdade.com|{}'.format('\033[4;34m', '\033[m'))
        elif curso == '2':
            print ('\n'+'\033[1m'+'\n[Público alvo]\n'+'\033[0m'+(nome)+','+'\n(1) Em '+str(nomeCurso(int(curso)))+', deve ter conhecimento sobre filosofia, lógica, política e economia, além de gostar de ler,\nrefletir e discutir todos os tipos de assuntos, com lógica e argumentação')
            print('Saiba mais em nosso site:'+'{}|www.minhafaculdade.com|{}'.format('\033[4;34m', '\033[m'))
        elif curso =='3':
            print ('\n'+'\033[1m'+'\n[Público alvo]\n'+'\033[0m'+(nome)+','+'\n(1) Em '+str(nomeCurso(int(curso)))+', necessita ter alta capacidade de concentração, observação, resolução e antecipação de problemas.')
            print('Saiba mais em nosso site:'+'{}|www.minhafaculdade.com|{}'.format('\033[4;34m', '\033[m'))
    if duvida== '2':
        if curso =='1':
            print ('\n'+'\033[1m'+'\n[Área de atuação]\n'+'\033[0m'+(nome)+','+'\n(2) Em '+str(nomeCurso(int(curso)))+', você pode atuar em: Educação Escolar - Educação Especial - Pedagogia Hospitalar - Administração Escolar \nCoordenação Pedagógica - Orientação Educacional - Psicopedagogia')
            print('Saiba mais em nosso site:'+'{}|www.minhafaculdade.com|{}'.format('\033[4;34m', '\033[m'))
        elif curso == '2':
            print ('\n'+'\033[1m'+'\n[Área de atuação]\n'+'\033[0m'+(nome)+','+'\n(2) Em '+str(nomeCurso(int(curso)))+', você pode atuar em: Direito Civil - Direito Ambiental - Direito Empresarial - Direito da Tecnologia da Informação - Direito do Consumidor.')
            print('Saiba mais em nosso site:'+'{}|www.minhafaculdade.com|{}'.format('\033[4;34m', '\033[m'))
        elif curso =='3':
            print ('\n'+'\033[1m'+'\n[Área de atuação]\n'+'\033[0m'+(nome)+','+'\n(2) Em '+str(nomeCurso(int(curso)))+', você pode atuar em: Administração de Banco de Dados - Infraestrutura de TI - Desenvolvimento de Software - Administração de Redes - Gestor de Projetos de Sistemas.')
            print('Saiba mais em nosso site:'+'{}|www.minhafaculdade.com|{}'.format('\033[4;34m', '\033[m'))
    if duvida== '3':
        if curso =='1':
            print ('\n'+'\033[1m'+'\n[Média Salarial]\n'+'\033[0m'+(nome)+','+'\n(3) Em '+str(nomeCurso(int(curso)))+', O salário médio no Brasil é de R$ 2.073,67.')
            print('Saiba mais em nosso site:'+'{}|www.minhafaculdade.com|{}'.format('\033[4;34m', '\033[m'))
        elif curso == '2':
            print ('\n'+'\033[1m'+'\n[Média Salarial]\n'+'\033[0m'+(nome)+','+'\n(3) Em '+str(nomeCurso(int(curso)))+', a média salarial de um advogado no Brasil é de R$ 4.537,62.')
            print('Saiba mais em nosso site:'+'{}|www.minhafaculdade.com|{}'.format('\033[4;34m', '\033[m'))
        elif curso =='3':
            print ('\n'+'\033[1m'+'\n[Média Salarial]\n'+'\033[0m'+(nome)+','+'\n(3) Em '+str(nomeCurso(int(curso)))+', a média salarial no Brasil é de R$ 4.348,45.')
            print('Saiba mais em nosso site:'+'{}|www.minhafaculdade.com|{}'.format('\033[4;34m', '\033[m'))
