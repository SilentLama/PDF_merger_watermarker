import PyPDF2
import sys

inputs = sys.argv[1:]		# will make a list out of all the inputs except the first

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write("output.pdf")

def watermarker(template, watermark):
	template = PyPDF2.PdfFileReader(open(template, "rb"))
	watermark = PyPDF2.PdfFileReader(open(watermark, "rb"))
	output = PyPDF2.PdfFileWriter()

	for i in range(template.getNumPages()):
		page = template.getPage(i)
		page.mergePage(watermark.getPage(0))
		output.addPage(page)

	with open("watermarked_output.pdf", "wb") as new_file:
			output.write(new_file)




if __name__ == "__main__":

	input_str = input("What do you wanna do with those files? merge/watermark: ")
	if input_str == "watermark":
		watermarker(inputs[0], inputs[1])
	if input_str == "merge":
		pdf_combiner(inputs)


