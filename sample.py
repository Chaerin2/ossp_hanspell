from hanspell import spell_checker

fp = open('1.txt','r',encoding='cp949')
text = fp.readlines()
txt = fp.read()
fp.close()

ready_list=[]


if (len(text)<500):
  for i in len(text):
        ready_list.append(text[i])

else:
  while (len(text)>500):
    for i in len(text):
      ready_list.append(text[i])
      
#    temp_str = text[:500]
#    last_space = temp_str.rfind(' ')
#    temp_str = text[0 : last_space]
#    ready_list.append(temp_str)    
#    text = text[last_space:]
#ready_list.append(text)

for ready in ready_list:
  spelled_sent = spell_checker.check(ready)
  checked_sent = spelled_sent.checked
  
  f = open("result.txt",'a+',encoding='utf8')
  f.write(checked_sent)
  f.close()
