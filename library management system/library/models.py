from django.db import models

class Books(models.Model):
    name = models.CharField("Book_Name",max_length = 200,unique=True)
    ISBN = models.CharField("ISBN",unique=True,primary_key=True,max_length=300)
    quantity = models.IntegerField("Quantity")
    author = models.CharField("Author_Name",max_length = 200)
    pages = models.IntegerField("No_of_pages")
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name
