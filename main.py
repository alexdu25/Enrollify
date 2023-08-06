import requests
import re
import sys
from bs4 import BeautifulSoup

spotsleft = []
enrolled = []
weekdays = []
discussionspace = {}
discussiontime = {}

def getclassdata(id):
    global spotsleft, enrolled, weekdays
    classid = ''
    for i in id:
        if i == '_': break
        classid += i
    classid = int(classid)
    url = "https://sa.ucla.edu/ro/public/soc/Results?t=23W&sBy=classidnumber&id="+str(classid)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        div = soup.find('div', {'id': id+'-status_data'})
        if div:
            p = div.find('p')
            for i in p:
                mylist = str(i).split()
                if "Spots" in mylist:
                    spotsleft = mylist
                if "Enrolled" in mylist:
                    enrolled = mylist
        else:
            print('class does not exist')
            exit(1)
        div = soup.find('div', {'id': id+'-days_data'})
        if div:
            p = div.find('p')
            for i in p:
                pattern = r'data-content="[^"]+">([A-Z]+)'
                match = re.search(pattern, str(i))
                if match:
                    weekdays = match.group(0)
                    weekdays = weekdays[13:]

                else: print('no match')
        else:
            print("could not find div")
        
    else:
        print("Request failed with status code:", response.status_code)

def getdiscussiondata(id):
    global discussionspace,discussiontime
    classid = ''
    for i in id:
        if i == '_': break
        classid += i
    classid = int(classid)
    url = "https://sa.ucla.edu/ro/public/soc/Results?t=23W&sBy=classidnumber&id="+str(classid)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for i in range(1,10):
            sym = 'Dis 1' + chr(64+i) + ' = ' + str(classid+i)
            discussionid = str(classid+i)+'_'+id+'-status_data'
            div = soup.find('div', {'id': discussionid})
            if div:
                p = div.find('p')
                cont = False
                for j in p:
                    mylist = str(j).split()
                    if 'Closed' in mylist:
                        cont = True
                        break
                if cont: continue
                for j in p:
                    mylist = str(j).split()
                    if "Enrolled" in mylist:
                        discussionspace[sym] = mylist[0] + ' ' + mylist[1] + ' ' + mylist[2] + ' ' + mylist[3]

                div = soup.find('div', {'id': id+'-days_data'})
                p = div.find('p')
                for j in p:
                    pattern = r'data-content="[^"]+">([A-Z]+)'
                    match = re.search(pattern, str(j))
                    if match:
                        weekdays = match.group(0)
                        weekdays = weekdays[13:]
                        discussiontime[sym] = weekdays
                    else: print('no match')
            else:
                break

def main():
    if len(sys.argv) != 2:
        print("please enter class id; use '0' to default to CS151B class ID")
        exit(1)
    if sys.argv[1] == '0': id = "187650200_COMSCI0151BM"
    else: id = sys.argv[1]
    pattern = r'^\d{9}_[A-Z0-9]*$'
    if not re.match(pattern,id): 
        print('not a valid class id')
        exit(1)
    getclassdata(id)
    getdiscussiondata(id)
    print(enrolled)
    print(spotsleft)
    print(weekdays)
    print()
    print(discussionspace)
    print(discussiontime)

if __name__ == "__main__":
    main()
