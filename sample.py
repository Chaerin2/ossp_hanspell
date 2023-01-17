from hanspell import spell_checker

# 문자열 한줄씩 읽어서 리스트에 저장 
fp = open('1.txt','r',encoding='cp949')
text = fp.readlines()
fp.close()

num = len(text)

spelled_sent = spell_checker.check(text)

for i in range(0,num):
  checked_sent = spelled_sent[i].checked
  
  f = open("result.txt",'a',encoding='utf8')
  f.write(checked_sent)
  f.write('\n')
  f.close()
