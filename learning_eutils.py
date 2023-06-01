import eutils
ec = eutils.Client()

# search for pcos in pubmed
# any valid NCBI query may be used
query = ec.esearch(db='pubmed',term='pcos[all]')
#print(f"here is your query:\n{query}")
#print(f"here is your list of ids:\n{query.ids}")

#fetch all the records
fetch = ec.efetch(db="pubmed",id= query.ids)
#print(f"here is what you fetch:\n{fetch}")

#Iterate over a collection of pubmed articles
#Receives a eutils._internal.xmlfacades.PubmedArticleSet
#Returns str

for article in fetch:
    authors = article.authors
    title = article.title
    journal = article.jrnl
    issue =article.issue
    year = article.year
    pages = article.pages
    doi = article.doi
    pmc= article.pmc
    pmid = article.pmid
    print(f"\n{authors}.{title},{journal},{issue},DOI:{doi},PMCID:{pmc},PMID:{pmid}")


