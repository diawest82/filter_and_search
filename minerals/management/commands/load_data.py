from django.core.management.base import BaseCommand, CommandError

from minerals.models import Mineral

import json


class Command(BaseCommand):
    """Loads database upon launch"""
    help = "This loads the minerals data"

    def handle(self, *args, **options):
        with open('minerals.json', encoding='utf-8') as file:
            minerals = json.load(file)

            for mineral in minerals:
                Mineral(
                    name=mineral.get('name'),
                    image_filename=mineral.get('name') + '.jpg',
                    image_caption=mineral.get('image caption', ''),
                    category=mineral.get('category', ''),
                    formula=mineral.get('formula', ''),
                    strunz_classification=mineral.get('strunz classification', ''),
                    crystal_system=mineral.get('crystal system', ''),
                    unit_cell=mineral.get('unit cell', ''),
                    color=mineral.get('color', ''),
                    crystal_symmetry=mineral.get('crystal symmetry', ''),
                    cleavage=mineral.get('cleavage', ''),
                    mohs_scale_hardness=mineral.get('mohs scale hardness', ''),
                    luster=mineral.get('luster', ''),
                    streak=mineral.get('streak', ''),
                    diaphaneity=mineral.get('diaphaneity', ''),
                    optical_properties=mineral.get('optical properties', ''),
                    refractive_index=mineral.get('refractive index', ''),
                    crystal_habit=mineral.get('crystal habit', ''),
                    specific_gravity=mineral.get('specific gravity', ''),
                    group=mineral.get('group', ''),
                ).save()
            self.stdout.write(self.style.SUCCESS('Data Added"'))
