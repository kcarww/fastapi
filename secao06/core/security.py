from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificarSenha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

def gerarHashSenha(senha: str) -> str:
    return CRIPTO.hash(senha)