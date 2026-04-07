# Microsoft Graph Query Parameters
# Doku: https://learn.microsoft.com/de-de/graph/query-parameters?tabs=http

FETCH_MAIL_QUERY_PARAMS = {
    "top": 20,                                              # number of mails to request
    "orderby": "receivedDateTime desc",                     # sorting filter
    "select": "id,subject,receivedDateTime,bodyPreview"     # tells the api calls which values to return
}