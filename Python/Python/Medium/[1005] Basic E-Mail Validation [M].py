"""
####  Basic E-Mail Validation  ####

Create a function that accepts a string, checks if it's a valid email address and returns either True or False, depending on the evaluation.
___
*) The string must contain an @ character.
*) The string must contain a . character.
*) The @ must have at least one character in front of it.
e.g. "e@edabit.com" is valid while "@edabit.com" is invalid.
*) The . and the @ must be in the appropriate places.
e.g. "hello.email@com" is invalid while "john.smith@email.com" is valid.
___

If the string passes these tests, it's considered a valid email address.


[Examples]

___
validate_email("@gmail.com") ➞ False

validate_email("hello.gmail@com") ➞ False

validate_email("gmail") ➞ False

validate_email("hello@gmail") ➞ False

validate_email("hello@edabit.com") ➞ True
_____



[Notes]

___
*) Check the Tests tab to see exactly what's being evaluated.
*) You can solve this challenge with RegEx, but it's intended to be solved with logic.
*) Solutions using RegEx will be accepted but frowned upon :(
___



[logic] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Validate an Email Address Using Python
https://www.pythoncentral.io/how-to-validate-an-email-address-using-python/
This snippet shows you how to easily validate any email using Python's awesome isValidEmail() function. Validating an email means that you're testing whether or not it' …
_________
_________
email — An email and MIME handling package
https://docs.python.org/3/library/email.html
The email package is a library for managing email messages. It is specifically not designed to do any sending of email messages to SMTP (RFC 2821), NNTP, or other serv …
_________
_________
Check for valid email address?
https://stackoverflow.com/questions/8022530/python-check-for-valid-email-address/8022584
Is there a good way to check a form input using regex to make sure it is a proper style email address? Been searching since last night and everybody that has answered p …
_________
_________
re — Regular Expression Operations
https://docs.python.org/3.6/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________

"""
#Your code should go here:

