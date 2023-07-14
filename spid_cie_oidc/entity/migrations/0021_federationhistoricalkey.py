# Generated by Django 4.2.1 on 2023-07-08 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "spid_cie_oidc_entity",
            "0020_alter_federationentityconfiguration_jwks_core_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="FederationHistoricalKey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "kid",
                    models.CharField(
                        choices=[
                            (0, "unspecified"),
                            (1, "keyCompromise"),
                            (2, "cACompromise"),
                            (3, "affiliationChanged"),
                            (4, "superseded"),
                            (5, "cessationOfOperation"),
                            (6, "certificateHold"),
                            (8, "removeFromCRL"),
                            (9, "privilegeWithdrawn"),
                            (10, "aACompromise"),
                        ],
                        max_length=33,
                    ),
                ),
                (
                    "inactive_from",
                    models.DateTimeField(
                        help_text="Expired or Revocation date if revocation motivation is configured"
                    ),
                ),
                (
                    "revocation_motivation",
                    models.CharField(
                        blank=True,
                        choices=[
                            (0, "unspecified"),
                            (1, "keyCompromise"),
                            (2, "cACompromise"),
                            (3, "affiliationChanged"),
                            (4, "superseded"),
                            (5, "cessationOfOperation"),
                            (6, "certificateHold"),
                            (8, "removeFromCRL"),
                            (9, "privilegeWithdrawn"),
                            (10, "aACompromise"),
                        ],
                        max_length=33,
                    ),
                ),
                (
                    "entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spid_cie_oidc_entity.federationentityconfiguration",
                    ),
                ),
            ],
            options={
                "verbose_name": "Federation Historical Key",
                "verbose_name_plural": "Federation Historical Keys",
            },
        ),
    ]
