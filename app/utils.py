import aiohttp


async def get_questions(amount: int) -> dict:
    async with aiohttp.ClientSession() as session:
        url = f"https://jservice.io/api/random?count={amount}"
        try:
            async with session.get(url) as resp:
                return await resp.json()
        except Exception as e:
            print(e)
            return None
