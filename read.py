import tabula
  
# Read PDF File
# this contain a list
path="/media/devesh/DATA/research_work/"
filename="Haryana 1987 - Election Commission of India"
filename=path+filename
df = tabula.read_pdf(filename, pages='all')[0]
# convert PDF into CSV
print(df)
# Convert into Excel File
# df.to_csv('Excel File Path')
tabula.convert_into(filename, "iplmatch.csv", output_format="csv", pages='all')
print(df)

# import pdftables_api
  
# # API KEY VERIFICATION
# conversion = pdftables_api.Client('API KEY')
  
# # PDf to CSV 
# # (Hello.pdf, Hello)
# conversion.csv(pdf_file_path, output_file_path)
