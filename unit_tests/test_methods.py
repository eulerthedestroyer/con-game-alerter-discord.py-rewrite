class Test:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self._run = kwargs["run"]
    async def run(self):
        try:
            result = await self._run()
            self.success = result["success"]
            if "comment" in result:
                self.comment = result["comment"]
        except Exception as e:
            self.success = False
            self.comment = str(e)
        return self

