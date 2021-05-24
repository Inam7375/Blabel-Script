from blabel import LabelWriter
import pandas as pd

df = pd.read_excel("New_Data.xlsx")


label_writer = LabelWriter("template.html",
                           default_stylesheets=("template.css",))

i=0
records = []
for item in df["Weights"]:
    num = df['EAN/Barcode Number'][i]
    name = df['Name of artcile'][i]
    price = df['Price in €'][i]
    weight = df['Weights'][i]
    records.append(
    dict(sample_id=num, sample_name=name, sample_weight=weight, sample_price=price)
    )
    i = i + 1

label_writer.write_labels(records, target='qrcode_and_label.pdf')