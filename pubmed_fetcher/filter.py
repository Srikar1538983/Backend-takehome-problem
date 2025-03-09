def filter_papers(papers):
    """Filters papers to keep only those with non-academic authors affiliated with pharmaceutical or biotech companies."""
    keywords = ["Pharmaceutical", "Biotech", "Corporation", "Inc.", "LLC"]

    def is_industry_affiliated(affiliation):
        return any(keyword.lower() in affiliation.lower() for keyword in keywords)

    filtered = [paper for paper in papers if is_industry_affiliated(paper["affiliation"])]
    return filtered

def filter_papers(papers):
    # return [paper for paper in papers if is_industry_author(paper)]  # Comment this
    return papers  # Return all papers instead
