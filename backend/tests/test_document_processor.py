from backend.app.services.document_processor import extract_text, preprocess_text, chunk_text, extract_metadata


  # Test with your uploaded files
file_path = "uploads/Major Project Handbook.docx"
text = extract_text(file_path)
print(f"Extracted {len(text)} characters")
print(text[:2000])  # First 200 characters

print("\n" + "="*50)
print("TESTING TEXT CLEANING")
print("="*50)

  # Clean the extracted text
cleaned_text = preprocess_text(text)
print(f"Cleaned text: {len(cleaned_text)} characters")
print("\n--- CLEANED TEXT (first 2000 chars) ---")
print(cleaned_text[:2000])

  # Show the difference
print(f"\nCharacter reduction: {len(text)} → {len(cleaned_text)}")

print("\n" + "="*50)
print("TESTING TEXT CHUNKING")
print("="*50)
  # Chunk the cleaned text
chunks = chunk_text(cleaned_text, max_tokens=300, overlap=30)
print(f"Total chunks created: {len(chunks)}")
for i, chunk in enumerate(chunks[:3]):  # Show first 3 chunks
    print(f"\n--- CHUNK {i+1} (first 500 chars) ---")
    print(chunk[:500])
if len(chunks) >= 2:
    print(f"\n--- OVERLAP TEST ---")
    print(f"Chunk 1 ENDING (last 100 chars):")
    print(repr(chunks[0][-100:]))
    print(f"\nChunk 2 BEGINNING (first 100 chars):")
    print(repr(chunks[1][:100]))

import tiktoken
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
total_tokens = len(encoding.encode(cleaned_text))
print(f"Total tokens in text: {total_tokens}")
print("\n" + "="*50)
print("TESTING METADATA EXTRACTION FROM PDF")

metadata = extract_metadata(file_path)
print(metadata)