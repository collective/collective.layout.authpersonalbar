from setuptools import setup, find_packages
import os

version = '0.1.1'

setup(
    name='collective.layout.authpersonalbar',
    version=version,
    description="Show personal bar only to authenticated users.",
    long_description=open(os.path.join('collective', 'layout',
                            'authpersonalbar', 'README.txt')).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone collective layout',
    author='j23d',
    author_email='j23d@dein-cms.de',
    url='http://svn.plone.org/svn/collective/collective.layout.authpersonalbar/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.layout'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
          'setuptools',
          'five.grok',
    ],
    extras_require={
        'test': ['plone.app.testing [test]', ],
    },
    entry_points="""
    # -*- Entry points: -*-
        [z3c.autoinclude.plugin]
        target = plone
    """,
    setup_requires=["PasteScript"],
    paster_plugins=["ZopeSkel"],
)
