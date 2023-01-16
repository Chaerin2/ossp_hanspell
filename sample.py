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



------------------------------------------

fp = open('1.txt','r',encoding='cp949')
text = fp.read()
fp.close()

ready_list=[]


if (len(text)<500)):
  ready_list.append(text)

while (len(text)>500):
    temp_str = text[:500]
    last_space = temp_str.rfind(' ')
    temp_str = text[0 : last_space]
    ready_list.append(temp_str)
    ready_list.append('\n')
    
    text = text[last_space:]
ready_list.apeend(text)


new_text = ""
for ready in ready_list:
  spelled_sent = spell_checker.check(ready)
  checked_sent = spelled_sent.checked
  
  f = open("result.txt",'w',encoding='utf8')
  f.write(checked_sent)
  f.close()
