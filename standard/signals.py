from django.dispatch import Signal

'''
Note that sometimes you will get duplicate signals emitted, depending on configuration of your systems. 
If you do encounter this, you will need to add the "dispatch_uid" to your connect handlers

See http://code.djangoproject.com/wiki/Signals#Helppost_saveseemstobeemittedtwiceforeachsave for details
'''

# Sent when a payment is successfully processed.
payment_was_successful = Signal()

# Sent when a payment is flagged.
payment_was_flagged = Signal()

# Sent when a subscription cancellation is received/ processed
subscription_was_cancelled = Signal()

# Sent when a subscription End of Term is received/ processed
subscription_was_eot = Signal()

# Sent when a subscription End of Term is received/ processed
subscription_was_modified = Signal()

# Sent when a subscription End of Term is received/ processed
subscription_was_signed_up = Signal()