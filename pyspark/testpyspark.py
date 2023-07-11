import pandas as pd

df = pd.read_xml("D:\Souce_files\sample_XML_files\datafile.xml")
print("sample: ", df.head(5))
