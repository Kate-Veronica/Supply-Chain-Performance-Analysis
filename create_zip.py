import zipfile
import os

csv_file = 'cleaned_data.csv'

if not os.path.exists(csv_file):
    print(f"File not found: {csv_file}")
else:
    zip_file = 'cleaned_data.zip'

    with zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(csv_file, arcname='cleaned_data.csv') 

    print(f"ZIP created successfully: {zip_file}")