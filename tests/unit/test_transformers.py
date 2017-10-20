import unittest

import lore.transformers
import numpy
import pandas


class TestAreaCode(unittest.TestCase):
    def setUp(self):
        self.transformer = lore.transformers.AreaCode('phone')

    def test_phone_formats(self):
        values = pandas.DataFrame({
            'phone': [
                '12345678901',
                '+12345678901',
                '1(234)567-8901',
                '1 (234) 567-8901',
                '1.234.567.8901',
                '1-234-567-8901',
                '2345678901',
                '234.567.8901',
                '(234)5678901',
                '(234) 567-8901',
            ]
        })
        result = self.transformer.transform(values)
        self.assertEqual(result.tolist(), numpy.repeat('234', len(values)).tolist())

    def test_bad_data(self):
        values = pandas.DataFrame({
            'phone': [
                '1234567',
                '(123)4567',
                '',
                None,
                12345678901,
            ]
        })
        result = self.transformer.transform(values)
        self.assertEqual(result.tolist(), ['', '', '', None, ''])
    
        
class TestEmailDomain(unittest.TestCase):
    def setUp(self):
        self.transformer = lore.transformers.EmailDomain('email')

    def test_transform(self):
        values = pandas.DataFrame({
            'email': [
                'montana@instacart.com',
                'sue-bob+anne@instacart.com'
            ]
        })
        result = self.transformer.transform(values)
        self.assertEqual(result.tolist(), numpy.repeat('instacart.com', len(values)).tolist())


class TestNameFamilial(unittest.TestCase):
    def setUp(self):
        self.transformer = lore.transformers.NameFamilial('name')

    def test_transform(self):
        values = pandas.DataFrame({
            'name': [
                'mom',
                'Dad',
                'sue bob'
            ]
        })
        result = self.transformer.transform(values)
        self.assertEqual(result.tolist(), [True, True, False])
