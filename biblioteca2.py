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

