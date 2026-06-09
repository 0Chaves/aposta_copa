from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Time:
    id: int
    nome: str
    vitorias: int
    derrotas: int
    empates: int