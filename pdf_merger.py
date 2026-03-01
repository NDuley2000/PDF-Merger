import PyPDF2
import os

def pdf_merger():
    
    # Ask the user for the folder path
    input_path = input("Enter the full path to the folder containing your PDFs: ").strip()
    
    # Remove quotes if the user copied the path as "C:\users\etc"
    input_path = input_path.replace('"', '').replace("'", "")

    # Check if the path exists
    if not os.path.isdir(input_path):
        print(f"The path '{input_path}' does not exist.")
        return

    # Put the PDF files in a list and sort them
    files = [file for file in os.listdir(input_path) if file.endswith('.pdf')]
    files.sort()

    # Ask for the output name
    output_name = input("Enter the name for your merged PDF file: ").strip()
    if not output_name.endswith('.pdf'):
        output_name += '.pdf'

    # Perform the merge
    merger = PyPDF2.PdfMerger()
    
    for file in files:
        full_path = os.path.join(input_path, file)
        merger.append(full_path)

    # Save to the same folder the user specified
    output_path = os.path.join(input_path, output_name)
    merger.write(output_path)
    merger.close()

    print(f"\nFile saved at: {output_path}")

if __name__ == "__main__":

    pdf_merger()