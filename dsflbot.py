import discord
import requests
from bs4 import BeautifulSoup
import csv

TOKEN = 'my token'

client = discord.Client()

"""

BUNCH OF SCRAPING STUFF

"""
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

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

with open('dsflol.csv', 'w', newline='') as ol_file:
    olwr = csv.writer(ol_file)
    for olrow in oltable_rows:
        olrowPrintable = str(olrow)
        olrowPrintable = olrowPrintable.replace(',', '.')
        olrowPrintable = olrowPrintable.replace(' (R)', '')
        olrowPrintable = BeautifulSoup(olrowPrintable, "lxml").get_text(separator=',')
        olrowCSV = olrowPrintable.split(',')
        #print(rowPrintable)
        olwr.writerow(olrowCSV)

with open('dsflr.csv', 'w', newline='') as r_file:
    rwr = csv.writer(r_file)
    for rrow in rtable_rows:
        rrowPrintable = str(rrow)
        rrowPrintable = rrowPrintable.replace(',', '.')
        olrowPrintable = olrowPrintable.replace(' (R)', '')
        rrowPrintable = BeautifulSoup(rrowPrintable, "lxml").get_text(separator=',')
        rrowCSV = rrowPrintable.split(',')
        #print(rowPrintable)
        rwr.writerow(rrowCSV)

with open('dsflp.csv', 'w', newline='') as p_file:
    pwr = csv.writer(p_file)
    for prow in ptable_rows:
        prowPrintable = str(prow)
        prowPrintable = prowPrintable.replace(',', '.')
        prowPrintable = prowPrintable.replace(' (R)', '')
        prowPrintable = BeautifulSoup(prowPrintable, "lxml").get_text(separator=',')
        prowCSV = prowPrintable.split(',')
        #print(rowPrintable)
        pwr.writerow(prowCSV)


with open('dsflk.csv', 'w', newline='') as k_file:
    kwr = csv.writer(k_file)
    for krow in ktable_rows:
        krowPrintable = str(krow)
        krowPrintable = krowPrintable.replace(',', '.')
        krowPrintable = krowPrintable.replace(' (R)', '')
        krowPrintable = BeautifulSoup(krowPrintable, "lxml").get_text(separator=',')
        krowCSV = krowPrintable.split(',')
        #print(rowPrintable)
        kwr.writerow(krowCSV)

with open('dsfldf.csv', 'w', newline='') as df_file:
    dfwr = csv.writer(df_file)
    for dfrow in dftable_rows:
        dfrowPrintable = str(dfrow)
        dfrowPrintable = dfrowPrintable.replace(',', '.')
        dfrowPrintable = dfrowPrintable.replace(' (R)', '')
        dfrowPrintable = BeautifulSoup(dfrowPrintable, "lxml").get_text(separator=',')
        dfrowCSV = dfrowPrintable.split(',')
        #print(rowPrintable)
        dfwr.writerow(dfrowCSV)

with open('dsflrb.csv', 'w', newline='') as rb_file:
    rbwr = csv.writer(rb_file)
    for rbrow in rbtable_rows:
        rbrowPrintable = str(rbrow)
        rbrowPrintable = rbrowPrintable.replace(',', '.')
        rbrowPrintable = rbrowPrintable.replace(' (R)', '')
        rbrowPrintable = BeautifulSoup(rbrowPrintable, "lxml").get_text(separator=',')
        rbrowCSV = rbrowPrintable.split(',')
        #print(rowPrintable)
        rbwr.writerow(rbrowCSV)

with open('dsflwr.csv', 'w', newline='') as wr_file:
    wrwr = csv.writer(wr_file)
    for wrrow in wrtable_rows:
        wrrowPrintable = str(wrrow)
        wrrowPrintable = wrrowPrintable.replace(',', '.')
        wrrowPrintable = wrrowPrintable.replace(' (R)', '')
        wrrowPrintable = BeautifulSoup(wrrowPrintable, "lxml").get_text(separator=',')
        wrrowCSV = wrrowPrintable.split(',')
        #print(rowPrintable)
        wrwr.writerow(wrrowCSV)

with open('dsflqbs.csv', 'w', newline='') as qb_file:
    qbwr = csv.writer(qb_file)
    for row in table_rows:
        rowPrintable = str(row)
        rowPrintable = rowPrintable.replace(',', '.')
        rowPrintable = rowPrintable.replace(' (R)', '')
        rowPrintable = BeautifulSoup(rowPrintable, "lxml").get_text(separator=',')
        rowCSV = rowPrintable.split(',')
        #print(rowPrintable)
        qbwr.writerow(rowCSV)

