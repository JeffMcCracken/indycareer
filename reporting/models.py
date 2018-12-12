from django.db import models

class Office(models.Model):
    city = models.CharField(max_length=150)
    street_address = models.CharField(max_length=150)
    zip_code = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    exp_agent_goal = models.PositiveIntegerField(blank=True, null=True)
    exp_agents = models.PositiveIntegerField(blank=True, null=True)
    new_agent_goal = models.PositiveIntegerField(blank=True, null=True)
    new_agents = models.PositiveIntegerField(blank=True, null=True)
    agent_departures = models.PositiveIntegerField(blank=True, null=True)
    team_departures = models.PositiveIntegerField(blank=True, null=True)
    company_dollar = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        # Handling unique office names
        if self.zip_code == 46204:
            return 'Downtown'
        elif self.zip_code == 46240:
            return '96th Street'
        else:
            return self.city
