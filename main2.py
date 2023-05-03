from biblioteca2 import identificaUsuario

identificaUsuario()    

                   # função que retorna um texto de boas vindas, solicitando identificação do usuario
nomeUsuario =input()                         # variavel recebe o nome do usuario 
inicio =True
while inicio ==True:                         #laço que inicia o programa controlado pela variavel boleana inicio usado para opcao voltar
                     #variavel guarda a opcao de curso desejada pelo usuario
    contador = 5                               # contador implementado para controlar o numero de vezes que o usuario coloca opcao invalida, tem 5 tentativas depois sai
    while opcaoCurso  not in ('1','2','3','4'):#laco que identifica se o usuario colocou uma opcao valida, e mostra as opcoes novamente
        if contador >=2 :                    #condiçao que mostra se o usuario ja digitou as 5 tentativas 
             contador = contador-1              # contador vai decrementando de 5 ate 1 tentativas
             #def mostra mensagem de opcao invalida  
             #def mostra opcoes de curso disponiveis
             opcaoCurso = input()  #usuario vai digitando ate opcao de curso ser valida
        else:
               #caso digite 5 vezes opcoes invalidas o sistema sai   
             exit ()  
    if opcaoCurso == '4':                         #caso a opcao seja 4 o é a opcao sair, sai do sistema
         exit ()
        #usuario ja escolheu o curso agora vai aparecer a pergunta relacionada ao curso
        #          #mostra todas as duvidas relacionadas ao curso
    opcaoDuvida = input()
    contador = 5
    while opcaoDuvida not in ('1','2','3','4'):
        if contador >=2:
             contador = contador-1
            
        else:
               
             exit ()
    if opcaoDuvida == '4':
             inicio = True
    else:
                         #Função que exibe as respostas sobre todas as alternativas.
             
             resposta = input()
             while resposta not in ('1','2'):
                
                resposta =input()
             if resposta == '1':
                inicio = True
             else:
                print ('\n'+(nomeUsuario)+', obrigado por consultar nossa plataforma. Até breve!')
                inicio = False