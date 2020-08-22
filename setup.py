from setuptools import setup


setup(
      name='my_custom_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/bcr04/sklearn_transforms/',
      author='bcr04',
      author_email='',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms_maratona_IBM_desafio_02'
      ],
      zip_safe=False
)
