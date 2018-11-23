# Generated by Django 2.1.2 on 2018-11-23 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20181123_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='facebookAcc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='instagramAcc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='twitterAcc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='person',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='person',
            name='mobiles',
        ),
        migrations.RemoveField(
            model_name='person',
            name='twitter',
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_person_friends_+', to='persons.person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('นาย', 'นาย'), ('นาง', 'นาง'), ('น.ส.', 'นางสาว'), ('พล.ต.อ.', 'พลตำรวจเอก'), ('พล.ต.อ. หญิง', 'พลตำรวจเอก หญิง'), ('พล.ต.ท', 'พลตำรวจโท'), ('พล.ต.ท หญิง', 'พลตำรวจโท หญิง'), ('พล.ต.ต', 'พลตำรวจตรี'), ('พล.ต.ต หญิง', 'พลตำรวจตรี หญิง'), ('พ.ต.อ.', 'พันตำรวจเอก'), ('พ.ต.อ. หญิง', 'พันตำรวจเอก หญิง'), ('พ.ต.อ.(พิเศษ)', 'พันตำรวจเอกพิเศษ'), ('พ.ต.อ.(พิเศษ) หญิง', 'พันตำรวจเอกพิเศษ หญิง'), ('พ.ต.ท.', 'พันตำรวจโท'), ('พ.ต.ท. หญิง', 'พันตำรวจโท หญิง'), ('พ.ต.ต.', 'พันตำรวจตรี'), ('พ.ต.ต. หญิง', 'พันตำรวจตรี หญิง'), ('ร.ต.อ.', 'ร้อยตำรวจเอก'), ('ร.ต.อ. หญิง', 'ร้อยตำรวจเอก หญิง'), ('ร.ต.ท.', 'ร้อยตำรวจโท'), ('ร.ต.ท. หญิง', 'ร้อยตำรวจโท หญิง'), ('ร.ต.ต.', 'ร้อยตำรวจตรี'), ('ร.ต.ต. หญิง', 'ร้อยตำรวจตรี หญิง'), ('ด.ต.', 'นายดาบตำรวจ'), ('ด.ต. หญิง', 'ดาบตำรวจหญิง'), ('ส.ต.อ.', 'สิบตำรวจเอก'), ('ส.ต.อ. หญิง', 'สิบตำรวจเอก หญิง'), ('ส.ต.ท.', 'สิบตำรวจโท'), ('ส.ต.ท. หญิง', 'สิบตำรวจโท หญิง'), ('ส.ต.ต.', 'สิบตำรวจตรี'), ('ส.ต.ต. หญิง', 'สิบตำรวจตรี หญิง'), ('จ.ส.ต.', 'จ่าสิบตำรวจ'), ('จ.ส.ต. หญิง', 'จ่าสิบตำรวจ หญิง'), ('พลฯ', 'พลตำรวจ'), ('พลฯ หญิง', 'พลตำรวจ หญิง'), ('พล.อ.', 'พลเอก'), ('พล.อ. หญิง', 'พลเอก หญิง'), ('พล.ท.', 'พลโท'), ('พล.ท. หญิง', 'พลโท หญิง'), ('พล.ต.', 'พลตรี'), ('พล.ต.หญิง', 'พลตรี หญิง'), ('พ.อ.', 'พันเอก'), ('พ.อ.หญิง', 'พันเอก หญิง'), ('พ.อ.(พิเศษ)', 'พันเอกพิเศษ'), ('พ.อ.(พิเศษ) หญิง', 'พันเอกพิเศษ หญิง'), ('พ.ท.', 'พันโท'), ('พ.ท.หญิง', 'พันโท หญิง'), ('พ.ต.', 'พันตรี'), ('พ.ต.หญิง', 'พันตรี หญิง'), ('ร.อ.', 'ร้อยเอก'), ('ร.อ.หญิง', 'ร้อยเอก หญิง'), ('ร.ท.', 'ร้อยโท'), ('ร.ท.หญิง', 'ร้อยโท หญิง'), ('ร.ต.', 'ร้อยตรี'), ('ร.ต.หญิง', 'ร้อยตรี หญิง'), ('ส.อ.', 'สิบเอก'), ('ส.อ.หญิง', 'สิบเอก หญิง'), ('ส.ท.', 'สิบโท'), ('ส.ท.หญิง', 'สิบโท หญิง'), ('ส.ต.', 'สิบตรี'), ('ส.ต.หญิง', 'สิบตรี หญิง'), ('จ.ส.อ.', 'จ่าสิบเอก'), ('จ.ส.อ.หญิง', 'จ่าสิบเอก หญิง'), ('จ.ส.ท.', 'จ่าสิบโท'), ('จ.ส.ท.หญิง', 'จ่าสิบโท หญิง'), ('จ.ส.ต.', 'จ่าสิบตรี'), ('จ.ส.ต.หญิง', 'จ่าสิบตรี หญิง'), ('พลฯ', 'พลทหารบก'), ('ว่าที่ พ.ต.', 'ว่าที่ พ.ต.'), ('ว่าที่ พ.ต. หญิง', 'ว่าที่ พ.ต. หญิง'), ('ว่าที่ ร.อ.', 'ว่าที่ ร.อ.'), ('ว่าที่ ร.อ. หญิง', 'ว่าที่ ร.อ. หญิง'), ('ว่าที่ ร.ท.', 'ว่าที่ ร.ท.'), ('ว่าที่ ร.ท. หญิง', 'ว่าที่ ร.ท. หญิง'), ('ว่าที่ ร.ต.', 'ว่าที่ ร.ต.'), ('ว่าที่ ร.ต. หญิง', 'ว่าที่ ร.ต. หญิง'), ('พล.ร.อ.', 'พลเรือเอก'), ('พล.ร.อ.หญิง', 'พลเรือเอก หญิง'), ('พล.ร.ท.', 'พลเรือโท'), ('พล.ร.ท.หญิง', 'พลเรือโท หญิง'), ('พล.ร.ต.', 'พลเรือตรี'), ('พล.ร.ต.หญิง', 'พลเรือตรี หญิง'), ('น.อ.', 'นาวาเอก'), ('น.อ.หญิง', 'นาวาเอก หญิง'), ('น.อ.(พิเศษ)', 'นาวาเอกพิเศษ'), ('น.อ.(พิเศษ) หญิง', 'นาวาเอกพิเศษ หญิง'), ('น.ท.', 'นาวาโท'), ('น.ท.หญิง', 'นาวาโท หญิง'), ('น.ต.', 'นาวาตรี'), ('น.ต.หญิง', 'นาวาตรี หญิง'), ('ร.อ.', 'เรือเอก'), ('ร.อ.หญิง', 'เรือเอก หญิง'), ('ร.ท.', 'เรือโท'), ('ร.ท.หญิง', 'เรือโท หญิง'), ('ร.ต.', 'เรือตรี'), ('ร.ต.หญิง', 'เรือตรี หญิง'), ('พ.จ.อ.', 'พันจ่าเอก'), ('พ.จ.อ.หญิง', 'พันจ่าเอก หญิง'), ('พ.จ.ท.', 'พันจ่าโท'), ('พ.จ.ท.หญิง', 'พันจ่าโท หญิง'), ('พ.จ.ต.', 'พันจ่าตรี'), ('พ.จ.ต.หญิง', 'พันจ่าตรี หญิง'), ('จ.อ.', 'จ่าเอก'), ('จ.อ.หญิง', 'จ่าเอก หญิง'), ('จ.ท.', 'จ่าโท'), ('จ.ท.หญิง', 'จ่าโท หญิง'), ('จ.ต.', 'จ่าตรี'), ('จ.ต.หญิง', 'จ่าตรี หญิง'), ('พลฯ', 'พลทหารเรือ'), ('พล.อ.อ.', 'พลอากาศเอก'), ('พล.อ.อ.หญิง', 'พลอากาศเอก หญิง'), ('พล.อ.ท.', 'พลอากาศโท'), ('พล.อ.ท.หญิง', 'พลอากาศโท หญิง'), ('พล.อ.ต.', 'พลอากาศตรี'), ('พล.อ.ต.หญิง', 'พลอากาศตรี หญิง'), ('น.อ.', 'นาวาอากาศเอก'), ('น.อ.หญิง', 'นาวาอากาศเอก หญิง'), ('น.อ.(พิเศษ)', 'นาวาอากาศเอกพิเศษ'), ('น.อ.(พิเศษ) หญิง', 'นาวาอากาศเอกพิเศษ หญิง'), ('น.ท.', 'นาวาอากาศโท'), ('น.ท.หญิง', 'นาวาอากาศโท หญิง'), ('น.ต.', 'นาวาอากาศตรี'), ('น.ต.หญิง', 'นาวาอากาศตรี หญิง'), ('ร.อ.', 'เรืออากาศเอก'), ('ร.อ.หญิง', 'เรืออากาศเอก หญิง'), ('ร.ท.', 'เรืออากาศโท'), ('ร.ท.หญิง', 'เรืออากาศโท หญิง'), ('ร.ต.', 'เรืออากาศตรี'), ('ร.ต.หญิง', 'เรืออากาศตรี หญิง'), ('พ.อ.อ.', 'พันจ่าอากาศเอก'), ('พ.อ.อ.หญิง', 'พันจ่าอากาศเอก หญิง'), ('พ.อ.ท.', 'พันจ่าอากาศโท'), ('พ.อ.ท.หญิง', 'พันจ่าอากาศโท หญิง'), ('พ.อ.ต.', 'พันจ่าอากาศตรี'), ('พ.อ.ต.หญิง', 'พันจ่าอากาศตรี หญิง'), ('จ.อ.', 'จ่าอากาศเอก'), ('จ.อ.หญิง', 'จ่าอากาศเอก หญิง'), ('จ.ท.', 'จ่าอากาศโท'), ('จ.ท.หญิง', 'จ่าอากาศโท หญิง'), ('จ.ต.', 'จ่าอากาศตรี'), ('จ.ต.หญิง', 'จ่าอากาศตรี หญิง'), ('พลฯ', 'พลทหารอากาศ'), ('หม่อม', 'หม่อม'), ('ม.จ.', 'หม่อมเจ้า'), ('ม.ร.ว.', 'หม่อมราชวงศ์'), ('ม.ล.', 'หม่อมหลวง'), ('ดร.', 'ดร.'), ('ศ.ดร.', 'ศ.ดร.'), ('ศ.', 'ศ.'), ('ผศ.ดร.', 'ผศ.ดร.'), ('ผศ.', 'ผศ.'), ('รศ.ดร.', 'รศ.ดร.'), ('รศ.', 'รศ.'), ('นพ.', 'นพ.'), ('พญ.', 'แพทย์หญิง'), ('นสพ.', 'สัตวแพทย์'), ('สพญ.', 'สพญ.'), ('ทพ.', 'ทพ.'), ('ทพญ.', 'ทพญ.'), ('ภก.', 'เภสัชกร'), ('ภกญ.', 'ภกญ.'), ('พระ', 'พระ'), ('พระครู', 'พระครู'), ('พระมหา', 'พระมหา'), ('พระสมุห์', 'พระสมุห์'), ('พระอธิการ', 'พระอธิการ'), ('สามเณร', 'สามเณร'), ('แม่ชี', 'แม่ชี'), ('บาทหลวง', 'บาทหลวง'), ('Mr.', 'MR'), ('Mrs. ', 'MRS'), ('Ms. ', 'MS'), ('Miss', 'MISS'), ('Dr.', 'Dr.')], max_length=100),
        ),
        migrations.AddField(
            model_name='twitteracc',
            name='twitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.person'),
        ),
        migrations.AddField(
            model_name='instagramacc',
            name='instagram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.person'),
        ),
        migrations.AddField(
            model_name='facebookacc',
            name='facebook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.person'),
        ),
    ]
