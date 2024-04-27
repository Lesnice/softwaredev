#creating class  email

class Email():
    #create constructor with three arguments
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        has_been_read = False
#method to mark as read
    def mark_as_read(self):
        #marks the email as read
        
        self.has_been_read = True
        print(f"\nEmail from {self.email_address} marked as read.\n")
        
#initialise empty variable called inbox
inbox = []
def populate_inbox(email):
    #populates inbox with email
    inbox.append(email)
    
#list of all emails in the inbox with corresponding numbers
if not inbox:
    print("\nYour inbox is empty.")
 
print("\nInbox: ")
for index, email in enumerate(inbox):
    read_status = " (Read)" if email.has_been_read else ""
    print(f"{index}. {email.subject_line}{read_status}")


def read_email():
  """Allows the user to read a specific email by index."""
  list_emails()
  if not inbox:
    return

  while True:
    try:
      index = int(input("\nEnter the index of the email you want to read (or 'q' to quit): "))
      if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"\nContent:\n{email.email_content}")
        email.mark_as_read()
        break
      else:
        print("Invalid index. Please try again.")
    except ValueError:
      if input("Invalid input. Quit? (y/n): ").lower() == "y":
        break


def main():
  """Simulates an email application."""
  populate_inbox(email)

  while True:
    print("\nEmail App")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
      read_email()
    elif choice == "2":
      unread_emails = [email for email in inbox if not email.has_been_read]
      if not unread_emails:
        print("\nYou have no unread emails.")
      else:
        print("\nUnread emails:")
        for index, email in enumerate(unread_emails):
          print(f"{index}. {email.subject_line}")
    elif choice == "3":
      print("\nQuitting application.")
      break
    else:
      print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
  main()
        
        
            