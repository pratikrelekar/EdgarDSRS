from edgardsrs import EdgarDSRS

analyzer = EdgarDSRS()

# Cleaning the file
input_file = "your_10k_file.html"
cleaned_file = analyzer.process_html_file(input_file)
