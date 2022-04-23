from datetime import date
d1=date.today()
ds=str(d1)
print('системная дата ',ds)
lst=ds.split('-')
lst.reverse()
rusdate='/'.join(lst)
print('Российский стандарт',rusdate)