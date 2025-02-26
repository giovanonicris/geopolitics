import requests
import pandas as pd
from io import BytesIO
import os

# URL of the GPR data file
gpr_url = 'https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls'

def download_gpr_data():
    response = requests.get(gpr_url)
    if response.status_code == 200:
        data = BytesIO(response.content)
        df = pd.read_excel(data, sheet_name='Monthly Data')
        output_file = 'gpr_data.csv'
        df.to_csv(output_file, index=False)
        print(f"GPR data successfully saved to {output_file}")
    else:
        print(f"Failed to download GPR data: Status code {response.status_code}")
        exit(1)

if __name__ == "__main__":
    download_gpr_data()
