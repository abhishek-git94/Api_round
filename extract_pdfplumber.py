import pdfplumber

pdf_path = "sales_data.pdf"
print(f"Opening PDF: {pdf_path}...")

with pdfplumber.open(pdf_path) as pdf:
    print(f"Number of pages: {len(pdf.pages)}")
    for i, page in enumerate(pdf.pages):
        print(f"\n--- Page {i+1} ---")
        text = page.extract_text()
        print(f"Text length: {len(text) if text else 0}")
        if text:
            print("First 500 chars of text:")
            print(text[:500])
        
        tables = page.extract_tables()
        print(f"Tables found: {len(tables)}")
        for t_idx, table in enumerate(tables):
            print(f"  Table {t_idx+1} dimensions: {len(table)} rows x {len(table[0]) if table else 0} cols")
            print("  First row (headers):", table[0] if table else None)
            print("  Second row (data):", table[1] if len(table) > 1 else None)
