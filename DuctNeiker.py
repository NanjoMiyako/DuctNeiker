import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

import sys

def loadMailGroupInfo(path):

    with open(path) as f:
        l_strip = [s.strip() for s in f.readlines()]
        
        MailGroupId = l_strip[0].split(',')[1]
        MailTypeId = l_strip[1].split(',')[1]
        MailTypeName = l_strip[2].split(',')[1]
        SenderAddress = l_strip[3].split(',')[1]
        
        ToAddress = l_strip[4].split(',')
        ToAddress.pop(0)
        
        MailAppPassWord = l_strip[5].split(',')[1]
        
        return MailGroupId,MailTypeId,MailTypeName,SenderAddress,ToAddress,MailAppPassWord


def makeBodyText(comment, MailTypeName, MatchCount, ToleiningPosition, ExecutionDate, StartTime, NeikerFlg):

    string1 = "メールタイプ:" + MailTypeName +"\r\n"
    string1 += "以下の内容で一緒にジムトレーニング参加してくれる人を募集します\r\n"
    string1 += "募集人数:" + MatchCount + "人\r\n"
    string1 += "場所:" + ToleiningPosition + "\r\n"
    string1 += "活動日時:" + ExecutionDate + "\r\n"
    string1 += "開始時刻:" + StartTime + "\r\n"
    
    if NeikerFlg == True:
        string1 += "参加費は開催者側負担です\r\n"
    else:
        string1 += "参加費は参加者負担です\r\n"
        
    string1 += "参加希望者は当メールに返信お願いします\r\n"
    
    string1 += "コメント:" + comment + "\r\n"
    
    return string1


print("---DuctNeiker---")
while True:
    MailGroupFilePath = input("メールグループファイルURLを入力:")
    print("グループファイルパス:", MailGroupFilePath)
    
    string2 = input("-1を入力で決定:")
    if string2 == '-1':
        break

while True:
    titleLabel = input("メールタイトルラベルを入力:")
    print("タイトルラベル:", titleLabel)
    
    string2 = input("-1を入力で決定:")
    if string2 == '-1':
        break
        
while True:
    ExecutionDate = input("活動日時を入力:")
    print("活動日時:", ExecutionDate)
    
    string2 = input("-1を入力で決定:")
    if string2 == '-1':
        break
        
while True:
    StartTime = input("開始時刻を入力:")
    print("開始時刻:", StartTime)
    
    string2 = input("-1を入力で決定:")
    if string2 == '-1':
        break

while True:
    MatchCount = input("募集人数を入力:")
    print("募集人数:", MatchCount)
    
    string2 = input("-1を入力で決定:")
    if string2 == '-1':
        break

NeikerFlg = True        
while True:

    print("参加費用の負担者はメール送信者ですか?(y/n):" )
    NeikerStr = input("")
    
    if NeikerStr == 'y':
        NeikerFlg = True
        print("参加費負担:開催者")
    else:
        NeikerFlg = False
        print("参加費負担:参加者")
    
    string2 = input("-1を入力で決定:")
    if string2 == '-1':
        break

ToleiningPosition = ''        
while True:
    ToleiningPosition = input("トレーニング場所を入力:")
    print("場所:", ToleiningPosition)
    
            
    string3 = input("-1を入力で決定:")
    if string3 == '-1':
        break
            

while True:
    comment = input("コメントを入力:")
    
    string2 = input("-1を入力で決定:")
    if string2 == '-1':
        break            

MailGroupId, MailTypeId, MailTypeName, SenderAddress, ToAddressList, MailAppPassWord = loadMailGroupInfo(MailGroupFilePath)

# メール作成
bodyText = makeBodyText(comment, MailTypeName, MatchCount, ToleiningPosition, ExecutionDate, StartTime, NeikerFlg)

print("以下の内容でメールを送ります:")
print("メールグループID:", MailGroupId)
print("メールタイプID:", MailTypeId)
print("送信元アドレス:", SenderAddress)
print("送信先アドレス:", ToAddressList)
print("コメント:",comment)

string3 = input("以上の内容でメールを送信しますか(y/n):")
if string3 != 'y':
        print("送信をキャンセルしました")
        sys.exit()

subject = "DuctNeiker-MailGroup-" + MailGroupId + "-MailType-" + MailTypeId + "-Label-" + titleLabel

# SMTPサーバに接続
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.starttls()
smtpobj.login(SenderAddress, MailAppPassWord)



for toAddress in ToAddressList:
    # 作成したメールを送信
    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = SenderAddress
    msg['Date'] = formatdate()
    msg['To'] = toAddress
    smtpobj.send_message(msg)

print("メール送信しました")

smtpobj.close()



