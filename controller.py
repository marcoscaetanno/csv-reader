from fastapi import FastAPI, File, UploadFile
from Domain.useCase.read_csv_use_case import ReadCsvUseCase as read_csv_use_case
from Domain.useCase.get_uploads_use_case import GetUploadsUseCase as get_uploads_use_case

app = FastAPI()

@app.get("/last_uploads")
async def read_root(total_registries:int):
    result = await get_uploads_use_case.get_uploads(total_registries=total_registries)
    return {"last uploads": result}

@app.post("/upload")
async def upload(data: UploadFile = File(...)):
    print(f"{data.filename}")
    result = await read_csv_use_case.read_csv(data)
    return {"file uploaded with success at:": result}