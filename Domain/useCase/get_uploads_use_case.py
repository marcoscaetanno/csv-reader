from Infrastructure.database.database import Database as db

class GetUploadsUseCase:
    async def get_uploads(total_registries: int):
        if total_registries == 0:
            total_registries = 10
        
        result = db.get_last_uploads(total_registries=total_registries)
        return result