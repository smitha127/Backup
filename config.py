from practicing import Scrapy
from practicing import settingvalues
from practicing import excelcompare
from practicing import consumer
class config:
 s = Scrapy()
 carddata = s.card_details_data()
 excel=excelcompare()
 conNo=excel.extractvalues()
 for i in conNo:
  if (carddata['customId_ConsessionNo']!=i):
   dt=settingvalues()
   dataobject=dt.dataobjectcreation(carddata)
   c=consumer()
   reciver=c.consumed(carddata)















