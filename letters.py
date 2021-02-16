months=['january','february','march','april','may','june','july','august','september','october','november','december']
weekdays=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
letters={}
for month in months:
    for each in month:
        if each not in letters.keys():
            letters[each]=0
        letters[each]+=1
for weekday in weekdays:
    for each in weekday:
        if each not in letters.keys():
            letters[each]=0
        letters[each]+=1
sum_of_letters=sum(letters.values())
print(len(months))
print('-'*20)
print(len(weekdays))
print('-'*20)
print(len(letters))
print('-'*20)
print(letters)
print('-'*20)
print(sum_of_letters)
