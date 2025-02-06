from setuptools import setup, find_packages

setup(
    name='nlm-utils',
    version='0.1.3',    
    description='Common utilities used by all nlm-* libraries.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nlmatics/nlm-utils',
    author='Ambika Sukla',
    author_email='ambika.sukla@nlmatics.com',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "dateparser",
        "dnspython",
        "word2number",
        "minio",
        "money",
        "msgpack",
        "nltk",
        "numpy",
        "openai",
        "pymongo",
        "redis",
        "tiktoken",
        "urllib3",
        "xxhash",
        "python-magic",
        "dicttoxml"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only'        
    ],
)
