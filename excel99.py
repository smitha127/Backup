import pandas as pd
import xlsxwriter

def updated(self,carddata):
    df = pd.DataFrame({'consessionnum':carddata ["customId_ConsessionNo"],})
    writer = pd.ExcelWriter('C:\\Users\\1023816\\PycharmProjects\\rabbit\\utilites\\writeexcel.xlsx',
                            engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet1')

    writer.save()



