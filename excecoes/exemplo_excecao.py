# Utilizando try e except
def somar():
    try:
        8 + 's'
    except:
       print('Operação não permitida')

# Utilizando try, except e else
def abrir_arquivo():
    try:
        f = open('arquivo_qualquer.txt', 'w')
        f.write('Gravando no arquivo')
    except IOError:
        print('Erro: arquivo não encontrado ou não pode ser salvo.')
    else:
        print('Conteúdo gravado com sucesso!')
        f.close()

# Usando o finally
def abrir_arquivo_f():
    try:
        f = open('arquivo_qualquer.txt', 'w')
        f.write('Gravando no arquivo')
    except IOError:
        print('Erro: arquivo não encontrado ou não pode ser salvo.')
    else:
        print('Conteúdo gravado com sucesso!')
        f.close()
    finally:
        print('Comandos no bloco finally são sempre executados')

def askint():
    while True:
        try:
            val = int(input('Digite um número: '))
        except:
            print('Você não digitou um número!')
            continue
        else:
            print('Você digitou o número {}'.format(val))
            break
        finally:
            print('Fim da execuçaõ!')

def mensagem_erro():
    tuple = (1, 2, 3, 4, 5)
    try:
        tuple.append(6)
        for each in tuple:
            print(each)
    except AttributeError as e:
        print('Erro: ', e)
    except IOError as e:
        print('Erro de I/O: ', e)

mensagem_erro()