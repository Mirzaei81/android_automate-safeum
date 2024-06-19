import uiautomator2 as u2
from uiautomator2.exceptions import UiObjectNotFoundError
from typing import Dict

file :str = open("./user_pass.txt","r").read()
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.safeum.android',
    appActivity='.Settings',
    language='en',
    locale='US'
)
user_date:Dict[str,str]={}
user_pass=file.split()
MySafe_nums = []
d  =u2.connect("6716ff19")
d.app_start("com.safeum.android")
attempt=3
for up in user_pass:
    user_date[up.split(":")[0]] = up.split(":")[-1]
print("starting\n"+"_"*20)
for u,p in user_date.items():
    d(className='android.widget.EditText',packageName="com.safeum.android").set_text(u)
    d(text='Password ').set_text(p)
    d(text="CHECK ").click(1)
    d(text="Settings").wait(True,20)
    d(text="Settings").click()
    try:
        d(text="My SafeNUM: ").exists(timeout=2)
        safe_num_txt:str = d(resourceId="com.safeum.android:id/account_number_safenum").get_text(1)
        print(safe_num_txt.replace(" ","").replace("\t",""))
        MySafe_nums.append(safe_num_txt.replace(" ","").replace("\t",""))
        attempts=0
        clicked=False
        while attempts<=attempt:
            try:
                if not clicked:
                    d(resourceId="com.safeum.android:id/activity_main_ll_accounttab").wait(1)
                    d(resourceId="com.safeum.android:id/activity_main_ll_accounttab").click(0) 
                    clicked=True
                d(resourceId=" com.safeum.android:id/activity_main_multi_ll").wait(1)
                d(resourceId="com.safeum.android:id/activity_main_multi_ll").click(0) 
                break
            except:
                d(resourceId="com.safeum.android:id/activity_main_ll_accounttab").click(2) 
                attempt+=1

        d(resourceId="com.safeum.android:id/account_manager_listitem_btn_logof").click()
        d(text="EXIT").click()
    except UiObjectNotFoundError as e:
        print(MySafe_nums)
        print(MySafe_nums.__len__())
        print(e)
        break
print("_"*10+"\nend") 
with open("res.txt","w",encoding="utf-8") as f:
    f.write("\n".join(MySafe_nums))


