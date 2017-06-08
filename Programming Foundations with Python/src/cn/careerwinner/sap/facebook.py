'''
Created on Oct 13, 2016

@author: Andy Zhang
'''

from datetime import datetime, timedelta, tzinfo
import json
import locale
import re
import sys
import time
import urllib

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint, entitydefs
import urllib2


# ISO8601 TIME
__all__ = ["parse_date", "ParseError"]

# Adapted from http://delete.me.uk/2005/03/iso8601.html
ISO8601_REGEX = re.compile(r"(?P<year>[0-9]{4})(-(?P<month>[0-9]{1,2})(-(?P<day>[0-9]{1,2})"
                           r"((?P<separator>.)(?P<hour>[0-9]{2}):(?P<minute>[0-9]{2})(:(?P<second>[0-9]{2})(\.(?P<fraction>[0-9]+))?)?"
                           r"(?P<timezone>Z|(([-+])([0-9]{2}):([0-9]{2})))?)?)?)?")

TIMEZONE_REGEX = re.compile("(?P<prefix>[+-])(?P<hours>[0-9]{2}).(?P<minutes>[0-9]{2})")


class ParseError(Exception):
    """Raised when there is a problem parsing a date string"""

# Yoinked from python docs
ZERO = timedelta(0)


class Utc(tzinfo):
    """
    UTC
    """

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


UTC = Utc()


class FixedOffset(tzinfo):
    """
    Fixed offset in hours and minutes from UTC
    """

    def __init__(self, offset_hours, offset_minutes, name):
        self.__offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        self.__name = name

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return ZERO

    def __repr__(self):
        return "<FixedOffset %r>" % self.__name


def parse_timezone(tzstring, default_timezone=UTC):
    """Parses ISO 8601 time zone specs into tzinfo offsets

    """
    if tzstring == "Z":
        return default_timezone
        # This isn't strictly correct, but it's common to encounter dates without
    # timezones so I'll assume the default (which defaults to UTC).
    # Addresses issue 4.
    if tzstring is None:
        return default_timezone
    m = TIMEZONE_REGEX.match(tzstring)
    prefix, hours, minutes = m.groups()
    hours, minutes = int(hours), int(minutes)
    if prefix == "-":
        hours = -hours
        minutes = -minutes
    return FixedOffset(hours, minutes, tzstring)


def parse_date(datestring, default_timezone=UTC):
    """Parses ISO 8601 dates into datetime objects

    The timezone is parsed from the date string. However it is quite common to
    have dates without a timezone (not strictly correct). In this case the
    default timezone specified in default_timezone is used. This is UTC by
    default.
    """
    if not isinstance(datestring, basestring):
        raise ParseError("Expecting a string %r" % datestring)
    m = ISO8601_REGEX.match(datestring)
    if not m:
        raise ParseError("Unable to parse date string %r" % datestring)
    groups = m.groupdict()
    tz = parse_timezone(groups["timezone"], default_timezone=default_timezone)
    if groups["fraction"] is None:
        groups["fraction"] = 0
    else:
        groups["fraction"] = int(float("0.%s" % groups["fraction"]) * 1e6)
    return datetime(int(groups["year"]), int(groups["month"]), int(groups["day"]),
                    int(groups["hour"]), int(groups["minute"]), int(groups["second"]),
                    int(groups["fraction"]), tz)

# END ISO8601 TIME


