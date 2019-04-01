import gspread
from oauth2client.service_account import ServiceAccountCredentials
from jira import JIRA


scope = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/spreadsheets' ]

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

client = gspread.authorize(credentials)

sheet = client.open('test').sheet1

row = sheet.row_count + 1

for i in range(row - 10, row):
    data = sheet.row_values(i)
    try:
      if str(data[10]) == 'x':
          continue
    except IndexError:
      cell_list = sheet.range('K1:'+'K'+str(row))
      for cell in cell_list:
          cell.value = 'x'
      sheet.update_cells(cell_list)
      sheet.delete_row(sheet.row_count + 1)
      new_data = [['New Employee Name: ', str(data[2])],
                  [],
                  ['New Employee Start: ', str(data[3])],
                  [],
                  ['================================================================================'],
                  ['Which laptop should we have ready?: ', str(data[5])],
                  [],
                  ['If Lenovo selected; Windows or Linux: ', str(data[6])],
                  [],
                  ['Will a desktop tower be needed?: ', str(data[7])],
                  ['================================================================================'],
                  [],
                  ['Anything else to consider? ie. software licenses that IT manages.: ', str(data[9])],
                  [],
                  ['Manager: ', str(data[1])],
                  [],
                  ['Department: ', str(data[8])],
                  [],
                  ['Which email group(s) should new hire be added to?: ', str(data[4])]]
      print('\n'.join(' '.join(sub) for sub in new_data))



# AUTH WILL CHANGE WHEN I GENERATE API TOKEN
# options = {
#     'server': 'http://ithelp.zee.aero:8080',}
# jira = JIRA(options)
# username = input("What is your JIRA Username")
# password = input("What is your JIRA Password")
# 
# 
# jira = JIRA(auth=(username, password), options={'server':'http://ithelp.zee.aero:8080'})
# 
# new_issue = jira.create_issue(project='ITS', summary='Onboarding: Start Date - '+str(data[3])+' Name - '+str(data[2])+' Device - '+str(data[5])+'', labels=['New_Hire_System'],
#                               description='\n'.join(' '.join(sub) for sub in new_data), issuetype={'name': 'Service Request'})




