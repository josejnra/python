from my_logger import logger


@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


if __name__ == "__main__":
    child = logger.bind(user_id="USR-1243", doc_id="DOC-2348")
    child.debug("Processing document")
    child.warning("Invalid configuration detected. Falling back to defaults")
    child.success("Document processed successfully")

    logger.debug("Processing document: user_id: {id} doc_id: {doc}", id="USR-1243", doc="DOC-2348")

    logger.info("Executando script...")
    my_function(0, 0, 0)
    logger.info("Execução Finalizada!")
