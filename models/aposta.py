from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Aposta:
    id: int
    pontos: float
    palpite: str
    status: str
    multiplicador: float