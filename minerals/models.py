from django.db import models

import json

# Create your models here.


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=255)
    image_caption = models.CharField(max_length=255, blank=True,
                                     default='', null=True)
    category = models.CharField(max_length=255, blank=True,
                                default='', null=True)
    formula = models.CharField(max_length=255, blank=True,
                               default='', null=True)
    strunz_classification = models.CharField(max_length=255, blank=True,
                                             default='', null=True)
    crystal_system = models.CharField(max_length=255, blank=True,
                                      default='', null=True)
    unit_cell = models.CharField(max_length=255, blank=True,
                                 default='', null=True)
    color = models.CharField(max_length=255, blank=True,
                             default='', null=True)
    crystal_symmetry = models.CharField(max_length=255, blank=True,
                                        default='', null=True)
    cleavage = models.CharField(max_length=255, blank=True,
                                default='', null=True)
    mohs_scale_hardness = models.CharField(max_length=255,
                                           blank=True, default='', null=True)
    luster = models.CharField(max_length=255, blank=True,
                              default='', null=True)
    streak = models.CharField(max_length=255, blank=True,
                              default='', null=True)
    diaphaneity = models.CharField(max_length=255, blank=True,
                                   default='', null=True)
    optical_properties = models.CharField(max_length=255, blank=True,
                                          default='', null=True)
    refractive_index = models.CharField(max_length=255, blank=True,
                                        default='', null=True)
    crystal_habit = models.CharField(max_length=255, blank=True,
                                     default='', null=True)
    specific_gravity = models.CharField(max_length=255, blank=True,
                                        default='', null=True)
    group = models.CharField(max_length=255, blank=True, default='', null=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name
