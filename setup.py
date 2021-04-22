import motor.motor_asyncio

async def setup():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.users
    return db