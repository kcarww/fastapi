from core.configs import settings
from core.database import engine

async def createTables() -> None:
    import models.__all_models
    print('Criando tabelas...')
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso...')
    
if __name__ == '__main__':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 
    asyncio.run(createTables())