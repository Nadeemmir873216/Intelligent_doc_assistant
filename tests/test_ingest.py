from rag.ingest import load_pdf

doc = load_pdf("data/report.pdf")

print("total pages:", len(doc))

page_num = int(input("enter page number to print: "))

print(doc[page_num-1])