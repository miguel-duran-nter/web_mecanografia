from django.db import migrations, models
from django.utils import timezone

def set_created_at(apps, schema_editor):
    Scoreboard = apps.get_model('scoreboard', 'Scoreboard')
    for instance in Scoreboard.objects.all():
        instance.created_at = timezone.now()
        instance.save()

class Migration(migrations.Migration):
    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreboard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
        ),
        migrations.RunPython(set_created_at),
    ]