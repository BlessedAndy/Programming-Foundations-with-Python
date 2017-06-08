# '''
# Created on Aug 16, 2016
#  
# @author: Andy Zhang
# '''
#  
# import urllib2;  
# import urllib;  
# import sys;  
# import json;  
# import time;
# import binascii;  
# import copy;
# import ssl;
#  
# ssl._create_default_https_context = ssl._create_unverified_context
#  
# contact_prefab = {
#     "Id": "",
#     "IdOrigin": "",
#     "Timestamp": "",
#     "FirstName": "",
#     "LastName": "",
#     "TitleDescription": "",
#     "CompanyId": "",
#     "CompanyIdOrigin": "",
#     "CountryDescription": "",
#     "CustomerName": "",
#     "DepartmentDescription": "",
#     "City": "",
#     "Street": "",
#     "HouseNumber": "",
#     "IndustryDescription": "",
#     "IsConsumer": "",
#     "IsContact": "",
#     "LanguageDescription": "",
#     "Latitude": "",
#     "Longitude": "",
#     "MaritalStatusDescription": "",
#     "GenderDescription": "",
#     "SAPERPConsumerAccountId": "",
#     "SAPERPAccountId": "",
#     "SAPHybrisConsumerAccountId": "",
#     "FunctionDescription": "",
#     "EMailAddress": "",
#     "EMailOptIn": "",
#     "PhoneNumber": "",
#     "PhoneOptin": "",
#     "MobilePhoneNumber": "",
#     "MobilePhoneOptIn": "",
#     "MobileSMSOptIn": "",
#     "Obsolete": "",
#     "PostalCode": "",
#     "PostalOptin": "",
#     "RegionDescription": "",
#     "SAPCRMBusinessPartnerId": "",
#     "SAPCRMMarketingProspectId": "",
#     "DateOfBirth": "",
#     "TwitterId": "",
#     "TwitterOptIn": "",
#     "FacebookId": "",
#     "FacebookOptIn": "",
#     "FaxNumber": "",
#     "FaxOptIn": "",
#     "FullName": "",
#     "GooglePlusId": "",
#     "GooglePlusOptIn": "",
#     "SAPERPContactId": "",
#     "EMailAddress2": "",
#     "EMail2OptIn": "",
#     "EMailAddress3": "",
#     "EMail3OptIn": "",
#     "Boolean1": "",
#     "Boolean2": "",
#     "Boolean4": "",
#     "Time1": "",
#     "Date1": "",
#     "Date3": "",
#     "Number1": "",
#     "Number2": "",
#     "Number3": "",
#     "Text201": "",
#     "Text202": "",
#     "Text401": "",
#     "Text402": "",
#     "Text403": "",
#     "Text801": "",
#     "Text802": ""
# }
#  
#  
# payload_prefab = {
#     "Id": "",
#     "Timestamp": "",
#     "UserName": "USER",
#     "SourceSystemType": "EXT",
#     "SourceSystemId": "PYTHON",
#     "Contacts": []
# }
#  
# def intToCUANTimestamp(t):
#     return "/Date(" + str(t) + ")/";
#  
# # Extract all "set-cookie" headers from a given urllib2 response Info end create
# # a single String containing all those Cookies. This is done using a variety of
# # String operations. The Cookie String can later be send as a Cookie Header
# def extractCookies(info):
#     final_cookie = "";
#     cookie_list = info.getallmatchingheaders("set-cookie");
#     for i in range(0, len(cookie_list)):
#         cookie_str = cookie_list[i].split(": ", 1)[1];
#         final_cookie += cookie_str.split(";", 1)[0];
#         if i < (len(cookie_list) - 1):
#             final_cookie += "; ";
#     return final_cookie;
#  
# # Extract the value of the 'x-csrf-token' Header in the given urllib2 response Info
# def extractCSRFToken(info):
#     token_str = info.getfirstmatchingheader("x-csrf-token")[0];
#     return token_str.split(": ", 1)[1][:-2];
#  
# # Construct the Payload for the CUAN_IMPORT service
# replication_created_at = intToCUANTimestamp(int(time.time())); 
# payload = copy.deepcopy(payload_prefab);
# payload["Timestamp"] = replication_created_at;
# contact_ids = [];
#      
# contact_count = 0;
# #interaction_count = 0;
#  
#  
# print 'beging to load data...'
# collectionSize = Collection.Size()
# dataRecords = DataManager.NewDataRecord()
# terms = []
#  
#  
# for recNum in range(collectionSize, 0, -1):
#     Collection.GetRecord(dataRecords, recNum)
#     id = dataRecords.GetField(u'IN_ID')
#     idOrigin = dataRecords.GetField(u'IN_IDORIGIN')
#     timestamp = dataRecords.GetField(u'IN_TIMESTAMP')
#     firstName = dataRecords.GetField(u'IN_FIRSTNAME')
#     lastName = dataRecords.GetField(u'IN_LASTNAME')
#     titleDescription = dataRecords.GetField(u'IN_TITLEDESCRIPTION')
#     companyId = dataRecords.GetField(u'IN_COMPANYID')
#     companyIdOrigin = dataRecords.GetField(u'IN_COMPANYIDORIGIN')
#     countryDescription = dataRecords.GetField(u'IN_COUNTRYDESCRIPTION')
#     customerName = dataRecords.GetField(u'IN_CUSTOMERNAME')
#     departmentDescription = dataRecords.GetField(u'IN_DEPARTMENTDESCRIPTION')
#     city = dataRecords.GetField(u'IN_CITY')
#     street = dataRecords.GetField(u'IN_STREET')
#     houseNumber = dataRecords.GetField(u'IN_HOUSENUMBER')
#     industryDescription = dataRecords.GetField(u'IN_INDUSTRYDESCRIPTION')
#     if dataRecords.GetField(u'IN_ISCONSUMER') == "X":
#         isConsumer = True;
#     else : 
#         isConsumer = False; 
#     if dataRecords.GetField(u'IN_ISCONTACT') == "X":
#         isContact = True;
#     else : 
#         isContact = False; 
#     languageDescription = dataRecords.GetField(u'IN_LANGUAGEDESCRIPTION')
#     latitude = dataRecords.GetField(u'IN_LATITUDE')
#     longitude = dataRecords.GetField(u'IN_LONGITUDE')
#     maritalStatusDescription = dataRecords.GetField(u'IN_MARITALSTATUSDESCRIPTION')
#     genderDescription = dataRecords.GetField(u'IN_GENDERDESCRIPTION')
#     SAPERPConsumerAccountId = dataRecords.GetField(u'IN_SAPERPCONSUMERACCOUNTID')
#     SAPERPAccountId = dataRecords.GetField(u'IN_SAPERPACCOUNTID')
#     SAPHybrisConsumerAccountId = dataRecords.GetField(u'IN_SAPHYBRISCONSUMERACCOUNTID')
#     functionDescription = dataRecords.GetField(u'IN_FUNCTIONDESCRIPTION')
#     emailAddress = dataRecords.GetField(u'IN_EMAILADDRESS')
#     emailOptIn = dataRecords.GetField(u'IN_EMAILOPTIN')
#     phoneNumber = dataRecords.GetField(u'IN_PHONENUMBER')
#     phoneOptIn = dataRecords.GetField(u'IN_PHONEOPTIN')
#     mobilePhoneNumber = dataRecords.GetField(u'IN_MOBILEPHONENUMBER')
#     mobilePhoneOptIn = dataRecords.GetField(u'IN_MOBILEPHONEOPTIN')
#     mobileSMSOptIn = dataRecords.GetField(u'IN_MOBILESMSOPTIN')
#     if dataRecords.GetField(u'IN_OBSOLETE') == "X":
#         obsolete = True;
#     else : 
#         obsolete = False;
#     postalCode = dataRecords.GetField(u'IN_POSTALCODE')
#     postalOptIn = dataRecords.GetField(u'IN_POSTALOPTIN')
#     regionDescription = dataRecords.GetField(u'IN_REGIONDESCRIPTION')
#     SAPCRMBusinessPartnerId = dataRecords.GetField(u'IN_SAPCRMBUSINESSPARTNERID')
#     SAPCRMMarketingProspectId = dataRecords.GetField(u'IN_SAPCRMMARKETINGPROSPECTID')
#     dateOfBirth = dataRecords.GetField(u'IN_DATEOFBIRTH')
#     twitterId = dataRecords.GetField(u'IN_TWITTERID')
#     twitterOptIn = dataRecords.GetField(u'IN_TWITTEROPTIN')
#     facebookId = dataRecords.GetField(u'IN_FACEBOOKID')
#     facebookOptIn = dataRecords.GetField(u'IN_FACEBOOKOPTIN')
#     faxNumber = dataRecords.GetField(u'IN_FAXNUMBER')
#     faxOptIn = dataRecords.GetField(u'IN_FAXOPTIN')
#     fullName = dataRecords.GetField(u'IN_FULLNAME')
#     googlePlusId = dataRecords.GetField(u'IN_GOOGLEPLUSID')
#     googlePlusOptIn = dataRecords.GetField(u'IN_GOOGLEPLUSOPTIN')
#     SAPERPContactId = dataRecords.GetField(u'IN_SAPERPCONTACTID')
#     emailAddress2 = dataRecords.GetField(u'IN_EMAILADDRESS2')
#     email2OptIn = dataRecords.GetField(u'IN_EMAIL2OPTIN')
#     emailAddress3 = dataRecords.GetField(u'IN_EMAILADDRESS3')
#     email3OptIn = dataRecords.GetField(u'IN_EMAIL3OPTIN')
#     if dataRecords.GetField(u'IN_BOOLEAN1') in ("TRUE", "X"):
#         boolean1 = True;
#     else : 
#         boolean1 = False; 
#     if dataRecords.GetField(u'IN_BOOLEAN2') in ("TRUE", "X"):
#         boolean2 = True;
#     else : 
#         boolean2 = False; 
#     if dataRecords.GetField(u'IN_BOOLEAN4') in ("TRUE", "X"):
#         boolean4 = True;
#     else : 
#         boolean4 = False; 
#     time1 = dataRecords.GetField(u'IN_TIME1')
#     date1 = dataRecords.GetField(u'IN_DATE1')
#     date3 = dataRecords.GetField(u'IN_DATE3')
#     number1 = int(dataRecords.GetField(u'IN_NUMBER1'))
#     number2 = int(dataRecords.GetField(u'IN_NUMBER2'))
#     number3 = int(dataRecords.GetField(u'IN_NUMBER3'))
#     text201 = dataRecords.GetField(u'IN_TEXT201')
#     text202 = dataRecords.GetField(u'IN_TEXT202')
#     text401 = dataRecords.GetField(u'IN_TEXT401')
#     text402 = dataRecords.GetField(u'IN_TEXT402')
#     text403 = dataRecords.GetField(u'IN_TEXT403')
#     text801 = dataRecords.GetField(u'IN_TEXT801')
#     text802 = dataRecords.GetField(u'IN_TEXT802')
#     cuan_url = dataRecords.GetField(u'IN_ODATA_URL')
#     username = dataRecords.GetField(u'IN_ODATA_USERNAME')
#     password = dataRecords.GetField(u'IN_ODATA_PASSWORD')
#  
#  
#  
#     # Create a contact for every Tweet (only if it does not exist already) and add a facet
#     if not id in contact_ids:
#         contact_ids.append(id);
#         contact = copy.deepcopy(contact_prefab);
#         contact["Id"] = id;
#         contact["IdOrigin"] = idOrigin;
#         contact["Timestamp"] = '/Date(%s)/' % timestamp;
#         contact["FirstName"] = firstName;
#         contact["LastName"] = lastName;
#         contact["TitleDescription"] = titleDescription;
#         contact["CompanyId"] = companyId;
#         contact["CompanyIdOrigin"] = companyIdOrigin;
#         contact["CountryDescription"] = countryDescription;
#         contact["CustomerName"] = customerName;
#         contact["DepartmentDescription"] = departmentDescription;
#         contact["City"] = city;
#         contact["Street"] = street;
#         contact["HouseNumber"] = houseNumber;
#         contact["IndustryDescription"] = industryDescription;
#         contact["IsConsumer"] = isConsumer;
#         contact["IsContact"] = isContact;
#         contact["LanguageDescription"] = languageDescription;
#         contact["Latitude"] = latitude;
#         contact["Longitude"] = longitude;
#         contact["MaritalStatusDescription"] = maritalStatusDescription;
#         contact["GenderDescription"] = genderDescription;
#         contact["SAPERPConsumerAccountId"] = SAPERPConsumerAccountId;
#         contact["SAPERPAccountId"] = SAPERPAccountId;
#         contact["SAPHybrisConsumerAccountId"] = SAPHybrisConsumerAccountId;
#         contact["FunctionDescription"] = functionDescription;
#         contact["EMailAddress"] = emailAddress;
#         contact["EMailOptIn"] = emailOptIn;
#         contact["PhoneNumber"] = phoneNumber;
#         contact["PhoneOptin"] = phoneOptIn;
#         contact["MobilePhoneNumber"] = mobilePhoneNumber;
#         contact["MobilePhoneOptIn"] = mobilePhoneOptIn;
#         contact["MobileSMSOptIn"] = mobileSMSOptIn;
#         contact["Obsolete"] = obsolete;
#         contact["PostalCode"] = postalCode;
#         contact["PostalOptin"] = postalOptIn;
#         contact["RegionDescription"] = regionDescription;
#         contact["SAPCRMBusinessPartnerId"] = SAPCRMBusinessPartnerId;
#         contact["SAPCRMMarketingProspectId"] = SAPCRMMarketingProspectId;
#         contact["DateOfBirth"] = '/Date(%s)/' % dateOfBirth;
#         contact["TwitterId"] = twitterId;
#         contact["TwitterOptIn"] = twitterOptIn;
#         contact["FacebookId"] = facebookId;
#         contact["FacebookOptIn"] = facebookOptIn;
#         contact["FaxNumber"] = faxNumber;
#         contact["FaxOptIn"] = faxOptIn;
#         contact["FullName"] = fullName;
#         contact["GooglePlusId"] = googlePlusId;
#         contact["GooglePlusOptIn"] = googlePlusOptIn;
#         contact["SAPERPContactId"] = SAPERPContactId;
#         contact["EMailAddress2"] = emailAddress2;
#         contact["EMail2OptIn"] = email2OptIn;
#         contact["EMailAddress3"] = emailAddress3;
#         contact["EMail3OptIn"] = email3OptIn;
#         contact["Boolean1"] = boolean1;
#         contact["Boolean2"] = boolean2;
#         contact["Boolean4"] = boolean4;
#         contact["Time1"] = time1;
#         contact["Date1"] = '/Date(%s)/' % date1;
#         contact["Date3"] = '/Date(%s)/' % date3;
#         contact["Number1"] = number1;
#         contact["Number2"] = number2;
#         contact["Number3"] = number3;
#         contact["Text201"] = text201;
#         contact["Text202"] = text202;
#         contact["Text401"] = text401;
#         contact["Text402"] = text402;
#         contact["Text403"] = text403;
#         contact["Text801"] = text801;
#         contact["Text802"] = text802;
#         payload["Contacts"].append(contact);
#         contact_count = contact_count + 1;
#      
#     Collection.DeleteRecord(dataRecords)
#  
# DataManager.DeleteDataRecord(dataRecords)
#  
# # Convert the Payload to JSON
# json_payload = json.dumps(payload);
#  
# # Create HTTP Basic Auth Header
# cuan_user_creds = binascii.b2a_base64(username + ":" + password)[:-1];
# user_auth = "Basic %s" % cuan_user_creds;
#  
# # Fetch a CSRF Token and store the Cookies of the response (for later use)
# opener = urllib2.build_opener();
# opener.addheaders = [('x-csrf-token', "fetch"), ("Authorization", user_auth)];
# response = opener.open(cuan_url);
# csrf_token = extractCSRFToken(response.info());
# cookies = extractCookies(response.info());
#  
# # Create a POST request and execute it. The Request will contain the payload,
# # the previously fetched CSRF Token and the Cookies
# opener.addheaders = [('x-csrf-token', csrf_token), ("Authorization", user_auth), ("Cookie", cookies)];
# import_headers_url = cuan_url + ("/" if cuan_url[-1] != "/" else "") + "ImportHeaders";
# data = json.dumps(payload);
# req = urllib2.Request(import_headers_url, data, headers = {
#     "Content-Type": "application/json",
#     "Content-Length": len(data)
# });
# response = None;
# try:
#     response = opener.open(req);
# except urllib2.HTTPError as e:
#     # Something went wrong. Display information to the user and exit
#     error_message = e.read()
#     print "An Error occurred:";
#     print error_message;
#     sys.exit(error_message);
#  
# # Success
# print "%d Contact(s) created or updated" % contact_count;
# #print "%d Interaction(s) created or updated" % interaction_count;
#  
#  
# print 'total %d records to load.'%(collectionSize)
#  
# newRecord = DataManager.NewDataRecord(1)
# newRecord.SetField(u'OUT_RESPONSE', unicode(response))
# Collection.AddRecord(newRecord)
# del newRecord
#      
# print 'done'
#      