class FacebookHtmlParse(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.result = []

    def handle_data(self, data):
        self.result.append(data)

    def handle_charref(self, name):
        try:
            self.result.append(unichr(name2codepoint[name]))
        except KeyError:
            self.result.append(name)

    def handle_entityref(self, name):
        if name in entitydefs:
            self.handle_data(entitydefs[name])
        else:
            self.handle_data('&' + name)

    def get_str(self):
        return "".join(self.result)


def strip_tags(html):
    """
    Strip html tags.
    """
    html = html.strip()
    html = html.strip("\n")

    parse = FacebookHtmlParse()
    parse.feed(html)
    data = parse.get_str()
    parse.close()
    return data


class NestedObj(dict):
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

    def SetField(self, attr, value):
        self[attr] = value


class SearchError(StandardError):
    def __init__(self, error):
        self.error = error
        StandardError.__init__(self, error)


def getData(url, proxy, queryString, method=0, **queryParams):
    """
    Send an http or https request and expect to return a json object if no error.
    """

    handler = urllib2.BaseHandler()
    # Determine if the request must use a proxy
    if proxy is not None and proxy != '':
        print 'Using proxy: ' + str(proxy)
        handler = urllib2.ProxyHandler({'http': proxy, 'https': proxy})


    params = urllib.urlencode(queryParams)
    http_body = None if method == 0 else params

    if queryString is None:
        params = urllib.urlencode(queryParams)
        http_url = '%s?%s' % (url, params) if method == 0 else url
    else:
        http_url = queryString
    print 'Searching:', http_url

    try:
        opener = urllib2.build_opener(handler)
        data = opener.open(http_url, data=http_body).read()
        # print data
        try:
            result = json.loads(data)
        except ValueError:
            print 'Value Error'
            return None
        return result
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Failed to reach the %s server due to %s .' % (http_url, str(e.reason))
        elif hasattr(e, 'code'):
            print 'The server could not fulfill the request due to %s.' % str(e.code)
        return None


class FacebookCollector(object):
    """
    The collector for Facebook.
    """

    def __init__(self, request_url, proxy, access_token, limit, max_page, max_id, client, language, channel, term, fields):
        self.access_token = access_token
        self.request_url = request_url
        self.proxy = proxy
        self.limit = limit
        self.max_page = max_page
        self.max_id = max_id
        self.since_time = 0 if max_id == '' else long(max_id)
        self.client = client
        self.language = language
        self.channel = channel
        self.term = term
        self.fields = fields

    def search(self):
        facebooks = 0
        next_page = None
        current_page = 1
        max_id = self.since_time
        
        if self.language == 'en':
            local_language = 'en_US'
        elif self.language == 'de':
            local_language = 'de_DE'
        elif self.language == 'fr':
            local_language = 'fr_FR'
        elif self.language == 'es':
            local_language = 'es_ES'
        elif self.language == 'zh':
            local_language = 'zh_CN'
        else:
            local_language = 'en_US'


        params = {'limit': self.limit, 'locale': local_language, 'access_token': self.access_token, 'fields': self.fields}
        if self.since_time != 0:
            params['since'] = self.since_time

        try:
            while True:
                result = getData(self.request_url, self.proxy, next_page, **params)
                if result is None:
                    result = {}

                if 'data' not in result:
                    break

                if 'paging' not in result:
                    next_page = None
                else:
                    next_page = result[u'paging'][u'next']
                    if current_page == 1:
                        max_id = long(result[u'paging'][u'previous'].split('since=')[1][:10])

                print 'next_page:', next_page

                search_results = result['data']

                # print 'Extracting %d facebooks for the <%s> search term.' % (len(search_results), self.term)

                # facebook information
                for innerIndex in (range(len(search_results))):
                    sResult = search_results[innerIndex]

                    # validate since time
                    createdTime = sResult[u'created_time']
                    dt = parse_date(createdTime)
                    created_at = dt.strftime("%a, %d %b %Y %H:%M:%S +0000")
                    
                    timestamp = long(time.mktime(dt.timetuple()))
                    
                    if timestamp > max_id:
                        print 'Update facebook max_id value: %d, old max_id: %d.' % (timestamp, max_id)
                        max_id = timestamp

                    if timestamp <= self.since_time:
                        raise SearchError('Find repeated data,time stamp:%d,sinceTime is %d,stop this term search.' % (timestamp, self.since_time))

                    # validate text
                    if 'message' in sResult:
                        text = sResult[u'message']

                        if len(text) == 0:
                            continue
                        text = text if len(text) <= 1000 else text[:1000]

                        id_str = sResult[u'id']

                        if u'from' not in sResult:
                            continue
                        userId = sResult[u'from'][u'id']
                        #print 'userId:%s' % userId
                        userName = sResult[u'from'][u'name']
                        category = sResult[u'from'][u'category'] if 'category' in sResult[u'from'] else 'user'
                        socialPostLink = None
                        categoryList = ['user','Community']
                        if category in categoryList:
                           socialPostLink = 'https://www.facebook.com/%s' % id_str
                           
                        userProfileLink = 'https://www.facebook.com/%s' % userId
                        #userImageLink = sResult[u'picture'] if u'picture' in sResult else ''
                        userImageLink = 'http://graph.facebook.com/%s/picture' % userId
                        createDatetimeUTC = dt.strftime('%Y%m%d%H%M%S')
                        
                        createDate = datetime.strftime(datetime.utcnow(),'%Y%m%d%H%M%S')                       
                        postType = sResult[u'type'] if 'type' in sResult else ''
                        
                        if 'comments' in sResult:
                           comments = sResult[u'comments'][u'data']
                           for i in (range(len(comments))):
                              comment = comments[i]
                              C_ID = comment[u'id']
                              C_UserId = comment[u'from'][u'id']
                              C_UserName = comment[u'from'][u'name']
                              C_Category = sResult[u'from'][u'category']  if 'category' in comment[u'from'] else 'user'
                              C_UserImageLink = None
                              C_CategoryList = ['user','Community']
                              if category in C_CategoryList:
                                 C_SocialPostLink = 'https://www.facebook.com/%s' % C_ID
                                 
                              C_UserProfileLink = 'https://www.facebook.com/%s' % C_UserId
                              C_UserImageLink = 'http://graph.facebook.com/%s/picture' % C_UserId
                                                            
                              C_Text = comment[u'message']
                              C_CreateTime = comment[u'created_time']
                              C_DT = parse_date(C_CreateTime)
                              C_CreatedAt = C_DT.strftime("%a, %d %b %Y %H:%M:%S +0000")
                              C_CreateDatetimeUTC = C_DT.strftime('%Y%m%d%H%M%S')
                              C_CreateDate = datetime.strftime(datetime.utcnow(),'%Y%m%d%H%M%S')
                              C_PostType = 'comment'                              
                              
                              DSRecord = DataManager.NewDataRecord(1)
                              DSRecord.SetField(u'OUT_ID_STR', unicode(C_ID))
                              DSRecord.SetField(u'OUT_FROM_USER_ID', unicode(C_UserId))
                              DSRecord.SetField(u'OUT_FROM_USER', unicode(C_UserName))
                              DSRecord.SetField(u'OUT_FROM_USER_ACCOUNT', unicode(C_UserId))
                              DSRecord.SetField(u'OUT_SOCIAL_POST_LINK', unicode(C_SocialPostLink))
                              DSRecord.SetField(u'OUT_USER_IMAGE_LINK', unicode(C_UserImageLink))
                              DSRecord.SetField(u'OUT_CREATED_AT', unicode(C_CreatedAt))
                              DSRecord.SetField(u'OUT_CREATEDAT', unicode(C_CreateDate))
                              DSRecord.SetField(u'OUT_CREATEDATETIME_UTC', unicode(C_CreateDatetimeUTC))
                              DSRecord.SetField(u'OUT_TEXT', unicode(C_Text))
                              DSRecord.SetField(u'OUT_CHANNEL', unicode(self.channel))
                              DSRecord.SetField(u'OUT_LANGUAGE', unicode(self.language))
                              DSRecord.SetField(u'OUT_CLIENT', unicode(self.client))
                              DSRecord.SetField(u'OUT_ACCESSTOKEN', unicode(self.access_token))
                              DSRecord.SetField(u'OUT_PROXY', unicode(self.proxy))
                              DSRecord.SetField(u'OUT_SEARCHTERM', unicode(self.term))
                              DSRecord.SetField(u'OUT_CATEGORY', unicode(C_Category))
                              DSRecord.SetField(u'OUT_POST_TYPE', unicode(C_PostType))
                              Collection.AddRecord(DSRecord)
                              del DSRecord
                           
                           
                        

                        DSRecord = DataManager.NewDataRecord(1)
                        DSRecord.SetField(u'OUT_MAX_ID', unicode(max_id))
                        DSRecord.SetField(u'OUT_CREATED_AT', unicode(created_at))
                        # change the From_User field to user name
                        DSRecord.SetField(u'OUT_FROM_USER', unicode(userName))
                        DSRecord.SetField(u'OUT_FROM_USER_ID', unicode(userId))
                        DSRecord.SetField(u'OUT_FROM_USER_ACCOUNT', unicode(userId))
                        DSRecord.SetField(u'OUT_ID_STR', unicode(id_str))
                        DSRecord.SetField(u'OUT_TEXT', unicode(text))
                        #DSRecord.SetField(u'OUT_USER_PROFILE_LINK', unicode(userProfileLink))
                        DSRecord.SetField(u'OUT_SOCIAL_POST_LINK', unicode(socialPostLink))
                        DSRecord.SetField(u'OUT_USER_IMAGE_LINK', unicode(userImageLink))
                        DSRecord.SetField(u'OUT_CREATEDAT', unicode(createDate))
                        DSRecord.SetField(u'OUT_CREATEDATETIME_UTC', unicode(createDatetimeUTC))
                        DSRecord.SetField(u'OUT_CHANNEL', unicode(self.channel))
                        DSRecord.SetField(u'OUT_LANGUAGE', unicode(self.language))
                        DSRecord.SetField(u'OUT_CLIENT', unicode(self.client))
                        DSRecord.SetField(u'OUT_ACCESSTOKEN', unicode(self.access_token))
                        DSRecord.SetField(u'OUT_PROXY', unicode(self.proxy))
                        DSRecord.SetField(u'OUT_POST_TYPE', unicode(postType))
                        DSRecord.SetField(u'OUT_CATEGORY', unicode(category))
                        DSRecord.SetField(u'OUT_SEARCHTERM', unicode(self.term))
                        Collection.AddRecord(DSRecord)
                        del DSRecord
                        
                       # set record size
                        facebooks += 1

                current_page += 1

                if current_page > int(self.max_page):
                    print 'Reach max page limit, stop this term search.'
                    break

                if next_page is None:
                    print 'This is the last page, stop this term search.'
                    break

        except SearchError, e:
            print e
        except Exception, e1:
            print e1
        return facebooks

  

# Begin Search Job
print 'Begin to search facebook data...'

print 'Clear locale setting...'
locale.setlocale(locale.LC_ALL, 'C')

print 'Load input tasks...'
collectionSize = Collection.Size()
searchTermRec = DataManager.NewDataRecord()
searchCollectors = []

for recNum in range(collectionSize, 0, -1):
    Collection.GetRecord(searchTermRec, recNum)
    try:
        
        max_id = searchTermRec.GetField(u'IN_MAX_ID')
        
        pagesize = searchTermRec.GetField(u'IN_PAGESIZE')
        max_page = searchTermRec.GetField(u'IN_MAXPAGE')
        request_url = searchTermRec.GetField(u'IN_REQUESTURL')
        proxy = searchTermRec.GetField(u'IN_PROXY')
        
        access_token = searchTermRec.GetField(u'IN_ACCESSTOKEN')
        
        client = searchTermRec.GetField(u'IN_CLIENT')
        language = searchTermRec.GetField(u'IN_LANGUAGE')
        channel = searchTermRec.GetField(u'IN_CHANNEL')
        term = searchTermRec.GetField(u'IN_SEARCHTERM')
        fields = searchTermRec.GetField(u'IN_FIELDS')

        #print 'Preparing search task: %s(%s-%s).' % (term, language, 'f')
        searchCollectors.append(FacebookCollector(request_url, proxy, access_token, pagesize, max_page, max_id, client, language, channel, term, fields))

        # delete this dataRecord
        Collection.DeleteRecord(searchTermRec)

    except Exception, e:
        print "Append collectors error: %s" % e

DataManager.DeleteDataRecord(searchTermRec)
print 'Total %d task to search.\n' % len(searchCollectors)

print 'Begin data search...'
for sc in searchCollectors:
    #print 'Processing the term: %s(%s-%s).' % (sc.tag, sc.lang, sc.channel)
    results = sc.search()
    print 'The term search finished. Total size:%d.\n' % results

print 'Facebook processed.'


h