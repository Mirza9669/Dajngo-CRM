from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50) 
    email = models.CharField(max_length= 100) 
    phone = models.CharField(max_length= 50) 
    address = models.CharField(max_length= 200)
    city = models.CharField(max_length= 50)  
    state = models.CharField(max_length= 50)
    zipcode = models.CharField(max_length= 10)

    def __str__(self) -> str:
        return (
            f"""
            {self.created_at}
            {self.id}
            {self.first_name}
            {self.last_name}
            {self.email}
            {self.phone}
            {self.address}
            {self.city}
            {self.state}
            {self.zipcode}
            """
        )