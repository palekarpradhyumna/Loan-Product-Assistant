def clean_text(text):
    cleaned = []
    for line in text.split("\n"):
        line = line.strip()
        if len(line) > 10:  
            cleaned.append(line)
    return "\n".join(cleaned)

with open("loan_data_raw.txt", "r", encoding="utf-8") as infile:
    raw = infile.read()

print(f"Original characters: {len(raw)}") 

cleaned = clean_text(raw)

with open("loan_data_cleaned.txt", "w", encoding="utf-8") as outfile:
    outfile.write(cleaned)

print(f"Cleaned characters: {len(cleaned)}")
