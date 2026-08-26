class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            clean_local_name = local_name.replace(".", "")
            min_local_name = clean_local_name.split("+")[0]
            # (if no + this returns original string)
            unique_emails.add(f"{min_local_name}{domain_name}")
        return len(unique_emails)
