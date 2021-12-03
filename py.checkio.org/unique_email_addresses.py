'https://py.checkio.org/en/mission/unique-email-addresses/share/8b10f46fe5550aec98d8b13583b8addb/'

'''
Every valid email consists of name and domain, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'. 
For example, in "alex@checkio.org", "alex" is the name, and "checkio.org" is the domain.

If you add periods '.' between some characters in the name part of an email address, mail sent there will be delivered to the same address without dots in the name. 
Note that this rule does not apply to domain names. For example, "a.lyabah@checkio.org" and "alyabah@checkio.org" delivered to the same email address.

If you add a plus '+' in the name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. 
Note that this rule does not apply to domain names. For example, "alex+home@checkio.org" will be delivered to "alex@checkio.org".

It is possible to use both of these rules at the same time.

Given an array of strings - valid emails, return the number of unique emails.

Input: Array of strings(valid emails)

Output: Int.
'''

import re

def unique_emails(emails: list[str]) -> int:
    if emails == []:
        return 0
    
    emails_new = list()
    
    for item in emails:
        username = item.split('@')[0]
        domain = item.split('@')[1]
        username_new = re.sub('\.', '', username)
        username_new = username_new.split('+')[0]
        item_new = username_new.lower() + '@' + domain.lower()
        
        emails_new.append(item_new)
        
    print(emails_new)
        
    return len(set(emails_new))


print("Example:")
#print(unique_emails(["john@checkio.org", "mike@google.com", "lili@apple.com"]))
print(unique_emails(["john+john@checkio.org", "john.john@checkio.org", "john@checkio.org", "mike.mike@google.com", "lili+work@apple.com"]))

assert unique_emails(["alex@checkio.org", "mike@google.com", "lili@apple.com"]) == 3
assert (
    unique_emails(
        ["mi.ke@google.com", "alex@checkio.org", "mike@google.com", "lili@apple.com"]
    )
    == 3
)
assert (
    unique_emails(
        [
            "alex+home@checkio.org",
            "lili+work@apple.com",
            "alex@checkio.org",
            "lili@apple.com",
        ]
    )
    == 2
)
assert (
    unique_emails(
        [
            "l.ili+work@apple.com",
            "a.lex@checkio.org",
            "alex+home@checkio.org",
            "lili+work@apple.com",
            "alex@checkio.org",
            "lili@apple.com",
        ]
    )
    == 2
)
assert unique_emails(["Alex@checkIO.org", "alex@checkio.org", "alex@check.io.org"]) == 2
assert unique_emails([]) == 0