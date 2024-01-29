"""Setup script for discord oauth support on weblate"""

from setuptools import setup

setup(
    name="discord_oauth_weblate",
    version="0.0.1",
    packages=["discord_oauth_weblate", "discord_oauth_weblate.backends"],
    include_package_data=True,
    license="Unlicense",
    description="Discord Oauth support for Weblate",
    install_requires=["Weblate"],
    zip_safe=False
)
