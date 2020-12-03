from typing import Deque, Any, Iterator
from collections import deque

class Conteudo_loteria:

    def __init__(self, maxlen=None) -> None:
        self.__itens: Deque[Any] = deque(maxlen=maxlen)

    def inserir(self, *itens: Any) -> None:
        for item in itens:
            self.__itens.append(item)

    def executar(self) -> Any:
        if not self:
            return None
        em_exe = self.__itens.popleft()
        return em_exe


    def __repr__(self,tempo_total) -> str:
        em_espera = ''
        if not self:
            return '-'
        for i in range(0, len(self)):
            if i == 0:
                if tempo_total != 0:
                    em_espera += '(' + self[i][1] + ',' + str(round((self[i][4]/tempo_total),2))+ ')'
                else:
                    em_espera += '(' + self[i][1] + ',' + str(0)+ ')'
            else:
                if tempo_total != 0:
                    em_espera += ';' + '(' + self[i][1] + ',' + str(round(self[i][4]/tempo_total,2)) + ')'
                else:
                    em_espera += ';' + '(' +  self[i][1] + ',' + str(0) + ')'
        return em_espera

    def __bool__(self) -> bool:
        return bool(self.__itens)

    def __len__(self) -> int:
        return len(self.__itens)

    def __iter__(self) -> Iterator:
        return self.__itens.__iter__()

    def __getitem__(self, index: int) -> Any:
        if not self:
            return ['', '']
        return self.__itens[index]
