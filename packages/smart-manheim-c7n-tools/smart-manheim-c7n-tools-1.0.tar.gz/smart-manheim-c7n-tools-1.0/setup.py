
import setuptools

setuptools.setup(
    name="smart-manheim-c7n-tools",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=['boto3', 'docutils>=0.10,<0.15', 'tabulate>=0.8.0,<0.9.0', 'pyyaml', 'c7n==0.8.45.2', 'c7n-mailer==0.5.6', 'sphinx>=1.8.0,<1.9.0', 'sphinx_rtd_theme'],
)
