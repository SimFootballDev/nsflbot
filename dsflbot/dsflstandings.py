import csv
import discord

TOKEN = 'token'
client = discord.Client()

#ignore the copypaste code with east/west
#East = SFC South
#West = NFC North

@client.event
async def on_message(message):
    if message.content.startswith("!standings dsfl") or message.content.startswith("!standings DSFL"):
        with open('dsflstandings.csv', 'r', newline='') as file:
            data = list(csv.reader(file))
            eastone = data[0][0].strip()
            easttwo = data[0][12].strip()
            eastthree = data[0][24].strip()
            eastfour = data[0][36].strip()
            westone = data[1][0].strip()
            westtwo = data[1][12].strip()
            westthree = data[1][24].strip()
            westfour = data[1][36].strip()
            eastonerecord = data[0][1].strip() + "-" + data[0][2].strip() + "-" + data[0][3].strip()
            easttworecord = data[0][13].strip() + "-" + data[0][14].strip() + "-" + data[0][15].strip()
            eastthreerecord = data[0][25].strip() + "-" + data[0][26].strip() + "-" + data[0][27].strip()
            eastfourrecord = data[0][37].strip() + "-" + data[0][38].strip() + "-" + data[0][39].strip()
            westonerecord = data[1][1].strip() + "-" + data[1][2].strip() + "-" + data[1][3].strip()
            westtworecord = data[1][13].strip() + "-" + data[1][14].strip() + "-" + data[1][15].strip()
            westthreerecord = data[1][25].strip() + "-" + data[1][26].strip() + "-" + data[1][27].strip()
            westfourrecord = data[1][37].strip() + "-" + data[1][38].strip() + "-" + data[1][39].strip()

        embed = discord.Embed(title="DSFL Standings", description="", color=0x0080ff)
        embed.set_thumbnail(url="https://i.imgur.com/NBmz1lH.png")
        embed.add_field(name="SFC South", value="""{0} {1}
        {2} {3}
        {4} {5}
        {6} {7}""".format(eastone, eastonerecord, easttwo, easttworecord, eastthree, eastthreerecord, eastfour, eastfourrecord), inline=True)
        embed.add_field(name="NFC North", value="""{0} {1}
        {2} {3}
        {4} {5}
        {6} {7}""".format(westone, westonerecord, westtwo, westtworecord, westthree, westthreerecord, westfour, westfourrecord), inline=True)
        embed.set_footer(text="made by Nykonax#7723")
        await message.channel.send(embed=embed)

    else:
        return

client.run('token')