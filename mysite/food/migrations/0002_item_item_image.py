# Generated by Django 5.2 on 2025-04-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://www.google.com/imgres?q=font%20awesome%20icons%20food%20place%20holders&imgurl=https%3A%2F%2Ffontawesome.com%2Fsocial%2Fpot-food%3Ff%3D%26s%3D&imgrefurl=https%3A%2F%2Ffontawesome.com%2Ficons%2Fpot-food&docid=RFMeX5WRR1CJzM&tbnid=qMmQJ6SVkgEPeM&vet=12ahUKEwj-34TOouKMAxUW5DQHHVmQA6UQM3oECBoQAA..i&w=1200&h=630&hcb=2&ved=2ahUKEwj-34TOouKMAxUW5DQHHVmQA6UQM3oECBoQAA",
                max_length=500,
            ),
        ),
    ]
