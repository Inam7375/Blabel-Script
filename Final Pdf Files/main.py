import os

os.environ['PATH'] += 'E:\GTK2+\GTK-for-Windows-Runtime-Environment-Installer\gtk-nsis-pack\bin'

from blabel import LabelWriter

label_writer = LabelWriter("template.html",
                           default_stylesheets=("template.css",))
records= [
    dict(sample_id="5901234123457", sample_name="Sample 1"),
    dict(sample_id="5901234123457", sample_name="Sample 2")
]

label_writer.write_labels(records, target='qrcode_and_label.pdf')