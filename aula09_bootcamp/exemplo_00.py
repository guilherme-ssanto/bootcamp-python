from loguru import logger
from utils_log import log_decorator

logger.add("meu_app.log", 
           format="{time} {level} {message} {file}",
           level="CRITICAL")

@log_decorator
def soma(x, y):
    try:
        soma = x + y
        logger.info(f"voce digitou valores corretos, parabens {soma}")
        return soma
    except:
        logger.critical("voce tem que digitar valores corretos")

soma(2, "3")
soma(2,7)
soma(2,3)