"""

NORMAL SEASON STATS FIRST

"""

@client.event
async def on_message(message):

    if message.content.startswith("!qb stats"):
        # reads data
        with open('dsflqbs.csv', 'r') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            names = []
            yards = []
            teams = []
            comps = []
            attempts = []
            percentages = []
            longests = []
            touchdowns = []
            ints = []
            ratings = []
            for row in readCSV:
                name = row[0]
                yard = row[6]
                team = row[2]
                comp = row[4]
                att = row[5]
                pct = row[7]
                longest = row[8]
                touchdown = row[9]
                int = row[10]
                rating = row[11]

                names.append(name)
                yards.append(yard)
                teams.append(team)
                comps.append(comp)
                attempts.append(att)
                percentages.append(pct)
                longests.append(longest)
                touchdowns.append(touchdown)
                ints.append(int)
                ratings.append(rating)

            s = message.content
            s = str(s)
            prefix = str(s[:8])
            whatQB = str(s[10:100])


            namedex = names.index(whatQB)
            theYards = yards[namedex]
            theTeams = teams[namedex]
            theComps = comps[namedex]
            theAttempts = attempts[namedex]
            thePct = percentages[namedex]
            theLongests = longests[namedex]
            theTouchdowns = touchdowns[namedex]
            theInts = ints[namedex]
            theRatings = ratings[namedex]

            embed = discord.Embed(title="{0} Stats".format(whatQB), description="QB Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/NBmz1lH.png")
            embed.add_field(name="Team", value="{0}".format(theTeams), inline=True)
            embed.add_field(name="Completions", value="{0}".format(theComps), inline=True)
            embed.add_field(name="Attempts", value="{0}".format(theAttempts), inline=True)
            embed.add_field(name="Percentage", value="{0}".format(thePct), inline=True)
            embed.add_field(name="Yards", value="{0}".format(theYards), inline=True)
            embed.add_field(name="TDs", value="{0}".format(theTouchdowns), inline=True)
            embed.add_field(name="INTs", value="{0}".format(theInts), inline=True)
            embed.add_field(name="Rating", value="{0}".format(theRatings), inline=True)
            embed.add_field(name="Longest Throw", value="{0}".format(theLongests), inline=True)
            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)

    elif message.content.startswith("!wr stats"):
        with open('dsflwr.csv', 'r') as wrcsvfile:
            wrreadCSV = csv.reader(wrcsvfile, delimiter=',')
            wrnames = []
            wryards = []
            wrteams = []
            catches = []
            wraverages = []
            wrlongests = []
            wrtouchdowns = []
            for row in wrreadCSV:
                wrname = row[0]
                wryard = row[5]
                wrteam = row[2]
                catch = row[4]
                wravg = row[6]
                wrlongest = row[7]
                wrtouchdown = row[8]

                wrnames.append(wrname)
                wryards.append(wryard)
                wrteams.append(wrteam)
                catches.append(catch)
                wraverages.append(wravg)
                wrlongests.append(wrlongest)
                wrtouchdowns.append(wrtouchdown)

            wrs = message.content
            wrs = str(wrs)
            prefix = str(wrs[:8])
            whatWR = str(wrs[10:100])

            wrnamedex = wrnames.index(whatWR)
            WRtheYards = wryards[wrnamedex]
            WRtheTeams = wrteams[wrnamedex]
            theCatches = catches[wrnamedex]
            WRtheAverages = wraverages[wrnamedex]
            WRtheLongests = wrlongests[wrnamedex]
            WRtheTouchdowns = wrtouchdowns[wrnamedex]

            embed = discord.Embed(title="{0} Stats".format(whatWR), description="Receiving Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/NBmz1lH.png")
            embed.add_field(name="Team", value="{0}".format(WRtheTeams), inline=True)
            embed.add_field(name="Catches", value="{0}".format(theCatches), inline=True)
            embed.add_field(name="Average", value="{0}".format(WRtheAverages), inline=True)
            embed.add_field(name="Yards", value="{0}".format(WRtheYards), inline=True)
            embed.add_field(name="TDs", value="{0}".format(WRtheTouchdowns), inline=True)
            embed.add_field(name="Longest Catch", value="{0}".format(WRtheLongests), inline=True)
            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)

    elif message.content.startswith("!rb stats"):
        with open('dsflrb.csv', 'r') as rbcsvfile:
            rbreadCSV = csv.reader(rbcsvfile, delimiter=',')
            rbnames = []
            rbyards = []
            rbteams = []
            carries = []
            rbaverages = []
            rblongests = []
            rbtouchdowns = []
            for row in rbreadCSV:
                rbname = row[0]
                rbyard = row[5]
                rbteam = row[2]
                carry = row[4]
                rbavg = row[6]
                rblongest = row[7]
                rbtouchdown = row[8]

                rbnames.append(rbname)
                rbyards.append(rbyard)
                rbteams.append(rbteam)
                carries.append(carry)
                rbaverages.append(rbavg)
                rblongests.append(rblongest)
                rbtouchdowns.append(rbtouchdown)

            rbs = message.content
            rbs = str(rbs)
            prefix = str(rbs[:8])
            whatRB = str(rbs[10:100])

            rbnamedex = rbnames.index(whatRB)
            rbtheYards = rbyards[rbnamedex]
            rbtheTeams = rbteams[rbnamedex]
            theCarries = carries[rbnamedex]
            rbtheAverages = rbaverages[rbnamedex]
            rbtheLongests = rblongests[rbnamedex]
            rbtheTouchdowns = rbtouchdowns[rbnamedex]

            embed = discord.Embed(title="{0} Stats".format(whatRB), description="Rushing Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/NBmz1lH.png")
            embed.add_field(name="Team", value="{0}".format(rbtheTeams), inline=True)
            embed.add_field(name="Carries", value="{0}".format(theCarries), inline=True)
            embed.add_field(name="Average", value="{0}".format(rbtheAverages), inline=True)
            embed.add_field(name="Yards", value="{0}".format(rbtheYards), inline=True)
            embed.add_field(name="TDs", value="{0}".format(rbtheTouchdowns), inline=True)
            embed.add_field(name="Longest Carry", value="{0}".format(rbtheLongests), inline=True)
            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)

    elif message.content.startswith("!df stats"):
        with open('dsfldf.csv', 'r') as dfcsvfile:
            dfreadCSV = csv.reader(dfcsvfile, delimiter=',')
            dfnames = []
            dftackles = []
            dfteams = []
            dftfls = []
            dfFFFRs = []
            dfsacks = []
            dfints = []
            dfpds = []
            dfsafeties = []
            dftouchdowns = []


            for row in dfreadCSV:
                dfname = row[0]
                dftackle = row[4]
                dfteam = row[2]
                dftfl = row[5]
                dfFFFR = row[6]
                dfsack = row[7]
                dfint = row[8]
                dfpd = row[9]
                dfsafety = row[10]
                dftouchdown = row[11]


                dfnames.append(dfname)
                dftackles.append(dftackle)
                dfteams.append(dfteam)
                dftfls.append(dftfl)
                dfFFFRs.append(dfFFFR)
                dfsacks.append(dfsack)
                dfints.append(dfint)
                dfpds.append(dfpd)
                dfsafeties.append(dfsafety)
                dftouchdowns.append(dftouchdown)

            dfs = message.content
            dfs = str(dfs)
            prefix = str(dfs[:8])
            whatDF = str(dfs[10:100])

            dfnamedex = dfnames.index(whatDF)
            dftheTackles = dftackles[dfnamedex]
            dftheTeams = dfteams[dfnamedex]
            dftheTFLs = dftfls[dfnamedex]
            dftheFFFRs = dfFFFRs[dfnamedex]
            dftheSacks = dfsacks[dfnamedex]
            dftheInts = dfints[dfnamedex]
            dfthePDs = dfpds[dfnamedex]
            dftheSafeties = dfsafeties[dfnamedex]
            dftheTouchdowns = dftouchdowns[dfnamedex]

            embed = discord.Embed(title="{0} Stats".format(whatDF), description="Defensive Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/NBmz1lH.png")
            embed.add_field(name="Team", value="{0}".format(dftheTeams), inline=True)
            embed.add_field(name="Tackles", value="{0}".format(dftheTackles), inline=True)
            embed.add_field(name="TFLs", value="{0}".format(dftheTFLs), inline=True)
            embed.add_field(name="FF/FR", value="{0}".format(dftheFFFRs), inline=True)
            embed.add_field(name="Sacks", value="{0}".format(dftheSacks), inline=True)
            embed.add_field(name="Interceptions", value="{0}".format(dftheInts), inline=True)
            embed.add_field(name="PDs", value="{0}".format(dfthePDs), inline=True)
            embed.add_field(name="Safeties", value="{0}".format(dftheSafeties), inline=True)
            embed.add_field(name="Touchdowns", value="{0}".format(dftheTouchdowns), inline=True)

            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)

    elif message.content.startswith("!r stats"):
        with open('dsflr.csv', 'r') as rcsvfile:
            rreadCSV = csv.reader(rcsvfile, delimiter=',')
            rnames = []
            rkrs = []
            rteams = []
            rkryards = []
            rkravgs = []
            rkrlongests = []
            rkrtds = []
            rprs = []
            rpryards = []
            rprtds = []
            rprlongests = []
            rpravgs = []

            for row in rreadCSV:
                rname = row[0]
                rkr = row[4]
                rteam = row[2]
                rkryard = row[5]
                rkravg = row[6]
                rkrlongest = row[7]
                rkrtd = row[8]
                rpr = row[9]
                rpryard = row[10]
                rprtd = row[13]
                rprlongest = row[12]
                rpravg = row[11]

                rnames.append(rname)
                rkrs.append(rkr)
                rteams.append(rteam)
                rkryards.append(rkryard)
                rkravgs.append(rkravg)
                rkrlongests.append(rkrlongest)
                rkrtds.append(rkrtd)
                rprs.append(rpr)
                rpryards.append(rpryard)
                rprtds.append(rprtd)
                rprlongests.append(rprlongest)
                rpravgs.append(rpravg)

            rs = message.content
            rs = str(rs)
            prefix = str(rs[:7])
            whatR = str(rs[9:100])

            rnamedex = rnames.index(whatR)
            rtheKRs = rkrs[rnamedex]
            rtheTeams = rteams[rnamedex]
            rtheKRYards = rkryards[rnamedex]
            rtheKRAvgs = rkravgs[rnamedex]
            rtheKRLongests = rkrlongests[rnamedex]
            rtheKRTDs = rkrtds[rnamedex]
            rthePRs = rprs[rnamedex]
            rthePRAvgs = rpravgs[rnamedex]
            rthePRYards = rpryards[rnamedex]
            rthePRTDs = rprtds[rnamedex]
            rthePRLongests = rprlongests[rnamedex]

            embed = discord.Embed(title="{0} Stats".format(whatR), description="Returning Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/NBmz1lH.png")
            embed.add_field(name="Team", value="{0}".format(rtheTeams), inline=True)
            embed.add_field(name="Kick Returns", value="{0}".format(rtheKRs), inline=True)
            embed.add_field(name="KR Yards", value="{0}".format(rtheKRYards), inline=True)
            embed.add_field(name="KR TDs", value="{0}".format(rtheKRTDs), inline=True)
            embed.add_field(name="KR Avg", value="{0}".format(rtheKRAvgs), inline=True)
            embed.add_field(name="KR Longest", value="{0}".format(rtheKRLongests), inline=True)
            embed.add_field(name="Punt Returns", value="{0}".format(rthePRs), inline=True)
            embed.add_field(name="PR Yards", value="{0}".format(rthePRYards), inline=True)
            embed.add_field(name="PR TDs", value="{0}".format(rthePRTDs), inline=True)
            embed.add_field(name="PR Avg", value="{0}".format(rthePRAvgs), inline=True)
            embed.add_field(name="PR Longest", value="{0}".format(rthePRLongests), inline=True)


            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)

    elif message.content.startswith("!ol stats"):
        with open('dsflol.csv', 'r') as olcsvfile:
            olreadCSV = csv.reader(olcsvfile, delimiter=',')
            olnames = []
            olpancakes = []
            olteams = []
            olsacksalloweds = []

            for row in olreadCSV:
                olname = row[0]
                olpancake = row[4]
                olteam = row[2]
                olsacksallowed = row[5]

                olnames.append(olname)
                olpancakes.append(olpancake)
                olteams.append(olteam)
                olsacksalloweds.append(olsacksallowed)

            ols = message.content
            ols = str(ols)
            prefix = str(ols[:8])
            whatOL = str(ols[10:100])

            olnamedex = olnames.index(whatOL)
            olthePancakes = olpancakes[olnamedex]
            oltheTeams = olteams[olnamedex]
            oltheSacksAllowed = olsacksalloweds[olnamedex]
            embed = discord.Embed(title="{0} Stats".format(whatOL), description="Blocking Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/NBmz1lH.png")
            embed.add_field(name="Team", value="{0}".format(oltheTeams), inline=True)
            embed.add_field(name="Pancakes", value="{0}".format(olthePancakes), inline=True)
            embed.add_field(name="Sacks Allowed", value="{0}".format(oltheSacksAllowed), inline=True)
            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)

    elif message.content.startswith("!k stats"):
        with open('dsflk.csv', 'r') as kcsvfile:
            kreadCSV = csv.reader(kcsvfile, delimiter=',')
            knames = []
            kxpms = []
            kxpas = []
            kfgms = []
            kfgas = []
            kfgpcts = []
            kxppcts = []
            klongests = []
            kteams = []
            for row in kreadCSV:
                kname = row[0]
                kxpm = row[4]
                kteam = row[2]
                kxpa = row[5]
                kfgm = row[7]
                kfga = row[8]
                kfgpct = row[9]
                kxppct = row[6]
                klongest = row[15]


                knames.append(kname)
                kxpms.append(kxpm)
                kteams.append(kteam)
                kxpas.append(kxpa)
                kfgms.append(kfgm)
                kfgas.append(kfga)
                kfgpcts.append(kfgpct)
                kxppcts.append(kxppct)
                klongests.append(klongest)


            ks = message.content
            ks = str(ks)
            prefix = str(ks[:7])
            whatK = str(ks[9:100])

            knamedex = knames.index(whatK)
            kthexpms = kxpms[knamedex]
            kthexpas = kxpas[knamedex]
            kthefgms = kfgms[knamedex]
            kthefgas = kfgas[knamedex]
            kthefgpcts = kfgpcts[knamedex]
            kthexppcts = kxppcts[knamedex]
            kthelongests = klongests[knamedex]
            ktheteams = kteams[knamedex]

        with open('dsflp.csv', 'r') as pcsvfile:
            preadCSV = csv.reader(pcsvfile, delimiter=',')
            pnames = []
            ppunts = []
            pyards = []
            pavgs = []
            pintwenties = []
            plongests = []
            pteams = []
            for row in preadCSV:
                pname = row[0]
                ppunt = row[4]
                pteam = row[2]
                pyard = row[5]
                pavg = row[6]
                pintwenty = row[7]
                plongest = row[8]

                pnames.append(pname)
                ppunts.append(ppunt)
                pteams.append(pteam)
                pyards.append(pyard)
                pavgs.append(pavg)
                pintwenties.append(pintwenty)
                plongests.append(plongest)

            ps = message.content
            ps = str(ps)
            prefix = str(ps[:7])
            whatP = str(ps[9:100])

            pnamedex = pnames.index(whatP)
            pthepunts = ppunts[pnamedex]
            ptheteams = pteams[pnamedex]
            ptheyards = pyards[pnamedex]
            ptheavgs = pavgs[pnamedex]
            pthetwenties = pintwenties[pnamedex]
            pthelongests = plongests[pnamedex]

            embed = discord.Embed(title="{0} Stats".format(whatK), description="K/P Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/NBmz1lH.png")
            embed.add_field(name="Team", value="{0}".format(ktheteams), inline=True)
            embed.add_field(name="XPM", value="{0}".format(kthexpms), inline=True)
            embed.add_field(name="XPA", value="{0}".format(kthexpas), inline=True)
            embed.add_field(name="XP%", value="{0}%".format(kthexppcts), inline=True)
            embed.add_field(name="FGM", value="{0}".format(kthefgms), inline=True)
            embed.add_field(name="FGA", value="{0}".format(kthefgas), inline=True)
            embed.add_field(name="FG%", value="{0}%".format(kthefgpcts), inline=True)
            embed.add_field(name="Longest Kick", value="{0}".format(kthelongests), inline=True)
            embed.add_field(name="Punts", value="{0}".format(pthepunts), inline=True)
            embed.add_field(name="Punting Yards", value="{0}".format(ptheyards), inline=True)
            embed.add_field(name="Average Yards", value="{0}".format(ptheavgs), inline=True)
            embed.add_field(name="Inside 20", value="{0}".format(pthetwenties), inline=True)
            embed.add_field(name="Longest Punt", value="{0}".format(pthelongests), inline=True)
            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)

client.run('my token')
