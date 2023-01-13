from hanspell import spell_checker

f = open('1.txt','r',encoding='utf-8')
text = f.readlines()
f.close()

new_txt = []

for i in text:
  new_txt.append(i.replace('\n',""))
  str_txt=""
for i in new_txt:
  str_txt = str_txt +i +""
  
for i in range(0,50):
  globals()['sent{}'.format(i)] = str_txt[500*i:500*i+499]
  
 spelled_sent = spell_checker.check(globals()['sent'{}.format(i)])
 checked_Sent = spelled_sent.checked
  
 f = open('result.txt','a+',encoding = 'utf-8')
 f.write(checked_sent)
 f.close()
