from emailrep import EmailRep

def getReputation(emailAddress):
    reputation = EmailRep('nyvyh92m0ek24vehe6j2zo881awtzk2iw8d4cp5gpw0vpuhq')
    result = reputation.query(emailAddress)
    return [result['reputation'], result['suspicious'], result['summary']]

def reportEmail(emailAddress, reasonCode, reasonText=None):
    reputation = EmailRep('nyvyh92m0ek24vehe6j2zo881awtzk2iw8d4cp5gpw0vpuhq')
    if (reasonCode == 1):
        reputation.report(emailAddress, "account_takeover", reasonText)
    elif (reasonCode == 2):
        reputation.report(emailAddress, "brand_impersonation", reasonText)
    elif (reasonCode == 3):
        reputation.report(emailAddress, "generic_phising", reasonText)
    elif (reasonCode == 4):
        reputation.report(emailAddress, "malware", reasonText)
    elif (reasonCode == 5):
        reputation.report(emailAddress, "scam", reasonText)
    elif (reasonCode == 6):
        reputation.report(emailAddress, "spam", reasonText)
    elif (reasonCode == 7):
        reputation.report(emailAddress, "task_request", reasonText)
    else:
        return("Invalid error code")

    return("Successfully reported")
    
# Email Report Codes
# 1: Legitimate email account has been taken over by malicious actor
# 2: Impersonating a well-known brand
# 3: Phising attempt
# 4: Malicious documents and droppers
# 5: Catch-all for scams.
# 6: Unsolicited spam or spammy behavior
# 7: Request that the recipient perform a task
