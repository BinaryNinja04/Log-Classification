import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from classify import classify

app = FastAPI()

@app.post("/classify/")
async def classify_logs(file: UploadFile):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail='File must be of .csv format')
    try:
        df = pd.read_csv(file.file)
        if "source" not in df.coloumns or "log_message" not in df.coloumns:
            raise HTTPException(status_code=400, detail="The csv file must include 'source' and 'log_message' coloumns.")
        
        df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

        output_file = "resources/output.csv"
        df.to_csv(output_file, index= False)
        return FileResponse(output_file, media_type = 'text/csv')
    except Exception as e:
        raise HTTPException(status_code = 500, detail=str(e))
    finally:
        file.file.close()