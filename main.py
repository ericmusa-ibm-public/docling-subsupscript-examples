import json 
import re
import time
from docling.document_converter import DocumentConverter, PdfFormatOption, _format_to_default_options
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from docling_core.types.doc import ImageRefMode, DoclingDocument, TableItem
from pathlib import Path
IMAGE_RESOLUTION_SCALE = 2.0

example_dir = Path('example_pdfs')

output_dir = Path('output')
if not output_dir.exists():
    output_dir.mkdir(parents=True)

force_parse = False
documents = []
for document_path in example_dir.iterdir():
    document_json_path = output_dir / f"{document_path.stem}.json"
    start_time = time.time()
    if not document_json_path.is_file() or force_parse:
        print(f"Converting document: {document_path}")

        pipeline_options = PdfPipelineOptions()
        pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
        pipeline_options.generate_page_images = True
        pipeline_options.generate_table_images = True
        pipeline_options.generate_picture_images = True

        doc_converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )
        conv_res = doc_converter.convert(document_path)
        
        document = conv_res.document

        with open(document_json_path, 'w') as f:
            json.dump(document.export_to_dict(), f, indent=4)

    else:
        print(f"Document already converted: {document_path}")
        
        with open(document_json_path, 'r') as f:
            document = DoclingDocument.model_validate_json(f.read())
    
    documents.append((document, document_path))

    content_md = document.export_to_markdown(image_mode=ImageRefMode.EMBEDDED)

    markdown_path = output_dir / f"{document_path.stem}.md"
    with open(markdown_path, "w") as f:
        f.write(content_md)

        
    if len(document.tables) > 0:
        for i, table in enumerate(document.tables):
            table_path = output_dir / f"{document_path.stem}_table_{i}.csv"
            print(f"Exporting table to CSV: {table_path}")
            table.export_to_dataframe().to_csv(table_path, index=False)
        
    end_time = time.time() - start_time
    print(f"Document converted and DoclingDocument exported to JSON and Markdown in {end_time:.2f} seconds.")

