# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_untranslated_fields'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='categorytranslation',
            name='master',
        ),
        migrations.AlterUniqueTogether(
            name='producttranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='producttranslation',
            name='master',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Категории', 'ordering': ('name',), 'verbose_name': 'Категория'},
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, db_index=True, default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, default=23, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, default=23),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
        migrations.DeleteModel(
            name='CategoryTranslation',
        ),
        migrations.DeleteModel(
            name='ProductTranslation',
        ),
    ]
