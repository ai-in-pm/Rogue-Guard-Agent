from setuptools import setup, find_packages

setup(
    name="rogueguard",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'agno>=1.2.3',
        'openai>=1.0.0',
        'python-dotenv>=1.0.0',
        'rich>=13.0.0',
        'pydantic>=2.0.0',
        'numpy>=1.24.0',
        'pandas>=2.0.0',
        'scikit-learn>=1.3.0',
        'PyYAML>=6.0.0',
    ],
    entry_points={
        'console_scripts': [
            'rogueguard=rogueguard.cli:main',
        ],
    },
    author="RogueWatch Team",
    author_email="contact@rogueguard.ai",
    description="Advanced AI system for detecting and analyzing potential rogue AI behavior",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords="ai, security, monitoring, rogue-ai, safety",
    url="https://github.com/rogueguard/rogueguard",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
)
