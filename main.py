import os, re

path = os.getcwd()

files = os.listdir(path)
fileListRaw = []
fullNames = []
extensions = []

title = raw_input("Title:")
season = input("Season:")
if len(str(season)) < 2:
    season = "0" + str(season)
print ("This script assumes this layout: Title, Episode")
print ("All text before the title and after the episode number will be discarded")
print ("")

for f in files:
    if title in f:
        fileListRaw.append(f)
        extensions.append(f[-4:])

print("Files found with specified title:")
for s in fileListRaw:
    print (s)

#Give user option to quit

for f in fileListRaw:
    cut = (re.sub("[\(\[].*?[\)\]]", "", f)).strip()
    l = len(cut)
    cut = (cut[:l-4]).strip()
    last2 = cut[-2:]
    if 'v' in last2.lower():
        l = len(cut)
        cut = (cut[:l - 2]).strip()

    print (cut)

    num = cut[-2:]
    print (num)
    if num.isdigit():
        #print ("episode is 2 digits")
        episode = num
    else:
        num = cut[-1:]

        if num.isdigit():
            #print ("episode is 1 digit")
            episode = "0"+str(num)
        else:
            print("Episode number not found on one or more files.")
            os.exit()

    fullNames.append(title + " " + "S" + str(season) + "E" + str(episode))


final = [i+j for i, j in zip(fullNames, extensions)]

print ("Files Renamed to:")
for n in final:
    print (n)

print
renameBool = raw_input("Commit rename? (y/n):")
if renameBool.lower() == "y":
    #rename files
    numFiles = len(final)
    for n in range(0,numFiles):
        os.rename(fileListRaw[n], final[n])
    print ("Operation completed!")
else:
    print ("Rename aborted")