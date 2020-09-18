#!/usr/bin/env python
# coding: utf-8

# Loader_to_sharepoint.py
#
#

from pathlib import Path
import os.path
import requests,json,urllib
import pandas as pd
import collections
from collections import defaultdict
import xmltodict
import getpass
from shareplum import Office365
from shareplum.site import Version
from shareplum import Site
from requests_ntlm import HttpNtlmAuth
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.message import EmailMessage
import pprint


# print("\nEnter Your MS ID: ")
MSID = input("\nEnter Your MS ID: ")
# print("\nEnter MS Password: ")
MSID_password = getpass.getpass("\nEnter MS Password: ")


url1="http://server.com/sites/Lists/MIA%20Testing/AllItems.aspx"
url2="http://server.com/sites/Lists/MIS%20MIA%20testing/AllItems.aspx"
head={'Accept': "application/json",'content-type': "application/json;odata=verbose", "X-HTTP-Method": "MERGE"}
# headers = {'Accept': "application/json",'content-type': "application/json;odata=verbose", 'X-RequestDigest': form_digest, "X-HTTP-Method": "MERGE"}
# "X-RequestDigest": digest_value}
##"DOMAIN\username",password 

cred=HttpNtlmAuth(MSID, MSID_password)
#cred=HttpNtlmAuth("jsmith", "")


def decom_load():

    # authcookie = Office365('https://jsmith.sharepoint.com/teams/project_name', username='jsmith@smith.com',
    # password='').GetCookies()
    # site365 = Site('https://company.sharepoint.com', version=Version.v2016, authcookie=authcookie)
    
    # site365 = Site('https://company.sharepoint.com/teams/project', version=Version.v2016, authcookie=authcookie)
    # site.AddList('decommission apps', description='Great List!', template_id='Custom List')
        
#    try:

        site = Site('http://server.com/sites/project', auth=cred)
        sp_list = site.List("project apps")
        sp_data = sp_list.GetListItems('All Items')

        with open('Output2.json', 'rb') as file1:
            decom=json.load(file1)
            all_decom=decom["decommRequests"]
            
            update_data = []
            pc_error_data = []
            #cr="\n"

            for decom_row in all_decom:     # Getting each row data from the API file DecomOutput2.json

                decom_col=decom_row["Global ID"]   # get the ID only
                fields = ['ID','Global ID']
                query = {'Where': [('Eq', 'Global ID', decom_col)]}  # query amd fetch matching rows in the ED SHarepoint DB
                spt_data = sp_list.GetListItems(fields=fields, query=query) # store matching records in SHAREPOINT
                pd_data=""

                pd_all_decom=pd.DataFrame(all_decom)
                pd_data=pd.DataFrame(spt_data)  ####.  DATAFRAME OF MATCHING SHAREPOINT ###
                
                for SP_id in spt_data:  #  SHAREPOINT ID matched
                        
                    if SP_id['Global ID'] == decom_row["Global ID"]:
                                
                        decom_row.update({"ID": SP_id['ID']})
                        update_data.append(decom_row)
                        sp_list.UpdateListItems(data=update_data, kind='Update')
                        print("updating:", SP_id['Global ID'])


                if decom_row not in update_data:
                    print(decom_row)
                    new_records = []
                    new_records.append(decom_row)

                    #sp_list.UpdateListItems(data=new_records, kind='New')                
	
                    try:

                        sp_list.UpdateListItems(data=new_records, kind='New')
				
                    except KeyError as e:

                        #PC_user=(decom_row["Primary Contact"])
                        pc_error_data.append(decom_row)
                        # pc_error_data.append(e.args)
                        #print(PC_user)	
                        print(e.args)
                        #emailer(PC_user)
                        Path('/tmp/ifr.txt').touch()
                    
            #emailer(pc_error_data)
            if os.path.isfile('/tmp/ifr.txt'):
                print ("Incorrect records emailed")
                emailer(pc_error_data)
                os.remove("/tmp/ifr.txt")
            else:
                print ("No errors")
			

    #except:     #except OSError as e:
                    #print(e)
        # print(PC_user)           
        #PC_user=decom_row["Primary Contact"]        
        #print(PC_user)
        #emailer(PC_user)

        # PC_user=decom_row["Primary Contact"]

def decom_update():

    site = Site('http://server.com/sites/project', auth=cred)
    sp_list = site.List("decommission apps")
    id_var=input("Enter the global ID")
    fields = ['ID', 'Global ID']
    query = {'Where': [('Eq', 'Global ID', out)]}
    sp_data = sp_list.GetListItems(fields=fields, query=query)
    print(sp_data)
 
    for i in sp_data:
        print(i['ID'])

        var1=i['ID']
        print(var1)
        var2='"ID":"'
        print(var2)
        var3='"'
        print(var3)
        row = var2 + var1 + var3
        print(row)

def emailer(pc_error_data):


    print("starting email")
    msg = MIMEMultipart()
    sender = "jsmith@smith.com"
    recipients = "jsmith@smtih.com"

    server=smtplib.SMTP('mailo2.server.com')
    msg['Subject']=f'project loading issues'
    msg['From']=sender
    msg['To']=recipients
    #form_ped=print(str(pc_error_data).strip('[]'))
    #print(form_ped)

    #pprint.pc_error_data

    # Create the body of the message (a plain-text and an HTML version).
    text =(f"Hi {MSID}, "
            +"\n========================\n"
            +f"loading issues encountered.\n"
            +f"\n please investigate any issues.\n"
            +f"\nWe found no record for the users ..\n"
            +f"\n{pc_error_data}\n"
            +f"\n in Sharepoint.\n"
            +f"So most likely updates are required.")
            
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)
    server.sendmail(sender, recipients.split(","), msg.as_string())
    server.quit()

    print("completing email")

if __name__ == '__main__':   
    decom_load()

