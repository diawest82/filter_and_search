from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Mineral
# Create your tests here.

mineral_one = {'name': "Abelsonite",
               'category': 'Organic Minerals',
               'formula': 'C31H32N4Ni',
               'strunz_classification': '10.Ca.20',
               'crystal_system': 'crystal test',
               'unit_cell': 'A = 8.508 Å, B = 11.185 Åc=7.299 Å, Α = 90.85°Β = 114.1°, Γ = 79.99°Z = 1',
               'color': 'Pink-Purple, Dark Greyish Purple, Pale Purplish Red, Reddish Brown',
               'crystal_symmetry': 'symmetry test',
               'cleavage': 'cleavage',
               'mohs_scale_hardness': '2-3',
               'crystal_habit': 'None',
               }

mineral_two = {'name': "Epsomite",
               'category': 'Sulfate',
               'formula': 'Mgso4·7H2O',
               'strunz_classification': '07.Cb.40',
               'crystal_system': 'crystal test',
               'unit_cell': 'A = 11.86 Å, B = 11.99 Å, C = 6.858 Å; Z=4',
               'color': 'White, Grey, Colorless, Or Pink, Greenish',
               'crystal_symmetry': 'symmetry test',
               'cleavage': 'cleavage',
               'mohs_scale_hardness': '2-3',
               'crystal_habit': 'Acicular To Fibrous Encrustations',
               }


class MineralModelTestcase(TestCase):
    def test_mineral_model(self):
        minerals = Mineral.objects.create(**mineral_one)
        self.assertEqual(minerals.name, 'Abelsonite')


class MineralViewTestCase(TestCase):
    def setUp(self):
        self.minerals1 = Mineral.objects.create(**mineral_one)
        self.minerals2 = Mineral.objects.create(**mineral_two)

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.minerals1, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.minerals1.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.minerals1.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.minerals1, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

    def test_mineral_letter_list(self):
        resp = self.client.get(reverse('minerals:letter',
                                       kwargs={'letter': 'e'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.minerals2, resp.context['minerals'])
        self.assertNotIn(self.minerals1, resp.context['minerals'])

    def test_search_group(self):
        resp = self.client.get(reverse('minerals:group',
                                       kwargs={'group': 'organic minerals'}))
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(self.minerals2, resp.context['minerals'])

    def test_search_box(self):
        resp = self.client.get(reverse('minerals:search'), {'q': 'eps'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.minerals2, resp.context['minerals'])
