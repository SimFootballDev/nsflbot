import discord
import requests
from bs4 import BeautifulSoup
import csv

###
#note that this bot needs to be in the same dir as all the csvs.
###

TOKEN = 'my token'

client = discord.Client()


"""

ACTUAL STAT SENDING STUFF

"""

@client.event
async def on_message(message):
    if message.content.startswith("!help"):

        embed = discord.Embed(title="Commands", description="", color=0x0080ff)
        embed.set_thumbnail(url="https://i.imgur.com/cwY9q0f.png")
        embed.add_field(name="Stats Commands", value="!qb/wr/rb/df/k/ol/r stats Lastname. Firstletter.", inline=False)
        #embed.add_field(name="Career Stats Commands", value="!qb/wr/rb/df/k/ol/r cstats Lastname, Firstletter.", inline=False)
        embed.set_footer(text="made by Nykonax#7723")
        await message.channel.send(embed=embed)

    elif message.content.startswith("!qb stats"):
        # reads data
        with open('qbs.csv', 'r') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            names = []
            games = []
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
                game = row[3]
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
                games.append(game)
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
            thegames = games[namedex]
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
            embed.set_thumbnail(url="https://i.imgur.com/cwY9q0f.png")
            embed.add_field(name="Team", value="{0}".format(theTeams), inline=True)
            embed.add_field(name="Games", value="{0}".format(thegames), inline=True)
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
        with open('wr.csv', 'r') as wrcsvfile:
            wrreadCSV = csv.reader(wrcsvfile, delimiter=',')
            wrnames = []
            wrgames = []
            wryards = []
            wrteams = []
            catches = []
            wraverages = []
            wrlongests = []
            wrtouchdowns = []
            for row in wrreadCSV:
                wrname = row[0]
                wrgame = row[3]
                wryard = row[5]
                wrteam = row[2]
                catch = row[4]
                wravg = row[6]
                wrlongest = row[7]
                wrtouchdown = row[8]

                wrnames.append(wrname)
                wrgames.append(wrgame)
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

            if whatWR == "Trash":
                whatWR = "Swift. N."

            wrnamedex = wrnames.index(whatWR)
            wrthegames = wrgames[wrnamedex]
            WRtheYards = wryards[wrnamedex]
            WRtheTeams = wrteams[wrnamedex]
            theCatches = catches[wrnamedex]
            WRtheAverages = wraverages[wrnamedex]
            WRtheLongests = wrlongests[wrnamedex]
            WRtheTouchdowns = wrtouchdowns[wrnamedex]

            embed = discord.Embed(title="{0} Stats".format(whatWR), description="Receiving Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/cwY9q0f.png")
            embed.add_field(name="Team", value="{0}".format(WRtheTeams), inline=True)
            embed.add_field(name="Games", value="{0}".format(wrthegames), inline=True)
            embed.add_field(name="Catches", value="{0}".format(theCatches), inline=True)
            embed.add_field(name="Average", value="{0}".format(WRtheAverages), inline=True)
            embed.add_field(name="Yards", value="{0}".format(WRtheYards), inline=True)
            embed.add_field(name="TDs", value="{0}".format(WRtheTouchdowns), inline=True)
            embed.add_field(name="Longest Catch", value="{0}".format(WRtheLongests), inline=True)
            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)

    elif message.content.startswith("!rb stats"):
        with open('rb.csv', 'r') as rbcsvfile:
            rbreadCSV = csv.reader(rbcsvfile, delimiter=',')
            rbnames = []
            rbgames = []
            rbyards = []
            rbteams = []
            carries = []
            rbaverages = []
            rblongests = []
            rbtouchdowns = []
            for row in rbreadCSV:
                rbname = row[0]
                rbgame = row[3]
                rbyard = row[5]
                rbteam = row[2]
                carry = row[4]
                rbavg = row[6]
                rblongest = row[7]
                rbtouchdown = row[8]

                rbnames.append(rbname)
                rbgames.append(rbgame)
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
            rbthegames = rbgames[rbnamedex]
            rbtheYards = rbyards[rbnamedex]
            rbtheTeams = rbteams[rbnamedex]
            theCarries = carries[rbnamedex]
            rbtheAverages = rbaverages[rbnamedex]
            rbtheLongests = rblongests[rbnamedex]
            rbtheTouchdowns = rbtouchdowns[rbnamedex]

            embed = discord.Embed(title="{0} Stats".format(whatRB), description="Rushing Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/cwY9q0f.png")
            embed.add_field(name="Team", value="{0}".format(rbtheTeams), inline=True)
            embed.add_field(name="Games", value="{0}".format(rbthegames), inline=True)
            embed.add_field(name="Carries", value="{0}".format(theCarries), inline=True)
            embed.add_field(name="Average", value="{0}".format(rbtheAverages), inline=True)
            embed.add_field(name="Yards", value="{0}".format(rbtheYards), inline=True)
            embed.add_field(name="TDs", value="{0}".format(rbtheTouchdowns), inline=True)
            embed.add_field(name="Longest Carry", value="{0}".format(rbtheLongests), inline=True)
            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)

    elif message.content.startswith("!df stats"):
        with open('df.csv', 'r') as dfcsvfile:
            dfreadCSV = csv.reader(dfcsvfile, delimiter=',')
            dfnames = []
            dfgames = []
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
                dfgame = row[3]
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
                dfgames.append(dfgame)
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
            dfthegames = dfgames[dfnamedex]
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
            embed.set_thumbnail(url="https://i.imgur.com/cwY9q0f.png")
            embed.add_field(name="Team", value="{0}".format(dftheTeams), inline=True)
            embed.add_field(name="Games", value="{0}".format(dfthegames), inline=True)
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
        with open('r.csv', 'r') as rcsvfile:
            rreadCSV = csv.reader(rcsvfile, delimiter=',')
            rnames = []
            rgames = []
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
                rgame = row[3]
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
                rgames.append(rgame)
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
            rthegames = rgames[rnamedex]
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
            embed.set_thumbnail(url="https://i.imgur.com/cwY9q0f.png")
            embed.add_field(name="Team", value="{0}".format(rtheTeams), inline=True)
            embed.add_field(name="Games", value="{0}".format(rthegames), inline=True)
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
        with open('ol.csv', 'r') as olcsvfile:
            olreadCSV = csv.reader(olcsvfile, delimiter=',')
            olnames = []
            olgames = []
            olpancakes = []
            olteams = []
            olsacksalloweds = []

            for row in olreadCSV:
                olname = row[0]
                olgame = row[3]
                olpancake = row[4]
                olteam = row[2]
                olsacksallowed = row[5]

                olnames.append(olname)
                olgames.append(olgame)
                olpancakes.append(olpancake)
                olteams.append(olteam)
                olsacksalloweds.append(olsacksallowed)

            ols = message.content
            ols = str(ols)
            prefix = str(ols[:8])
            whatOL = str(ols[10:100])

            olnamedex = olnames.index(whatOL)
            olthegames = olgames[olnamedex]
            olthePancakes = olpancakes[olnamedex]
            oltheTeams = olteams[olnamedex]
            oltheSacksAllowed = olsacksalloweds[olnamedex]
            embed = discord.Embed(title="{0} Stats".format(whatOL), description="Blocking Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/cwY9q0f.png")
            embed.add_field(name="Team", value="{0}".format(oltheTeams), inline=True)
            embed.add_field(name="Games", value="{0}".format(olthegames), inline=True)
            embed.add_field(name="Pancakes", value="{0}".format(olthePancakes), inline=True)
            embed.add_field(name="Sacks Allowed", value="{0}".format(oltheSacksAllowed), inline=True)
            embed.set_footer(text="made by Nykonax#7723")
            await message.channel.send(embed=embed)


    elif message.content.startswith("!k stats"):
        with open('k.csv', 'r') as kcsvfile:
            kreadCSV = csv.reader(kcsvfile, delimiter=',')
            knames = []
            kgames = []
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
                kgame = row[3]
                kxpm = row[4]
                kteam = row[2]
                kxpa = row[5]
                kfgm = row[7]
                kfga = row[8]
                kfgpct = row[9]
                kxppct = row[6]
                klongest = row[15]


                knames.append(kname)
                kgames.append(kgame)
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
            kthegames = kgames[knamedex]
            kthexpms = kxpms[knamedex]
            kthexpas = kxpas[knamedex]
            kthefgms = kfgms[knamedex]
            kthefgas = kfgas[knamedex]
            kthefgpcts = kfgpcts[knamedex]
            kthexppcts = kxppcts[knamedex]
            kthelongests = klongests[knamedex]
            ktheteams = kteams[knamedex]

        with open('p.csv', 'r') as pcsvfile:
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
            ptheyards = pyards[pnamedex]
            ptheavgs = pavgs[pnamedex]
            pthetwenties = pintwenties[pnamedex]
            pthelongests = plongests[pnamedex]

            embed = discord.Embed(title="{0} Stats".format(whatK), description="K/P Stats", color=0x0080ff)
            embed.set_thumbnail(url="https://i.imgur.com/cwY9q0f.png")
            embed.add_field(name="Team", value="{0}".format(ktheteams), inline=True)
            embed.add_field(name="Games", value="{0}".format(kthegames), inline=True)
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