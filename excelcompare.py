import pandas as pd
import json
class excelcompare:
    def extractvalues(self):
        df = pd.ExcelFile('C:\\Users\\1023816\\PycharmProjects\\rabbit\\practicing\\ExcelTrack.xlsx').parse(
            'Sheet1')
        # you could add index_col=0 if there's an index

        x = []
        x.append(df['consessionnum'])
        print(x)
        conNo = x[0].values
        return conNo

    def insertValues(self, carddata):
        mok=json.dumps(carddata._dict_)
        df = pd.DataFrame(mok)
        writer = pd.ExcelWriter('C:\\Users\\1023816\\PycharmProjects\\rabbit\\practicing\\ExcelTrack.xlsx',
                                engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        value = writer.save()
        return value










