from django.db import models
from accounts.models import User


from django.db import models

class GarbageBin(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    bin_type_choices = [
        ('recycling', 'Recycling Bin'),
        ('compost', 'Compost Bin'),
        ('landfill', 'Landfill Bin')
    ]
    bin_type = models.CharField(max_length=20, choices=bin_type_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name_plural = 'Garbage Bins'
        db_table = 'garbage_bins'

class GarbageCollection(models.Model):
    bin = models.ForeignKey(GarbageBin, on_delete=models.CASCADE)
    pickup_time = models.DateTimeField()
    status_choices = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=20, choices=status_choices)

    class Meta:
        verbose_name_plural = 'Garbage Collections'
        db_table = 'garbage_collections'

    def __str__(self):
        return self.bin.location + ' - ' + str(self.pickup_time)

class GarbageCollectionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bin = models.ForeignKey(GarbageBin, on_delete=models.CASCADE)
    pickup_time = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    is_picked = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Garbage Collection Requests'
        db_table = 'garbage_collection_requests'

    def __str__(self):
        return self.bin.location + ' - ' + str(self.pickup_time)



class WasteDisposal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    waste_type_choices = [
        ('plastic', 'Plastic'),
        ('organic', 'Organic'),
        ('metal', 'Metal'),
        ('glass', 'Glass'),
        ('paper', 'Paper')
    ]
    waste_type = models.CharField(max_length=20, choices=waste_type_choices)

    class Meta:
        verbose_name_plural = 'Waste Disposals'
        db_table = 'waste_disposals'

class CreditScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Credit Scores'
        db_table = 'credit_scores'

    def __str__(self):
        return self.user.email + ' - ' + str(self.score)

class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    cost = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Rewards'
        db_table = 'rewards'

    def __str__(self):
        return self.name + ' - ' + str(self.cost)

