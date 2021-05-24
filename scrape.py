import requests
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen

url = "https://github.com/facebook/react"
# url = "https://github.com/matiassingers/awesome-readme"



author = ""
repo = ""

code = requests.get(url)
plain = code.text

s = BeautifulSoup(plain, "html.parser")


def scrape_repo_data():

    if author and repo:

        # Description
        desc = ""
        for link in s.findAll('p', {'class': 'f4 mt-3'}):
            desc = link.get_text()
            # print(desc)
            desc = desc.strip()

        # print("Desc = ", desc)

        # Contributors

        check = "/" + author + "/" + repo + "/graphs/contributors"

        contrib_no = []
        for contrib in s.findAll('a', {'href': check}):
            # print(contrib)
            try:
                contrib_no.append(contrib.span.get_text())
            except AttributeError as e:
                contrib_no.append(contrib.get_text())

        # print(contrib_no)
        contrib_no_mod = []
        sum_contrib = 0
        for j in contrib_no:
            j = str(j).replace(",", "")
            contrib_no_mod.append([int(i) for i in str(j).split() if i.isdigit()])
        # print(contrib_no_mod)
        for i in contrib_no_mod:
            sum_contrib = sum_contrib + int(i[0])

        # print("Contributors = ", sum_contrib)
        # ['1,541', '\n      + 1,530 contributors\n']
        # ['66', '\n      + 55 contributors\n']

        # star and fork

        git_star_fork = []
        stars_no = 0
        fork_no = 0
        for forker in s.findAll('a', {'class': 'social-count'}):
            git_star_fork.append(forker.get_text())

        for i in git_star_fork:
            stars_no = git_star_fork[0].strip()
            fork_no = git_star_fork[1].strip()

        # print("Stars = ", stars_no)
        # print("Fork = ", fork_no)

        # Issues
        issues_no = 0
        try:
            for iss in s.findAll('a', {'data-tab-item': 'i1issues-tab'}):
                # print(iss)
                issues_no = iss.find('span', {'class': 'Counter'}).get_text()
        except:
            issues_no = 0

        # print("Issues = ", issues_no)

        prog_lang = []
        percent = []
        for lang in s.findAll('a', {
            'class': 'd-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3'}):
            prog_lang.append(lang.span.get_text())
            percent.append(lang.find('span', {'class': None}).get_text())

        # print("Programming Languages : ")
        # for i in range(len(prog_lang)):
            # print(str(prog_lang[i]) + " with " + percent[i])


        return desc, sum_contrib, stars_no, fork_no, issues_no, prog_lang, percent

def scrape_basic_data():

        global author, repo
    #try:
        author = s.find('a', {'class': 'url fn'}).get_text()
        repo = s.find('a', {'data-pjax': '#js-repo-pjax-container'}).get_text()

        # print(author)
        # print(repo)
        # print()

        s_desc, s_contrib, s_stars, s_forks, s_issues, s_lang, s_percent= scrape_repo_data()

        return author, repo, s_desc, s_contrib, s_stars, s_forks, s_issues, s_lang, s_percent
        # print(author, repo, s_desc, s_contrib, s_stars, s_forks, s_issues, s_lang, s_percent)

    #except Exception as e:
    #    print("Invalid URL : ", e)



# scrape_basic_data()