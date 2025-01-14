class EmailReader:
    def __init__(self, client):
        try:
            self._client = client
        except Exception as e:
            raise e

    def read(self):
        # Implement function here
        pass
