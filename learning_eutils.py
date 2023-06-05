import eutils
from eutils._internal.xmlfacades.pubmedarticle import PubmedArticle
from eutils._internal.xmlfacades.pubmedarticleset import PubmedArticleSet
import csv


ec = eutils.Client()    

#SUBSTITUTE
csvfile = "pmid_list.csv"

#Get IDs from a csv
pmid_list= list()
with open(csvfile) as csv_file:
    csv_reader= csv.DictReader(csv_file, delimiter=",")
    for row in csv_reader:
        pmid=row['pmid']
        if pmid == "NA" or None:
            continue
        pmid_list.append(pmid)


#fetch all the records. Collection of Pubmed Articles
article_set = ec.efetch(db="pubmed",id=pmid_list)
print(article_set)

#Iterate over a collection of pubmed articles
#Receives a eutils._internal.xmlfacades.PubmedArticleSet
def articleRIS(article: PubmedArticle):
    all_authors=""
    for author in article.authors:
        all_authors = all_authors + f"AU  - {author}\n"
    all_authors = all_authors.strip("\n")
    all_pages=""
    if article.pages:
        sp = article.pages.split('-')[0]
        ep = article.pages.split('-')[-1]
        all_pages = f"SP  - {sp}\nEP  - {ep}"
    all_ids=""
    if article.pmc:
        all_ids=f"M2  - PMID: {article.pmid} PMCID: {article.pmc}\n"
    else:
        all_ids= f"M2  - PMID: {article.pmid}\n"

    output = f"""TY  - JOUR
TI  - {article.title}
{all_authors}
PY  - {article.year}
T2  - {article.jrnl}
VL  - {article.volume}
IS  - {article.issue}
{all_pages}
DO  - {article.doi}
{all_ids}
AB  - {article.abstract}
UR  - https://www.ncbi.nlm.nih.gov/pubmed/{article.pmid}
ER  - 
""".replace("\n\n","\n")
    return output

#Create a list of articles
def articleSetRIS(aSet: PubmedArticleSet):
    output = list()
    for article in aSet:
        output.append(articleRIS(article))
    return output

#Creates a RIS file
def savingRIS(articlesetRIS:list):  
    f = open("nowak_fixed.ris", "w")
    f.writelines(formated_article_set)
    f.close()

formated_article_set= articleSetRIS(article_set)
savingRIS(formated_article_set)