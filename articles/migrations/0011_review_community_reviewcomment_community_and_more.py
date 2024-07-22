# Generated by Django 5.0.6 on 2024-07-16 15:54

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0010_articlepdf_anonymousidentity"),
        ("communities", "0006_communityarticle_articlesubmissionassessment_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="community",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="communities.community",
            ),
        ),
        migrations.AddField(
            model_name="reviewcomment",
            name="community",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="communities.community",
            ),
        ),
        migrations.AddField(
            model_name="reviewcomment",
            name="rating",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ]
            ),
        ),
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("article", "user", "community")},
        ),
    ]