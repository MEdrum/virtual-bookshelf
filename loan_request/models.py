from django.db import models
import uuid

class LoanRequest(models.Model):
    loanID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requesterID = models.ForeignKey('home.User', on_delete=models.CASCADE, related_name='requested_loans')
    receiverID = models.ForeignKey('home.User', on_delete=models.CASCADE, related_name='received_loans')
    state = models.IntegerField(default=0)  # 0: pending, 1: accepted, -1: rejected
    requestedBookID = models.ForeignKey('bookshelf.Book', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan {self.loanID} for {self.requestedBookID.title}"

