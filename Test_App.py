import gspread
sa = gspread.service_account(filename="credentialsfile.json")
sh = sa.open("Tracks (after spring) (Responses)")
wks = sh.worksheet("Form Responses 1")
array = wks.get('A1:A90')
x = input("Please Enter Your GPA: ")
count = 0
while len(x) != 4:
    if len(x)==1:
        x = x + '.'
    else:
        x = x+'0'
    count += 1
count = 0
check = False
for i in array:
    if array[count][0] == x:
        check = True
        if count%10 == 1:
            print(f'Congratulations you are the {count}st!')
        elif count%10 == 2:
            print(f'Congratulations you are the {count}nd!')
        elif count%10 == 3:
            print(f'Congratulations you are the {count}rd!')
        else:
            print(f'Congratulations you are the {count}th!')
        break;
    count += 1
if check == False:
    print("Please Fill the Form and Try Again")