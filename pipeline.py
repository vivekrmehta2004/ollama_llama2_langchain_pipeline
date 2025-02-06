import pandas as pd
from convert import convert_all_files
from keyword1 import extract_keywords
from question import generate_questions

# Output file
OUTPUT_EXCEL = "res.xlsx"

def run_pipeline():
    documents = convert_all_files()
    all_data = []

    for filename, text in documents.items():
        keywords = extract_keywords(text)
        questions = generate_questions(text)
        all_data.append([filename, "\n".join(keywords), "\n".join(questions)])

    # Save results to Excel
    df = pd.DataFrame(all_data, columns=["File Name", "Keywords", "Policy Questions"])
    df.to_excel(OUTPUT_EXCEL, index=False)
    print(f"✅ Results saved to {OUTPUT_EXCEL}")

if __name__ == "__main__":
    print("🚀 Running Policy Analysis Pipeline...")
    run_pipeline()
