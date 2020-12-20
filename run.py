import imaplib

m = imaplib.IMAP4_SSL("imap.mail.yahoo.com")
m.login(input('Enter your email ID:\n'),input('Enter your app password:\n'))
#m.list()
m.select('Inbox')
status, resp = m.search(None, 'UNSEEN')				# status; is return message indicating success [OK] or failure. resp ; a list of only one element is resturned as <class : Bytes> Containing all the email_IDs of the search query.
unread_count = resp[0].split()

#m.fetch(messageID, 'RFC something')				#retrieves the message from messageID. To view the message.

#Delete one by one : will take a long time if the count is large
'''
for em_id in unread_count:			
	m.copy(em_id, 'Trash')
	m.store(em_id, '+FLAGS', '(\\Deleted)')
	print('Delete Successful for {em_id}')
'''

# Taking bacthes of 500 emails to byepass operation limits
for j in range(0,len(unread_count),500):
	m.copy(','.join(str(i)[2:-1] for i in unread_count[j:j+500]), 'Trash')		#batch transfer to Trash bin
	m.store(','.join(str(i)[2:-1] for i in unread_count[j:j+500]), '+FLAGS', '\\Deleted')   #batch delete from current mailbox
	m.expunge()
m.expunge()
m.logout()
