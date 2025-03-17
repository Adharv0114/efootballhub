from django.db import models

# Player Model
class Player(models.Model):
    # Main Details
    name = models.CharField(max_length=100, default="Unknown")
    position = models.CharField(max_length=20, default="Unknown")
    best_position = models.CharField(max_length=20, default="Unknown")
    max_rating = models.IntegerField(default=0)
    base_rating = models.IntegerField(default=0)
    team = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    playing_style = models.CharField(max_length=50, blank=True, null=True)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=18)
    foot = models.CharField(max_length=10, choices=[("Left", "Left"), ("Right", "Right"), ("Both", "Both")], default="Right")

    # Attacking Attributes
    offensive_awareness = models.IntegerField(default=0)
    ball_control = models.IntegerField(default=0)
    dribbling = models.IntegerField(default=0)
    tight_possession = models.IntegerField(default=0)
    low_pass = models.IntegerField(default=0)
    lofted_pass = models.IntegerField(default=0)
    finishing = models.IntegerField(default=0)
    heading = models.IntegerField(default=0)
    place_kicking = models.IntegerField(default=0)
    curl = models.IntegerField(default=0)

    # Defending Attributes
    defensive_awareness = models.IntegerField(default=0)
    defensive_engagement = models.IntegerField(default=0)
    tackling = models.IntegerField(default=0)
    aggression = models.IntegerField(default=0)
    goalkeeping = models.IntegerField(default=0)
    gk_catching = models.IntegerField(default=0)
    gk_parrying = models.IntegerField(default=0)
    gk_reflexes = models.IntegerField(default=0)
    gk_reach = models.IntegerField(default=0)

    # Athleticism
    speed = models.IntegerField(default=0)
    acceleration = models.IntegerField(default=0)
    kicking_power = models.IntegerField(default=0)
    jump = models.IntegerField(default=0)
    physical_contact = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)
    weak_foot_usage = models.IntegerField(default=0)
    weak_foot_accuracy = models.IntegerField(default=0)
    form = models.IntegerField(default=0)
    injury_resistance = models.IntegerField(default=0)

    # Skills (Max 10)
    skills = models.JSONField(default=list)

    def __str__(self):
        return self.name



# User Squad Model
class Squad(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, related_name="squads")

    def __str__(self):
        return self.name


# Player Comparison Model
class Comparison(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="comparison_player1")
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="comparison_player2")

    def __str__(self):
        return f"Compare: {self.player1.name} vs {self.player2.name}"