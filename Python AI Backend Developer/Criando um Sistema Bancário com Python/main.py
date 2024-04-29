import os
import time

class Conta:
    def __init__(self) -> None:
        "Construtor que define saldo, limite e quantas vezes foi sacado"
        self._balance = 0.0
        self.__limit = 500
        self._saq_count = 0

    def dep(self, value:float) -> float:
        "Função para depositar na conta"
        if (value >= 1):
            self._balance += value
            return self._balance  

    def ext(self) -> float:
        "Função para consultar o extrato"
        print(self._balance)
        return self._balance

    def saq(self, value:float) -> float:
        "Função para sacar e que obedece o limite e as quantas vezes foi sacado"
        if ((self._balance - value) >= 1 and (self._balance - value) <= 0 and value <= self.__limit and self._saq_count < 3):
            self._balance -= value
            self._saq_count += 1
            return value
        else:
            raise KeyError()
            return 0.0
        
def show(message):
    os.system("cls" if os.name == 'nt' else 'clear')
    return (f"{'*' * (len(message)//2)}\n{message}\n{'*' * (len(message)//2)}\n")

self_conta = Conta()

if __name__ == "__main__":
    while True:
        opt = input(show("a - Depositar.\nb - Consultar Extrato.\nc - Sacar.\nd - Sair.")).lower()
        match opt:
            case "a":
                try: 
                    value = float(input(show("Insira o valor a ser depositado:")))
                    self_conta.dep(value)
                    continue
                except:
                    print(show("Valor inválido."))
                    input("Aperte enter para continuar")
                    continue
            case "b":
                print(show(f"Valor em conta: R${self_conta.ext()} ."))
                input("Aperte enter para continuar")
                continue
            case "c":
                try: 
                    value = float(input(show("Insira o valor a ser sacado:")))
                    self_conta.saq(value)
                    continue
                except:
                    print(show(f"Valor inválido, Você pode sacar 1500 reais por dia divididos em 3 saques. Você sacou {self_conta._saq_count} vez(es), e possui R${self_conta._balance}."))
                    input("Aperte enter para continuar")
                    continue
            case "d":
                break
            case _:
                continue
