import re, csv
def wordcount(file_name):
  quantity=input('Введите кол-во слов, в случае буквенного значения так будет назван csv файл')
  if quantity=='':
    quantity=100
  filee=quantity
  words={}
  string=''
  lst=[]
  with open(file_name) as txt:
    x={}
    line=(txt.read()).lower()
    line=re.sub('\n|[,;!?]', ' ', line)
    keys=(re.split(' ', line))
    words={word:(line).count(word) for word in keys}
    words_sort=sorted(words,key=words.get, reverse=True)
    try:
      quantity=int(quantity)
      for w in words_sort:
        lst.append(w)
        if len(lst)==quantity:
          break
      for w in lst:
        print(w, words[w])
    except ValueError:
      names=['слово','частота']
      table=[]
      for w in words_sort:
        lst.append({names[0]:w,names[1]:words[w]})
      with open(filee+'.csv', 'w+') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames = names)
        writer.writeheader()
        writer.writerows(lst)
        
def wordstat(*names):
    with open('text.csv','w')as csvfile:
        writer=csv.writer(csvfile, delimiter=',')
        for name in names:
            try:
                csvfile=open(name,'r')
                assert name[-4::]=='.csv'
            except AssertionError:
                print('файл',name,'не .csv')
                return
            except FileNotFoundError:
                print('файл',name,'не найден')
                return
            with open(name,'r') as file2:
              reader2=csv.reader(file2, delimiter=',')
              for row in reader2:
                writer.writerow(row)
    with open('text.csv','r') as filee:
     dic={}
     reader2=csv.reader(filee, delimiter=',')
     for key, value in reader2:
      if value=='частота':
        pass
      elif key not in dic:
        dic[key]=int(value)
      else:
        dic[key]+=int(value)
    x=0
    while x==0:
      result=input('Введите имя файла для результата')
      if '.csv' not in result:
        print('Неверный формат файла, необходим файл csv')
      else:
        x=1
    with open(result,'w+') as csvfile:
      writer=csv.writer(csvfile, delimiter=',')
      writer.writerow(['Слово','Частота'])
      for k, v in dic.items():
        writer.writerow([k,v])
      print('Ваш файл -',result)
