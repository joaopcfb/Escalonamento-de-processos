from typing import Deque, Any, Iterator
from collections import deque


class Conteudo:

    def __init__(self, maxlen=None) -> None:
        self.__itens: Deque[Any] = deque (maxlen=maxlen)

    def inserir(self, *itens: Any) -> None:
        for item in itens:
            self.__itens.append(item)

    def remover(self) -> Any:
        if not self:
            raise IndexError('Tentando remover de uma lista vazia')

        return self.__itens.popleft()

    def __repr__(self) -> str:
        em_espera = ''
        if not self:
            return ''
        for i in range(1,len(self)):
            if i == 1:
                em_espera += self[i][1]
            else:
                em_espera += '->' + self[i][1]
        return ' ' + em_espera + '  '

    def __bool__(self) -> bool:
        return bool(self.__itens)

    def __len__(self) -> int:
        return len(self.__itens)

    def __iter__(self) -> Iterator:
        return self.__itens.__iter__()

    def __getitem__(self, index: int) -> Any:
        if not self:
            return ['','']
        return self.__itens[index]
