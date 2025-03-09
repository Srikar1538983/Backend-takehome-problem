import csv

def export_to_csv(papers, filename):
    """Exports filtered research papers to a CSV file."""
    if not papers:
        print("No papers to export.")
        return
    
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "authors", "affiliation", "journal", "doi"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(papers)
    
    print(f"Results saved to {filename}")