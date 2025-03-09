import click
from pubmed_fetcher.fetcher import fetch_papers
from pubmed_fetcher.filter import filter_papers
from pubmed_fetcher.exporter import export_to_csv  # ✅ Make sure this matches exactly

@click.command()
@click.argument("query")
@click.option("-f", "--file", default="results.csv", help="Output CSV filename")
def main(query, file):
    """Fetch research papers from PubMed based on a query and filter results."""
    papers = fetch_papers(query)
    print("Fetched Papers:", papers) 
    filtered_papers = filter_papers(papers)

    if not filtered_papers:
        print("No relevant papers found.")
        return

    export_to_csv(filtered_papers, file)

if __name__ == "__main__":
    main()

