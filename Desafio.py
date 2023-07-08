class desafio:
    def __init__(self, string: str):
        # classe que recebe uma string como input
        self.string = string
        
    def inversao(self):
        """Inverte a ordem das palavras na string (frase)
           
           inversao(self) -> string        
        """
        # divisao em lista de palavras por espaço em branco
        temp = self.string.split()
        # inverte a ordem da lista
        temp = temp[::-1]
        # junta as palavras em uma string novamente
        temp = ' '.join(temp)
        return temp
    
    def rm_dup(self):
        """Retorna uma copia sem caracteres repetidos, e como nao foi 
           especificado no exercicio, os espaços em branco também foram
           incluidos
                 
            rm_dup(self) -> string
        """
        temp = ''
        # coloca na string temp todos os caracteres sem precedente
        for caract in self.string:
            if caract not in temp:
                temp += caract
        return temp
    
    def palindromo(self):
        """Identifica os palindromos na string e retorna o mais comprido

           palindromo(self) -> string
        """
        # lista para guardar palindromos
        palindromos = []
        # procura palindromos
        for i in range(1, len(self.string) - 1):
            substring = self.string[i-1 : i+2]
            cont = 1
            temp = ''
            # encontra e determina o tamanho do palindromo
            while substring == substring[::-1]\
            and (i - cont >= 0)\
            and (i + cont <= len(self.string)):
                temp = substring
                cont += 1
                substring = self.string[i-cont : i+cont+1]
            # guarda o palindromo se ele existir
            if len(temp) > 0:
                palindromos.append(temp)
        maior = ''
        # se existir um palindromo o maior sera retornado
        if len(palindromos) > 0:
            maior = palindromos.pop(0)
            for x in palindromos:
                if len(x) > len(maior):
                    maior = x
        return maior
    
    def maiusculo(self):
        """Coloca em maiusculo o inicio de todas as frases da string

           maiusculo(self) -> string
        """
        # marcaçoes de fim de frase
        fim = ['.','?','!']
        # capitaliza a string
        txt = self.string.capitalize()
        up = False
        for i, caract in enumerate(txt):
            if up:
                if caract != ' ':
                    # encontra a primeira letra e transforma em maiuscula
                    txt = txt[:i] + txt[i].upper() + txt[i + 1:]
                    up = False
            # identifica a marcaçao de fim de frase na string
            if caract in fim:
                up = True
        return txt
    
    def anagrama_p(self):
        """Procura algum anagrama na string que possa ser um palindromo

           anagrama(self) -> bool
        """
        # verifica se a string tem comprimento par
        if len(self.string)%2 == 0:
            palin = True
            for caract in self.string:
                # se houver algum caractere com contagem impar
                # nao e possivel formar um palindromo
                if self.string.count(caract)%2 != 0:
                    palin = False
        # se a string tiver comprimento impar:
        else:
            palin = False
            for caract in self.string:
                # nesse caso procura o centro, um caractere com n ocorrencias impar
                if (self.string.count(caract) - 1)%2 == 0:
                    palin = True
                    temp = caract
            for caract in self.string:
                # os outros caracteres devem ter todos contagem par
                if self.string.count(caract)%2 != 0 and caract != temp:
                    palin = False
        return palin