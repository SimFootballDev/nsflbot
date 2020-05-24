import requests
from bs4 import BeautifulSoup
from simplified_scrapy import SimplifiedDoc,req,utils
import csv
import time

while True:
    time.sleep(14400)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    standingsURL = "https://index.sim-football.com/DSFLS22/"
    standingsPage = req.get(standingsURL)
    doc = SimplifiedDoc(standingsPage)
    standingTable = doc.selects('table.Grid')
    standingTitles = standingTable.selects("tr.hilite")
    standingHeaders = standingTable.selects("tr.alt")
    standinglist = standingTitles.tds.text

    url = "http://sim-football.com/indexes/DSFLS22/LeaguePassingStats.html"
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    tb = soup.find('table', class_='tablesorter')
    table_rows = tb.find_all("tr")

    wrurl = "http://sim-football.com/indexes/DSFLS22/LeagueReceivingStats.html"
    wrpage = requests.get(wrurl, headers=headers)
    wrsoup = BeautifulSoup(wrpage.content, 'html.parser')
    wrtb = wrsoup.find('table', class_='tablesorter')
    wrtable_rows = wrtb.find_all("tr")

    rburl = "http://sim-football.com/indexes/DSFLS22/LeagueRushingStats.html"
    rbpage = requests.get(rburl, headers=headers)
    rbsoup = BeautifulSoup(rbpage.content, 'html.parser')
    rbtb = rbsoup.find('table', class_='tablesorter')
    rbtable_rows = rbtb.find_all("tr")

    dfurl = "http://sim-football.com/indexes/DSFLS22/LeagueDefensiveStats.html"
    dfpage = requests.get(dfurl, headers=headers)
    dfsoup = BeautifulSoup(dfpage.content, 'html.parser')
    dftb = dfsoup.find('table', class_='tablesorter')
    dftable_rows = dftb.find_all("tr")

    kurl = "http://sim-football.com/indexes/DSFLS22/LeagueKickingStats.html"
    kpage = requests.get(kurl, headers=headers)
    ksoup = BeautifulSoup(kpage.content, 'html.parser')
    ktb = ksoup.find('table', class_='tablesorter')
    ktable_rows = ktb.find_all("tr")

    purl = "http://sim-football.com/indexes/DSFLS22/LeaguePuntingStats.html"
    ppage = requests.get(purl, headers=headers)
    psoup = BeautifulSoup(ppage.content, 'html.parser')
    ptb = psoup.find('table', class_='tablesorter')
    ptable_rows = ptb.find_all("tr")

    olurl = "http://sim-football.com/indexes/DSFLS22/LeagueOffensiveLineStats.html"
    olpage = requests.get(olurl, headers=headers)
    olsoup = BeautifulSoup(olpage.content, 'html.parser')
    oltb = olsoup.find('table', class_='tablesorter')
    oltable_rows = oltb.find_all("tr")

    rurl = "http://sim-football.com/indexes/DSFLS22/LeagueSpecialTeamsStats.html"
    rpage = requests.get(rurl, headers=headers)
    rsoup = BeautifulSoup(rpage.content, 'html.parser')
    rtb = rsoup.find('table', class_='tablesorter')
    rtable_rows = rtb.find_all("tr")

    """
    
    WRITES SEASON STAT DATA
    
    """
    with open('dsflstandings.csv', 'w', newline='') as file:
        swr = csv.writer(file)
        for srow in standinglist:
            srowPrintable = str(srow)
            srowPrintable = srowPrintable.replace('[', '')
            srowPrintable = srowPrintable.replace(']', '')
            srowPrintable = srowPrintable.replace('\'', '')
            srowCSV = srowPrintable.split(',')
            swr.writerow(srowCSV)

    with open('dsflol.csv', 'w', newline='') as ol_file:
        olwr = csv.writer(ol_file)
        for olrow in oltable_rows:
            olrowPrintable = str(olrow)
            olrowPrintable = olrowPrintable.replace(',', '.')
            olrowPrintable = olrowPrintable.replace(' (R)', '')
            olrowPrintable = BeautifulSoup(olrowPrintable, "lxml").get_text(separator=',')
            olrowCSV = olrowPrintable.split(',')
            olwr.writerow(olrowCSV)

    with open('dsflr.csv', 'w', newline='') as r_file:
        rwr = csv.writer(r_file)
        for rrow in rtable_rows:
            rrowPrintable = str(rrow)
            rrowPrintable = rrowPrintable.replace(',', '.')
            rrowPrintable = rrowPrintable.replace(' (R)', '')
            rrowPrintable = BeautifulSoup(rrowPrintable, "lxml").get_text(separator=',')
            rrowCSV = rrowPrintable.split(',')
            rwr.writerow(rrowCSV)

    with open('dsflp.csv', 'w', newline='') as p_file:
        pwr = csv.writer(p_file)
        for prow in ptable_rows:
            prowPrintable = str(prow)
            prowPrintable = prowPrintable.replace(',', '.')
            prowPrintable = prowPrintable.replace(' (R)', '')
            prowPrintable = BeautifulSoup(prowPrintable, "lxml").get_text(separator=',')
            prowCSV = prowPrintable.split(',')
            pwr.writerow(prowCSV)

    with open('dsflk.csv', 'w', newline='') as k_file:
        kwr = csv.writer(k_file)
        for krow in ktable_rows:
            krowPrintable = str(krow)
            krowPrintable = krowPrintable.replace(',', '.')
            krowPrintable = krowPrintable.replace(' (R)', '')
            krowPrintable = BeautifulSoup(krowPrintable, "lxml").get_text(separator=',')
            krowCSV = krowPrintable.split(',')
            kwr.writerow(krowCSV)

    with open('dsfldf.csv', 'w', newline='') as df_file:
        dfwr = csv.writer(df_file)
        for dfrow in dftable_rows:
            dfrowPrintable = str(dfrow)
            dfrowPrintable = dfrowPrintable.replace(',', '.')
            dfrowPrintable = dfrowPrintable.replace(' (R)', '')
            dfrowPrintable = BeautifulSoup(dfrowPrintable, "lxml").get_text(separator=',')
            dfrowCSV = dfrowPrintable.split(',')
            dfwr.writerow(dfrowCSV)

    with open('dsflrb.csv', 'w', newline='') as rb_file:
        rbwr = csv.writer(rb_file)
        for rbrow in rbtable_rows:
            rbrowPrintable = str(rbrow)
            rbrowPrintable = rbrowPrintable.replace(',', '.')
            rbrowPrintable = rbrowPrintable.replace(' (R)', '')
            rbrowPrintable = BeautifulSoup(rbrowPrintable, "lxml").get_text(separator=',')
            rbrowCSV = rbrowPrintable.split(',')
            rbwr.writerow(rbrowCSV)

    with open('dsflwr.csv', 'w', newline='') as wr_file:
        wrwr = csv.writer(wr_file)
        for wrrow in wrtable_rows:
            wrrowPrintable = str(wrrow)
            wrrowPrintable = wrrowPrintable.replace(',', '.')
            wrrowPrintable = wrrowPrintable.replace(' (R)', '')
            wrrowPrintable = BeautifulSoup(wrrowPrintable, "lxml").get_text(separator=',')
            wrrowCSV = wrrowPrintable.split(',')
            wrwr.writerow(wrrowCSV)

    with open('dsflqbs.csv', 'w', newline='') as qb_file:
        qbwr = csv.writer(qb_file)
        for row in table_rows:
            rowPrintable = str(row)
            rowPrintable = rowPrintable.replace(',', '.')
            rowPrintable = rowPrintable.replace(' (R)', '')
            rowPrintable = BeautifulSoup(rowPrintable, "lxml").get_text(separator=',')
            rowCSV = rowPrintable.split(',')
            qbwr.writerow(rowCSV)
