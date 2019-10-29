from django.db import models
from datetime import datetime

from floor.models import Room

class StatsLog(models.Model):
	'''
	Contains useful occupancy statistics
	@member (s)
		room - Room for which the logs are stored for
		event - enter/exit-1/0
		roomID = room ID of room
		timeStamp - exact date time of the log
	'''
	event = models.IntegerField(default = 0)
	roomID = models.CharField(max_length = 5)
	timeStamp = models.DateTimeField(auto_now_add=True, editable=False)
